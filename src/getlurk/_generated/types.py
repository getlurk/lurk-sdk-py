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
    BlockState,
    Brief,
    BudgetList,
    ChatDirectory,
    ChatMirror,
    ChatMirrorList,
    ChatMirrorPreview,
    ChatSettings,
    ClaimIdentityLinkOutput,
    ClientEventsSetting,
    CreateIdentityLinkOutput,
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
    DeleteIdentityLinkOutput,
    DeleteLurkyConversationOutput,
    DeletedChatMirror,
    DeletedWebhookEndpoint,
    DisabledKnownValues,
    DisconnectedIntegration,
    EndUserDetail,
    ErasureDetail,
    ErasureRequest,
    EventsCatalog,
    ExplainActivityOutput,
    ExportDownload,
    ExportJob,
    ExportJobList,
    FeedList,
    FeedbackReceipt,
    GivePreview,
    GiveUnitsOutput,
    Hold,
    HoldList,
    IdentityLinkList,
    InstallTemplateOutput,
    IntegrationConnectLink,
    IntegrationHealthOutput,
    IntegrationInstallation,
    IntegrationInstallations,
    IntegrationList,
    Invite,
    IssuerIdentity,
    KnownValuesList,
    KnownValuesSetting,
    LurkyConversation,
    LurkyConversationList,
    LurkySettings,
    LurkyUsage,
    Me,
    Member,
    MemberList,
    MergeUsersOutput,
    MyInviteList,
    Organization,
    OrganizationList,
    PersonAlias,
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
    TestTrustedIssuerOutput,
    TrustedIssuer,
    UndoActivityOutput,
    Unit,
    UnitLeaderboard,
    UnitList,
    UnmergeUsersOutput,
    UpdateClientEventsOutput,
    UpdatedChatSettings,
    UseUnitsOutput,
    UserHistory,
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
    "kind": NotRequired[Literal["all", "given", "skipped", "held", "effect", "mirror"]],
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

ChatDirectoryListInput = TypedDict(
    "ChatDirectoryListInput",
    {
    "installation": Required[str],
    "type": NotRequired[Literal["channel", "role", "group"]],
    },
)

ChatMirrorsCreateInput = TypedDict(
    "ChatMirrorsCreateInput",
    {
    "installation": Required[str],
    "unit": Required[str],
    "threshold": Required[int],
    "target": Required[str],
    "label": NotRequired[str],
    },
)

ChatMirrorsDeleteInput = TypedDict(
    "ChatMirrorsDeleteInput",
    {
    "id": Required[str],
    },
)

ChatMirrorsGetInput = TypedDict(
    "ChatMirrorsGetInput",
    {
    "id": Required[str],
    },
)

ChatMirrorsListInput = TypedDict(
    "ChatMirrorsListInput",
    {
    "limit": NotRequired[int],
    "cursor": NotRequired[str],
    "installation": NotRequired[str],
    "status": NotRequired["ChatMirrorStatus"],
    },
)

ChatMirrorsPauseInput = TypedDict(
    "ChatMirrorsPauseInput",
    {
    "id": Required[str],
    },
)

ChatMirrorsPreviewInput = TypedDict(
    "ChatMirrorsPreviewInput",
    {
    "id": NotRequired[str],
    "installation": NotRequired[str],
    "unit": NotRequired[str],
    "threshold": NotRequired[int],
    "target": NotRequired[str],
    },
)

ChatMirrorsPublishInput = TypedDict(
    "ChatMirrorsPublishInput",
    {
    "id": Required[str],
    },
)

ChatMirrorsUpdateInput = TypedDict(
    "ChatMirrorsUpdateInput",
    {
    "id": Required[str],
    "threshold": NotRequired[int],
    "label": NotRequired[str],
    "unit": NotRequired[str],
    "target": NotRequired[str],
    },
)

ChatSettingsGetInput = TypedDict(
    "ChatSettingsGetInput",
    {
    "installation": Required[str],
    },
)

ChatSettingsUpdateInput = TypedDict(
    "ChatSettingsUpdateInput",
    {
    "installation": Required[str],
    "settings": Required["ChatSettingsChange"],
    },
)

ClientEventsUpdateInput = TypedDict(
    "ClientEventsUpdateInput",
    {
    "expected_revision": Required[int],
    "daily_cap_per_person": NotRequired[int],
    "daily_cap_project": NotRequired[Union[int, None]],
    "new_people_per_hour": NotRequired[Union[int, None]],
    "events": NotRequired[List["ClientEventAllow"]],
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

ErasuresGetInput = TypedDict(
    "ErasuresGetInput",
    {
    "id": Required[str],
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
    "profile": NotRequired["EventsSendInputProfile"],
    "alias": NotRequired[str],
    },
)

EventsSendInputProfile = TypedDict(
    "EventsSendInputProfile",
    {
    "email": NotRequired[Union[str, None]],
    "name": NotRequired[Union[str, None]],
    "avatar_url": NotRequired[Union[str, None]],
    "handles": NotRequired[Dict[str, "HandleChange"]],
    "locale": NotRequired[Union[str, None]],
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

FeedbackSendInput = TypedDict(
    "FeedbackSendInput",
    {
    "kind": Required["FeedbackKind"],
    "impact": Required["FeedbackImpact"],
    "message": Required[str],
    "operation": NotRequired[str],
    "request_ids": NotRequired[List[str]],
    "docs_path": NotRequired[str],
    "client": NotRequired["FeedbackSendInputClient"],
    "idempotency_key": NotRequired[str],
    },
)

FeedbackSendInputClient = TypedDict(
    "FeedbackSendInputClient",
    {
    "sdk": NotRequired["FeedbackSendInputClientSdk"],
    "agent": NotRequired["FeedbackSendInputClientAgent"],
    },
)

FeedbackSendInputClientAgent = TypedDict(
    "FeedbackSendInputClientAgent",
    {
    "name": Required[str],
    "version": Required[str],
    },
)

FeedbackSendInputClientSdk = TypedDict(
    "FeedbackSendInputClientSdk",
    {
    "name": Required[str],
    "version": Required[str],
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

IdentityLinksClaimInput = TypedDict(
    "IdentityLinksClaimInput",
    {
    "code": Required[str],
    "user": Required[str],
    },
)

IdentityLinksCreateInput = TypedDict(
    "IdentityLinksCreateInput",
    {
    "platform": Required[str],
    "platform_user": Required[str],
    "user": Required[str],
    },
)

IdentityLinksDeleteInput = TypedDict(
    "IdentityLinksDeleteInput",
    {
    "id": Required[str],
    },
)

IdentityLinksListInput = TypedDict(
    "IdentityLinksListInput",
    {
    "user": Required[str],
    },
)

IntegrationsCheckInput = TypedDict(
    "IntegrationsCheckInput",
    {
    "installation": Required[str],
    },
)

IntegrationsConnectInput = TypedDict(
    "IntegrationsConnectInput",
    {
    "connector": Required[str],
    "ask": NotRequired[Literal["messages", "groups", "dms", "messages_and_groups", "messages_and_dms", "groups_and_dms", "messages_and_groups_and_dms"]],
    },
)

IntegrationsDisconnectInput = TypedDict(
    "IntegrationsDisconnectInput",
    {
    "id": Required[str],
    },
)

IntegrationsGetInput = TypedDict(
    "IntegrationsGetInput",
    {
    "connector": Required[str],
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

IntegrationsUpdateInput = TypedDict(
    "IntegrationsUpdateInput",
    {
    "id": Required[str],
    "settings": Required["IntegrationSettingsChange"],
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

IssuerIdentitiesListInput = TypedDict(
    "IssuerIdentitiesListInput",
    {
    "issuer_id": NotRequired[str],
    "user": NotRequired[str],
    "limit": NotRequired[int],
    "cursor": NotRequired[str],
    },
)

IssuerIdentitiesListOutput = TypedDict(
    "IssuerIdentitiesListOutput",
    {
    "data": Required[List["IssuerIdentity"]],
    "next_cursor": Required[Union[str, None]],
    },
)

IssuerIdentitiesMapInput = TypedDict(
    "IssuerIdentitiesMapInput",
    {
    "issuer_id": Required[str],
    "subject": Required[str],
    "user": Required[str],
    },
)

IssuerIdentitiesUnmapInput = TypedDict(
    "IssuerIdentitiesUnmapInput",
    {
    "id": Required[str],
    },
)

IssuerIdentitiesUnmapOutput = TypedDict(
    "IssuerIdentitiesUnmapOutput",
    {
    "id": Required[str],
    "removed": Required[Literal[True]],
    },
)

KnownValuesDisableInput = TypedDict(
    "KnownValuesDisableInput",
    {
    "event": Required[str],
    "property": Required[str],
    },
)

KnownValuesEnableInput = TypedDict(
    "KnownValuesEnableInput",
    {
    "event": Required[str],
    "property": Required[str],
    },
)

KnownValuesListInput = TypedDict(
    "KnownValuesListInput",
    {
    "event": NotRequired[str],
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
    "effects": NotRequired[List["RuleEffect"]],
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
    "effects": NotRequired[List["RuleEffect"]],
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
    "effects": NotRequired[List["RuleEffect"]],
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

TrustedIssuersActivateInput = TypedDict(
    "TrustedIssuersActivateInput",
    {
    "id": Required[str],
    "expected_revision": Required[int],
    },
)

TrustedIssuersArchiveInput = TypedDict(
    "TrustedIssuersArchiveInput",
    {
    "id": Required[str],
    "expected_revision": Required[int],
    },
)

TrustedIssuersCheckInput = TypedDict(
    "TrustedIssuersCheckInput",
    {
    "id": Required[str],
    "expected_revision": Required[int],
    },
)

TrustedIssuersCreateInput = TypedDict(
    "TrustedIssuersCreateInput",
    {
    "name": Required[str],
    "profile": Required[Union["TrustedIssuersCreateInputProfile1", "TrustedIssuersCreateInputProfile2", "TrustedIssuersCreateInputProfile3"]],
    },
)

TrustedIssuersCreateInputProfile1 = TypedDict(
    "TrustedIssuersCreateInputProfile1",
    {
    "provider": Required[Literal["supabase"]],
    "project_ref": Required[str],
    "audiences": NotRequired[List[str]],
    "algorithms": NotRequired[List[Literal["RS256", "ES256"]]],
    "max_token_lifetime_seconds": NotRequired[int],
    },
)

TrustedIssuersCreateInputProfile2 = TypedDict(
    "TrustedIssuersCreateInputProfile2",
    {
    "provider": Required[Literal["clerk"]],
    "issuer": Required[str],
    "authorized_parties": Required[List[str]],
    "audiences": NotRequired[List[str]],
    "max_token_lifetime_seconds": NotRequired[int],
    },
)

TrustedIssuersCreateInputProfile3 = TypedDict(
    "TrustedIssuersCreateInputProfile3",
    {
    "provider": Required[Literal["oidc"]],
    "issuer": Required[str],
    "jwks_url": Required[str],
    "audiences": Required[List[str]],
    "algorithms": Required[List[Literal["RS256", "ES256"]]],
    "max_token_lifetime_seconds": NotRequired[int],
    },
)

TrustedIssuersGetInput = TypedDict(
    "TrustedIssuersGetInput",
    {
    "id": Required[str],
    },
)

TrustedIssuersListInput = TypedDict(
    "TrustedIssuersListInput",
    {
    "limit": NotRequired[int],
    "cursor": NotRequired[str],
    },
)

TrustedIssuersListOutput = TypedDict(
    "TrustedIssuersListOutput",
    {
    "data": Required[List["TrustedIssuer"]],
    "next_cursor": Required[Union[str, None]],
    },
)

TrustedIssuersPauseInput = TypedDict(
    "TrustedIssuersPauseInput",
    {
    "id": Required[str],
    "expected_revision": Required[int],
    },
)

TrustedIssuersTestInput = TypedDict(
    "TrustedIssuersTestInput",
    {
    "id": Required[str],
    "expected_revision": Required[int],
    "token": Required[str],
    },
)

TrustedIssuersUpdateInput = TypedDict(
    "TrustedIssuersUpdateInput",
    {
    "id": Required[str],
    "expected_revision": Required[int],
    "name": Required[str],
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

UnitsLeaderboardInput = TypedDict(
    "UnitsLeaderboardInput",
    {
    "unit": Required[str],
    "limit": NotRequired[int],
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

UsersAliasInput = TypedDict(
    "UsersAliasInput",
    {
    "id": Required[str],
    "alias": Required[str],
    },
)

UsersBlockInput = TypedDict(
    "UsersBlockInput",
    {
    "user": Required[str],
    },
)

UsersEraseInput = TypedDict(
    "UsersEraseInput",
    {
    "id": Required[str],
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

UsersHistoryInput = TypedDict(
    "UsersHistoryInput",
    {
    "id": Required[str],
    "event": NotRequired[str],
    "kind": NotRequired[Literal["event", "receipt"]],
    "since": NotRequired[str],
    "until": NotRequired[str],
    "limit": NotRequired[int],
    "cursor": NotRequired[str],
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

UsersMergeInput = TypedDict(
    "UsersMergeInput",
    {
    "from": Required[str],
    "into": Required[str],
    },
)

UsersUnaliasInput = TypedDict(
    "UsersUnaliasInput",
    {
    "id": Required[str],
    "alias": Required[str],
    },
)

UsersUnblockInput = TypedDict(
    "UsersUnblockInput",
    {
    "user": Required[str],
    },
)

UsersUnmergeInput = TypedDict(
    "UsersUnmergeInput",
    {
    "user": Required[str],
    },
)

UsersUpdateInput = TypedDict(
    "UsersUpdateInput",
    {
    "id": Required[str],
    "profile": Required[Union["UsersUpdateInputProfile", None]],
    },
)

UsersUpdateInputProfile = TypedDict(
    "UsersUpdateInputProfile",
    {
    "email": NotRequired[Union[str, None]],
    "name": NotRequired[Union[str, None]],
    "avatar_url": NotRequired[Union[str, None]],
    "handles": NotRequired[Dict[str, "HandleChange"]],
    "locale": NotRequired[Union[str, None]],
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
    "source": NotRequired[Literal["trusted", "platform", "any"]],
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
ChatSettingsGetInput = ChatSettingsGetInput
ChatSettingsGetOutput = ChatSettings
ChatSettingsUpdateInput = ChatSettingsUpdateInput
ChatSettingsUpdateOutput = UpdatedChatSettings
ChatDirectoryListInput = ChatDirectoryListInput
ChatDirectoryListOutput = ChatDirectory
ChatMirrorsListInput = ChatMirrorsListInput
ChatMirrorsListOutput = ChatMirrorList
ChatMirrorsCreateInput = ChatMirrorsCreateInput
ChatMirrorsCreateOutput = ChatMirror
ChatMirrorsGetInput = ChatMirrorsGetInput
ChatMirrorsGetOutput = ChatMirror
ChatMirrorsUpdateInput = ChatMirrorsUpdateInput
ChatMirrorsUpdateOutput = ChatMirror
ChatMirrorsDeleteInput = ChatMirrorsDeleteInput
ChatMirrorsDeleteOutput = DeletedChatMirror
ChatMirrorsPreviewInput = ChatMirrorsPreviewInput
ChatMirrorsPreviewOutput = ChatMirrorPreview
ChatMirrorsPublishInput = ChatMirrorsPublishInput
ChatMirrorsPublishOutput = ChatMirror
ChatMirrorsPauseInput = ChatMirrorsPauseInput
ChatMirrorsPauseOutput = ChatMirror
EventsCatalogInput = EventsCatalogInput
EventsCatalogOutput = EventsCatalog
KnownValuesListInput = KnownValuesListInput
KnownValuesListOutput = KnownValuesList
KnownValuesEnableInput = KnownValuesEnableInput
KnownValuesEnableOutput = KnownValuesSetting
KnownValuesDisableInput = KnownValuesDisableInput
KnownValuesDisableOutput = DisabledKnownValues
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
UsersUpdateInput = UsersUpdateInput
UsersUpdateOutput = EndUserDetail
UsersHistoryInput = UsersHistoryInput
UsersHistoryOutput = UserHistory
UsersAliasInput = UsersAliasInput
UsersAliasOutput = PersonAlias
UsersUnaliasInput = UsersUnaliasInput
UsersUnaliasOutput = PersonAlias
UsersMergeInput = UsersMergeInput
UsersMergeOutput = MergeUsersOutput
UsersUnmergeInput = UsersUnmergeInput
UsersUnmergeOutput = UnmergeUsersOutput
UsersBlockInput = UsersBlockInput
UsersBlockOutput = BlockState
UsersUnblockInput = UsersUnblockInput
UsersUnblockOutput = BlockState
UsersEraseInput = UsersEraseInput
UsersEraseOutput = ErasureRequest
ErasuresGetInput = ErasuresGetInput
ErasuresGetOutput = ErasureDetail
FeedbackSendInput = FeedbackSendInput
FeedbackSendOutput = FeedbackReceipt
IdentityLinksListInput = IdentityLinksListInput
IdentityLinksListOutput = IdentityLinkList
IdentityLinksCreateInput = IdentityLinksCreateInput
IdentityLinksCreateOutput = CreateIdentityLinkOutput
IdentityLinksClaimInput = IdentityLinksClaimInput
IdentityLinksClaimOutput = ClaimIdentityLinkOutput
IdentityLinksDeleteInput = IdentityLinksDeleteInput
IdentityLinksDeleteOutput = DeleteIdentityLinkOutput
UnitsListInput = UnitsListInput
UnitsListOutput = UnitList
UnitsCreateInput = UnitsCreateInput
UnitsCreateOutput = Unit
UnitsGetInput = UnitsGetInput
UnitsGetOutput = Unit
UnitsUpdateInput = UnitsUpdateInput
UnitsUpdateOutput = Unit
UnitsLeaderboardInput = UnitsLeaderboardInput
UnitsLeaderboardOutput = UnitLeaderboard
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
TrustedIssuersListInput = TrustedIssuersListInput
TrustedIssuersListOutput = TrustedIssuersListOutput
TrustedIssuersCreateInput = TrustedIssuersCreateInput
TrustedIssuersCreateOutput = TrustedIssuer
TrustedIssuersGetInput = TrustedIssuersGetInput
TrustedIssuersGetOutput = TrustedIssuer
TrustedIssuersUpdateInput = TrustedIssuersUpdateInput
TrustedIssuersUpdateOutput = TrustedIssuer
TrustedIssuersActivateInput = TrustedIssuersActivateInput
TrustedIssuersActivateOutput = TrustedIssuer
TrustedIssuersPauseInput = TrustedIssuersPauseInput
TrustedIssuersPauseOutput = TrustedIssuer
TrustedIssuersArchiveInput = TrustedIssuersArchiveInput
TrustedIssuersArchiveOutput = TrustedIssuer
ClientEventsGetInput = Dict[str, Any]
ClientEventsGetOutput = ClientEventsSetting
ClientEventsUpdateInput = ClientEventsUpdateInput
ClientEventsUpdateOutput = UpdateClientEventsOutput
TrustedIssuersCheckInput = TrustedIssuersCheckInput
TrustedIssuersCheckOutput = TrustedIssuer
TrustedIssuersTestInput = TrustedIssuersTestInput
TrustedIssuersTestOutput = TestTrustedIssuerOutput
IssuerIdentitiesListInput = IssuerIdentitiesListInput
IssuerIdentitiesListOutput = IssuerIdentitiesListOutput
IssuerIdentitiesMapInput = IssuerIdentitiesMapInput
IssuerIdentitiesMapOutput = IssuerIdentity
IssuerIdentitiesUnmapInput = IssuerIdentitiesUnmapInput
IssuerIdentitiesUnmapOutput = IssuerIdentitiesUnmapOutput
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
IntegrationsGetInput = IntegrationsGetInput
IntegrationsGetOutput = IntegrationInstallations
IntegrationsConnectInput = IntegrationsConnectInput
IntegrationsConnectOutput = IntegrationConnectLink
IntegrationsUpdateInput = IntegrationsUpdateInput
IntegrationsUpdateOutput = IntegrationInstallation
IntegrationsDisconnectInput = IntegrationsDisconnectInput
IntegrationsDisconnectOutput = DisconnectedIntegration
IntegrationsCheckInput = IntegrationsCheckInput
IntegrationsCheckOutput = IntegrationInstallation
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
