"""Generated from openapi/openapi.json by scripts/generate.ts. Do not edit."""

from __future__ import annotations

from typing import Any, Dict, List, Literal, NotRequired, Required, TypedDict, Union

from .schema import (
    ActivityList,
    AddAudienceUsersOutput,
    AgentKey,
    AgentKeyList,
    ApiKey,
    ApiKeyList,
    Audience,
    AudienceList,
    Brief,
    BudgetList,
    CreatePromotionOutput,
    CreatedAgentKey,
    CreatedApiKey,
    CreatedWebhookEndpoint,
    CsvExport,
    Dashboard,
    DashboardList,
    DashboardSummary,
    DashboardWithAnswers,
    DecideHoldOutput,
    DecideProposalOutput,
    DeclinedInvite,
    DeleteLurkyConversationOutput,
    DeletedWebhookEndpoint,
    EndUserDetail,
    EventsCatalog,
    ExplainActivityOutput,
    ExportDownload,
    ExportJob,
    ExportJobList,
    FeedList,
    GivePreview,
    GiveUnitsOutput,
    Hold,
    HoldList,
    InstallTemplateOutput,
    IntegrationHealthOutput,
    IntegrationList,
    Invite,
    LurkyConversation,
    LurkyConversationList,
    LurkySettings,
    LurkyUsage,
    Me,
    Member,
    MemberList,
    MyInviteList,
    Organization,
    OrganizationList,
    PlanTemplateOutput,
    PreviewPromotionOutput,
    PreviewRuleOutput,
    Project,
    ProjectClock,
    ProjectList,
    ProjectSetup,
    Proposal,
    ProposalCard,
    ProposalList,
    RemoveTemplateOutput,
    RemovedMember,
    RevokedInvite,
    Rule,
    RuleDetail,
    RuleList,
    RuleStatsOutput,
    SendEventOutput,
    SendUnitsOutput,
    SpendUnitsOutput,
    SuggestionHidden,
    SuggestionList,
    Template,
    TemplateList,
    UndoActivityOutput,
    Unit,
    UnitList,
    UseUnitsOutput,
    UserList,
    View,
    ViewList,
    ViewWithAnswer,
    WebhookEndpointList,
)


ActivityExplainInput = TypedDict(
    "ActivityExplainInput",
    {
    "id": Required[str],
    },
)

ActivityExportInput = TypedDict(
    "ActivityExportInput",
    {
    "user": NotRequired[str],
    "rule": NotRequired[str],
    "unit": NotRequired[str],
    "since": NotRequired[str],
    "until": NotRequired[str],
    },
)

ActivityFeedInput = TypedDict(
    "ActivityFeedInput",
    {
    "limit": NotRequired[int],
    "cursor": NotRequired[str],
    "kind": NotRequired[Literal["all", "given", "skipped", "held"]],
    "user": NotRequired[str],
    "rule": NotRequired[str],
    "unit": NotRequired[str],
    "since": NotRequired[str],
    "until": NotRequired[str],
    },
)

ActivityListInput = TypedDict(
    "ActivityListInput",
    {
    "limit": NotRequired[int],
    "cursor": NotRequired[str],
    "user": NotRequired[str],
    "rule": NotRequired[str],
    "unit": NotRequired[str],
    "cause": NotRequired[Literal["spend", "use", "send", "receive"]],
    "transfer": NotRequired[str],
    "since": NotRequired[str],
    "until": NotRequired[str],
    },
)

ActivityUndoInput = TypedDict(
    "ActivityUndoInput",
    {
    "id": Required[str],
    },
)

AgentKeysCreateInput = TypedDict(
    "AgentKeysCreateInput",
    {
    "name": Required[str],
    },
)

AgentKeysListInput = TypedDict(
    "AgentKeysListInput",
    {
    "limit": NotRequired[int],
    "cursor": NotRequired[str],
    },
)

AgentKeysRevokeInput = TypedDict(
    "AgentKeysRevokeInput",
    {
    "id": Required[str],
    },
)

ApiKeysCreateInput = TypedDict(
    "ApiKeysCreateInput",
    {
    "name": Required[str],
    "expires_at": NotRequired[str],
    },
)

ApiKeysListInput = TypedDict(
    "ApiKeysListInput",
    {
    "limit": NotRequired[int],
    "cursor": NotRequired[str],
    },
)

ApiKeysRevokeInput = TypedDict(
    "ApiKeysRevokeInput",
    {
    "id": Required[str],
    },
)

AudiencesAddUsersInput = TypedDict(
    "AudiencesAddUsersInput",
    {
    "id": Required[str],
    "users": Required[List[str]],
    },
)

AudiencesCreateInput1 = TypedDict(
    "AudiencesCreateInput1",
    {
    "name": Required[str],
    "key": NotRequired[str],
    "description": NotRequired[str],
    "kind": Required[Literal["list"]],
    },
)

AudiencesCreateInput2 = TypedDict(
    "AudiencesCreateInput2",
    {
    "name": Required[str],
    "key": NotRequired[str],
    "description": NotRequired[str],
    "kind": Required[Literal["condition"]],
    "conditions": Required[List["AudienceCondition"]],
    },
)

AudiencesListInput = TypedDict(
    "AudiencesListInput",
    {
    "limit": NotRequired[int],
    "cursor": NotRequired[str],
    "kind": NotRequired["AudienceKind"],
    },
)

BudgetsListInput = TypedDict(
    "BudgetsListInput",
    {
    "limit": NotRequired[int],
    "cursor": NotRequired[str],
    "rule": NotRequired[str],
    "nearly_used": NotRequired[Union[bool, str]],
    },
)

ClocksAdvanceInput = TypedDict(
    "ClocksAdvanceInput",
    {
    "days": NotRequired[int],
    "hours": NotRequired[int],
    "minutes": NotRequired[int],
    },
)

ClocksSetInput = TypedDict(
    "ClocksSetInput",
    {
    "to": Required[str],
    },
)

DashboardsCreateInput = TypedDict(
    "DashboardsCreateInput",
    {
    "name": Required[str],
    "unit": NotRequired[str],
    "tiles": NotRequired[List["DashboardTileInput"]],
    },
)

DashboardsGetInput = TypedDict(
    "DashboardsGetInput",
    {
    "id": Required[str],
    },
)

DashboardsListInput = TypedDict(
    "DashboardsListInput",
    {
    "limit": NotRequired[int],
    "cursor": NotRequired[str],
    "pinned": NotRequired[Union[bool, str]],
    "unit": NotRequired[str],
    },
)

DashboardsPinInput = TypedDict(
    "DashboardsPinInput",
    {
    "id": Required[str],
    "pinned": Required[bool],
    },
)

DashboardsReadInput = TypedDict(
    "DashboardsReadInput",
    {
    "id": Required[str],
    "range": NotRequired[Literal["now", "today", "this_week", "last_week", "last_7_days", "last_14_days", "last_30_days", "last_90_days", "this_month", "all_time"]],
    "compare": NotRequired[Union[bool, str]],
    "audience": NotRequired[str],
    },
)

DashboardsUpdateInput = TypedDict(
    "DashboardsUpdateInput",
    {
    "id": Required[str],
    "name": NotRequired[str],
    "home": NotRequired[Literal[True]],
    "tiles": NotRequired[List["DashboardTileInput"]],
    },
)

EventsCatalogInput = TypedDict(
    "EventsCatalogInput",
    {
    "limit": NotRequired[int],
    "cursor": NotRequired[str],
    "search": NotRequired[str],
    },
)

EventsSendInput = TypedDict(
    "EventsSendInput",
    {
    "event": Required[str],
    "user": Required[str],
    "properties": NotRequired[Dict[str, Union[str, float, bool, None, List[Union[str, float, bool, None]]]]],
    "idempotency_key": NotRequired[str],
    "timestamp": NotRequired[str],
    },
)

ExportsCancelInput = TypedDict(
    "ExportsCancelInput",
    {
    "id": Required[str],
    },
)

ExportsCreateInput = TypedDict(
    "ExportsCreateInput",
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

ExportsDownloadInput = TypedDict(
    "ExportsDownloadInput",
    {
    "id": Required[str],
    },
)

ExportsGetInput = TypedDict(
    "ExportsGetInput",
    {
    "id": Required[str],
    },
)

ExportsListInput = TypedDict(
    "ExportsListInput",
    {
    "limit": NotRequired[int],
    "cursor": NotRequired[str],
    },
)

HoldsDecideInput = TypedDict(
    "HoldsDecideInput",
    {
    "id": Required[str],
    "decision": Required[Literal["give", "refuse"]],
    "note": NotRequired[str],
    },
)

HoldsGetInput = TypedDict(
    "HoldsGetInput",
    {
    "id": Required[str],
    },
)

HoldsListInput = TypedDict(
    "HoldsListInput",
    {
    "limit": NotRequired[int],
    "cursor": NotRequired[str],
    "status": NotRequired[Literal["held", "given", "refused"]],
    "user": NotRequired[str],
    "rule": NotRequired[str],
    },
)

IntegrationsHealthInput = TypedDict(
    "IntegrationsHealthInput",
    {
    "key": NotRequired[str],
    },
)

IntegrationsListInput = TypedDict(
    "IntegrationsListInput",
    {
    "limit": NotRequired[int],
    "cursor": NotRequired[str],
    "filter": NotRequired[Literal["all", "connected", "events_in", "mirrored_out"]],
    },
)

InvitesAcceptInput = TypedDict(
    "InvitesAcceptInput",
    {
    "id": Required[str],
    },
)

InvitesDeclineInput = TypedDict(
    "InvitesDeclineInput",
    {
    "id": Required[str],
    },
)

InvitesListInput = TypedDict(
    "InvitesListInput",
    {
    "limit": NotRequired[int],
    "cursor": NotRequired[str],
    },
)

InvitesRevokeInput = TypedDict(
    "InvitesRevokeInput",
    {
    "id": Required[str],
    },
)

LurkyDeleteConversationInput = TypedDict(
    "LurkyDeleteConversationInput",
    {
    "id": Required[str],
    },
)

LurkyGetConversationInput = TypedDict(
    "LurkyGetConversationInput",
    {
    "id": Required[str],
    },
)

LurkyHideSuggestionInput = TypedDict(
    "LurkyHideSuggestionInput",
    {
    "id": Required[str],
    "signature": Required[str],
    },
)

LurkyListConversationsInput = TypedDict(
    "LurkyListConversationsInput",
    {
    "limit": NotRequired[int],
    "cursor": NotRequired[str],
    },
)

LurkyShowSuggestionInput = TypedDict(
    "LurkyShowSuggestionInput",
    {
    "id": Required[str],
    },
)

LurkyUpdateSettingsInput = TypedDict(
    "LurkyUpdateSettingsInput",
    {
    "enabled": Required[bool],
    },
)

MembersInviteInput = TypedDict(
    "MembersInviteInput",
    {
    "organization_id": Required[str],
    "email": Required[str],
    "role": Required["AssignableRole"],
    },
)

MembersListInput = TypedDict(
    "MembersListInput",
    {
    "organization_id": Required[str],
    "limit": NotRequired[int],
    "cursor": NotRequired[str],
    "status": NotRequired[Literal["active", "invited"]],
    },
)

MembersRemoveInput = TypedDict(
    "MembersRemoveInput",
    {
    "id": Required[str],
    },
)

MembersUpdateInput = TypedDict(
    "MembersUpdateInput",
    {
    "id": Required[str],
    "role": Required["AssignableRole"],
    },
)

OrganizationsCreateInput = TypedDict(
    "OrganizationsCreateInput",
    {
    "name": Required[str],
    "slug": NotRequired[str],
    },
)

OrganizationsListInput = TypedDict(
    "OrganizationsListInput",
    {
    "limit": NotRequired[int],
    "cursor": NotRequired[str],
    },
)

ProjectsCreateInput = TypedDict(
    "ProjectsCreateInput",
    {
    "organization_id": Required[str],
    "name": Required[str],
    "slug": NotRequired[str],
    "kind": NotRequired["ProjectKind"],
    "timezone": NotRequired[str],
    },
)

ProjectsGetInput = TypedDict(
    "ProjectsGetInput",
    {
    "id": Required[str],
    },
)

ProjectsListInput = TypedDict(
    "ProjectsListInput",
    {
    "limit": NotRequired[int],
    "cursor": NotRequired[str],
    "organization_id": Required[str],
    },
)

ProjectsUpdateInput = TypedDict(
    "ProjectsUpdateInput",
    {
    "id": Required[str],
    "name": NotRequired[str],
    "timezone": NotRequired[str],
    "approvers": NotRequired["Approvers"],
    "new_for_days": NotRequired[int],
    "lapsing_after_days": NotRequired[int],
    },
)

PromotionsCreateInput = TypedDict(
    "PromotionsCreateInput",
    {
    "from": Required[str],
    "to": Required[str],
    "rules": NotRequired[List[str]],
    "units": NotRequired[List[str]],
    "title": NotRequired[str],
    "summary": NotRequired[str],
    },
)

PromotionsPreviewInput = TypedDict(
    "PromotionsPreviewInput",
    {
    "from": Required[str],
    "to": Required[str],
    "rules": NotRequired[List[str]],
    "units": NotRequired[List[str]],
    "title": NotRequired[str],
    "summary": NotRequired[str],
    },
)

ProposalsCardInput = TypedDict(
    "ProposalsCardInput",
    {
    "id": Required[str],
    },
)

ProposalsCreateInput = TypedDict(
    "ProposalsCreateInput",
    {
    "title": NotRequired[str],
    "summary": NotRequired[str],
    "changes": Required[List["ProposalsCreateInputChangesItem"]],
    },
)

ProposalsCreateInputChangesItem = TypedDict(
    "ProposalsCreateInputChangesItem",
    {
    "operation": Required["ProposableOperation"],
    "input": Required[Dict[str, Any]],
    },
)

ProposalsDecideInput = TypedDict(
    "ProposalsDecideInput",
    {
    "id": Required[str],
    "decision": Required[Literal["approve", "decline"]],
    "note": NotRequired[str],
    },
)

ProposalsGetInput = TypedDict(
    "ProposalsGetInput",
    {
    "id": Required[str],
    },
)

ProposalsListInput = TypedDict(
    "ProposalsListInput",
    {
    "limit": NotRequired[int],
    "cursor": NotRequired[str],
    "status": NotRequired[Literal["open", "approved", "declined", "expired"]],
    },
)

RulesCreateInput = TypedDict(
    "RulesCreateInput",
    {
    "name": Required[str],
    "key": NotRequired[str],
    "when": Required["RuleWhen"],
    "if": NotRequired[List["Condition"]],
    "limit": NotRequired[List["Limit"]],
    "do": Required[List["Action"]],
    "budget": NotRequired[List["RuleBudget"]],
    "modify": NotRequired[List["Modifier"]],
    },
)

RulesGetInput = TypedDict(
    "RulesGetInput",
    {
    "id": Required[str],
    },
)

RulesListInput = TypedDict(
    "RulesListInput",
    {
    "limit": NotRequired[int],
    "cursor": NotRequired[str],
    "status": NotRequired[Literal["draft", "live", "paused"]],
    "unit": NotRequired[str],
    "event": NotRequired[str],
    "search": NotRequired[str],
    },
)

RulesPauseInput = TypedDict(
    "RulesPauseInput",
    {
    "id": Required[str],
    },
)

RulesPreviewInput = TypedDict(
    "RulesPreviewInput",
    {
    "id": Required[str],
    "days": NotRequired[int],
    "definition": NotRequired["RulesPreviewInputDefinition"],
    },
)

RulesPreviewInputDefinition = TypedDict(
    "RulesPreviewInputDefinition",
    {
    "when": Required["RuleWhen"],
    "if": NotRequired[List["Condition"]],
    "limit": NotRequired[List["Limit"]],
    "do": Required[List["Action"]],
    "budget": NotRequired[List["RuleBudget"]],
    "modify": NotRequired[List["Modifier"]],
    },
)

RulesPublishInput = TypedDict(
    "RulesPublishInput",
    {
    "id": Required[str],
    },
)

RulesResumeInput = TypedDict(
    "RulesResumeInput",
    {
    "id": Required[str],
    },
)

RulesStatsInput = TypedDict(
    "RulesStatsInput",
    {
    "id": Required[str],
    "days": NotRequired[int],
    },
)

RulesUpdateInput = TypedDict(
    "RulesUpdateInput",
    {
    "id": Required[str],
    "name": NotRequired[str],
    "when": NotRequired["RuleWhen"],
    "if": NotRequired[List["Condition"]],
    "limit": NotRequired[List["Limit"]],
    "do": NotRequired[List["Action"]],
    "budget": NotRequired[List["RuleBudget"]],
    "modify": NotRequired[List["Modifier"]],
    },
)

TemplatesGetInput = TypedDict(
    "TemplatesGetInput",
    {
    "id": Required[str],
    },
)

TemplatesInstallInput = TypedDict(
    "TemplatesInstallInput",
    {
    "id": Required[str],
    "settings": NotRequired[Dict[str, Union[str, int]]],
    },
)

TemplatesListInput = TypedDict(
    "TemplatesListInput",
    {
    "limit": NotRequired[int],
    "cursor": NotRequired[str],
    "filter": NotRequired[Literal["all", "in_use"]],
    "category": NotRequired["TemplateCategory"],
    },
)

TemplatesPlanInput = TypedDict(
    "TemplatesPlanInput",
    {
    "id": Required[str],
    "settings": NotRequired[Dict[str, Union[str, int]]],
    },
)

TemplatesRemoveInput = TypedDict(
    "TemplatesRemoveInput",
    {
    "id": Required[str],
    },
)

UnitsCreateInput = TypedDict(
    "UnitsCreateInput",
    {
    "name": Required[str],
    "key": NotRequired[str],
    "singular": NotRequired[str],
    "group": Required["UnitGroup"],
    "shows_as": NotRequired[Literal["amount", "thing", "level"]],
    "color": NotRequired[Literal["blue", "green", "amber", "red", "purple", "pink", "teal", "gray"]],
    "switches": NotRequired["UnitsCreateInputSwitches"],
    },
)

UnitsCreateInputSwitches = TypedDict(
    "UnitsCreateInputSwitches",
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

UnitsGetInput = TypedDict(
    "UnitsGetInput",
    {
    "id": Required[str],
    },
)

UnitsGiveInput = TypedDict(
    "UnitsGiveInput",
    {
    "unit": Required[str],
    "amount": Required[int],
    "users": Required[List[str]],
    "note": NotRequired[str],
    "count_against": NotRequired[str],
    },
)

UnitsGivePreviewInput = TypedDict(
    "UnitsGivePreviewInput",
    {
    "unit": Required[str],
    "amount": Required[int],
    "users": Required[List[str]],
    "note": NotRequired[str],
    "count_against": NotRequired[str],
    },
)

UnitsListInput = TypedDict(
    "UnitsListInput",
    {
    "limit": NotRequired[int],
    "cursor": NotRequired[str],
    "group": NotRequired["UnitGroup"],
    },
)

UnitsSendInput = TypedDict(
    "UnitsSendInput",
    {
    "from": Required[str],
    "to": Required[str],
    "unit": Required[str],
    "amount": Required[int],
    "reason": NotRequired[str],
    },
)

UnitsSpendInput = TypedDict(
    "UnitsSpendInput",
    {
    "user": Required[str],
    "unit": Required[str],
    "amount": Required[int],
    "reason": Required[str],
    "reference": NotRequired[str],
    },
)

UnitsUpdateInput = TypedDict(
    "UnitsUpdateInput",
    {
    "id": Required[str],
    "name": NotRequired[str],
    "singular": NotRequired[str],
    "group": NotRequired["UnitGroup"],
    "shows_as": NotRequired["UnitShowsAs"],
    "color": NotRequired[Literal["blue", "green", "amber", "red", "purple", "pink", "teal", "gray", None]],
    "switches": NotRequired["UnitsUpdateInputSwitches"],
    },
)

UnitsUpdateInputSwitches = TypedDict(
    "UnitsUpdateInputSwitches",
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

UnitsUseInput = TypedDict(
    "UnitsUseInput",
    {
    "user": Required[str],
    "unit": Required[str],
    "amount": NotRequired[int],
    "reason": NotRequired[str],
    "reference": NotRequired[str],
    },
)

UsersExportInput = TypedDict(
    "UsersExportInput",
    {
    "search": NotRequired[str],
    },
)

UsersGetInput = TypedDict(
    "UsersGetInput",
    {
    "id": Required[str],
    },
)

UsersListInput = TypedDict(
    "UsersListInput",
    {
    "limit": NotRequired[int],
    "cursor": NotRequired[str],
    "search": NotRequired[str],
    "audience": NotRequired[str],
    "status": NotRequired[Literal["new", "returning", "lapsing"]],
    "sort": NotRequired[Literal["newest", "oldest"]],
    "include": NotRequired[Literal["total"]],
    },
)

ViewsCreateInput = TypedDict(
    "ViewsCreateInput",
    {
    "name": Required[str],
    "key": NotRequired[str],
    "description": NotRequired[str],
    "definition": Required["ViewDefinition"],
    },
)

ViewsGetInput = TypedDict(
    "ViewsGetInput",
    {
    "id": Required[str],
    "range": NotRequired[Literal["now", "today", "this_week", "last_week", "last_7_days", "last_14_days", "last_30_days", "last_90_days", "this_month", "all_time"]],
    "compare": NotRequired[Union[bool, str]],
    "audience": NotRequired[str],
    },
)

ViewsListInput = TypedDict(
    "ViewsListInput",
    {
    "limit": NotRequired[int],
    "cursor": NotRequired[str],
    "search": NotRequired[str],
    },
)

ViewsUpdateInput = TypedDict(
    "ViewsUpdateInput",
    {
    "id": Required[str],
    "name": NotRequired[str],
    "description": NotRequired[Union[str, None]],
    "definition": NotRequired["ViewsUpdateInputDefinition"],
    },
)

ViewsUpdateInputDefinition = TypedDict(
    "ViewsUpdateInputDefinition",
    {
    "who": Required["ViewWho"],
    "what": Required[List["ViewMeasure"]],
    "over": Required["ViewRange"],
    "shape": Required["ViewShape"],
    },
)

WebhookEndpointsCreateInput = TypedDict(
    "WebhookEndpointsCreateInput",
    {
    "url": Required[str],
    "events": NotRequired[List[Literal["activity.created", "rule.live", "unit.used"]]],
    "description": NotRequired[str],
    },
)

WebhookEndpointsDeleteInput = TypedDict(
    "WebhookEndpointsDeleteInput",
    {
    "id": Required[str],
    },
)

WebhookEndpointsListInput = TypedDict(
    "WebhookEndpointsListInput",
    {
    "limit": NotRequired[int],
    "cursor": NotRequired[str],
    },
)


EventsSendInput = EventsSendInput
EventsSendOutput = SendEventOutput
EventsCatalogInput = EventsCatalogInput
EventsCatalogOutput = EventsCatalog
ActivityListInput = ActivityListInput
ActivityListOutput = ActivityList
ActivityExportInput = ActivityExportInput
ActivityExportOutput = CsvExport
ActivityExplainInput = ActivityExplainInput
ActivityExplainOutput = ExplainActivityOutput
ActivityUndoInput = ActivityUndoInput
ActivityUndoOutput = UndoActivityOutput
UsersListInput = UsersListInput
UsersListOutput = UserList
UsersExportInput = UsersExportInput
UsersExportOutput = CsvExport
UsersGetInput = UsersGetInput
UsersGetOutput = EndUserDetail
UnitsListInput = UnitsListInput
UnitsListOutput = UnitList
UnitsCreateInput = UnitsCreateInput
UnitsCreateOutput = Unit
UnitsGetInput = UnitsGetInput
UnitsGetOutput = Unit
UnitsUpdateInput = UnitsUpdateInput
UnitsUpdateOutput = Unit
RulesCreateInput = RulesCreateInput
RulesCreateOutput = Rule
RulesListInput = RulesListInput
RulesListOutput = RuleList
RulesPublishInput = RulesPublishInput
RulesPublishOutput = Rule
RulesGetInput = RulesGetInput
RulesGetOutput = RuleDetail
RulesUpdateInput = RulesUpdateInput
RulesUpdateOutput = Rule
RulesPauseInput = RulesPauseInput
RulesPauseOutput = Rule
RulesResumeInput = RulesResumeInput
RulesResumeOutput = Rule
RulesPreviewInput = RulesPreviewInput
RulesPreviewOutput = PreviewRuleOutput
RulesStatsInput = RulesStatsInput
RulesStatsOutput = RuleStatsOutput
ApiKeysCreateInput = ApiKeysCreateInput
ApiKeysCreateOutput = CreatedApiKey
ApiKeysListInput = ApiKeysListInput
ApiKeysListOutput = ApiKeyList
ApiKeysRevokeInput = ApiKeysRevokeInput
ApiKeysRevokeOutput = ApiKey
WebhookEndpointsCreateInput = WebhookEndpointsCreateInput
WebhookEndpointsCreateOutput = CreatedWebhookEndpoint
WebhookEndpointsListInput = WebhookEndpointsListInput
WebhookEndpointsListOutput = WebhookEndpointList
WebhookEndpointsDeleteInput = WebhookEndpointsDeleteInput
WebhookEndpointsDeleteOutput = DeletedWebhookEndpoint
MembersMeInput = Dict[str, Any]
MembersMeOutput = Me
OrganizationsListInput = OrganizationsListInput
OrganizationsListOutput = OrganizationList
OrganizationsCreateInput = OrganizationsCreateInput
OrganizationsCreateOutput = Organization
ProjectsListInput = ProjectsListInput
ProjectsListOutput = ProjectList
ProjectsCreateInput = ProjectsCreateInput
ProjectsCreateOutput = Project
ProjectsGetInput = ProjectsGetInput
ProjectsGetOutput = Project
ProjectsUpdateInput = ProjectsUpdateInput
ProjectsUpdateOutput = Project
MembersListInput = MembersListInput
MembersListOutput = MemberList
MembersInviteInput = MembersInviteInput
MembersInviteOutput = Invite
InvitesListInput = InvitesListInput
InvitesListOutput = MyInviteList
MembersUpdateInput = MembersUpdateInput
MembersUpdateOutput = Member
MembersRemoveInput = MembersRemoveInput
MembersRemoveOutput = RemovedMember
InvitesRevokeInput = InvitesRevokeInput
InvitesRevokeOutput = RevokedInvite
InvitesAcceptInput = InvitesAcceptInput
InvitesAcceptOutput = Organization
InvitesDeclineInput = InvitesDeclineInput
InvitesDeclineOutput = DeclinedInvite
ProposalsCreateInput = ProposalsCreateInput
ProposalsCreateOutput = Proposal
ProposalsListInput = ProposalsListInput
ProposalsListOutput = ProposalList
PromotionsCreateInput = PromotionsCreateInput
PromotionsCreateOutput = CreatePromotionOutput
PromotionsPreviewInput = PromotionsPreviewInput
PromotionsPreviewOutput = PreviewPromotionOutput
ProposalsGetInput = ProposalsGetInput
ProposalsGetOutput = Proposal
ProposalsCardInput = ProposalsCardInput
ProposalsCardOutput = ProposalCard
LurkyUsageInput = Dict[str, Any]
LurkyUsageOutput = LurkyUsage
LurkyGetSettingsInput = Dict[str, Any]
LurkyGetSettingsOutput = LurkySettings
LurkyUpdateSettingsInput = LurkyUpdateSettingsInput
LurkyUpdateSettingsOutput = LurkySettings
LurkyListConversationsInput = LurkyListConversationsInput
LurkyListConversationsOutput = LurkyConversationList
LurkyGetConversationInput = LurkyGetConversationInput
LurkyGetConversationOutput = LurkyConversation
LurkyDeleteConversationInput = LurkyDeleteConversationInput
LurkyDeleteConversationOutput = DeleteLurkyConversationOutput
ProposalsDecideInput = ProposalsDecideInput
ProposalsDecideOutput = DecideProposalOutput
HoldsListInput = HoldsListInput
HoldsListOutput = HoldList
HoldsGetInput = HoldsGetInput
HoldsGetOutput = Hold
HoldsDecideInput = HoldsDecideInput
HoldsDecideOutput = DecideHoldOutput
AgentKeysCreateInput = AgentKeysCreateInput
AgentKeysCreateOutput = CreatedAgentKey
AgentKeysListInput = AgentKeysListInput
AgentKeysListOutput = AgentKeyList
AgentKeysRevokeInput = AgentKeysRevokeInput
AgentKeysRevokeOutput = AgentKey
AudiencesListInput = AudiencesListInput
AudiencesListOutput = AudienceList
AudiencesCreateInput = Union["AudiencesCreateInput1", "AudiencesCreateInput2"]
AudiencesCreateOutput = Audience
AudiencesAddUsersInput = AudiencesAddUsersInput
AudiencesAddUsersOutput = AddAudienceUsersOutput
BudgetsListInput = BudgetsListInput
BudgetsListOutput = BudgetList
ActivityFeedInput = ActivityFeedInput
ActivityFeedOutput = FeedList
TemplatesListInput = TemplatesListInput
TemplatesListOutput = TemplateList
TemplatesGetInput = TemplatesGetInput
TemplatesGetOutput = Template
TemplatesPlanInput = TemplatesPlanInput
TemplatesPlanOutput = PlanTemplateOutput
TemplatesInstallInput = TemplatesInstallInput
TemplatesInstallOutput = InstallTemplateOutput
TemplatesRemoveInput = TemplatesRemoveInput
TemplatesRemoveOutput = RemoveTemplateOutput
UnitsGivePreviewInput = UnitsGivePreviewInput
UnitsGivePreviewOutput = GivePreview
UnitsGiveInput = UnitsGiveInput
UnitsGiveOutput = GiveUnitsOutput
UnitsSpendInput = UnitsSpendInput
UnitsSpendOutput = SpendUnitsOutput
UnitsSendInput = UnitsSendInput
UnitsSendOutput = SendUnitsOutput
UnitsUseInput = UnitsUseInput
UnitsUseOutput = UseUnitsOutput
ViewsListInput = ViewsListInput
ViewsListOutput = ViewList
ViewsCreateInput = ViewsCreateInput
ViewsCreateOutput = View
ViewsGetInput = ViewsGetInput
ViewsGetOutput = ViewWithAnswer
ViewsUpdateInput = ViewsUpdateInput
ViewsUpdateOutput = View
DashboardsListInput = DashboardsListInput
DashboardsListOutput = DashboardList
DashboardsCreateInput = DashboardsCreateInput
DashboardsCreateOutput = Dashboard
DashboardsGetInput = DashboardsGetInput
DashboardsGetOutput = Dashboard
DashboardsUpdateInput = DashboardsUpdateInput
DashboardsUpdateOutput = Dashboard
DashboardsReadInput = DashboardsReadInput
DashboardsReadOutput = DashboardWithAnswers
DashboardsPinInput = DashboardsPinInput
DashboardsPinOutput = DashboardSummary
IntegrationsListInput = IntegrationsListInput
IntegrationsListOutput = IntegrationList
IntegrationsHealthInput = IntegrationsHealthInput
IntegrationsHealthOutput = IntegrationHealthOutput
ProjectsSetupInput = Dict[str, Any]
ProjectsSetupOutput = ProjectSetup
LurkyBriefInput = Dict[str, Any]
LurkyBriefOutput = Brief
LurkySuggestionsInput = Dict[str, Any]
LurkySuggestionsOutput = SuggestionList
LurkyHideSuggestionInput = LurkyHideSuggestionInput
LurkyHideSuggestionOutput = SuggestionHidden
LurkyShowSuggestionInput = LurkyShowSuggestionInput
LurkyShowSuggestionOutput = SuggestionHidden
ClocksGetInput = Dict[str, Any]
ClocksGetOutput = ProjectClock
ClocksAdvanceInput = ClocksAdvanceInput
ClocksAdvanceOutput = ProjectClock
ClocksSetInput = ClocksSetInput
ClocksSetOutput = ProjectClock
ClocksResetInput = Dict[str, Any]
ClocksResetOutput = ProjectClock
ExportsCreateInput = ExportsCreateInput
ExportsCreateOutput = ExportJob
ExportsListInput = ExportsListInput
ExportsListOutput = ExportJobList
ExportsGetInput = ExportsGetInput
ExportsGetOutput = ExportJob
ExportsDownloadInput = ExportsDownloadInput
ExportsDownloadOutput = ExportDownload
ExportsCancelInput = ExportsCancelInput
ExportsCancelOutput = ExportJob
