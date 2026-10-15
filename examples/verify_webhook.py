import os

from flask import Flask, abort, request  # any framework: you only need the raw body and the headers

from getlurk import WebhookVerificationError, construct_event

app = Flask(__name__)


@app.post("/webhooks/lurk")
def lurk_webhook():
    try:
        event = construct_event(request.get_data(), request.headers, os.environ["LURK_WEBHOOK_SECRET"])
    except WebhookVerificationError:
        abort(400)
    if event["type"] == "activity.created":
        print(event["data"]["receipts"])
    return "", 204
