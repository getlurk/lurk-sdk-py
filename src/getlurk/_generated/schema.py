"""Generated from openapi/openapi.json by scripts/generate.ts. Do not edit."""

from __future__ import annotations

from typing import Any, Dict, List, Literal, NotRequired, Required, TypedDict, Union


Action = Union["Action1", "Action2", "Action3", "Action4"]

ActivityCheck = TypedDict(
    "ActivityCheck",
    {
    "rule": Required[str],
    "check": Required[Literal["when", "audience", "time", "property", "balance", "source", "limit", "action", "unit", "hold", "budget", "amount", "streak", "modifier", "effect"]],
    "ok": Required[bool],
    "detail": Required[str],
    },
)

ActivityItem = TypedDict(
    "ActivityItem",
    {
    "id": Required[str],
    "at": Required[str],
    "user": Required["ActivityItemUser"],
    "by": Required[str],
    "via": Required[Literal["api", "agent", "lurky", "dashboard", "system", "chat", "device"]],
    "agent": Required[Union[str, None]],
    "event": Required[Union["ActivityItemEvent", None]],
    "lines": Required[List["ActivityLine"]],
    "reverses": Required[Union[str, None]],
    "reversed_by": Required[Union[str, None]],
    "note": Required[Union[str, None]],
    "cause": Required[Literal["spend", "use", "send", "receive", None]],
    "reference": Required[Union[str, None]],
    "transfer": Required[Union[str, None]],
    },
)

ActivityLine = TypedDict(
    "ActivityLine",
    {
    "unit": Required[str],
    "change": Required[int],
    "balance": Required[int],
    "rule": Required[Union[str, None]],
    },
)

ActivityList = TypedDict(
    "ActivityList",
    {
    "data": Required[List["ActivityItem"]],
    "has_more": Required[bool],
    "next_cursor": Required[Union[str, None]],
    },
)

AddAudienceUsersOutput = TypedDict(
    "AddAudienceUsersOutput",
    {
    "id": Required[str],
    "added": Required[int],
    "already_in": Required[int],
    "not_found": Required[List[str]],
    "users": Required[int],
    },
)

AdvanceClockInput = TypedDict(
    "AdvanceClockInput",
    {
    "days": NotRequired[int],
    "hours": NotRequired[int],
    "minutes": NotRequired[int],
    },
)

AgentKey = TypedDict(
    "AgentKey",
    {
    "id": Required[str],
    "name": Required[str],
    "kind": Required[Literal["agent"]],
    "prefix": Required[str],
    "created_at": Required[str],
    "created_by": NotRequired[Union["AgentKeyCreatedBy", None]],
    "last_used_at": Required[Union[str, None]],
    "revoked_at": Required[Union[str, None]],
    },
)

AgentKeyList = TypedDict(
    "AgentKeyList",
    {
    "data": Required[List["AgentKey"]],
    "has_more": Required[bool],
    "next_cursor": Required[Union[str, None]],
    },
)

AmountFrom = TypedDict(
    "AmountFrom",
    {
    "from": Required[str],
    "per": NotRequired[int],
    "max": NotRequired[int],
    },
)

ApiKey = TypedDict(
    "ApiKey",
    {
    "id": Required[str],
    "name": Required[str],
    "kind": Required[Literal["secret"]],
    "prefix": Required[str],
    "created_at": Required[str],
    "created_by": NotRequired[Union["ApiKeyCreatedBy", None]],
    "last_used_at": Required[Union[str, None]],
    "expires_at": Required[Union[str, None]],
    "revoked_at": Required[Union[str, None]],
    },
)

ApiKeyList = TypedDict(
    "ApiKeyList",
    {
    "data": Required[List["ApiKey"]],
    "has_more": Required[bool],
    "next_cursor": Required[Union[str, None]],
    },
)

Approvers = Literal["owners", "owners_and_admins"]

AssignableRole = Literal["admin", "developer", "viewer"]

Audience = TypedDict(
    "Audience",
    {
    "id": Required[str],
    "key": Required[str],
    "name": Required[str],
    "description": Required[Union[str, None]],
    "kind": Required["AudienceKind"],
    "conditions": Required[List["AudienceCondition"]],
    "summary": Required[str],
    "status": Required["AudienceStatus"],
    "problems": Required[List["AudienceProblem"]],
    "users": Required[int],
    "refreshed_at": Required[Union[str, None]],
    "used_by": Required[List["AudienceReader"]],
    "created_at": Required[str],
    },
)

AudienceCondition = Union["AudienceCondition1", "AudienceCondition2", "AudienceCondition3", "AudienceCondition4", "AudienceCondition5", "AudienceCondition6", "AudienceCondition7", "AudienceCondition8", "AudienceCondition9", "AudienceCondition10", "AudienceCondition11"]

AudienceKind = Literal["list", "condition"]

AudienceList = TypedDict(
    "AudienceList",
    {
    "data": Required[List["Audience"]],
    "has_more": Required[bool],
    "next_cursor": Required[Union[str, None]],
    },
)

AudienceProblem = TypedDict(
    "AudienceProblem",
    {
    "condition": Required[int],
    "code": Required[Literal["community_removed", "role_gone", "group_gone", "tag_gone", "not_synced"]],
    "message": Required[str],
    },
)

AudienceReader = TypedDict(
    "AudienceReader",
    {
    "type": Required[Literal["rule", "view"]],
    "id": Required[str],
    "name": Required[str],
    "status": Required[Literal["draft", "live", "paused", None]],
    },
)

AudienceStatus = Literal["ok", "broken", "not_synced"]

BlockState = TypedDict(
    "BlockState",
    {
    "user": Required[str],
    "blocked_at": Required[Union[str, None]],
    "blocked_by": Required["MemberRef"],
    },
)

Brief = TypedDict(
    "Brief",
    {
    "day": Required[str],
    "line": Required[Union[str, None]],
    "active_users": Required["BriefActiveUsers"],
    "new_users": Required["BriefNewUsers"],
    "events": Required["BriefEvents"],
    "given": Required[List["BriefGivenItem"]],
    },
)

Budget = TypedDict(
    "Budget",
    {
    "rule": Required["BudgetRule"],
    "unit": Required[str],
    "amount": Required[int],
    "per": Required[Literal["day", "week", "month"]],
    "used": Required[int],
    "window_start": Required[str],
    "window_end": Required[str],
    },
)

BudgetList = TypedDict(
    "BudgetList",
    {
    "data": Required[List["Budget"]],
    "has_more": Required[bool],
    "next_cursor": Required[Union[str, None]],
    },
)

CardLine = TypedDict(
    "CardLine",
    {
    "field": Required[str],
    "before": NotRequired[Any],
    "after": NotRequired[Any],
    "label": Required[str],
    "before_text": Required[Union[str, None]],
    "after_text": Required[Union[str, None]],
    },
)

CatalogEvent = TypedDict(
    "CatalogEvent",
    {
    "event": Required[str],
    "kind": Required[Literal["own", "lurk"]],
    "title": Required[Union[str, None]],
    "description": Required[Union[str, None]],
    "platforms": Required[List[Literal["discord", "slack", "telegram"]]],
    "count_30d": Required[int],
    "last_seen_at": Required[Union[str, None]],
    "properties": Required[List[str]],
    "property_types": Required[Dict[str, "CatalogPropertyType"]],
    "value_sources": Required[Dict[str, "PropertyValueSource"]],
    "known_values": Required[Dict[str, "KnownValues"]],
    "rules": Required[List["CatalogEventRulesItem"]],
    },
)

CatalogPropertyType = Literal["string", "number", "boolean", "list", "null"]

ChatDirectory = TypedDict(
    "ChatDirectory",
    {
    "installation": Required[str],
    "connector": Required[str],
    "type": Required["ChatDirectoryType"],
    "status": Required[Literal["listed", "unavailable"]],
    "reason": Required[Literal["not_set_up", "no_access", "not_found", "rate_limited", "platform_error", "not_listable", "plan_missing", None]],
    "sentence": Required[Union[str, None]],
    "entries": Required[List["ChatDirectoryEntry"]],
    },
)

ChatDirectoryEntry = TypedDict(
    "ChatDirectoryEntry",
    {
    "id": Required[str],
    "name": Required[str],
    "type": Required["ChatDirectoryType"],
    "kind": Required[Literal["text", "announcement", "voice", "forum", "other", "role", "group"]],
    "can_post": Required[Union[bool, None]],
    "can_give": NotRequired[Union[bool, None]],
    "note": NotRequired[Union[str, None]],
    },
)

ChatDirectoryType = Literal["channel", "role", "group"]

ChatListening = TypedDict(
    "ChatListening",
    {
    "kinds": Required[List["ChatSignalKind"]],
    "channels_only": Required[List[str]],
    "channels_except": Required[List[str]],
    "daily_new_people": Required[int],
    "count_external": Required[bool],
    },
)

ChatMirror = TypedDict(
    "ChatMirror",
    {
    "id": Required[str],
    "installation": Required[str],
    "connector": Required[str],
    "unit": Required[str],
    "threshold": Required[int],
    "target": Required["ChatMirrorTarget"],
    "status": Required["ChatMirrorStatus"],
    "summary": Required[str],
    "problem": Required[Union["ChatMirrorProblem", None]],
    "last_run_at": Required[Union[str, None]],
    "counts": Required[Union["ChatMirrorCounts", None]],
    "created_at": Required[str],
    "updated_at": Required[str],
    },
)

ChatMirrorList = TypedDict(
    "ChatMirrorList",
    {
    "data": Required[List["ChatMirror"]],
    "has_more": Required[bool],
    "next_cursor": Required[Union[str, None]],
    },
)

ChatMirrorPreview = TypedDict(
    "ChatMirrorPreview",
    {
    "installation": Required[str],
    "unit": Required[str],
    "threshold": Required[int],
    "wanted": Required[int],
    "would_give": Required[int],
    "already_have": Required[int],
    "state_unknown": Required[int],
    "would_take_back": Required[int],
    "unknown_holders": Required[int],
    "without_account": Required[int],
    "sentence": Required[str],
    },
)

ChatMirrorStatus = Literal["draft", "live", "paused"]

ChatSettings = TypedDict(
    "ChatSettings",
    {
    "installation": Required[str],
    "connector": Required[str],
    "workspace_name": Required[Union[str, None]],
    "listening": Required["ChatListening"],
    "switches": Required[List["ChatSwitch"]],
    },
)

ChatSettingsChange = TypedDict(
    "ChatSettingsChange",
    {
    "kinds": NotRequired[List["ChatSignalKind"]],
    "channels_only": NotRequired[List[str]],
    "channels_except": NotRequired[List[str]],
    "daily_new_people": NotRequired[int],
    "count_external": NotRequired[bool],
    },
)

ChatSignalKind = Literal["message", "reaction", "voice", "join", "leave"]

ChatSwitch = TypedDict(
    "ChatSwitch",
    {
    "key": Required[str],
    "title": Required[str],
    "counts": Required[str],
    "kinds": Required[List["ChatSignalKind"]],
    "on": Required[bool],
    "events": Required[List[str]],
    "heard": Required[bool],
    },
)

ClaimIdentityLinkInput = TypedDict(
    "ClaimIdentityLinkInput",
    {
    "code": Required[str],
    "user": Required[str],
    },
)

ClaimIdentityLinkOutput = TypedDict(
    "ClaimIdentityLinkOutput",
    {
    "id": Required[str],
    "platform": Required[str],
    "platform_user": Required[str],
    "user": Required[str],
    "linked_at": Required[str],
    "external_id": Required[str],
    "merged_from": Required[Union[str, None]],
    "moved": Required[List["MergedUnit"]],
    },
)

ClientEventAllow = TypedDict(
    "ClientEventAllow",
    {
    "event": Required[str],
    "daily_cap": NotRequired[Union[int, None]],
    "properties": NotRequired[List["ClientEventPropertyRule"]],
    },
)

ClientEventPropertyRule = Union["ClientEventPropertyRule1", "ClientEventPropertyRule2", "ClientEventPropertyRule3"]

ClientEventsSetting = TypedDict(
    "ClientEventsSetting",
    {
    "revision": Required[int],
    "daily_cap_per_person": Required[int],
    "daily_cap_project": Required[Union[int, None]],
    "new_people_per_hour": Required[Union[int, None]],
    "events": Required[List["ClientEventAllow"]],
    "updated_at": Required[Union[str, None]],
    "updated_by": Required["MemberRef"],
    },
)

ClientEventWarning = TypedDict(
    "ClientEventWarning",
    {
    "code": Required[Literal["no_rule_with_source", "rule_without_source", "server_trigger_name"]],
    "event": Required[str],
    "rules": NotRequired[List["RuleRef"]],
    "message": Required[str],
    },
)

Condition = Union["Condition1", "Condition2", "Condition3", "Condition4", "Condition5", "Condition6"]

CreateAgentKeyInput = TypedDict(
    "CreateAgentKeyInput",
    {
    "name": Required[str],
    },
)

CreateApiKeyInput = TypedDict(
    "CreateApiKeyInput",
    {
    "name": Required[str],
    "expires_at": NotRequired[str],
    },
)

CreateAudienceInput = Union["CreateAudienceInput1", "CreateAudienceInput2"]

CreateChatMirrorInput = TypedDict(
    "CreateChatMirrorInput",
    {
    "installation": Required[str],
    "unit": Required[str],
    "threshold": Required[int],
    "target": Required[str],
    "label": NotRequired[str],
    },
)

CreatedAgentKey = TypedDict(
    "CreatedAgentKey",
    {
    "id": Required[str],
    "name": Required[str],
    "kind": Required[Literal["agent"]],
    "prefix": Required[str],
    "created_at": Required[str],
    "created_by": NotRequired[Union["CreatedAgentKeyCreatedBy", None]],
    "last_used_at": Required[Union[str, None]],
    "revoked_at": Required[Union[str, None]],
    "secret": Required[str],
    },
)

CreatedApiKey = TypedDict(
    "CreatedApiKey",
    {
    "id": Required[str],
    "name": Required[str],
    "kind": Required[Literal["secret"]],
    "prefix": Required[str],
    "created_at": Required[str],
    "created_by": NotRequired[Union["CreatedApiKeyCreatedBy", None]],
    "last_used_at": Required[Union[str, None]],
    "expires_at": Required[Union[str, None]],
    "revoked_at": Required[Union[str, None]],
    "secret": Required[str],
    },
)

CreateDashboardInput = TypedDict(
    "CreateDashboardInput",
    {
    "name": Required[str],
    "unit": NotRequired[str],
    "tiles": NotRequired[List["DashboardTileInput"]],
    },
)

CreatedWebhookEndpoint = TypedDict(
    "CreatedWebhookEndpoint",
    {
    "id": Required[str],
    "url": Required[str],
    "events": Required[List[Literal["activity.created", "rule.live", "unit.used"]]],
    "description": Required[Union[str, None]],
    "status": Required[Literal["active", "disabled"]],
    "disabled_reason": Required[Literal["failing", "manual", None]],
    "created_at": Required[str],
    "secret": Required[str],
    },
)

CreateExportInput = TypedDict(
    "CreateExportInput",
    {
    "kind": Required[Literal["activity", "users"]],
    "format": NotRequired[Literal["csv"]],
    "user": NotRequired[str],
    "rule": NotRequired[str],
    "unit": NotRequired[str],
    "since": NotRequired[str],
    "until": NotRequired[str],
    "search": NotRequired[str],
    },
)

CreateIdentityLinkInput = TypedDict(
    "CreateIdentityLinkInput",
    {
    "platform": Required[str],
    "platform_user": Required[str],
    "user": Required[str],
    },
)

CreateIdentityLinkOutput = TypedDict(
    "CreateIdentityLinkOutput",
    {
    "id": Required[str],
    "platform": Required[str],
    "platform_user": Required[str],
    "user": Required[str],
    "linked_at": Required[str],
    "external_id": Required[str],
    "merged_from": Required[Union[str, None]],
    "moved": Required[List["MergedUnit"]],
    },
)

CreateOrganizationInput = TypedDict(
    "CreateOrganizationInput",
    {
    "name": Required[str],
    "slug": NotRequired[str],
    },
)

CreateProjectInput = TypedDict(
    "CreateProjectInput",
    {
    "organization_id": Required[str],
    "name": Required[str],
    "slug": NotRequired[str],
    "kind": NotRequired["ProjectKind"],
    "timezone": NotRequired[str],
    },
)

CreatePromotionInput = TypedDict(
    "CreatePromotionInput",
    {
    "from": Required[str],
    "to": Required[str],
    "rules": NotRequired[List[str]],
    "units": NotRequired[List[str]],
    "title": NotRequired[str],
    "summary": NotRequired[str],
    },
)

CreatePromotionOutput = TypedDict(
    "CreatePromotionOutput",
    {
    "proposal": Required["CreatePromotionOutputProposal"],
    "included": Required[List["PromotionItem"]],
    "skipped": Required[List["PromotionSkipped"]],
    },
)

CreateProposalInput = TypedDict(
    "CreateProposalInput",
    {
    "title": NotRequired[str],
    "summary": NotRequired[str],
    "changes": Required[List["CreateProposalInputChangesItem"]],
    },
)

CreateRuleInput = TypedDict(
    "CreateRuleInput",
    {
    "name": Required[str],
    "key": NotRequired[str],
    "when": Required["RuleWhen"],
    "if": NotRequired[List["Condition"]],
    "limit": NotRequired[List["Limit"]],
    "do": Required[List["Action"]],
    "budget": NotRequired[List["RuleBudget"]],
    "modify": NotRequired[List["Modifier"]],
    "effects": NotRequired[List["RuleEffect"]],
    },
)

CreateTrustedIssuerInput = TypedDict(
    "CreateTrustedIssuerInput",
    {
    "name": Required[str],
    "profile": Required[Union["CreateTrustedIssuerInputProfile1", "CreateTrustedIssuerInputProfile2", "CreateTrustedIssuerInputProfile3"]],
    },
)

CreateUnitInput = TypedDict(
    "CreateUnitInput",
    {
    "name": Required[str],
    "key": NotRequired[str],
    "singular": NotRequired[str],
    "group": Required["UnitGroup"],
    "shows_as": NotRequired[Literal["amount", "thing", "level"]],
    "color": NotRequired[Literal["blue", "green", "amber", "red", "purple", "pink", "teal", "gray"]],
    "switches": NotRequired["CreateUnitInputSwitches"],
    },
)

CreateViewInput = TypedDict(
    "CreateViewInput",
    {
    "name": Required[str],
    "key": NotRequired[str],
    "description": NotRequired[str],
    "definition": Required["ViewDefinition"],
    },
)

CreateWebhookEndpointInput = TypedDict(
    "CreateWebhookEndpointInput",
    {
    "url": Required[str],
    "events": NotRequired[List[Literal["activity.created", "rule.live", "unit.used"]]],
    "description": NotRequired[str],
    },
)

CsvExport = TypedDict(
    "CsvExport",
    {
    "filename": Required[str],
    "content_type": Required[Literal["text/csv"]],
    "csv": Required[str],
    "rows": Required[int],
    "truncated": Required[bool],
    },
)

Dashboard = TypedDict(
    "Dashboard",
    {
    "id": Required[str],
    "name": Required[str],
    "home": Required[bool],
    "pinned": Required[bool],
    "unit": Required[Union[str, None]],
    "tiles": Required[List["DashboardTile"]],
    "updated_at": Required[str],
    "created_at": Required[str],
    },
)

DashboardList = TypedDict(
    "DashboardList",
    {
    "data": Required[List["DashboardSummary"]],
    "has_more": Required[bool],
    "next_cursor": Required[Union[str, None]],
    },
)

DashboardSummary = TypedDict(
    "DashboardSummary",
    {
    "id": Required[str],
    "name": Required[str],
    "home": Required[bool],
    "pinned": Required[bool],
    "unit": Required[Union[str, None]],
    "tiles": Required[int],
    "updated_at": Required[str],
    },
)

DashboardTile = TypedDict(
    "DashboardTile",
    {
    "id": Required[str],
    "view": Required["ViewSummary"],
    "x": Required[int],
    "y": Required[int],
    "w": Required[int],
    "h": Required[int],
    },
)

DashboardTileInput = TypedDict(
    "DashboardTileInput",
    {
    "id": NotRequired[str],
    "view": Required[str],
    "x": Required[int],
    "y": Required[int],
    "w": Required[int],
    "h": Required[int],
    },
)

DashboardWithAnswers = TypedDict(
    "DashboardWithAnswers",
    {
    "id": Required[str],
    "name": Required[str],
    "home": Required[bool],
    "pinned": Required[bool],
    "unit": Required[Union[str, None]],
    "tiles": Required[List["DashboardTile"]],
    "updated_at": Required[str],
    "created_at": Required[str],
    "answers": Required[Dict[str, "ViewAnswer"]],
    },
)

DecideHoldOutput = TypedDict(
    "DecideHoldOutput",
    {
    "id": Required[str],
    "hold": Required["Hold"],
    "receipts": Required[List["Receipt"]],
    },
)

DecideProposalOutput = TypedDict(
    "DecideProposalOutput",
    {
    "id": Required[str],
    "proposal": Required["Proposal"],
    "applied": Required[List["DecideProposalOutputAppliedItem"]],
    },
)

DeclinedInvite = TypedDict(
    "DeclinedInvite",
    {
    "id": Required[str],
    "declined": Required[Literal[True]],
    },
)

DeletedChatMirror = TypedDict(
    "DeletedChatMirror",
    {
    "id": Required[str],
    "deleted": Required[Literal[True]],
    "note": Required[str],
    },
)

DeletedWebhookEndpoint = TypedDict(
    "DeletedWebhookEndpoint",
    {
    "id": Required[str],
    "deleted": Required[Literal[True]],
    },
)

DeleteIdentityLinkOutput = TypedDict(
    "DeleteIdentityLinkOutput",
    {
    "id": Required[str],
    "deleted": Required[Literal[True]],
    "block_copied": Required[bool],
    },
)

DeleteLurkyConversationOutput = TypedDict(
    "DeleteLurkyConversationOutput",
    {
    "id": Required[str],
    "deleted": Required[Literal[True]],
    },
)

DisabledKnownValues = TypedDict(
    "DisabledKnownValues",
    {
    "id": Required[str],
    "event": Required[str],
    "property": Required[str],
    "state": Required[Literal["off"]],
    "deleted_values": Required[int],
    },
)

DisconnectedIntegration = TypedDict(
    "DisconnectedIntegration",
    {
    "id": Required[str],
    "connector": Required[str],
    "disconnected": Required[Literal[True]],
    },
)

DmEffect = TypedDict(
    "DmEffect",
    {
    "community": Required[str],
    "text": Required[str],
    },
)

EnableKnownValuesInput = TypedDict(
    "EnableKnownValuesInput",
    {
    "event": Required[str],
    "property": Required[str],
    },
)

EndUser = TypedDict(
    "EndUser",
    {
    "id": Required[str],
    "external_id": Required[str],
    "created_at": Required[str],
    "last_active_at": Required[Union[str, None]],
    "status": Required["PersonStatus"],
    "balances": Required[List["UnitBalance"]],
    "profile": Required["PersonProfile"],
    "blocked_at": Required[Union[str, None]],
    "blocked_by": Required[Union["EndUserBlockedBy", None]],
    "erased_at": NotRequired[Union[str, None]],
    },
)

EndUserDetail = TypedDict(
    "EndUserDetail",
    {
    "id": Required[str],
    "external_id": Required[str],
    "created_at": Required[str],
    "last_active_at": Required[Union[str, None]],
    "status": Required["PersonStatus"],
    "balances": Required[List["UnitBalance"]],
    "profile": Required["PersonProfile"],
    "blocked_at": Required[Union[str, None]],
    "blocked_by": Required[Union["EndUserDetailBlockedBy", None]],
    "erased_at": NotRequired[Union[str, None]],
    "timezone": Required[Union[str, None]],
    "receipts": Required[int],
    "last_receipt_at": Required[Union[str, None]],
    },
)

ErasureDetail = TypedDict(
    "ErasureDetail",
    {
    "id": Required[str],
    "user": Required[str],
    "state": Required[Literal["queued", "running", "done", "failed"]],
    "requested_at": Required[str],
    "requested_by": Required[str],
    "phase": Required[int],
    "people": Required[int],
    "counts": Required[Dict[str, int]],
    "finished_at": Required[Union[str, None]],
    "removed": Required[List[str]],
    "not_reached": Required[List[str]],
    "notice": Required[str],
    },
)

ErasureRequest = TypedDict(
    "ErasureRequest",
    {
    "id": Required[str],
    "user": Required[str],
    "state": Required[Literal["queued", "running", "done", "failed"]],
    "requested_at": Required[str],
    "requested_by": Required[str],
    },
)

ErrorBody = TypedDict(
    "ErrorBody",
    {
    "error": Required["ErrorBodyError"],
    },
)

EventsCatalog = TypedDict(
    "EventsCatalog",
    {
    "data": Required[List["CatalogEvent"]],
    "has_more": Required[bool],
    "next_cursor": Required[Union[str, None]],
    },
)

ExplainActivityOutput = TypedDict(
    "ExplainActivityOutput",
    {
    "activity": Required["ActivityItem"],
    "checks": Required[List["ActivityCheck"]],
    "traced": Required[bool],
    },
)

ExportDownload = TypedDict(
    "ExportDownload",
    {
    "url": Required[str],
    "expires_at": Required[str],
    "filename": Required[str],
    "requires_auth": Required[bool],
    },
)

ExportJob = TypedDict(
    "ExportJob",
    {
    "id": Required[str],
    "kind": Required[Literal["activity", "users"]],
    "status": Required[Literal["queued", "running", "ready", "failed", "cancelled", "expired"]],
    "filters": Required[Dict[str, Any]],
    "rows": Required[int],
    "bytes": Required[int],
    "truncated": Required[bool],
    "error": Required[Union[str, None]],
    "requested_by": Required[str],
    "created_at": Required[str],
    "started_at": Required[Union[str, None]],
    "finished_at": Required[Union[str, None]],
    "expires_at": Required[Union[str, None]],
    },
)

ExportJobList = TypedDict(
    "ExportJobList",
    {
    "data": Required[List["ExportJob"]],
    "has_more": Required[bool],
    "next_cursor": Required[Union[str, None]],
    },
)

FeedbackImpact = Literal["blocked", "annoying", "minor"]

FeedbackKind = Literal["bug", "gap", "idea", "docs", "question"]

FeedbackReceipt = TypedDict(
    "FeedbackReceipt",
    {
    "id": Required[str],
    "status": Required[Literal["received"]],
    "received_at": Required[str],
    },
)

FeedEffect = TypedDict(
    "FeedEffect",
    {
    "kind": Required[Literal["effect"]],
    "id": Required[str],
    "at": Required[str],
    "user": Required[Union["FeedEffectUser", None]],
    "by": Required[str],
    "rule": Required["FeedEffectRule"],
    "event": Required[Union["FeedEffectEvent", None]],
    "effect": Required[Literal["post", "dm"]],
    "status": Required[Literal["pending", "held", "sent", "failed", "skipped"]],
    "firings": Required[int],
    "summary": Required[str],
    "detail": Required[Union[str, None]],
    },
)

FeedGiven = TypedDict(
    "FeedGiven",
    {
    "id": Required[str],
    "at": Required[str],
    "user": Required["FeedGivenUser"],
    "by": Required[str],
    "via": Required[Literal["api", "agent", "lurky", "dashboard", "system", "chat", "device"]],
    "agent": Required[Union[str, None]],
    "event": Required[Union["FeedGivenEvent", None]],
    "lines": Required[List["ActivityLine"]],
    "reverses": Required[Union[str, None]],
    "reversed_by": Required[Union[str, None]],
    "note": Required[Union[str, None]],
    "cause": Required[Literal["spend", "use", "send", "receive", None]],
    "reference": Required[Union[str, None]],
    "transfer": Required[Union[str, None]],
    "kind": Required[Literal["given"]],
    },
)

FeedHeld = TypedDict(
    "FeedHeld",
    {
    "kind": Required[Literal["held"]],
    "id": Required[str],
    "at": Required[str],
    "user": Required["FeedHeldUser"],
    "by": Required[str],
    "rule": Required["FeedHeldRule"],
    "event": Required["FeedHeldEvent"],
    "changes": Required[List["FeedHeldChangesItem"]],
    "reason": Required[str],
    },
)

FeedItem = Union["FeedGiven", "FeedSkipped", "FeedHeld", "FeedEffect", "FeedMirror"]

FeedList = TypedDict(
    "FeedList",
    {
    "data": Required[List["FeedItem"]],
    "has_more": Required[bool],
    "next_cursor": Required[Union[str, None]],
    },
)

FeedMirror = TypedDict(
    "FeedMirror",
    {
    "kind": Required[Literal["mirror"]],
    "id": Required[str],
    "at": Required[str],
    "user": Required["FeedMirrorUser"],
    "by": Required[str],
    "mirror": Required["FeedMirrorMirror"],
    "connector": Required[str],
    "action": Required[Literal["given", "taken"]],
    "summary": Required[str],
    "detail": Required[Union[str, None]],
    },
)

FeedSkipped = TypedDict(
    "FeedSkipped",
    {
    "kind": Required[Literal["skipped"]],
    "id": Required[str],
    "at": Required[str],
    "user": Required["FeedSkippedUser"],
    "by": Required[str],
    "rule": Required["FeedSkippedRule"],
    "event": Required[Union["FeedSkippedEvent", None]],
    "reason": Required[Literal["condition_failed", "limit_reached", "insufficient_balance", "unit_setting", "hold_refused", "budget_reached", "supply_gone"]],
    "check": Required[str],
    },
)

GiveLine = TypedDict(
    "GiveLine",
    {
    "user": Required["GiveLineUser"],
    "status": Required[Literal["given", "would_give", "skipped"]],
    "reason": Required[Union[str, None]],
    "balance_after": Required[Union[int, None]],
    "activity": Required[Union[str, None]],
    },
)

GivePreview = TypedDict(
    "GivePreview",
    {
    "unit": Required[str],
    "amount": Required[int],
    "people": Required[List["GiveLine"]],
    "not_found": Required[List[str]],
    "totals": Required["GivePreviewTotals"],
    "budget": Required[Union["GivePreviewBudget", None]],
    },
)

GiveUnitsInput = TypedDict(
    "GiveUnitsInput",
    {
    "unit": Required[str],
    "amount": Required[int],
    "users": Required[List[str]],
    "note": NotRequired[str],
    "count_against": NotRequired[str],
    },
)

GiveUnitsOutput = TypedDict(
    "GiveUnitsOutput",
    {
    "id": Required[str],
    "unit": Required[str],
    "amount": Required[int],
    "people": Required[List["GiveLine"]],
    "not_found": Required[List[str]],
    "totals": Required["GiveUnitsOutputTotals"],
    "budget": Required[Union["GiveUnitsOutputBudget", None]],
    },
)

HandleChange = TypedDict(
    "HandleChange",
    {
    "handle": Required[str],
    "account_id": NotRequired[Union[str, None]],
    },
)

Held = TypedDict(
    "Held",
    {
    "hold": Required[str],
    "by": Required[str],
    "reason": Required[str],
    "changes": Required[List["HeldChangesItem"]],
    },
)

HideSuggestionInput = TypedDict(
    "HideSuggestionInput",
    {
    "id": Required[str],
    "signature": Required[str],
    },
)

HistoryEvent = TypedDict(
    "HistoryEvent",
    {
    "kind": Required[Literal["event"]],
    "id": Required[str],
    "name": Required[str],
    "at": Required[str],
    "recorded_at": Required[str],
    "properties": Required[Dict[str, Any]],
    "source": Required[Literal["trusted", "platform", "untrusted"]],
    "session": Required[Union[str, None]],
    "seen_as": Required[Union["HistoryEventSeenAs", None]],
    },
)

HistoryItem = Union["HistoryEvent", "HistoryReceipt"]

HistoryReceipt = TypedDict(
    "HistoryReceipt",
    {
    "kind": Required[Literal["receipt"]],
    "id": Required[str],
    "at": Required[str],
    "recorded_at": Required[str],
    "receipt": Required["ActivityItem"],
    "seen_as": Required[Union["HistoryReceiptSeenAs", None]],
    },
)

Hold = TypedDict(
    "Hold",
    {
    "id": Required[str],
    "status": Required["HoldStatus"],
    "user": Required["HoldUser"],
    "rule": Required["HoldRule"],
    "event": Required["HoldEvent"],
    "changes": Required[List["HoldChangesItem"]],
    "reason": Required[str],
    "held_at": Required[str],
    "decided_at": Required[Union[str, None]],
    "decided_by": Required[Union[str, None]],
    "note": Required[Union[str, None]],
    "activity": Required[Union[str, None]],
    },
)

HoldList = TypedDict(
    "HoldList",
    {
    "data": Required[List["Hold"]],
    "has_more": Required[bool],
    "next_cursor": Required[Union[str, None]],
    "waiting": Required[int],
    },
)

HoldStatus = Literal["held", "given", "refused"]

IdentityLink = TypedDict(
    "IdentityLink",
    {
    "id": Required[str],
    "platform": Required[str],
    "platform_user": Required[str],
    "user": Required[str],
    "linked_at": Required[str],
    },
)

IdentityLinkList = TypedDict(
    "IdentityLinkList",
    {
    "data": Required[List["IdentityLink"]],
    },
)

IdentityMode = Literal["platform", "linked"]

InstallTemplateOutput = TypedDict(
    "InstallTemplateOutput",
    {
    "template": Required[str],
    "installed_at": Required[str],
    "units": Required[List["InstallTemplateOutputUnitsItem"]],
    "rules": Required[List["InstallTemplateOutputRulesItem"]],
    "views": Required[List["InstallTemplateOutputViewsItem"]],
    "dashboards": Required[List["InstallTemplateOutputDashboardsItem"]],
    },
)

Integration = TypedDict(
    "Integration",
    {
    "key": Required[str],
    "name": Required[str],
    "description": Required[str],
    "directions": Required[List[Literal["events_in", "mirrored_out", "agents"]]],
    "status": Required["IntegrationStatus"],
    "stat": Required[Union["IntegrationStat", None]],
    "problems": Required[List["IntegrationProblem"]],
    "connected_at": Required[Union[str, None]],
    },
)

IntegrationConnectLink = TypedDict(
    "IntegrationConnectLink",
    {
    "url": Required[str],
    "expires_at": Required[str],
    "note": Required[str],
    },
)

IntegrationHealth = TypedDict(
    "IntegrationHealth",
    {
    "key": Required[str],
    "status": Required["IntegrationStatus"],
    "problems": Required[List["IntegrationProblem"]],
    "checked_at": Required[str],
    },
)

IntegrationHealthOutput = TypedDict(
    "IntegrationHealthOutput",
    {
    "data": Required[List["IntegrationHealth"]],
    "needs_attention": Required[int],
    },
)

IntegrationInstallation = TypedDict(
    "IntegrationInstallation",
    {
    "id": Required[str],
    "connector": Required[str],
    "workspace_name": Required[Union[str, None]],
    "status": Required[Literal["connected", "needs_attention"]],
    "settings": Required["IntegrationSettings"],
    "health": Required[Union["IntegrationInstallationHealth", None]],
    "connected_at": Required[str],
    "state_synced_at": NotRequired[Union[str, None]],
    },
)

IntegrationInstallations = TypedDict(
    "IntegrationInstallations",
    {
    "connector": Required[str],
    "status": Required["IntegrationStatus"],
    "installations": Required[List["IntegrationInstallation"]],
    },
)

IntegrationList = TypedDict(
    "IntegrationList",
    {
    "data": Required[List["Integration"]],
    "has_more": Required[bool],
    "next_cursor": Required[Union[str, None]],
    },
)

IntegrationProblem = TypedDict(
    "IntegrationProblem",
    {
    "code": Required[str],
    "message": Required[str],
    "fix": Required[Union[str, None]],
    "fix_url": Required[Union[str, None]],
    },
)

IntegrationSettings = TypedDict(
    "IntegrationSettings",
    {
    "tip": Required[bool],
    "announce_tips": Required[bool],
    "identity": Required["IdentityMode"],
    },
)

IntegrationSettingsChange = TypedDict(
    "IntegrationSettingsChange",
    {
    "tip": NotRequired[bool],
    "announce_tips": NotRequired[bool],
    "identity": NotRequired[Literal["platform", "linked"]],
    },
)

IntegrationStatus = Literal["connected", "needs_attention", "not_connected", "later"]

Invite = TypedDict(
    "Invite",
    {
    "status": Required[Literal["invited"]],
    "id": Required[str],
    "email": Required[str],
    "role": Required["AssignableRole"],
    "invited_by": Required["InviteInvitedBy"],
    "invited_at": Required[str],
    "expires_at": Required[str],
    },
)

InviteMemberInput = TypedDict(
    "InviteMemberInput",
    {
    "organization_id": Required[str],
    "email": Required[str],
    "role": Required["AssignableRole"],
    },
)

IssuerIdentity = TypedDict(
    "IssuerIdentity",
    {
    "id": Required[str],
    "issuer_id": Required[str],
    "person_id": Required[str],
    "origin": Required[Literal["first_sight", "mapping"]],
    "mapped_by": Required[Union["IssuerIdentityMappedBy", None]],
    "created_at": Required[str],
    "last_used_at": Required[Union[str, None]],
    },
)

KnownValue = TypedDict(
    "KnownValue",
    {
    "value": Required[str],
    "type": Required["KnownValueType"],
    },
)

KnownValues = TypedDict(
    "KnownValues",
    {
    "values": Required[List["KnownValue"]],
    },
)

KnownValuesList = TypedDict(
    "KnownValuesList",
    {
    "data": Required[List["KnownValuesSetting"]],
    "cap": Required[int],
    },
)

KnownValuesSetting = TypedDict(
    "KnownValuesSetting",
    {
    "id": Required[str],
    "event": Required[str],
    "property": Required[str],
    "state": Required[Literal["on", "stopped"]],
    "values": Required[List["KnownValue"]],
    "stopped": Required[Union["KnownValuesSettingStopped", None]],
    "enabled_by": Required[str],
    "enabled_at": Required[str],
    "updated_at": Required[str],
    },
)

KnownValuesStopReason = Literal["too_many", "too_long", "personal"]

KnownValueType = Literal["text", "number", "yes_no"]

Limit = TypedDict(
    "Limit",
    {
    "max": Required[int],
    "per": Required[Literal["day", "week", "month", "ever"]],
    "by": NotRequired[Literal["user"]],
    },
)

LurkyConversation = TypedDict(
    "LurkyConversation",
    {
    "id": Required[str],
    "title": Required[str],
    "created_at": Required[str],
    "updated_at": Required[str],
    "expires_at": Required[str],
    "messages": Required[List["LurkyMessage"]],
    },
)

LurkyConversationList = TypedDict(
    "LurkyConversationList",
    {
    "data": Required[List["LurkyConversationSummary"]],
    "has_more": Required[bool],
    "next_cursor": Required[Union[str, None]],
    },
)

LurkyConversationSummary = TypedDict(
    "LurkyConversationSummary",
    {
    "id": Required[str],
    "title": Required[str],
    "created_at": Required[str],
    "updated_at": Required[str],
    "expires_at": Required[str],
    },
)

LurkyMessage = TypedDict(
    "LurkyMessage",
    {
    "role": Required[Literal["user", "assistant"]],
    "text": Required[str],
    "tools": Required[List["LurkyMessageToolsItem"]],
    "cards": Required[List[str]],
    "at": Required[str],
    },
)

LurkySettings = TypedDict(
    "LurkySettings",
    {
    "available": Required[bool],
    "enabled": Required[bool],
    },
)

LurkyUsage = TypedDict(
    "LurkyUsage",
    {
    "enabled": Required[bool],
    "status": Required[Literal["off", "ok", "warning", "stopped"]],
    "message": Required[Union[str, None]],
    "month": Required[str],
    "resets_on": Required[str],
    "allowance_cents": Required[float],
    "used_cents": Required[float],
    "percent": Required[int],
    "calls": Required[int],
    "tokens": Required["LurkyUsageTokens"],
    },
)

Me = TypedDict(
    "Me",
    {
    "id": Required[str],
    "name": Required[str],
    "email": Required[str],
    "membership": Required[Union["MeMembership", None]],
    },
)

Member = TypedDict(
    "Member",
    {
    "status": Required[Literal["active"]],
    "id": Required[str],
    "name": Required[str],
    "email": Required[str],
    "role": Required["MemberRole"],
    "joined_at": Required[str],
    "last_active_at": Required[Union[str, None]],
    },
)

MemberList = TypedDict(
    "MemberList",
    {
    "data": Required[List[Union["Member", "Invite"]]],
    "has_more": Required[bool],
    "next_cursor": Required[Union[str, None]],
    "total": Required[int],
    },
)

MemberRef = TypedDict(
    "MemberRef",
    {
    "id": Required[str],
    "name": Required[str],
    },
)

MemberRole = Literal["owner", "admin", "developer", "viewer"]

MergedPerson = TypedDict(
    "MergedPerson",
    {
    "id": Required[str],
    "external_id": Required[str],
    },
)

MergedUnit = TypedDict(
    "MergedUnit",
    {
    "unit": Required[str],
    "amount": Required[int],
    "transfer": Required[str],
    "receipt": Required[str],
    },
)

MergeUsersInput = TypedDict(
    "MergeUsersInput",
    {
    "from": Required[str],
    "into": Required[str],
    },
)

MergeUsersOutput = TypedDict(
    "MergeUsersOutput",
    {
    "from": Required["MergedPerson"],
    "into": Required["MergedPerson"],
    "moved": Required[List["MergedUnit"]],
    },
)

Modifier = Union["Modifier1", "Modifier2"]

MyInvite = TypedDict(
    "MyInvite",
    {
    "id": Required[str],
    "organization": Required["MyInviteOrganization"],
    "role": Required["AssignableRole"],
    "invited_by": Required["MyInviteInvitedBy"],
    "invited_at": Required[str],
    "expires_at": Required[str],
    },
)

MyInviteList = TypedDict(
    "MyInviteList",
    {
    "data": Required[List["MyInvite"]],
    "has_more": Required[bool],
    "next_cursor": Required[Union[str, None]],
    },
)

Organization = TypedDict(
    "Organization",
    {
    "id": Required[str],
    "name": Required[str],
    "slug": Required[str],
    "role": Required[Literal["owner", "admin", "developer", "viewer"]],
    "projects": Required[int],
    "created_at": Required[str],
    },
)

OrganizationList = TypedDict(
    "OrganizationList",
    {
    "data": Required[List["Organization"]],
    "has_more": Required[bool],
    "next_cursor": Required[Union[str, None]],
    },
)

Period = TypedDict(
    "Period",
    {
    "from": Required[str],
    "to": Required[str],
    },
)

PersonAlias = TypedDict(
    "PersonAlias",
    {
    "user": Required["PersonAliasUser"],
    "alias": Required[str],
    "person": Required[Union["PersonAliasPerson", None]],
    "created_at": Required[str],
    },
)

PersonHandle = TypedDict(
    "PersonHandle",
    {
    "handle": Required[str],
    "account_id": Required[Union[str, None]],
    },
)

PersonProfile = TypedDict(
    "PersonProfile",
    {
    "email": Required[Union[str, None]],
    "name": Required[Union[str, None]],
    "avatar_url": Required[Union[str, None]],
    "handles": Required[Dict[str, "PersonHandle"]],
    "locale": Required[Union[str, None]],
    "updated_at": Required[Union[str, None]],
    },
)

PersonStatus = Literal["new", "returning", "lapsing"]

PlanTemplateOutput = TypedDict(
    "PlanTemplateOutput",
    {
    "template": Required[str],
    "units": Required[List["PlanTemplateOutputUnitsItem"]],
    "rules": Required[List["PlanTemplateOutputRulesItem"]],
    "views": Required[List["PlanTemplateOutputViewsItem"]],
    "test_week": Required["PlanTemplateOutputTestWeek"],
    "notes": Required[List[str]],
    },
)

PostEffect = TypedDict(
    "PostEffect",
    {
    "community": Required[str],
    "channel": Required[str],
    "channel_name": NotRequired[str],
    "text": Required[str],
    "every": NotRequired[Literal["hour", "day"]],
    "max_per_day": NotRequired[int],
    },
)

PreviewChatMirrorInput = TypedDict(
    "PreviewChatMirrorInput",
    {
    "id": NotRequired[str],
    "installation": NotRequired[str],
    "unit": NotRequired[str],
    "threshold": NotRequired[int],
    "target": NotRequired[str],
    },
)

PreviewEffect = TypedDict(
    "PreviewEffect",
    {
    "effect": Required[Literal["post", "dm"]],
    "words": Required[str],
    "firings": Required[int],
    "messages": Required[int],
    },
)

PreviewPromotionOutput = TypedDict(
    "PreviewPromotionOutput",
    {
    "included": Required[List["PromotionItem"]],
    "skipped": Required[List["PromotionSkipped"]],
    "can_send": Required[bool],
    "problem": Required[Union[str, None]],
    },
)

PreviewRuleOutput = TypedDict(
    "PreviewRuleOutput",
    {
    "trigger": Required[Literal["event", "schedule", "balance"]],
    "schedule": Required[Union["PreviewRuleOutputSchedule", None]],
    "balance": Required[Union["PreviewRuleOutputBalance", None]],
    "rule": Required[str],
    "version": Required[Union[int, None]],
    "period": Required["RulePeriod"],
    "events": Required[int],
    "users": Required[int],
    "receipts": Required[int],
    "held": Required[int],
    "given": Required[List["UnitTotal"]],
    "effects": Required[List["PreviewEffect"]],
    "skipped": Required[List["SkipCount"]],
    "top_users": Required[List["PreviewUserTotal"]],
    "truncated": Required[bool],
    "notes": Required[List[str]],
    },
)

PreviewUserTotal = TypedDict(
    "PreviewUserTotal",
    {
    "user": Required[str],
    "given": Required[List["UnitTotal"]],
    },
)

Project = TypedDict(
    "Project",
    {
    "id": Required[str],
    "organization_id": Required[str],
    "name": Required[str],
    "slug": Required[str],
    "kind": Required["ProjectKind"],
    "timezone": Required[str],
    "approvers": Required[Literal["owners", "owners_and_admins"]],
    "new_for_days": Required[int],
    "lapsing_after_days": Required[int],
    "created_at": Required[str],
    },
)

ProjectClock = TypedDict(
    "ProjectClock",
    {
    "test": Required[bool],
    "now": Required[str],
    "real_now": Required[str],
    "offset_seconds": Required[int],
    },
)

ProjectKind = Literal["production", "staging"]

ProjectList = TypedDict(
    "ProjectList",
    {
    "data": Required[List["Project"]],
    "has_more": Required[bool],
    "next_cursor": Required[Union[str, None]],
    },
)

ProjectSetup = TypedDict(
    "ProjectSetup",
    {
    "steps": Required[List["SetupStep"]],
    "areas": Required[List["SetupAreaState"]],
    "next": Required[Union[str, None]],
    "complete": Required[bool],
    "live": Required[bool],
    },
)

PromotionItem = TypedDict(
    "PromotionItem",
    {
    "type": Required[Literal["unit", "rule"]],
    "key": Required[str],
    "action": Required[Literal["create", "update"]],
    },
)

PromotionSkipped = TypedDict(
    "PromotionSkipped",
    {
    "type": Required[Literal["unit", "rule"]],
    "key": Required[str],
    "reason": Required[str],
    },
)

PropertyValueSource = Union["PropertyValueSource1", "PropertyValueSource2", "PropertyValueSource3"]

ProposableOperation = Literal["rules.publish", "rules.resume", "rules.pause", "units.create", "rules.create", "rules.update", "templates.install", "units.give"]

Proposal = TypedDict(
    "Proposal",
    {
    "id": Required[str],
    "status": Required["ProposalStatus"],
    "title": Required[str],
    "summary": Required[str],
    "by": Required[str],
    "via": Required[Literal["api", "agent", "lurky", "dashboard", "system"]],
    "agent": Required[Union[str, None]],
    "changes": Required[List["ProposalChange"]],
    "created_at": Required[str],
    "expires_at": Required[str],
    "decided_at": Required[Union[str, None]],
    "decided_by": Required[Union[str, None]],
    "note": Required[Union[str, None]],
    "url": Required[Union[str, None]],
    },
)

ProposalCard = TypedDict(
    "ProposalCard",
    {
    "id": Required[str],
    "status": Required["ProposalStatus"],
    "title": Required[str],
    "summary": Required[str],
    "by": Required[str],
    "via": Required[Literal["api", "agent", "lurky", "dashboard", "system"]],
    "agent": Required[Union[str, None]],
    "applicable": Required[bool],
    "refusal": Required[Union[str, None]],
    "changes": Required[List["ProposalCardChangesItem"]],
    "expires_at": Required[str],
    "url": Required[Union[str, None]],
    },
)

ProposalChange = TypedDict(
    "ProposalChange",
    {
    "operation": Required["ProposableOperation"],
    "target": Required["ProposalChangeTarget"],
    "summary": Required[str],
    "input": Required[Dict[str, Any]],
    "before": Required[Dict[str, Any]],
    "after": Required[Dict[str, Any]],
    "effect": NotRequired[Union[str, None]],
    },
)

ProposalList = TypedDict(
    "ProposalList",
    {
    "data": Required[List["Proposal"]],
    "has_more": Required[bool],
    "next_cursor": Required[Union[str, None]],
    "waiting": Required[int],
    },
)

ProposalStatus = Literal["open", "approved", "declined", "expired"]

Receipt = TypedDict(
    "Receipt",
    {
    "by": Required[str],
    "via": NotRequired[Literal["api", "agent", "lurky", "dashboard", "system", "chat", "device"]],
    "agent": NotRequired[str],
    "unit": Required[str],
    "change": Required[int],
    "balance": Required[int],
    },
)

RemovedMember = TypedDict(
    "RemovedMember",
    {
    "id": Required[str],
    "removed": Required[Literal[True]],
    },
)

RemoveTemplateOutput = TypedDict(
    "RemoveTemplateOutput",
    {
    "template": Required[str],
    "removed_rules": Required[List[str]],
    "kept": Required["RemoveTemplateOutputKept"],
    },
)

ResetClockInput = Dict[str, Any]

RevokedInvite = TypedDict(
    "RevokedInvite",
    {
    "id": Required[str],
    "revoked": Required[Literal[True]],
    },
)

Rule = TypedDict(
    "Rule",
    {
    "id": Required[str],
    "key": Required[str],
    "name": Required[str],
    "status": Required[Literal["draft", "live", "paused"]],
    "version": Required[int],
    "live_version": Required[Union[int, None]],
    "definition": Required["RuleDefinition"],
    },
)

RuleBudget = TypedDict(
    "RuleBudget",
    {
    "unit": Required[str],
    "max": Required[int],
    "per": Required[Literal["day", "week", "month"]],
    },
)

RuleCounts = TypedDict(
    "RuleCounts",
    {
    "all": Required[int],
    "live": Required[int],
    "paused": Required[int],
    "draft": Required[int],
    },
)

RuleDetail = TypedDict(
    "RuleDetail",
    {
    "id": Required[str],
    "key": Required[str],
    "name": Required[str],
    "status": Required[Literal["draft", "live", "paused"]],
    "version": Required[int],
    "live_version": Required[Union[int, None]],
    "definition": Required["RuleDetailDefinition"],
    "units": Required[List[str]],
    "created_at": Required[str],
    "updated_at": Required[str],
    "live_definition": Required[Union["RuleDetailLiveDefinition", None]],
    },
)

RuleEffect = Union["RuleEffect1", "RuleEffect2"]

RuleList = TypedDict(
    "RuleList",
    {
    "data": Required[List["RuleListItem"]],
    "has_more": Required[bool],
    "next_cursor": Required[Union[str, None]],
    "counts": Required["RuleCounts"],
    },
)

RuleListItem = TypedDict(
    "RuleListItem",
    {
    "id": Required[str],
    "key": Required[str],
    "name": Required[str],
    "status": Required[Literal["draft", "live", "paused"]],
    "version": Required[int],
    "live_version": Required[Union[int, None]],
    "definition": Required["RuleListItemDefinition"],
    "units": Required[List[str]],
    "created_at": Required[str],
    "updated_at": Required[str],
    },
)

RulePeriod = TypedDict(
    "RulePeriod",
    {
    "from": Required[str],
    "to": Required[str],
    },
)

RuleRef = TypedDict(
    "RuleRef",
    {
    "id": Required[str],
    "key": Required[str],
    "name": Required[str],
    },
)

RuleStatsOutput = TypedDict(
    "RuleStatsOutput",
    {
    "rule": Required[str],
    "period": Required["RulePeriod"],
    "receipts": Required[int],
    "users": Required[int],
    "given": Required[List["UnitTotal"]],
    "skipped": Required[List["SkipCount"]],
    "top_users": Required[List["RuleStatsUser"]],
    },
)

RuleStatsUser = TypedDict(
    "RuleStatsUser",
    {
    "id": Required[str],
    "external_id": Required[str],
    "receipts": Required[int],
    "given": Required[List["UnitTotal"]],
    },
)

RuleWhen = Union["RuleWhen1", "RuleWhen2", "RuleWhen3", "RuleWhen4"]

Schedule = TypedDict(
    "Schedule",
    {
    "every": Required[Literal["day", "week", "month"]],
    "at": Required[str],
    "on": NotRequired[Union[Literal["mon", "tue", "wed", "thu", "fri", "sat", "sun"], int]],
    },
)

SendEventInput = TypedDict(
    "SendEventInput",
    {
    "event": Required[str],
    "user": Required[str],
    "properties": NotRequired[Dict[str, Union[str, float, bool, None, List[Union[str, float, bool, None]]]]],
    "idempotency_key": Required[str],
    "timestamp": NotRequired[str],
    "profile": NotRequired["SendEventInputProfile"],
    "alias": NotRequired[str],
    },
)

SendEventOutput = TypedDict(
    "SendEventOutput",
    {
    "activity": Required[Union[str, None]],
    "user": Required[str],
    "event": Required[str],
    "receipts": Required[List["Receipt"]],
    "skipped": Required[List["Skipped"]],
    "held": NotRequired[List["Held"]],
    "alias": NotRequired["SendEventOutputAlias"],
    },
)

SendFeedbackInput = TypedDict(
    "SendFeedbackInput",
    {
    "kind": Required["FeedbackKind"],
    "impact": Required["FeedbackImpact"],
    "message": Required[str],
    "operation": NotRequired[str],
    "request_ids": NotRequired[List[str]],
    "docs_path": NotRequired[str],
    "client": NotRequired["SendFeedbackInputClient"],
    "idempotency_key": Required[str],
    },
)

SendUnitsInput = TypedDict(
    "SendUnitsInput",
    {
    "from": Required[str],
    "to": Required[str],
    "unit": Required[str],
    "amount": Required[int],
    "reason": NotRequired[str],
    },
)

SendUnitsOutput = TypedDict(
    "SendUnitsOutput",
    {
    "transfer": Required[str],
    "receipt": Required[str],
    "from": Required["SendUnitsOutputFrom"],
    "to": Required["SendUnitsOutputTo"],
    "unit": Required[str],
    "amount": Required[int],
    "sent_today": Required[int],
    "daily_limit": Required[int],
    },
)

SetClockInput = TypedDict(
    "SetClockInput",
    {
    "to": Required[str],
    },
)

SetupArea = Literal["home", "dashboards", "users", "activity", "rules", "units", "audiences", "events", "promote", "templates", "integrations", "developers", "partners", "settings"]

SetupAreaState = TypedDict(
    "SetupAreaState",
    {
    "area": Required["SetupArea"],
    "locked": Required[bool],
    "opened_by": Required[Union[str, None]],
    },
)

SetupStep = TypedDict(
    "SetupStep",
    {
    "id": Required[str],
    "title": Required[str],
    "line": Required[str],
    "ask": Required[str],
    "done": Required[bool],
    "opens": Required[List["SetupArea"]],
    },
)

ShowSuggestionInput = TypedDict(
    "ShowSuggestionInput",
    {
    "id": Required[str],
    },
)

SkipCount = TypedDict(
    "SkipCount",
    {
    "reason": Required[Literal["condition_failed", "limit_reached", "insufficient_balance", "unit_setting", "hold_refused", "budget_reached", "supply_gone"]],
    "count": Required[int],
    },
)

Skipped = TypedDict(
    "Skipped",
    {
    "by": Required[str],
    "reason": Required[Literal["condition_failed", "limit_reached", "insufficient_balance", "unit_setting", "hold_refused", "budget_reached", "supply_gone"]],
    "check": Required[str],
    },
)

SpendUnitsInput = TypedDict(
    "SpendUnitsInput",
    {
    "user": Required[str],
    "unit": Required[str],
    "amount": Required[int],
    "reason": Required[str],
    "reference": NotRequired[str],
    },
)

SpendUnitsOutput = TypedDict(
    "SpendUnitsOutput",
    {
    "id": Required[str],
    "user": Required["SpendUnitsOutputUser"],
    "unit": Required[str],
    "amount": Required[int],
    "balance_after": Required[int],
    "reference": Required[Union[str, None]],
    },
)

Suggestion = TypedDict(
    "Suggestion",
    {
    "id": Required[str],
    "kind": Required[str],
    "tier": Required["SuggestionTier"],
    "title": Required[str],
    "why": Required[str],
    "ask": Required[Union[str, None]],
    "opens": Required["SuggestionOpens"],
    "signature": Required[str],
    },
)

SuggestionHidden = TypedDict(
    "SuggestionHidden",
    {
    "id": Required[str],
    "hidden": Required[bool],
    },
)

SuggestionList = TypedDict(
    "SuggestionList",
    {
    "data": Required[List["Suggestion"]],
    "total": Required[int],
    },
)

SuggestionPage = Literal["home", "dashboards", "users", "activity", "rules", "units", "audiences", "events", "promote", "templates", "integrations", "developers", "partners", "settings", "approve"]

SuggestionTier = Literal["needs_you", "change", "idea"]

Template = TypedDict(
    "Template",
    {
    "id": Required[str],
    "key": Required[str],
    "name": Required[str],
    "tagline": Required[str],
    "for": Required[str],
    "category": Required["TemplateCategory"],
    "status": Required["TemplateStatus"],
    "counts": Required["TemplateCounts"],
    "description": Required[str],
    "adds": Required["TemplateAdds"],
    "settings": Required[List["TemplateSetting"]],
    "installed_at": Required[Union[str, None]],
    },
)

TemplateCategory = Literal["earn_and_spend", "progress", "growth_and_community"]

TemplateList = TypedDict(
    "TemplateList",
    {
    "data": Required[List["TemplateSummary"]],
    "has_more": Required[bool],
    "next_cursor": Required[Union[str, None]],
    },
)

TemplateSetting = TypedDict(
    "TemplateSetting",
    {
    "key": Required[str],
    "label": Required[str],
    "type": Required[Literal["text", "integer", "unit"]],
    "default": Required[Union[str, int]],
    },
)

TemplateStatus = Literal["available", "in_use", "later"]

TemplateSummary = TypedDict(
    "TemplateSummary",
    {
    "id": Required[str],
    "key": Required[str],
    "name": Required[str],
    "tagline": Required[str],
    "for": Required[str],
    "category": Required["TemplateCategory"],
    "status": Required["TemplateStatus"],
    "counts": Required["TemplateSummaryCounts"],
    },
)

TestTrustedIssuerOutput = Union["TestTrustedIssuerOutput1", "TestTrustedIssuerOutput2"]

TrustedIssuer = TypedDict(
    "TrustedIssuer",
    {
    "id": Required[str],
    "name": Required[str],
    "profile": Required[Union["TrustedIssuerProfile1", "TrustedIssuerProfile2", "TrustedIssuerProfile3"]],
    "issuer": Required[str],
    "jwks_url": Required[str],
    "revision": Required[int],
    "status": Required[Literal["paused", "active", "archived"]],
    "created_at": Required[str],
    "checked_at": Required[Union[str, None]],
    "last_used_at": Required[Union[str, None]],
    "key_origin_differs": Required[bool],
    "key_count": Required[int],
    "key_ids_hash": Required[Union[str, None]],
    "algorithms": Required[List[Literal["RS256", "ES256"]]],
    "problem": Required[Literal["unavailable", "invalid_keys", "no_supported_key", "configuration_changed", None]],
    "can_activate": Required[bool],
    },
)

UndoActivityOutput = TypedDict(
    "UndoActivityOutput",
    {
    "id": Required[str],
    "activity": Required["UndoActivityOutputActivity"],
    "note": Required[Union[str, None]],
    },
)

Unit = TypedDict(
    "Unit",
    {
    "id": Required[str],
    "key": Required[str],
    "name": Required[str],
    "singular": Required[str],
    "group": Required["UnitGroup"],
    "shows_as": Required[Literal["amount", "thing", "level"]],
    "color": Required[Literal["blue", "green", "amber", "red", "purple", "pink", "teal", "gray", None]],
    "switches": Required["UnitSwitches"],
    "stats": Required["UnitStats"],
    "created_at": Required[str],
    "updated_at": Required[str],
    },
)

UnitBalance = TypedDict(
    "UnitBalance",
    {
    "unit": Required[str],
    "amount": Required[int],
    },
)

UnitGroup = Literal["points", "progress", "badge", "perk"]

UnitLeaderboard = TypedDict(
    "UnitLeaderboard",
    {
    "unit": Required["UnitLeaderboardUnit"],
    "rows": Required[List["UnitLeaderboardRowsItem"]],
    },
)

UnitList = TypedDict(
    "UnitList",
    {
    "data": Required[List["Unit"]],
    "has_more": Required[bool],
    "next_cursor": Required[Union[str, None]],
    "counts": Required["UnitListCounts"],
    },
)

UnitShowsAs = Literal["amount", "thing", "level"]

UnitStats = TypedDict(
    "UnitStats",
    {
    "held": Required[int],
    "holders": Required[int],
    "given_30d": Required[int],
    "spent_30d": Required[int],
    "issued": Required[int],
    },
)

UnitSwitches = TypedDict(
    "UnitSwitches",
    {
    "goes_up": Required[bool],
    "goes_down": Required[bool],
    "spendable": Required[bool],
    "usable": Required[bool],
    "sendable": Required[bool],
    "send_cap_per_day": Required[int],
    "resets": Required[bool],
    "starts_at": Required[int],
    "held_by": Required[Union[str, None]],
    "cap": Required[Union[int, None]],
    "min_balance": Required[int],
    "visible": Required[bool],
    "supply": Required[Union[int, None]],
    "expires_after_days": Required[Union[int, None]],
    "expires_at": Required[Union[str, None]],
    },
)

UnitTotal = TypedDict(
    "UnitTotal",
    {
    "unit": Required[str],
    "amount": Required[int],
    },
)

UnmergeUsersInput = TypedDict(
    "UnmergeUsersInput",
    {
    "user": Required[str],
    },
)

UnmergeUsersOutput = TypedDict(
    "UnmergeUsersOutput",
    {
    "user": Required["MergedPerson"],
    "was_merged_into": Required["UnmergeUsersOutputWasMergedInto"],
    "moved_back": Required[List["MergedUnit"]],
    "block_copied": Required[bool],
    },
)

UpdateClientEventsInput = TypedDict(
    "UpdateClientEventsInput",
    {
    "expected_revision": Required[int],
    "daily_cap_per_person": NotRequired[int],
    "daily_cap_project": NotRequired[Union[int, None]],
    "new_people_per_hour": NotRequired[Union[int, None]],
    "events": NotRequired[List["ClientEventAllow"]],
    },
)

UpdateClientEventsOutput = TypedDict(
    "UpdateClientEventsOutput",
    {
    "setting": Required["ClientEventsSetting"],
    "warnings": Required[List["ClientEventWarning"]],
    },
)

UpdatedChatSettings = TypedDict(
    "UpdatedChatSettings",
    {
    "installation": Required[str],
    "connector": Required[str],
    "workspace_name": Required[Union[str, None]],
    "listening": Required["ChatListening"],
    "switches": Required[List["ChatSwitch"]],
    "id": Required[str],
    },
)

UpdateLurkySettingsInput = TypedDict(
    "UpdateLurkySettingsInput",
    {
    "enabled": Required[bool],
    },
)

UserHistory = TypedDict(
    "UserHistory",
    {
    "data": Required[List["HistoryItem"]],
    "has_more": Required[bool],
    "next_cursor": Required[Union[str, None]],
    "includes": Required[List["MergedPerson"]],
    },
)

UserList = TypedDict(
    "UserList",
    {
    "data": Required[List["EndUser"]],
    "has_more": Required[bool],
    "next_cursor": Required[Union[str, None]],
    "total": NotRequired[int],
    },
)

UseUnitsInput = TypedDict(
    "UseUnitsInput",
    {
    "user": Required[str],
    "unit": Required[str],
    "amount": NotRequired[int],
    "reason": NotRequired[str],
    "reference": NotRequired[str],
    },
)

UseUnitsOutput = TypedDict(
    "UseUnitsOutput",
    {
    "id": Required[str],
    "user": Required["UseUnitsOutputUser"],
    "unit": Required[str],
    "amount": Required[int],
    "balance_after": Required[int],
    "reference": Required[Union[str, None]],
    },
)

View = TypedDict(
    "View",
    {
    "id": Required[str],
    "key": Required[str],
    "name": Required[str],
    "shape": Required[Literal["number", "over_time", "list"]],
    "visibility": Required["ViewVisibility"],
    "updated_at": Required[str],
    "description": Required[Union[str, None]],
    "definition": Required["ViewDefinition"],
    "endpoint": Required[str],
    "made_by": Required[Literal["template", "member", "key", "agent"]],
    "template": Required[Union[str, None]],
    "dashboards": Required[List["ViewDashboardsItem"]],
    "created_at": Required[str],
    },
)

ViewAnswer = TypedDict(
    "ViewAnswer",
    {
    "period": Required["Period"],
    "compared_with": Required[Any],
    "series": Required[List["ViewSeries"]],
    "rows": Required[List["ViewRow"]],
    "total_rows": Required[Union[int, None]],
    "computed_at": Required[str],
    },
)

ViewDefinition = TypedDict(
    "ViewDefinition",
    {
    "who": Required["ViewWho"],
    "what": Required[List["ViewMeasure"]],
    "over": Required["ViewRange"],
    "shape": Required["ViewShape"],
    "source": NotRequired[Literal["trusted", "platform", "any"]],
    },
)

ViewList = TypedDict(
    "ViewList",
    {
    "data": Required[List["ViewSummary"]],
    "has_more": Required[bool],
    "next_cursor": Required[Union[str, None]],
    },
)

ViewMeasure = Union["ViewMeasure1", "ViewMeasure2", "ViewMeasure3"]

ViewPoint = TypedDict(
    "ViewPoint",
    {
    "at": Required[str],
    "value": Required[int],
    },
)

ViewRange = Literal["now", "today", "this_week", "last_week", "last_7_days", "last_14_days", "last_30_days", "last_90_days", "this_month", "all_time"]

ViewRow = TypedDict(
    "ViewRow",
    {
    "rank": Required[int],
    "label": Required[str],
    "user": Required[Union["ViewRowUser", None]],
    "rule": Required[Union["ViewRowRule", None]],
    "property": Required[Union["ViewRowProperty", None]],
    "value": Required[int],
    "previous_rank": Required[Union[int, None]],
    "values": Required[List[int]],
    },
)

ViewSeries = TypedDict(
    "ViewSeries",
    {
    "measure": Required["ViewMeasure"],
    "unit": Required[Union[str, None]],
    "total": Required[int],
    "previous_total": Required[Union[int, None]],
    "points": Required[List["ViewPoint"]],
    "previous_points": Required[List["ViewPoint"]],
    },
)

ViewShape = Union["ViewShape1", "ViewShape2", "ViewShape3"]

ViewSummary = TypedDict(
    "ViewSummary",
    {
    "id": Required[str],
    "key": Required[str],
    "name": Required[str],
    "shape": Required[Literal["number", "over_time", "list"]],
    "visibility": Required["ViewVisibility"],
    "updated_at": Required[str],
    },
)

ViewVisibility = Literal["team"]

ViewWho = Union[Literal["everyone"], "ViewWho2"]

ViewWithAnswer = TypedDict(
    "ViewWithAnswer",
    {
    "id": Required[str],
    "key": Required[str],
    "name": Required[str],
    "shape": Required[Literal["number", "over_time", "list"]],
    "visibility": Required["ViewVisibility"],
    "updated_at": Required[str],
    "description": Required[Union[str, None]],
    "definition": Required["ViewDefinition"],
    "endpoint": Required[str],
    "made_by": Required[Literal["template", "member", "key", "agent"]],
    "template": Required[Union[str, None]],
    "dashboards": Required[List["ViewWithAnswerDashboardsItem"]],
    "created_at": Required[str],
    "answer": Required["ViewAnswer"],
    },
)

WebhookEndpoint = TypedDict(
    "WebhookEndpoint",
    {
    "id": Required[str],
    "url": Required[str],
    "events": Required[List[Literal["activity.created", "rule.live", "unit.used"]]],
    "description": Required[Union[str, None]],
    "status": Required[Literal["active", "disabled"]],
    "disabled_reason": Required[Literal["failing", "manual", None]],
    "created_at": Required[str],
    },
)

WebhookEndpointList = TypedDict(
    "WebhookEndpointList",
    {
    "data": Required[List["WebhookEndpoint"]],
    "has_more": Required[bool],
    "next_cursor": Required[Union[str, None]],
    },
)

Action1 = TypedDict(
    "Action1",
    {
    "unit": Required[str],
    "add": Required[Union[int, "AmountFrom"]],
    "hold_over": NotRequired[int],
    },
)

Action2 = TypedDict(
    "Action2",
    {
    "unit": Required[str],
    "remove": Required[Union[int, "AmountFrom"]],
    "hold_over": NotRequired[int],
    },
)

Action3 = TypedDict(
    "Action3",
    {
    "unit": Required[str],
    "reset": Required[Literal[True]],
    "hold_over": NotRequired[int],
    },
)

Action4 = TypedDict(
    "Action4",
    {
    "unit": Required[str],
    "streak": Required[Literal["extend", "reset"]],
    "hold_over": NotRequired[int],
    },
)

ActivityItemEvent = TypedDict(
    "ActivityItemEvent",
    {
    "id": Required[str],
    "name": Required[str],
    },
)

ActivityItemUser = TypedDict(
    "ActivityItemUser",
    {
    "id": Required[str],
    "external_id": Required[str],
    },
)

AgentKeyCreatedBy = TypedDict(
    "AgentKeyCreatedBy",
    {
    "kind": Required[Literal["member", "former_member", "bootstrap"]],
    "name": Required[Union[str, None]],
    },
)

ApiKeyCreatedBy = TypedDict(
    "ApiKeyCreatedBy",
    {
    "kind": Required[Literal["member", "former_member", "bootstrap"]],
    "name": Required[Union[str, None]],
    },
)

AudienceCondition1 = TypedDict(
    "AudienceCondition1",
    {
    "active": Required["AudienceCondition1Active"],
    },
)

AudienceCondition10 = TypedDict(
    "AudienceCondition10",
    {
    "chat_booster": Required["AudienceCondition10ChatBooster"],
    },
)

AudienceCondition10ChatBooster = TypedDict(
    "AudienceCondition10ChatBooster",
    {
    "community": Required[str],
    },
)

AudienceCondition11 = TypedDict(
    "AudienceCondition11",
    {
    "chat_tenure": Required["AudienceCondition11ChatTenure"],
    },
)

AudienceCondition11ChatTenure = TypedDict(
    "AudienceCondition11ChatTenure",
    {
    "community": Required[str],
    "gte": Required[int],
    },
)

AudienceCondition1Active = TypedDict(
    "AudienceCondition1Active",
    {
    "days": Required[int],
    "within_days": Required[int],
    },
)

AudienceCondition2 = TypedDict(
    "AudienceCondition2",
    {
    "first_seen": Required["AudienceCondition2FirstSeen"],
    },
)

AudienceCondition2FirstSeen = TypedDict(
    "AudienceCondition2FirstSeen",
    {
    "within_days": Required[int],
    },
)

AudienceCondition3 = TypedDict(
    "AudienceCondition3",
    {
    "inactive": Required["AudienceCondition3Inactive"],
    },
)

AudienceCondition3Inactive = TypedDict(
    "AudienceCondition3Inactive",
    {
    "days": Required[int],
    },
)

AudienceCondition4 = TypedDict(
    "AudienceCondition4",
    {
    "balance": Required["AudienceCondition4Balance"],
    },
)

AudienceCondition4Balance = TypedDict(
    "AudienceCondition4Balance",
    {
    "unit": Required[str],
    "gte": Required[int],
    },
)

AudienceCondition5 = TypedDict(
    "AudienceCondition5",
    {
    "property_total": Required["AudienceCondition5PropertyTotal"],
    },
)

AudienceCondition5PropertyTotal = TypedDict(
    "AudienceCondition5PropertyTotal",
    {
    "event": Required[str],
    "property": Required[str],
    "gte": Required[int],
    "within_days": Required[int],
    },
)

AudienceCondition6 = TypedDict(
    "AudienceCondition6",
    {
    "chat_role": Required["AudienceCondition6ChatRole"],
    },
)

AudienceCondition6ChatRole = TypedDict(
    "AudienceCondition6ChatRole",
    {
    "community": Required[str],
    "role": Required[str],
    "label": NotRequired[str],
    },
)

AudienceCondition7 = TypedDict(
    "AudienceCondition7",
    {
    "chat_group": Required["AudienceCondition7ChatGroup"],
    },
)

AudienceCondition7ChatGroup = TypedDict(
    "AudienceCondition7ChatGroup",
    {
    "community": Required[str],
    "group": Required[str],
    "label": NotRequired[str],
    },
)

AudienceCondition8 = TypedDict(
    "AudienceCondition8",
    {
    "chat_tag": Required["AudienceCondition8ChatTag"],
    },
)

AudienceCondition8ChatTag = TypedDict(
    "AudienceCondition8ChatTag",
    {
    "community": Required[str],
    "tag": Required[str],
    },
)

AudienceCondition9 = TypedDict(
    "AudienceCondition9",
    {
    "chat_admin": Required["AudienceCondition9ChatAdmin"],
    },
)

AudienceCondition9ChatAdmin = TypedDict(
    "AudienceCondition9ChatAdmin",
    {
    "community": Required[str],
    },
)

BriefActiveUsers = TypedDict(
    "BriefActiveUsers",
    {
    "value": Required[int],
    "previous": Required[int],
    },
)

BriefEvents = TypedDict(
    "BriefEvents",
    {
    "value": Required[int],
    "previous": Required[int],
    },
)

BriefGivenItem = TypedDict(
    "BriefGivenItem",
    {
    "unit": Required[str],
    "name": Required[str],
    "amount": Required[int],
    "previous": Required[int],
    },
)

BriefNewUsers = TypedDict(
    "BriefNewUsers",
    {
    "value": Required[int],
    "previous": Required[int],
    },
)

BudgetRule = TypedDict(
    "BudgetRule",
    {
    "id": Required[str],
    "key": Required[str],
    "name": Required[str],
    },
)

CatalogEventRulesItem = TypedDict(
    "CatalogEventRulesItem",
    {
    "id": Required[str],
    "key": Required[str],
    "name": Required[str],
    "status": Required[Literal["draft", "live", "paused"]],
    },
)

ChatMirrorCounts = TypedDict(
    "ChatMirrorCounts",
    {
    "wanted": Required[int],
    "holding": Required[int],
    "given_by_lurky": Required[int],
    "unknown_holders": Required[Union[int, None]],
    "without_account": Required[int],
    },
)

ChatMirrorProblem = TypedDict(
    "ChatMirrorProblem",
    {
    "code": Required[str],
    "message": Required[str],
    "fix": Required[str],
    },
)

ChatMirrorTarget = TypedDict(
    "ChatMirrorTarget",
    {
    "id": Required[str],
    "label": Required[str],
    },
)

ClientEventPropertyRule1 = TypedDict(
    "ClientEventPropertyRule1",
    {
    "name": Required[str],
    "type": Required[Literal["string"]],
    "max_length": Required[int],
    },
)

ClientEventPropertyRule2 = TypedDict(
    "ClientEventPropertyRule2",
    {
    "name": Required[str],
    "type": Required[Literal["number"]],
    "min": Required[float],
    "max": Required[float],
    },
)

ClientEventPropertyRule3 = TypedDict(
    "ClientEventPropertyRule3",
    {
    "name": Required[str],
    "type": Required[Literal["boolean"]],
    },
)

Condition1 = TypedDict(
    "Condition1",
    {
    "audience": Required[str],
    },
)

Condition2 = TypedDict(
    "Condition2",
    {
    "time": Required["Condition2Time"],
    },
)

Condition2Time = TypedDict(
    "Condition2Time",
    {
    "between": Required[List[Any]],
    },
)

Condition3 = TypedDict(
    "Condition3",
    {
    "property": Required["Condition3Property"],
    },
)

Condition3Property = TypedDict(
    "Condition3Property",
    {
    "name": Required[str],
    "equals": Required[Union[str, float, bool]],
    },
)

Condition4 = TypedDict(
    "Condition4",
    {
    "property_range": Required["Condition4PropertyRange"],
    },
)

Condition4PropertyRange = TypedDict(
    "Condition4PropertyRange",
    {
    "name": Required[str],
    "gte": NotRequired[float],
    "lte": NotRequired[float],
    },
)

Condition5 = TypedDict(
    "Condition5",
    {
    "balance": Required["Condition5Balance"],
    },
)

Condition5Balance = TypedDict(
    "Condition5Balance",
    {
    "unit": Required[str],
    "gte": Required[int],
    },
)

Condition6 = TypedDict(
    "Condition6",
    {
    "source": Required[Literal["trusted", "platform", "any"]],
    },
)

CreateAudienceInput1 = TypedDict(
    "CreateAudienceInput1",
    {
    "name": Required[str],
    "key": NotRequired[str],
    "description": NotRequired[str],
    "kind": Required[Literal["list"]],
    },
)

CreateAudienceInput2 = TypedDict(
    "CreateAudienceInput2",
    {
    "name": Required[str],
    "key": NotRequired[str],
    "description": NotRequired[str],
    "kind": Required[Literal["condition"]],
    "conditions": Required[List["AudienceCondition"]],
    },
)

CreatedAgentKeyCreatedBy = TypedDict(
    "CreatedAgentKeyCreatedBy",
    {
    "kind": Required[Literal["member", "former_member", "bootstrap"]],
    "name": Required[Union[str, None]],
    },
)

CreatedApiKeyCreatedBy = TypedDict(
    "CreatedApiKeyCreatedBy",
    {
    "kind": Required[Literal["member", "former_member", "bootstrap"]],
    "name": Required[Union[str, None]],
    },
)

CreatePromotionOutputProposal = TypedDict(
    "CreatePromotionOutputProposal",
    {
    "id": Required[str],
    "status": Required["ProposalStatus"],
    "title": Required[str],
    "summary": Required[str],
    "by": Required[str],
    "via": Required[Literal["api", "agent", "lurky", "dashboard", "system"]],
    "agent": Required[Union[str, None]],
    "changes": Required[List["ProposalChange"]],
    "created_at": Required[str],
    "expires_at": Required[str],
    "decided_at": Required[Union[str, None]],
    "decided_by": Required[Union[str, None]],
    "note": Required[Union[str, None]],
    "url": Required[Union[str, None]],
    },
)

CreateProposalInputChangesItem = TypedDict(
    "CreateProposalInputChangesItem",
    {
    "operation": Required["ProposableOperation"],
    "input": Required[Dict[str, Any]],
    },
)

CreateTrustedIssuerInputProfile1 = TypedDict(
    "CreateTrustedIssuerInputProfile1",
    {
    "provider": Required[Literal["supabase"]],
    "project_ref": Required[str],
    "audiences": NotRequired[List[str]],
    "algorithms": NotRequired[List[Literal["RS256", "ES256"]]],
    "max_token_lifetime_seconds": NotRequired[int],
    },
)

CreateTrustedIssuerInputProfile2 = TypedDict(
    "CreateTrustedIssuerInputProfile2",
    {
    "provider": Required[Literal["clerk"]],
    "issuer": Required[str],
    "authorized_parties": Required[List[str]],
    "audiences": NotRequired[List[str]],
    "max_token_lifetime_seconds": NotRequired[int],
    },
)

CreateTrustedIssuerInputProfile3 = TypedDict(
    "CreateTrustedIssuerInputProfile3",
    {
    "provider": Required[Literal["oidc"]],
    "issuer": Required[str],
    "jwks_url": Required[str],
    "audiences": Required[List[str]],
    "algorithms": Required[List[Literal["RS256", "ES256"]]],
    "max_token_lifetime_seconds": NotRequired[int],
    },
)

CreateUnitInputSwitches = TypedDict(
    "CreateUnitInputSwitches",
    {
    "goes_up": NotRequired[bool],
    "goes_down": NotRequired[bool],
    "spendable": NotRequired[bool],
    "usable": NotRequired[bool],
    "sendable": NotRequired[bool],
    "send_cap_per_day": NotRequired[int],
    "resets": NotRequired[bool],
    "starts_at": NotRequired[int],
    "held_by": NotRequired[Union[str, None]],
    "cap": NotRequired[Union[int, None]],
    "min_balance": NotRequired[int],
    "visible": NotRequired[bool],
    "supply": NotRequired[Union[int, None]],
    "expires_after_days": NotRequired[Union[int, None]],
    "expires_at": NotRequired[Union[str, None]],
    },
)

DecideProposalOutputAppliedItem = TypedDict(
    "DecideProposalOutputAppliedItem",
    {
    "operation": Required["ProposableOperation"],
    "target": Required[str],
    },
)

EndUserBlockedBy = TypedDict(
    "EndUserBlockedBy",
    {
    "id": Required[str],
    "name": Required[str],
    },
)

EndUserDetailBlockedBy = TypedDict(
    "EndUserDetailBlockedBy",
    {
    "id": Required[str],
    "name": Required[str],
    },
)

ErrorBodyError = TypedDict(
    "ErrorBodyError",
    {
    "status": Required[int],
    "code": Required[Literal["invalid_json", "invalid_key", "forbidden", "approval_required", "not_found", "idempotency_conflict", "conflict", "insufficient_balance", "reference_used", "validation_failed", "rate_limited", "internal", "unavailable"]],
    "message": Required[str],
    "param": NotRequired[str],
    "next_step": NotRequired[str],
    "request_id": Required[str],
    "doc_url": Required[str],
    },
)

FeedEffectEvent = TypedDict(
    "FeedEffectEvent",
    {
    "id": Required[str],
    "name": Required[str],
    },
)

FeedEffectRule = TypedDict(
    "FeedEffectRule",
    {
    "id": Required[str],
    "key": Required[str],
    "name": Required[str],
    },
)

FeedEffectUser = TypedDict(
    "FeedEffectUser",
    {
    "id": Required[str],
    "external_id": Required[str],
    },
)

FeedGivenEvent = TypedDict(
    "FeedGivenEvent",
    {
    "id": Required[str],
    "name": Required[str],
    },
)

FeedGivenUser = TypedDict(
    "FeedGivenUser",
    {
    "id": Required[str],
    "external_id": Required[str],
    },
)

FeedHeldChangesItem = TypedDict(
    "FeedHeldChangesItem",
    {
    "unit": Required[str],
    "change": Required[int],
    },
)

FeedHeldEvent = TypedDict(
    "FeedHeldEvent",
    {
    "id": Required[str],
    "name": Required[str],
    },
)

FeedHeldRule = TypedDict(
    "FeedHeldRule",
    {
    "id": Required[str],
    "key": Required[str],
    "name": Required[str],
    },
)

FeedHeldUser = TypedDict(
    "FeedHeldUser",
    {
    "id": Required[str],
    "external_id": Required[str],
    },
)

FeedMirrorMirror = TypedDict(
    "FeedMirrorMirror",
    {
    "id": Required[str],
    "label": Required[str],
    },
)

FeedMirrorUser = TypedDict(
    "FeedMirrorUser",
    {
    "id": Required[str],
    "external_id": Required[str],
    },
)

FeedSkippedEvent = TypedDict(
    "FeedSkippedEvent",
    {
    "id": Required[str],
    "name": Required[str],
    },
)

FeedSkippedRule = TypedDict(
    "FeedSkippedRule",
    {
    "id": Required[str],
    "key": Required[str],
    "name": Required[str],
    },
)

FeedSkippedUser = TypedDict(
    "FeedSkippedUser",
    {
    "id": Required[str],
    "external_id": Required[str],
    },
)

GiveLineUser = TypedDict(
    "GiveLineUser",
    {
    "id": Required[str],
    "external_id": Required[str],
    },
)

GivePreviewBudget = TypedDict(
    "GivePreviewBudget",
    {
    "rule": Required["GivePreviewBudgetRule"],
    "per": Required[Literal["day", "week", "month"]],
    "max": Required[int],
    "used_before": Required[int],
    "used_after": Required[int],
    },
)

GivePreviewBudgetRule = TypedDict(
    "GivePreviewBudgetRule",
    {
    "id": Required[str],
    "key": Required[str],
    "name": Required[str],
    },
)

GivePreviewTotals = TypedDict(
    "GivePreviewTotals",
    {
    "people": Required[int],
    "skipped": Required[int],
    "units": Required[int],
    },
)

GiveUnitsOutputBudget = TypedDict(
    "GiveUnitsOutputBudget",
    {
    "rule": Required["GiveUnitsOutputBudgetRule"],
    "per": Required[Literal["day", "week", "month"]],
    "max": Required[int],
    "used_before": Required[int],
    "used_after": Required[int],
    },
)

GiveUnitsOutputBudgetRule = TypedDict(
    "GiveUnitsOutputBudgetRule",
    {
    "id": Required[str],
    "key": Required[str],
    "name": Required[str],
    },
)

GiveUnitsOutputTotals = TypedDict(
    "GiveUnitsOutputTotals",
    {
    "people": Required[int],
    "skipped": Required[int],
    "units": Required[int],
    },
)

HeldChangesItem = TypedDict(
    "HeldChangesItem",
    {
    "unit": Required[str],
    "change": Required[int],
    },
)

HistoryEventSeenAs = TypedDict(
    "HistoryEventSeenAs",
    {
    "id": Required[str],
    "external_id": Required[str],
    },
)

HistoryReceiptSeenAs = TypedDict(
    "HistoryReceiptSeenAs",
    {
    "id": Required[str],
    "external_id": Required[str],
    },
)

HoldChangesItem = TypedDict(
    "HoldChangesItem",
    {
    "unit": Required[str],
    "change": Required[int],
    },
)

HoldEvent = TypedDict(
    "HoldEvent",
    {
    "id": Required[str],
    "name": Required[str],
    },
)

HoldRule = TypedDict(
    "HoldRule",
    {
    "id": Required[str],
    "key": Required[str],
    "name": Required[str],
    },
)

HoldUser = TypedDict(
    "HoldUser",
    {
    "id": Required[str],
    "external_id": Required[str],
    },
)

InstallTemplateOutputDashboardsItem = TypedDict(
    "InstallTemplateOutputDashboardsItem",
    {
    "id": Required[str],
    "name": Required[str],
    },
)

InstallTemplateOutputRulesItem = TypedDict(
    "InstallTemplateOutputRulesItem",
    {
    "id": Required[str],
    "key": Required[str],
    "name": Required[str],
    },
)

InstallTemplateOutputUnitsItem = TypedDict(
    "InstallTemplateOutputUnitsItem",
    {
    "id": Required[str],
    "key": Required[str],
    "name": Required[str],
    },
)

InstallTemplateOutputViewsItem = TypedDict(
    "InstallTemplateOutputViewsItem",
    {
    "id": Required[str],
    "key": Required[str],
    "name": Required[str],
    },
)

IntegrationInstallationHealth = TypedDict(
    "IntegrationInstallationHealth",
    {
    "status": Required[Literal["ok", "needs_attention"]],
    "checked_at": Required[str],
    "problems": Required[List["IntegrationProblem"]],
    },
)

IntegrationStat = TypedDict(
    "IntegrationStat",
    {
    "value": Required[int],
    "label": Required[str],
    },
)

InviteInvitedBy = TypedDict(
    "InviteInvitedBy",
    {
    "id": Required[str],
    "name": Required[str],
    },
)

IssuerIdentityMappedBy = TypedDict(
    "IssuerIdentityMappedBy",
    {
    "id": Required[str],
    "name": Required[str],
    },
)

KnownValuesSettingStopped = TypedDict(
    "KnownValuesSettingStopped",
    {
    "reason": Required["KnownValuesStopReason"],
    "message": Required[str],
    },
)

LurkyMessageToolsItem = TypedDict(
    "LurkyMessageToolsItem",
    {
    "operation": Required[str],
    "ok": Required[bool],
    },
)

LurkyUsageTokens = TypedDict(
    "LurkyUsageTokens",
    {
    "input": Required[int],
    "output": Required[int],
    "cache_read": Required[int],
    "cache_write": Required[int],
    },
)

MeMembership = TypedDict(
    "MeMembership",
    {
    "id": Required[str],
    "organization_id": Required[str],
    "project_id": Required[str],
    "role": Required["MemberRole"],
    },
)

Modifier1 = TypedDict(
    "Modifier1",
    {
    "if": Required[List["Condition"]],
    "unit": NotRequired[str],
    "times": Required[int],
    },
)

Modifier2 = TypedDict(
    "Modifier2",
    {
    "if": Required[List["Condition"]],
    "unit": NotRequired[str],
    "bonus": Required[int],
    },
)

MyInviteInvitedBy = TypedDict(
    "MyInviteInvitedBy",
    {
    "id": Required[str],
    "name": Required[str],
    },
)

MyInviteOrganization = TypedDict(
    "MyInviteOrganization",
    {
    "id": Required[str],
    "name": Required[str],
    },
)

PersonAliasPerson = TypedDict(
    "PersonAliasPerson",
    {
    "id": Required[str],
    "external_id": Required[str],
    },
)

PersonAliasUser = TypedDict(
    "PersonAliasUser",
    {
    "id": Required[str],
    "external_id": Required[str],
    },
)

PlanTemplateOutputRulesItem = TypedDict(
    "PlanTemplateOutputRulesItem",
    {
    "key": Required[str],
    "name": Required[str],
    "exists": Required[bool],
    "conflict": Required[bool],
    },
)

PlanTemplateOutputTestWeek = TypedDict(
    "PlanTemplateOutputTestWeek",
    {
    "users": Required[int],
    "events": Required[int],
    "receipts": Required[int],
    "given": Required[List["PlanTemplateOutputTestWeekGivenItem"]],
    "skipped": Required[int],
    },
)

PlanTemplateOutputTestWeekGivenItem = TypedDict(
    "PlanTemplateOutputTestWeekGivenItem",
    {
    "unit": Required[str],
    "amount": Required[int],
    },
)

PlanTemplateOutputUnitsItem = TypedDict(
    "PlanTemplateOutputUnitsItem",
    {
    "key": Required[str],
    "name": Required[str],
    "exists": Required[bool],
    },
)

PlanTemplateOutputViewsItem = TypedDict(
    "PlanTemplateOutputViewsItem",
    {
    "key": Required[str],
    "name": Required[str],
    "exists": Required[bool],
    },
)

PreviewRuleOutputBalance = TypedDict(
    "PreviewRuleOutputBalance",
    {
    "unit": Required[str],
    "reaches": Required[Union[int, None]],
    "every": Required[Union[int, None]],
    "fed_by": Required[List["PreviewRuleOutputBalanceFedByItem"]],
    "already_there": Required[Union[int, None]],
    },
)

PreviewRuleOutputBalanceFedByItem = TypedDict(
    "PreviewRuleOutputBalanceFedByItem",
    {
    "key": Required[str],
    "name": Required[str],
    "status": Required[Literal["draft", "live", "paused"]],
    },
)

PreviewRuleOutputSchedule = TypedDict(
    "PreviewRuleOutputSchedule",
    {
    "timezone": Required[str],
    "next": Required[List[str]],
    "people": Required[int],
    "audience": Required[Union[str, None]],
    },
)

PropertyValueSource1 = TypedDict(
    "PropertyValueSource1",
    {
    "kind": Required[Literal["enum"]],
    "values": Required[List["PropertyValueSource1ValuesItem"]],
    },
)

PropertyValueSource1ValuesItem = TypedDict(
    "PropertyValueSource1ValuesItem",
    {
    "value": Required[str],
    "label": Required[str],
    "installed": NotRequired[bool],
    },
)

PropertyValueSource2 = TypedDict(
    "PropertyValueSource2",
    {
    "kind": Required[Literal["community"]],
    },
)

PropertyValueSource3 = TypedDict(
    "PropertyValueSource3",
    {
    "kind": Required[Literal["channel"]],
    "community_property": Required[str],
    },
)

ProposalCardChangesItem = TypedDict(
    "ProposalCardChangesItem",
    {
    "operation": Required["ProposableOperation"],
    "target": Required["ProposalCardChangesItemTarget"],
    "summary": Required[str],
    "effect": Required[Union[str, None]],
    "lines": Required[List["CardLine"]],
    },
)

ProposalCardChangesItemTarget = TypedDict(
    "ProposalCardChangesItemTarget",
    {
    "type": Required[str],
    "id": Required[str],
    "name": Required[str],
    },
)

ProposalChangeTarget = TypedDict(
    "ProposalChangeTarget",
    {
    "type": Required[str],
    "id": Required[str],
    "name": Required[str],
    },
)

RemoveTemplateOutputKept = TypedDict(
    "RemoveTemplateOutputKept",
    {
    "rules": Required[int],
    "units": Required[int],
    "views": Required[int],
    },
)

RuleDefinition = TypedDict(
    "RuleDefinition",
    {
    "when": Required["RuleWhen"],
    "if": NotRequired[List["Condition"]],
    "limit": NotRequired[List["Limit"]],
    "do": Required[List["Action"]],
    "budget": NotRequired[List["RuleBudget"]],
    "modify": NotRequired[List["Modifier"]],
    "effects": NotRequired[List["RuleEffect"]],
    },
)

RuleDetailDefinition = TypedDict(
    "RuleDetailDefinition",
    {
    "when": Required["RuleWhen"],
    "if": NotRequired[List["Condition"]],
    "limit": NotRequired[List["Limit"]],
    "do": Required[List["Action"]],
    "budget": NotRequired[List["RuleBudget"]],
    "modify": NotRequired[List["Modifier"]],
    "effects": NotRequired[List["RuleEffect"]],
    },
)

RuleDetailLiveDefinition = TypedDict(
    "RuleDetailLiveDefinition",
    {
    "when": Required["RuleWhen"],
    "if": NotRequired[List["Condition"]],
    "limit": NotRequired[List["Limit"]],
    "do": Required[List["Action"]],
    "budget": NotRequired[List["RuleBudget"]],
    "modify": NotRequired[List["Modifier"]],
    "effects": NotRequired[List["RuleEffect"]],
    },
)

RuleEffect1 = TypedDict(
    "RuleEffect1",
    {
    "post": Required["PostEffect"],
    },
)

RuleEffect2 = TypedDict(
    "RuleEffect2",
    {
    "dm": Required["DmEffect"],
    },
)

RuleListItemDefinition = TypedDict(
    "RuleListItemDefinition",
    {
    "when": Required["RuleWhen"],
    "if": NotRequired[List["Condition"]],
    "limit": NotRequired[List["Limit"]],
    "do": Required[List["Action"]],
    "budget": NotRequired[List["RuleBudget"]],
    "modify": NotRequired[List["Modifier"]],
    "effects": NotRequired[List["RuleEffect"]],
    },
)

RuleWhen1 = TypedDict(
    "RuleWhen1",
    {
    "event": Required[str],
    },
)

RuleWhen2 = TypedDict(
    "RuleWhen2",
    {
    "schedule": Required["Schedule"],
    },
)

RuleWhen3 = TypedDict(
    "RuleWhen3",
    {
    "unit": Required[str],
    "reaches": Required[int],
    },
)

RuleWhen4 = TypedDict(
    "RuleWhen4",
    {
    "unit": Required[str],
    "every": Required[int],
    },
)

SendEventInputProfile = TypedDict(
    "SendEventInputProfile",
    {
    "email": NotRequired[Union[str, None]],
    "name": NotRequired[Union[str, None]],
    "avatar_url": NotRequired[Union[str, None]],
    "handles": NotRequired[Dict[str, "HandleChange"]],
    "locale": NotRequired[Union[str, None]],
    },
)

SendEventOutputAlias = TypedDict(
    "SendEventOutputAlias",
    {
    "made": Required[bool],
    "reason": NotRequired[str],
    },
)

SendFeedbackInputClient = TypedDict(
    "SendFeedbackInputClient",
    {
    "sdk": NotRequired["SendFeedbackInputClientSdk"],
    "agent": NotRequired["SendFeedbackInputClientAgent"],
    },
)

SendFeedbackInputClientAgent = TypedDict(
    "SendFeedbackInputClientAgent",
    {
    "name": Required[str],
    "version": Required[str],
    },
)

SendFeedbackInputClientSdk = TypedDict(
    "SendFeedbackInputClientSdk",
    {
    "name": Required[str],
    "version": Required[str],
    },
)

SendUnitsOutputFrom = TypedDict(
    "SendUnitsOutputFrom",
    {
    "id": Required[str],
    "external_id": Required[str],
    "balance_after": Required[int],
    },
)

SendUnitsOutputTo = TypedDict(
    "SendUnitsOutputTo",
    {
    "id": Required[str],
    "external_id": Required[str],
    "balance_after": Required[int],
    },
)

SpendUnitsOutputUser = TypedDict(
    "SpendUnitsOutputUser",
    {
    "id": Required[str],
    "external_id": Required[str],
    },
)

SuggestionOpens = TypedDict(
    "SuggestionOpens",
    {
    "page": Required["SuggestionPage"],
    "id": Required[Union[str, None]],
    },
)

TemplateAdds = TypedDict(
    "TemplateAdds",
    {
    "units": Required[List["TemplateAddsUnitsItem"]],
    "rules": Required[List["TemplateAddsRulesItem"]],
    "views": Required[List["TemplateAddsViewsItem"]],
    },
)

TemplateAddsRulesItem = TypedDict(
    "TemplateAddsRulesItem",
    {
    "key": Required[str],
    "name": Required[str],
    },
)

TemplateAddsUnitsItem = TypedDict(
    "TemplateAddsUnitsItem",
    {
    "key": Required[str],
    "name": Required[str],
    },
)

TemplateAddsViewsItem = TypedDict(
    "TemplateAddsViewsItem",
    {
    "key": Required[str],
    "name": Required[str],
    },
)

TemplateCounts = TypedDict(
    "TemplateCounts",
    {
    "units": Required[int],
    "rules": Required[int],
    "views": Required[int],
    },
)

TemplateSummaryCounts = TypedDict(
    "TemplateSummaryCounts",
    {
    "units": Required[int],
    "rules": Required[int],
    "views": Required[int],
    },
)

TestTrustedIssuerOutput1 = TypedDict(
    "TestTrustedIssuerOutput1",
    {
    "status": Required[Literal["verified"]],
    "issuer_id": Required[str],
    "revision": Required[int],
    "identity": Required[Union["TestTrustedIssuerOutput1Identity1", "TestTrustedIssuerOutput1Identity2"]],
    "access": Required[Literal["ready", "issuer_paused", "person_blocked", "not_yet_available"]],
    },
)

TestTrustedIssuerOutput1Identity1 = TypedDict(
    "TestTrustedIssuerOutput1Identity1",
    {
    "status": Required[Literal["unlinked"]],
    },
)

TestTrustedIssuerOutput1Identity2 = TypedDict(
    "TestTrustedIssuerOutput1Identity2",
    {
    "status": Required[Literal["linked"]],
    "person_id": Required[str],
    },
)

TestTrustedIssuerOutput2 = TypedDict(
    "TestTrustedIssuerOutput2",
    {
    "status": Required[Literal["refused"]],
    "code": Required[Literal["invalid_token", "wrong_issuer", "wrong_audience", "wrong_authorized_party", "pending_session", "anonymous_session", "expired", "lifetime_exceeded", "unsupported_algorithm", "unavailable", "configuration_changed"]],
    },
)

TrustedIssuerProfile1 = TypedDict(
    "TrustedIssuerProfile1",
    {
    "provider": Required[Literal["supabase"]],
    "project_ref": Required[str],
    "audiences": NotRequired[List[str]],
    "algorithms": NotRequired[List[Literal["RS256", "ES256"]]],
    "max_token_lifetime_seconds": NotRequired[int],
    },
)

TrustedIssuerProfile2 = TypedDict(
    "TrustedIssuerProfile2",
    {
    "provider": Required[Literal["clerk"]],
    "issuer": Required[str],
    "authorized_parties": Required[List[str]],
    "audiences": NotRequired[List[str]],
    "max_token_lifetime_seconds": NotRequired[int],
    },
)

TrustedIssuerProfile3 = TypedDict(
    "TrustedIssuerProfile3",
    {
    "provider": Required[Literal["oidc"]],
    "issuer": Required[str],
    "jwks_url": Required[str],
    "audiences": Required[List[str]],
    "algorithms": Required[List[Literal["RS256", "ES256"]]],
    "max_token_lifetime_seconds": NotRequired[int],
    },
)

UndoActivityOutputActivity = TypedDict(
    "UndoActivityOutputActivity",
    {
    "id": Required[str],
    "at": Required[str],
    "user": Required["UndoActivityOutputActivityUser"],
    "by": Required[str],
    "via": Required[Literal["api", "agent", "lurky", "dashboard", "system", "chat", "device"]],
    "agent": Required[Union[str, None]],
    "event": Required[Union["UndoActivityOutputActivityEvent", None]],
    "lines": Required[List["ActivityLine"]],
    "reverses": Required[Union[str, None]],
    "reversed_by": Required[Union[str, None]],
    "note": Required[Union[str, None]],
    "cause": Required[Literal["spend", "use", "send", "receive", None]],
    "reference": Required[Union[str, None]],
    "transfer": Required[Union[str, None]],
    },
)

UndoActivityOutputActivityEvent = TypedDict(
    "UndoActivityOutputActivityEvent",
    {
    "id": Required[str],
    "name": Required[str],
    },
)

UndoActivityOutputActivityUser = TypedDict(
    "UndoActivityOutputActivityUser",
    {
    "id": Required[str],
    "external_id": Required[str],
    },
)

UnitLeaderboardRowsItem = TypedDict(
    "UnitLeaderboardRowsItem",
    {
    "rank": Required[int],
    "user": Required[str],
    "amount": Required[int],
    },
)

UnitLeaderboardUnit = TypedDict(
    "UnitLeaderboardUnit",
    {
    "key": Required[str],
    "name": Required[str],
    },
)

UnitListCounts = TypedDict(
    "UnitListCounts",
    {
    "all": Required[int],
    "points": Required[int],
    "progress": Required[int],
    "badge": Required[int],
    "perk": Required[int],
    },
)

UnmergeUsersOutputWasMergedInto = TypedDict(
    "UnmergeUsersOutputWasMergedInto",
    {
    "id": Required[str],
    "external_id": Required[str],
    },
)

UseUnitsOutputUser = TypedDict(
    "UseUnitsOutputUser",
    {
    "id": Required[str],
    "external_id": Required[str],
    },
)

ViewDashboardsItem = TypedDict(
    "ViewDashboardsItem",
    {
    "id": Required[str],
    "name": Required[str],
    },
)

ViewMeasure1 = TypedDict(
    "ViewMeasure1",
    {
    "measure": Required[Literal["active_users", "returning_users", "new_users"]],
    },
)

ViewMeasure2 = TypedDict(
    "ViewMeasure2",
    {
    "measure": Required[Literal["events"]],
    "event": NotRequired[str],
    },
)

ViewMeasure3 = TypedDict(
    "ViewMeasure3",
    {
    "measure": Required[Literal["given", "spent", "held"]],
    "unit": Required[str],
    },
)

ViewRowProperty = TypedDict(
    "ViewRowProperty",
    {
    "value": Required[Union[str, None]],
    },
)

ViewRowRule = TypedDict(
    "ViewRowRule",
    {
    "id": Required[str],
    "key": Required[str],
    "name": Required[str],
    },
)

ViewRowUser = TypedDict(
    "ViewRowUser",
    {
    "id": Required[str],
    "external_id": Required[str],
    },
)

ViewShape1 = TypedDict(
    "ViewShape1",
    {
    "type": Required[Literal["number"]],
    },
)

ViewShape2 = TypedDict(
    "ViewShape2",
    {
    "type": Required[Literal["over_time"]],
    "every": Required[Literal["day", "week", "month"]],
    },
)

ViewShape3 = TypedDict(
    "ViewShape3",
    {
    "type": Required[Literal["list"]],
    "by": Required[Literal["user", "rule", "property"]],
    "property": NotRequired[str],
    "size": Required[int],
    },
)

ViewWho2 = TypedDict(
    "ViewWho2",
    {
    "audience": Required[str],
    },
)

ViewWithAnswerDashboardsItem = TypedDict(
    "ViewWithAnswerDashboardsItem",
    {
    "id": Required[str],
    "name": Required[str],
    },
)
