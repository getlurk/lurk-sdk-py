from getlurk import Lurk

lurk = Lurk()  # reads the key from LURK_KEY

receipt = lurk.events.send(
    {
        "event": "checkin.scanned",
        "user": "maya@example.com",
        "properties": {"venue": "mission-st"},
        "idempotency_key": "chk-mission-st-maya-0812",
    }
)

print(receipt["receipts"])
