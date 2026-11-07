"""Generated from openapi/openapi.json by scripts/generate.ts. Do not edit."""

from __future__ import annotations

from typing import Any, Callable, Mapping, Optional

from ..options import RequestOptions
from .types import (
    ActivityExplainInput,
    ActivityExplainOutput,
    ActivityExportInput,
    ActivityExportOutput,
    ActivityFeedInput,
    ActivityFeedOutput,
    ActivityListInput,
    ActivityListOutput,
    ActivityUndoInput,
    ActivityUndoOutput,
    AgentKeysCreateInput,
    AgentKeysCreateOutput,
    AgentKeysListInput,
    AgentKeysListOutput,
    AgentKeysRevokeInput,
    AgentKeysRevokeOutput,
    ApiKeysCreateInput,
    ApiKeysCreateOutput,
    ApiKeysListInput,
    ApiKeysListOutput,
    ApiKeysRevokeInput,
    ApiKeysRevokeOutput,
    AudiencesAddUsersInput,
    AudiencesAddUsersOutput,
    AudiencesCreateInput,
    AudiencesCreateOutput,
    AudiencesListInput,
    AudiencesListOutput,
    BudgetsListInput,
    BudgetsListOutput,
    ChatDirectoryListInput,
    ChatDirectoryListOutput,
    ChatMirrorsCreateInput,
    ChatMirrorsCreateOutput,
    ChatMirrorsDeleteInput,
    ChatMirrorsDeleteOutput,
    ChatMirrorsGetInput,
    ChatMirrorsGetOutput,
    ChatMirrorsListInput,
    ChatMirrorsListOutput,
    ChatMirrorsPauseInput,
    ChatMirrorsPauseOutput,
    ChatMirrorsPreviewInput,
    ChatMirrorsPreviewOutput,
    ChatMirrorsPublishInput,
    ChatMirrorsPublishOutput,
    ChatMirrorsUpdateInput,
    ChatMirrorsUpdateOutput,
    ChatSettingsGetInput,
    ChatSettingsGetOutput,
    ChatSettingsUpdateInput,
    ChatSettingsUpdateOutput,
    ClientEventsGetInput,
    ClientEventsGetOutput,
    ClientEventsUpdateInput,
    ClientEventsUpdateOutput,
    ClocksAdvanceInput,
    ClocksAdvanceOutput,
    ClocksGetInput,
    ClocksGetOutput,
    ClocksResetInput,
    ClocksResetOutput,
    ClocksSetInput,
    ClocksSetOutput,
    DashboardsCreateInput,
    DashboardsCreateOutput,
    DashboardsGetInput,
    DashboardsGetOutput,
    DashboardsListInput,
    DashboardsListOutput,
    DashboardsPinInput,
    DashboardsPinOutput,
    DashboardsReadInput,
    DashboardsReadOutput,
    DashboardsUpdateInput,
    DashboardsUpdateOutput,
    ErasuresGetInput,
    ErasuresGetOutput,
    EventsCatalogInput,
    EventsCatalogOutput,
    EventsSendInput,
    EventsSendOutput,
    ExportsCancelInput,
    ExportsCancelOutput,
    ExportsCreateInput,
    ExportsCreateOutput,
    ExportsDownloadInput,
    ExportsDownloadOutput,
    ExportsGetInput,
    ExportsGetOutput,
    ExportsListInput,
    ExportsListOutput,
    FeedbackSendInput,
    FeedbackSendOutput,
    HoldsDecideInput,
    HoldsDecideOutput,
    HoldsGetInput,
    HoldsGetOutput,
    HoldsListInput,
    HoldsListOutput,
    IdentityLinksClaimInput,
    IdentityLinksClaimOutput,
    IdentityLinksCreateInput,
    IdentityLinksCreateOutput,
    IdentityLinksDeleteInput,
    IdentityLinksDeleteOutput,
    IdentityLinksListInput,
    IdentityLinksListOutput,
    IntegrationsCheckInput,
    IntegrationsCheckOutput,
    IntegrationsConnectInput,
    IntegrationsConnectOutput,
    IntegrationsDisconnectInput,
    IntegrationsDisconnectOutput,
    IntegrationsGetInput,
    IntegrationsGetOutput,
    IntegrationsHealthInput,
    IntegrationsHealthOutput,
    IntegrationsListInput,
    IntegrationsListOutput,
    IntegrationsUpdateInput,
    IntegrationsUpdateOutput,
    InvitesAcceptInput,
    InvitesAcceptOutput,
    InvitesDeclineInput,
    InvitesDeclineOutput,
    InvitesListInput,
    InvitesListOutput,
    InvitesRevokeInput,
    InvitesRevokeOutput,
    IssuerIdentitiesListInput,
    IssuerIdentitiesListOutput,
    IssuerIdentitiesMapInput,
    IssuerIdentitiesMapOutput,
    IssuerIdentitiesUnmapInput,
    IssuerIdentitiesUnmapOutput,
    KnownValuesDisableInput,
    KnownValuesDisableOutput,
    KnownValuesEnableInput,
    KnownValuesEnableOutput,
    KnownValuesListInput,
    KnownValuesListOutput,
    LurkyBriefInput,
    LurkyBriefOutput,
    LurkyDeleteConversationInput,
    LurkyDeleteConversationOutput,
    LurkyGetConversationInput,
    LurkyGetConversationOutput,
    LurkyGetSettingsInput,
    LurkyGetSettingsOutput,
    LurkyHideSuggestionInput,
    LurkyHideSuggestionOutput,
    LurkyListConversationsInput,
    LurkyListConversationsOutput,
    LurkyShowSuggestionInput,
    LurkyShowSuggestionOutput,
    LurkySuggestionsInput,
    LurkySuggestionsOutput,
    LurkyUpdateSettingsInput,
    LurkyUpdateSettingsOutput,
    LurkyUsageInput,
    LurkyUsageOutput,
    MembersInviteInput,
    MembersInviteOutput,
    MembersListInput,
    MembersListOutput,
    MembersMeInput,
    MembersMeOutput,
    MembersRemoveInput,
    MembersRemoveOutput,
    MembersUpdateInput,
    MembersUpdateOutput,
    OrganizationsCreateInput,
    OrganizationsCreateOutput,
    OrganizationsListInput,
    OrganizationsListOutput,
    ProjectsCreateInput,
    ProjectsCreateOutput,
    ProjectsGetInput,
    ProjectsGetOutput,
    ProjectsListInput,
    ProjectsListOutput,
    ProjectsSetupInput,
    ProjectsSetupOutput,
    ProjectsUpdateInput,
    ProjectsUpdateOutput,
    PromotionsCreateInput,
    PromotionsCreateOutput,
    PromotionsPreviewInput,
    PromotionsPreviewOutput,
    ProposalsCardInput,
    ProposalsCardOutput,
    ProposalsCreateInput,
    ProposalsCreateOutput,
    ProposalsDecideInput,
    ProposalsDecideOutput,
    ProposalsGetInput,
    ProposalsGetOutput,
    ProposalsListInput,
    ProposalsListOutput,
    RulesCreateInput,
    RulesCreateOutput,
    RulesGetInput,
    RulesGetOutput,
    RulesListInput,
    RulesListOutput,
    RulesPauseInput,
    RulesPauseOutput,
    RulesPreviewInput,
    RulesPreviewOutput,
    RulesPublishInput,
    RulesPublishOutput,
    RulesResumeInput,
    RulesResumeOutput,
    RulesStatsInput,
    RulesStatsOutput,
    RulesUpdateInput,
    RulesUpdateOutput,
    TemplatesGetInput,
    TemplatesGetOutput,
    TemplatesInstallInput,
    TemplatesInstallOutput,
    TemplatesListInput,
    TemplatesListOutput,
    TemplatesPlanInput,
    TemplatesPlanOutput,
    TemplatesRemoveInput,
    TemplatesRemoveOutput,
    TrustedIssuersActivateInput,
    TrustedIssuersActivateOutput,
    TrustedIssuersArchiveInput,
    TrustedIssuersArchiveOutput,
    TrustedIssuersCheckInput,
    TrustedIssuersCheckOutput,
    TrustedIssuersCreateInput,
    TrustedIssuersCreateOutput,
    TrustedIssuersGetInput,
    TrustedIssuersGetOutput,
    TrustedIssuersListInput,
    TrustedIssuersListOutput,
    TrustedIssuersPauseInput,
    TrustedIssuersPauseOutput,
    TrustedIssuersTestInput,
    TrustedIssuersTestOutput,
    TrustedIssuersUpdateInput,
    TrustedIssuersUpdateOutput,
    UnitsCreateInput,
    UnitsCreateOutput,
    UnitsGetInput,
    UnitsGetOutput,
    UnitsGiveInput,
    UnitsGiveOutput,
    UnitsGivePreviewInput,
    UnitsGivePreviewOutput,
    UnitsLeaderboardInput,
    UnitsLeaderboardOutput,
    UnitsListInput,
    UnitsListOutput,
    UnitsSendInput,
    UnitsSendOutput,
    UnitsSpendInput,
    UnitsSpendOutput,
    UnitsUpdateInput,
    UnitsUpdateOutput,
    UnitsUseInput,
    UnitsUseOutput,
    UsersAliasInput,
    UsersAliasOutput,
    UsersBlockInput,
    UsersBlockOutput,
    UsersEraseInput,
    UsersEraseOutput,
    UsersExportInput,
    UsersExportOutput,
    UsersGetInput,
    UsersGetOutput,
    UsersHistoryInput,
    UsersHistoryOutput,
    UsersListInput,
    UsersListOutput,
    UsersMergeInput,
    UsersMergeOutput,
    UsersUnaliasInput,
    UsersUnaliasOutput,
    UsersUnblockInput,
    UsersUnblockOutput,
    UsersUnmergeInput,
    UsersUnmergeOutput,
    UsersUpdateInput,
    UsersUpdateOutput,
    ViewsCreateInput,
    ViewsCreateOutput,
    ViewsGetInput,
    ViewsGetOutput,
    ViewsListInput,
    ViewsListOutput,
    ViewsUpdateInput,
    ViewsUpdateOutput,
    WebhookEndpointsCreateInput,
    WebhookEndpointsCreateOutput,
    WebhookEndpointsDeleteInput,
    WebhookEndpointsDeleteOutput,
    WebhookEndpointsListInput,
    WebhookEndpointsListOutput,
)

Call = Callable[[str, Optional[Mapping[str, Any]], Optional[RequestOptions]], Any]


class ActivityResource:
    def __init__(self, call: Call) -> None:
        self._call = call

    def explain(
        self,
        input: Optional[ActivityExplainInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> ActivityExplainOutput:
        """Explain a receipt. The receipt and the checks the engine made for it, in order, from the trace stored with it: never reconstructed afterwards. A receipt written before traces were kept has none (`traced: false`)."""
        return self._call("activity.explain", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def export(
        self,
        input: Optional[ActivityExportInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> ActivityExportOutput:
        """Export receipts as CSV. Exports the receipts that match as one CSV file in the answer, newest first, one row for each unit a receipt changed. Up to 10,000 rows, then `truncated` is true. Owners and admins, in the dashboard. Every export is audited. [Activity](/activity#export-receipts)"""
        return self._call("activity.export", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def feed(
        self,
        input: Optional[ActivityFeedInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> ActivityFeedOutput:
        """List what happened and what didn't. Lists, newest first, receipts, rules that heard an event and did nothing (kept at least 30 days) and changes waiting for a person. Filter by `kind` (`given`, `skipped` or `held`), person, rule, unit or time. A unit filter keeps receipts and held changes. [Activity](/activity#the-feed)"""
        return self._call("activity.feed", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def list(
        self,
        input: Optional[ActivityListInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> ActivityListOutput:
        """List receipts. Newest first. Every receipt says who acted, through what, and each unit it changed with the balance after. Filter by person (a usr_… ID or the brand's own identifier), rule, unit or time."""
        return self._call("activity.list", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def undo(
        self,
        input: Optional[ActivityUndoInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> ActivityUndoOutput:
        """Undo a receipt. Undoes a receipt by writing a new one that reverses it; both stay. Owners and admins, in person. Refused for an undo, a receipt already undone, part of a merge or a send, or when the balance no longer allows it. [Activity](/activity#undo-a-receipt)"""
        return self._call("activity.undo", {**(input or {}), **fields}, options)  # type: ignore[arg-type]


class AgentKeysResource:
    def __init__(self, call: Call) -> None:
        self._call = call

    def create(
        self,
        input: Optional[AgentKeysCreateInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> AgentKeysCreateOutput:
        """Create an agent key. Makes a key for one coding agent; receipts and proposals carry its name. Owners and admins only, signed in as a person. The full key is in the response once: Lurk keeps only a hash, so a lost key is replaced, not recovered. [Keys](/projects-and-keys#keys)"""
        return self._call("agent_keys.create", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def list(
        self,
        input: Optional[AgentKeysListInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> AgentKeysListOutput:
        """List agent keys. Lists the project's agent keys, newest first: name, start and state. The full key is never shown again. Any member can read it, a viewer too. [Keys](/projects-and-keys#keys)"""
        return self._call("agent_keys.list", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def revoke(
        self,
        input: Optional[AgentKeysRevokeInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> AgentKeysRevokeOutput:
        """Revoke an agent key. Revokes an agent key; the agent stops working at once, on its next request. Owners and admins only, signed in as a person. Revoking a key that is already revoked changes nothing. [Keys](/projects-and-keys#keys)"""
        return self._call("agent_keys.revoke", {**(input or {}), **fields}, options)  # type: ignore[arg-type]


class ApiKeysResource:
    def __init__(self, call: Call) -> None:
        self._call = call

    def create(
        self,
        input: Optional[ApiKeysCreateInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> ApiKeysCreateOutput:
        """Create a project API key. Makes a project key for your server. Owners and admins only, signed in as a person; no key can call it. The full key is in the response once: Lurk keeps only a hash, so a lost key is replaced, not recovered. [Keys](/projects-and-keys#keys)"""
        return self._call("api_keys.create", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def list(
        self,
        input: Optional[ApiKeysListInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> ApiKeysListOutput:
        """List project API keys. Lists the project's API keys, newest first: name, start and state. The full key is never shown again. Any member can read it, a viewer too. [Keys](/projects-and-keys#keys)"""
        return self._call("api_keys.list", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def revoke(
        self,
        input: Optional[ApiKeysRevokeInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> ApiKeysRevokeOutput:
        """Revoke a project API key. Revokes a project key; it stops working at once. Owners and admins only, signed in as a person. Revoking a key that is already revoked changes nothing. [Keys](/projects-and-keys#keys)"""
        return self._call("api_keys.revoke", {**(input or {}), **fields}, options)  # type: ignore[arg-type]


class AudiencesResource:
    def __init__(self, call: Call) -> None:
        self._call = call

    def add_users(
        self,
        input: Optional[AudiencesAddUsersInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> AudiencesAddUsersOutput:
        """Add people to a list audience. Adds up to 1,000 people by `usr_…` ID or by the brand's own ID. People already in it are counted, not added twice. An ID that matches nobody is returned in `not_found` and nothing is created for it. Only a list audience takes people by hand: a condition audience keeps its own members."""
        return self._call("audiences.add_users", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def create(
        self,
        input: Optional[AudiencesCreateInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> AudiencesCreateOutput:
        """Create an audience. Makes a list (people you add) or a condition audience (kept up to date by its conditions). A new condition audience is empty until the worker's next pass (every five minutes). A project can have 100 condition audiences. Rules read it in `if`. [Audiences](/units#audiences)"""
        return self._call("audiences.create", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def list(
        self,
        input: Optional[AudiencesListInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> AudiencesListOutput:
        """List audiences. The groups of people rules can read, newest first, with how many are in each, which rules read it and whether a condition is broken (`status`, `problems`). A condition audience's members are worked out every five minutes: `refreshed_at` says when, and a rule sees it as it stood then."""
        return self._call("audiences.list", {**(input or {}), **fields}, options)  # type: ignore[arg-type]


class BudgetsResource:
    def __init__(self, call: Call) -> None:
        self._call = call

    def list(
        self,
        input: Optional[BudgetsListInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> BudgetsListOutput:
        """List rule budgets. What each live rule's budgets have given in the window they are in now ('5,000 Beans a week'), newest rule first, with the window's start and end in the project's time zone. A rule's budgets are never split across pages. `nearly_used` keeps those 80% or more used."""
        return self._call("budgets.list", {**(input or {}), **fields}, options)  # type: ignore[arg-type]


class ChatDirectoryResource:
    def __init__(self, call: Call) -> None:
        self._call = call

    def list(
        self,
        input: Optional[ChatDirectoryListInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> ChatDirectoryListOutput:
        """List a chat community's channels. Not available yet. What one community offers to pick from, by `type` (channel, role, group): channels (ID, name, `can_post`), Discord roles or Slack groups (`can_give`). If the platform cannot answer, `status` is `unavailable` with a `reason`: not an error. Refused after Lurky was removed."""
        return self._call("chat_directory.list", {**(input or {}), **fields}, options)  # type: ignore[arg-type]


class ChatMirrorsResource:
    def __init__(self, call: Call) -> None:
        self._call = call

    def create(
        self,
        input: Optional[ChatMirrorsCreateInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> ChatMirrorsCreateOutput:
        """Save a mirror as a draft. Not available yet. Saves a draft mirror: a role, user group or Telegram tag people have while they hold at least `threshold` of `unit`. `target` is the platform's ID (Slack: S…) or the Telegram tag. Only an owner or admin, in person. One mirror per community and target. Preview it, then publish."""
        return self._call("chat_mirrors.create", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def delete(
        self,
        input: Optional[ChatMirrorsDeleteInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> ChatMirrorsDeleteOutput:
        """Delete a mirror. Not available yet. Deletes a mirror. Nothing is taken away: every role, group and tag stays where it is, and Lurky stops keeping it true. To stop without losing the mirror, pause it. Only an owner or admin, in person: agents, keys and Lurky get `approval_required`."""
        return self._call("chat_mirrors.delete", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def get(
        self,
        input: Optional[ChatMirrorsGetInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> ChatMirrorsGetOutput:
        """Get a mirror. Not available yet. One mirror by ID: what it gives, at what balance, its status, what Lurky cannot do for it (`problem`) and counts from the last pass: how many should have it, how many do, how many Lurky gave it to, and how many have it that Lurky did not give (never taken away)."""
        return self._call("chat_mirrors.get", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def list(
        self,
        input: Optional[ChatMirrorsListInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> ChatMirrorsListOutput:
        """List the roles, groups and tags that follow a balance. Not available yet. The project's mirrors, newest first: a Discord role, Slack user group or Telegram tag people have while they hold at least a threshold of a unit. Each has its status (draft, live, paused), `problem` with the fix and the last pass's counts. Filter by `installation` or `status`."""
        return self._call("chat_mirrors.list", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def pause(
        self,
        input: Optional[ChatMirrorsPauseInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> ChatMirrorsPauseOutput:
        """Pause a mirror. Not available yet. Stops keeping a live mirror true. Nothing is taken away: everyone keeps what they have, and nobody new gets it. Take it live again with `POST /v1/chat-mirrors/{id}/publish`. Only an owner or admin, in person: agents, keys and Lurky get `approval_required`."""
        return self._call("chat_mirrors.pause", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def preview(
        self,
        input: Optional[ChatMirrorsPreviewInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> ChatMirrorsPreviewOutput:
        """Preview who a mirror would reach. Not available yet. Counts who would have a mirror's role, group or tag now: who is at the threshold with an account here, who Lurky would give it to, who has it, who it would take back. Send a mirror `id`, or `installation`, `unit`, `threshold` (and `target` to see who has it). Read only."""
        return self._call("chat_mirrors.preview", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def publish(
        self,
        input: Optional[ChatMirrorsPublishInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> ChatMirrorsPublishOutput:
        """Take a mirror live. Not available yet. Takes a draft or paused mirror live: Lurky gives the role, group or tag to everyone at the threshold and takes it back only from those it gave who fall below. Only an owner or admin, in person: keys and agents get `approval_required`. Refused if Lurky cannot give it."""
        return self._call("chat_mirrors.publish", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def update(
        self,
        input: Optional[ChatMirrorsUpdateInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> ChatMirrorsUpdateOutput:
        """Change a mirror. Not available yet. Changes a mirror's `threshold` or `label` (any time) or its `unit` or `target` (only while it is not live: pause it first). A live mirror's new threshold applies at the next pass. Only an owner or admin, in person: agents, keys and Lurky get `approval_required`."""
        return self._call("chat_mirrors.update", {**(input or {}), **fields}, options)  # type: ignore[arg-type]


class ChatSettingsResource:
    def __init__(self, call: Call) -> None:
        self._call = call

    def get(
        self,
        input: Optional[ChatSettingsGetInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> ChatSettingsGetOutput:
        """Get what Lurky counts in a chat community. Not available yet. What Lurky counts in one community: the kinds on, the channels it listens in or never in, the daily cap on new people and the `switches` a person can turn on. Bots are never counted. Everything is off until a person turns it on. Never anything anyone wrote."""
        return self._call("chat_settings.get", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def update(
        self,
        input: Optional[ChatSettingsUpdateInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> ChatSettingsUpdateOutput:
        """Change what Lurky counts in a chat community. Not available yet. Sets what Lurky counts in one community: `kinds`, `channels_only`, `channels_except`, `daily_new_people`, `count_external` (Slack only). A field left out stays. Only an owner or admin, in person: keys and agents get `approval_required`. Nothing counts until a live rule listens."""
        return self._call("chat_settings.update", {**(input or {}), **fields}, options)  # type: ignore[arg-type]


class ClientEventsResource:
    def __init__(self, call: Call) -> None:
        self._call = call

    def get(
        self,
        input: Optional[ClientEventsGetInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> ClientEventsGetOutput:
        """Get what a device may send. Not available yet: sign-in is staging only. The event names a device (a signed-in app user) may send, each with its cap and property limits, plus the per-person, project-wide and new-people caps. Empty until a person saves; any other name is refused. `revision` is 0 before the first save."""
        return self._call("client_events.get", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def update(
        self,
        input: Optional[ClientEventsUpdateInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> ClientEventsUpdateOutput:
        """Change what a device may send. Not available yet: sign-in is staging only. Saves what a device may send; `events` replaces the list. Send `expected_revision` (0 first) and a change. Refuses a reserved or repeated name, over 50 names, a cap out of range, or a live or paused rule hearing it with no `source`. Owner or admin only."""
        return self._call("client_events.update", {**(input or {}), **fields}, options)  # type: ignore[arg-type]


class ClocksResource:
    def __init__(self, call: Call) -> None:
        self._call = call

    def advance(
        self,
        input: Optional[ClocksAdvanceInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> ClocksAdvanceOutput:
        """Advance a staging project's clock. Moves the project's time forward by days, hours or minutes, so a seven-day streak, a weekly schedule or an expiry can be tried without waiting. Staging projects only. Scheduled rules and expiries that come due run within a minute. Time only moves forward, except for a reset."""
        return self._call("clocks.advance", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def get(
        self,
        input: Optional[ClocksGetInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> ClocksGetOutput:
        """Get the project's clock. What time it is in this project, and whether it has been moved from real time. Only a staging project's clock can be moved; a production project always shows real time."""
        return self._call("clocks.get", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def reset(
        self,
        input: Optional[ClocksResetInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> ClocksResetOutput:
        """Reset a staging project's clock to real time. Ends the test clock: the project runs on real time again. This is the one way time goes back, so receipts made while the clock was ahead will look as if they come from the future until real time catches up. Staging projects only."""
        return self._call("clocks.reset", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def set(
        self,
        input: Optional[ClocksSetInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> ClocksSetOutput:
        """Set a staging project's clock to a time. Sets the time the project thinks it is, such as the Monday a schedule should run. It cannot be earlier than the project's time now; use a reset to start over. Staging projects only."""
        return self._call("clocks.set", {**(input or {}), **fields}, options)  # type: ignore[arg-type]


class DashboardsResource:
    def __init__(self, call: Call) -> None:
        self._call = call

    def create(
        self,
        input: Optional[DashboardsCreateInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> DashboardsCreateOutput:
        """Make a dashboard. Makes a dashboard of views on a 12-column grid, up to 40 tiles. `unit` makes it that unit's own dashboard (a unit has one). It is not shown on Home until it is updated with `home: true`. Members only; a viewer can't."""
        return self._call("dashboards.create", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def get(
        self,
        input: Optional[DashboardsGetInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> DashboardsGetOutput:
        """Get a dashboard. One dashboard with its tiles: each tile is a view and a place on the 12-column grid. Use "home" for the one on Home, or "unit:<key>" for a unit's own. To read a tile's answer, read its view."""
        return self._call("dashboards.get", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def list(
        self,
        input: Optional[DashboardsListInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> DashboardsListOutput:
        """List dashboards. The project's dashboards, newest first: one is shown on Home, a unit can have its own, and each member pins their own to the sidebar (`pinned` is yours)."""
        return self._call("dashboards.list", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def pin(
        self,
        input: Optional[DashboardsPinInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> DashboardsPinOutput:
        """Pin a dashboard. Pins a dashboard to your sidebar, or unpins it. Each member pins their own."""
        return self._call("dashboards.pin", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def read(
        self,
        input: Optional[DashboardsReadInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> DashboardsReadOutput:
        """Read a dashboard with every tile's answer. A dashboard and the answer of each of its tiles in one call. `range`, `compare` and `audience` apply to every tile, as when reading a view; the answers are keyed by tile `id`. Use "home" for the one on Home, or "unit:<key>" for a unit's own."""
        return self._call("dashboards.read", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def update(
        self,
        input: Optional[DashboardsUpdateInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> DashboardsUpdateOutput:
        """Change a dashboard. Renames a dashboard, makes it the one on Home (any other stops being it), or replaces its whole layout: adding, moving, resizing and removing tiles all send `tiles`."""
        return self._call("dashboards.update", {**(input or {}), **fields}, options)  # type: ignore[arg-type]


class ErasuresResource:
    def __init__(self, call: Call) -> None:
        self._call = call

    def get(
        self,
        input: Optional[ErasuresGetInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> ErasuresGetOutput:
        """Read an erasure request. Not available yet. Reads an erasure request: its state, phase, how many people were in scope, what each step changed (numbers only), and two fixed lists: what erasure removes and what it does not reach. Owners and admins only. Where erasure is off no request exists, so any ID answers `not_found`."""
        return self._call("erasures.get", {**(input or {}), **fields}, options)  # type: ignore[arg-type]


class EventsResource:
    def __init__(self, call: Call) -> None:
        self._call = call

    def catalog(
        self,
        input: Optional[EventsCatalogInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> EventsCatalogOutput:
        """List the events this project has. Lists the event names your project sent in the last 30 days or that a rule listens for, with counts, property names and types, and the rules listening. Property values are never listed, except where a person turned on remembering them. [Events](/events#the-event-catalog)"""
        return self._call("events.catalog", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def send(
        self,
        input: Optional[EventsSendInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> EventsSendOutput:
        """Send an event. Sends something a user did. Lurk runs your live rules on it and returns the receipts: what changed and the balance after. A retry with the same `idempotency_key` returns the first answer. `timestamp` may be in the past, not over 5 minutes ahead. `profile` and `alias` ride along. [Events](/events)"""
        return self._call("events.send", {**(input or {}), **fields}, options)  # type: ignore[arg-type]


class ExportsResource:
    def __init__(self, call: Call) -> None:
        self._call = call

    def cancel(
        self,
        input: Optional[ExportsCancelInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> ExportsCancelOutput:
        """Stop an export. Not available yet. Stops a queued or running export and throws away what it wrote. A finished one is refused (`validation_failed`); its file is deleted when it expires. Owners and admins only."""
        return self._call("exports.cancel", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def create(
        self,
        input: Optional[ExportsCreateInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> ExportsCreateOutput:
        """Start an export. Not available yet. Starts a compressed CSV of receipts or people in the background, as a job to follow. Owners and admins only; attempts count toward 3 a person and 20 a project a day (UTC). Up to 1,000,000 rows, kept 3 days. `unavailable` without a file store. [Activity](/activity#export-receipts)"""
        return self._call("exports.create", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def download(
        self,
        input: Optional[ExportsDownloadInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> ExportsDownloadOutput:
        """Get the link to an export's file. Not available yet. A link to the finished file, good for 5 minutes; ask again for a new one. None once the file's 3 days are up, even if not yet deleted. `unavailable` without a file store. Owners and admins only; each download is audited."""
        return self._call("exports.download", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def get(
        self,
        input: Optional[ExportsGetInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> ExportsGetOutput:
        """See how an export is going. Not available yet. Whether the file is queued, being made (with the rows so far), ready (with when it is deleted), failed (with why), cancelled or expired. Owners and admins only."""
        return self._call("exports.get", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def list(
        self,
        input: Optional[ExportsListInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> ExportsListOutput:
        """List recent exports. Not available yet. Lists the project's exports, newest first, with who asked and how each went. Owners and admins only."""
        return self._call("exports.list", {**(input or {}), **fields}, options)  # type: ignore[arg-type]


class FeedbackResource:
    def __init__(self, call: Call) -> None:
        self._call = call

    def send(
        self,
        input: Optional[FeedbackSendInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> FeedbackSendOutput:
        """Send feedback to the Lurk team. Sends a bug, gap, idea, docs problem or question to the Lurk team. Staff read it before it is shared in their tracker; no reply is promised. Ask your user first, once per task. Never include secrets, keys or your users' data: removal is best effort, best in English. 5 a minute; 50 a project a day."""
        return self._call("feedback.send", {**(input or {}), **fields}, options)  # type: ignore[arg-type]


class HoldsResource:
    def __init__(self, call: Call) -> None:
        self._call = call

    def decide(
        self,
        input: Optional[HoldsDecideInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> HoldsDecideOutput:
        """Give or refuse a hold. A person gives or refuses a held change. Giving makes all the rule's changes as one receipt and spends the rule's budget, if it has one; if balance, supply or budget no longer allow it, nothing changes and the hold stays: refuse it. Owners and admins only (owners only if the project says so)."""
        return self._call("holds.decide", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def get(
        self,
        input: Optional[HoldsGetInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> HoldsGetOutput:
        """Get a hold. One hold with the changes it would make, why it waits, and how it was decided."""
        return self._call("holds.get", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def list(
        self,
        input: Optional[HoldsListInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> HoldsListOutput:
        """List holds. Changes a rule parked for a person, newest first. By default the ones still waiting; `waiting` counts them. Nothing has changed for the person until a hold is given."""
        return self._call("holds.list", {**(input or {}), **fields}, options)  # type: ignore[arg-type]


class IdentityLinksResource:
    def __init__(self, call: Call) -> None:
        self._call = call

    def claim(
        self,
        input: Optional[IdentityLinksClaimInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> IdentityLinksClaimOutput:
        """Claim a link code. Not available yet. Ties a chat account to your person: send the one-time `code` and your `user` ID (created if new). A code works once, 10 minutes; a bad one is `not_found`. Refused if the account or person is linked elsewhere: delete that link first. A brand agent asks (`approval_required`)."""
        return self._call("identity_links.claim", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def create(
        self,
        input: Optional[IdentityLinksCreateInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> IdentityLinksCreateOutput:
        """Link a chat account to a person. Not available yet. Ties a chat account whose platform ID you know to your person (`user`, created if new). Refused if the account is linked to another person or the person to another account: delete that link first. A chat-only person is merged in (`moved`). A brand agent asks (`approval_required`)."""
        return self._call("identity_links.create", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def delete(
        self,
        input: Optional[IdentityLinksDeleteInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> IdentityLinksDeleteOutput:
        """Remove a chat account's link. Not available yet. Unties a chat account from its person and undoes the merge made at linking (units that cannot go back stay). If the person kept is blocked, the block is copied to the account (`block_copied`): a key then gets `approval_required` and nothing changes. A brand agent always asks."""
        return self._call("identity_links.delete", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def list(
        self,
        input: Optional[IdentityLinksListInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> IdentityLinksListOutput:
        """List a person's chat accounts. Not available yet. The chat accounts tied to one person (`user`: a usr_… ID or your own identifier), one per platform at most, oldest first. Each account is masked to its last 4 characters. A person merged into another shows under the one they were merged into."""
        return self._call("identity_links.list", {**(input or {}), **fields}, options)  # type: ignore[arg-type]


class IntegrationsResource:
    def __init__(self, call: Call) -> None:
        self._call = call

    def check(
        self,
        input: Optional[IntegrationsCheckInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> IntegrationsCheckOutput:
        """Check a server's connection now. Not available yet. Asks the platform now whether Lurky still works in one installation, saves the result as its health and returns it. One check a minute (`rate_limited`). An unreachable platform keeps the last health until three checks fail. Only an owner or admin, in person."""
        return self._call("integrations.check", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def connect(
        self,
        input: Optional[IntegrationsConnectInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> IntegrationsConnectOutput:
        """Add Lurky to Discord, Slack or Telegram. Not available yet. Returns a one-time link where a person adds Lurky to a Discord server, Slack workspace or Telegram group; it works 10 minutes (Telegram 15). Only an owner or admin, in person: keys and agents get `approval_required`. `ask` is Slack only. `unavailable` if not set up."""
        return self._call("integrations.connect", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def disconnect(
        self,
        input: Optional[IntegrationsDisconnectInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> IntegrationsDisconnectOutput:
        """Remove Lurky from a server. Not available yet. Removes the installation and frees the server for any project to add. Lurk also asks the platform to take Lurky out where it can, best effort, never blocking the removal. Only an owner or admin, in person: agents and keys get `approval_required`."""
        return self._call("integrations.disconnect", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def get(
        self,
        input: Optional[IntegrationsGetInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> IntegrationsGetOutput:
        """Get where Lurky is added. Not available yet. The servers, workspaces or groups this project added Lurky to on Discord, Slack or Telegram: name, connected or needs attention, settings (`tip`, `announce_tips`, `identity`) and the last health check. Never a credential. `status` is the connector's status in the list."""
        return self._call("integrations.get", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def health(
        self,
        input: Optional[IntegrationsHealthInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> IntegrationsHealthOutput:
        """Get the health of the integrations. What is wrong with this project's connectors, and how to fix it. Without `key` it answers for those connected or needing attention; with `key`, for that one. `needs_attention` counts them all, for the sidebar. A failing webhook endpoint is a problem; one a person turned off is not."""
        return self._call("integrations.health", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def list(
        self,
        input: Optional[IntegrationsListInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> IntegrationsListOutput:
        """List integrations. Every way events reach Lurk or state leaves it, with its status: `connected`, `needs_attention`, `not_connected` or `later` (not available yet). Your app, MCP and webhooks come from your keys and endpoints; chat platforms are not available yet. `filter: connected` includes `needs_attention`."""
        return self._call("integrations.list", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def update(
        self,
        input: Optional[IntegrationsUpdateInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> IntegrationsUpdateOutput:
        """Change how Lurky behaves in a server. Not available yet. Changes an installation's `tip`, `announce_tips` and `identity` (`platform`: a person is their chat account; `linked`: an account of your own app, tied by a link code). Switching merges, links and deletes no one. A setting left out stays. Only an owner or admin, in person."""
        return self._call("integrations.update", {**(input or {}), **fields}, options)  # type: ignore[arg-type]


class InvitesResource:
    def __init__(self, call: Call) -> None:
        self._call = call

    def accept(
        self,
        input: Optional[InvitesAcceptInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> InvitesAcceptOutput:
        """Accept an invitation. Joins the organization with the invited role and returns it. Only the person signed in with the invited, verified address can; an expired invitation, or one from someone no longer an owner or admin, answers `not_found`. [Team](/projects-and-keys#team-and-invitations)"""
        return self._call("invites.accept", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def decline(
        self,
        input: Optional[InvitesDeclineInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> InvitesDeclineOutput:
        """Decline an invitation. Turns an invitation down. Only the person signed in with the invited, verified address can; any other caller, or an invitation that is not open, answers `not_found`. [Team](/projects-and-keys#team-and-invitations)"""
        return self._call("invites.decline", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def list(
        self,
        input: Optional[InvitesListInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> InvitesListOutput:
        """List the invitations to you. Lists the open invitations to the email address you signed in with, newest first. It is empty until that address is verified. [Team](/projects-and-keys#team-and-invitations)"""
        return self._call("invites.list", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def revoke(
        self,
        input: Optional[InvitesRevokeInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> InvitesRevokeOutput:
        """Cancel an invitation. Withdraws an invitation nobody has answered. Owners and admins only; an invitation that was already answered or withdrawn, or is in an organization you are not in, answers `not_found`. [Team](/projects-and-keys#team-and-invitations)"""
        return self._call("invites.revoke", {**(input or {}), **fields}, options)  # type: ignore[arg-type]


class IssuerIdentitiesResource:
    def __init__(self, call: Call) -> None:
        self._call = call

    def list(
        self,
        input: Optional[IssuerIdentitiesListInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> IssuerIdentitiesListOutput:
        """List identity bindings. Not available yet: sign-in is staging only. Newest first. Which person each sign-in subject of your trusted issuers is bound to. Filter by `issuer_id` or by `user` (that person and the people merged into them). The subject is never returned."""
        return self._call("issuer_identities.list", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def map(
        self,
        input: Optional[IssuerIdentitiesMapInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> IssuerIdentitiesMapOutput:
        """Bind a sign-in subject to a person. Not available yet: sign-in is staging only. Binds a provider user id (`subject`, write-only, never returned) to an existing person. Refused if already bound (unmap first), or for a merged-away person or archived issuer. Owner or admin in person; a key or agent gets `approval_required`."""
        return self._call("issuer_identities.map", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def unmap(
        self,
        input: Optional[IssuerIdentitiesUnmapInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> IssuerIdentitiesUnmapOutput:
        """Remove an identity binding. Not available yet: sign-in is staging only. Removes a binding, even a merged-away person's; the person stays. The next sign-in with that subject makes a new person unless it is mapped first or the new-people limit refuses it. Owner or admin in person; a key or agent gets `approval_required`."""
        return self._call("issuer_identities.unmap", {**(input or {}), **fields}, options)  # type: ignore[arg-type]


class KnownValuesResource:
    def __init__(self, call: Call) -> None:
        self._call = call

    def disable(
        self,
        input: Optional[KnownValuesDisableInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> KnownValuesDisableOutput:
        """Stop remembering the values of a property. Switches "remember values" off for one property and deletes the values Lurk kept for it (also when it had turned itself off: the note about why goes too). Rules that already use a value keep working: they hold their own copy. Only an owner or admin, in person."""
        return self._call("known_values.disable", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def enable(
        self,
        input: Optional[KnownValuesEnableInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> KnownValuesEnableOutput:
        """Remember the values of a property. Turns on "remember values" for one property of one of your own events, so rules and Lurky can offer its values. Refused when recent values look personal, are over 64 characters or number more than 20. Owners and admins, in person. [Events](/events#remember-values)"""
        return self._call("known_values.enable", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def list(
        self,
        input: Optional[KnownValuesListInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> KnownValuesListOutput:
        """List the properties that remember their values. Lists the properties of your own events that a person turned "remember values" on for, each with the values Lurk has seen (at most 20) or why it turned itself off. A property nobody turned on is not listed. [Events](/events#remember-values)"""
        return self._call("known_values.list", {**(input or {}), **fields}, options)  # type: ignore[arg-type]


class LurkyResource:
    def __init__(self, call: Call) -> None:
        self._call = call

    def brief(
        self,
        input: Optional[LurkyBriefInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> LurkyBriefOutput:
        """Yesterday in a line. Yesterday in the project's time zone: people active and new, events and what was given, each against the day before, with a sentence that sums it up. No model is used, so it costs nothing. `line` is null until the project has heard anything. Any member can read it."""
        return self._call("lurky.brief", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def delete_conversation(
        self,
        input: Optional[LurkyDeleteConversationInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> LurkyDeleteConversationOutput:
        """Delete one of your conversations with Lurky. Deletes it and its messages at once. Only the member who had it can; a viewer can too, because it is their own."""
        return self._call("lurky.delete_conversation", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def get_conversation(
        self,
        input: Optional[LurkyGetConversationInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> LurkyGetConversationOutput:
        """One of your conversations with Lurky. Its messages, oldest first, with what Lurky read to write each answer."""
        return self._call("lurky.get_conversation", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def get_settings(
        self,
        input: Optional[LurkyGetSettingsInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> LurkyGetSettingsOutput:
        """Whether Lurky is on. Whether Lurky can answer here: the deployment has it switched on, and the organization has not switched it off. It is on for every organization until an owner turns it off (the terms cover it), unless the deployment says otherwise."""
        return self._call("lurky.get_settings", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def hide_suggestion(
        self,
        input: Optional[LurkyHideSuggestionInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> LurkyHideSuggestionOutput:
        """Put a card on Home away. Hides a card for this member only. It comes back when the card's signal changes (its `signature` is no longer the one sent here). Hiding one that is already hidden updates it."""
        return self._call("lurky.hide_suggestion", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def list_conversations(
        self,
        input: Optional[LurkyListConversationsInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> LurkyListConversationsOutput:
        """Your conversations with Lurky. The signed-in member's own conversations, newest first. Nobody else's: not an owner's, not Lurk's staff's through the API. Each is deleted 90 days after its last message."""
        return self._call("lurky.list_conversations", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def show_suggestion(
        self,
        input: Optional[LurkyShowSuggestionInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> LurkyShowSuggestionOutput:
        """Bring a card on Home back. Undoes a hide for this member. Showing one that is not hidden is fine."""
        return self._call("lurky.show_suggestion", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def suggestions(
        self,
        input: Optional[LurkySuggestionsInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> LurkySuggestionsOutput:
        """What Home suggests. Lists the cards on Home, at most six: up to three that need a person, then what changed, then at most one idea, most urgent first in each. A viewer is not shown cards only a decider can act on. A card this member hid stays away until its signal changes. No model is used."""
        return self._call("lurky.suggestions", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def update_settings(
        self,
        input: Optional[LurkyUpdateSettingsInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> LurkyUpdateSettingsOutput:
        """Switch Lurky on or off for the organization. Only an owner. Off, nothing a member says reaches a model. It covers every project of the organization. Lurky is on unless an owner turns it off. It sends the project's configuration and aggregates to the model provider, with people's own ids replaced by placeholders, which the terms say at signup."""
        return self._call("lurky.update_settings", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def usage(
        self,
        input: Optional[LurkyUsageInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> LurkyUsageOutput:
        """What Lurky has cost this organization this month. The organization's Lurky allowance for the month (shared by all its projects), what the organization has used, and whether Lurky is answering: it warns at 80% and stops at 100% until the month resets. Only an owner or admin."""
        return self._call("lurky.usage", {**(input or {}), **fields}, options)  # type: ignore[arg-type]


class MembersResource:
    def __init__(self, call: Call) -> None:
        self._call = call

    def invite(
        self,
        input: Optional[MembersInviteInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> MembersInviteOutput:
        """Invite someone to an organization. Invites an email to an organization as admin, developer or viewer. Owners and admins only. Lasts 7 days. Daily (UTC): 20 for an organization, 10 for a person in all theirs, one email per address; withdrawn ones count. Over a cap: `rate_limited`. [Team](/projects-and-keys#team-and-invitations)"""
        return self._call("members.invite", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def list(
        self,
        input: Optional[MembersListInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> MembersListOutput:
        """List an organization's team. Lists an organization's members and its open invitations together, newest first, with a total. Any member of the organization can read it; an organization you are not in answers `not_found`, like one that does not exist. [Team](/projects-and-keys#team-and-invitations)"""
        return self._call("members.list", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def me(
        self,
        input: Optional[MembersMeInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> MembersMeOutput:
        """Who is signed in. Says who is signed in: their name and email and, when the request names a project, their membership and role in it. `membership` is null when it names none. [Projects and keys](/projects-and-keys)"""
        return self._call("members.me", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def remove(
        self,
        input: Optional[MembersRemoveInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> MembersRemoveOutput:
        """Remove a member. Takes a member out of the organization. Owners and admins only; an owner cannot be removed and nobody removes themselves. The keys they made are revoked, their webhook endpoints disabled and the invitations they sent cancelled. [Team](/projects-and-keys#team-and-invitations)"""
        return self._call("members.remove", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def update(
        self,
        input: Optional[MembersUpdateInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> MembersUpdateOutput:
        """Change a member's role. Gives a member another role: admin, developer or viewer. Owners and admins only; not for an owner. Below admin, the invitations they sent are cancelled; a viewer's keys (the ones they made) are revoked and their webhook endpoints disabled. [Team](/projects-and-keys#team-and-invitations)"""
        return self._call("members.update", {**(input or {}), **fields}, options)  # type: ignore[arg-type]


class OrganizationsResource:
    def __init__(self, call: Call) -> None:
        self._call = call

    def create(
        self,
        input: Optional[OrganizationsCreateInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> OrganizationsCreateOutput:
        """Create an organization. Starts a brand's account and makes you its owner. Not idempotent: a repeated slug is refused, and a retry with no slug makes a second organization (sprout-2). List yours before retrying. [Projects and keys](/projects-and-keys)"""
        return self._call("organizations.create", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def list(
        self,
        input: Optional[OrganizationsListInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> OrganizationsListOutput:
        """List your organizations. Lists the organizations you are a member of, newest first, with your role and project count in each. [Projects and keys](/projects-and-keys)"""
        return self._call("organizations.list", {**(input or {}), **fields}, options)  # type: ignore[arg-type]


class ProjectsResource:
    def __init__(self, call: Call) -> None:
        self._call = call

    def create(
        self,
        input: Optional[ProjectsCreateInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> ProjectsCreateOutput:
        """Create a project. Adds a project (Production or Staging) to an organization you own or administer. Not idempotent: a repeated slug is refused, so list the organization's projects to see whether the first call went through."""
        return self._call("projects.create", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def get(
        self,
        input: Optional[ProjectsGetInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> ProjectsGetOutput:
        """Get a project. One project of an organization the signed-in person is a member of. A project of another brand answers not_found, the same as one that does not exist."""
        return self._call("projects.get", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def list(
        self,
        input: Optional[ProjectsListInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> ProjectsListOutput:
        """List the projects of an organization. The projects of one organization the signed-in person is a member of, newest first. An organization you are not in answers not_found, the same as one that does not exist."""
        return self._call("projects.list", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def setup(
        self,
        input: Optional[ProjectsSetupInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> ProjectsSetupOutput:
        """Get what is left to set this project up. The steps to set the project up (a unit, a rule, an event, going live), which are done, and which dashboard areas they open. Worked out from what the project has, so what an agent made counts. Once a rule has been live nothing is locked. Locks are advice: no operation is refused."""
        return self._call("projects.setup", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def update(
        self,
        input: Optional[ProjectsUpdateInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> ProjectsUpdateOutput:
        """Update a project. Renames a project, sets its time zone, who says yes to proposals and held changes, or the days that make a person new or lapsing. Owners and admins; only an owner changes who says yes. Leave a field out to keep it."""
        return self._call("projects.update", {**(input or {}), **fields}, options)  # type: ignore[arg-type]


class PromotionsResource:
    def __init__(self, call: Call) -> None:
        self._call = call

    def create(
        self,
        input: Optional[PromotionsCreateInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> PromotionsCreateOutput:
        """Propose copying rules and units to another project. Proposes copying rules and units from one project of your organization into another, such as Staging into Production. Nothing is copied now: a person in the target project approves. Missing units are created; rules arrive as drafts. You must be in both projects, and not a viewer in the target."""
        return self._call("promotions.create", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def preview(
        self,
        input: Optional[PromotionsPreviewInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> PromotionsPreviewOutput:
        """See what copying into another project would do. Takes the same input as proposing a copy and says what would be added, updated and left, without making a proposal or writing anything. `can_send` says whether sending it would go through; if not, `problem` says why. You must be in both projects."""
        return self._call("promotions.preview", {**(input or {}), **fields}, options)  # type: ignore[arg-type]


class ProposalsResource:
    def __init__(self, call: Call) -> None:
        self._call = call

    def card(
        self,
        input: Optional[ProposalsCardInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> ProposalsCardOutput:
        """The change card for a proposal. What a person is asked to approve, field by field: the proposal's own before and after for every change, made by the server. `applicable` is true only while it is open and every change shows something that would differ. Lurky shows it beside its words; Apply decides that proposal."""
        return self._call("proposals.card", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def create(
        self,
        input: Optional[ProposalsCreateInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> ProposalsCreateOutput:
        """Propose a change for a person to approve. Asks for something that goes live, such as taking a rule live, without being able to do it. A person with the right to (an owner or admin) approves or declines it; approving runs the same change as them. Nothing runs now. The answer has a link to give that person."""
        return self._call("proposals.create", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def decide(
        self,
        input: Optional[ProposalsDecideInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> ProposalsDecideOutput:
        """Approve or decline a proposal. A person decides. Approving runs every change in the proposal, in order, as the person; if one cannot run, none does and the proposal stays open. Declining runs nothing. Only an owner or admin can (an owner only, if the project says so)."""
        return self._call("proposals.decide", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def get(
        self,
        input: Optional[ProposalsGetInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> ProposalsGetOutput:
        """Get a proposal. One proposal with its changes, who asked, and how it was decided."""
        return self._call("proposals.get", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def list(
        self,
        input: Optional[ProposalsListInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> ProposalsListOutput:
        """List proposals. Proposals newest first. By default the open ones, the ones waiting for a person; `waiting` counts them. An open proposal past its expiry reads as expired."""
        return self._call("proposals.list", {**(input or {}), **fields}, options)  # type: ignore[arg-type]


class RulesResource:
    def __init__(self, call: Call) -> None:
        self._call = call

    def create(
        self,
        input: Optional[RulesCreateInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> RulesCreateOutput:
        """Create a rule as a draft. Nothing runs until an owner or admin takes the draft live, in person. Keys and agents can create and preview rules, but saving a rule with `effects` (not available yet) is refused with `approval_required`. `key` defaults to a slug of the name. See [Rules](/rules)."""
        return self._call("rules.create", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def get(
        self,
        input: Optional[RulesGetInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> RulesGetOutput:
        """Get a rule. By ID or key. `definition` is the newest version; `live_definition` is what is running now, which differs while an edit waits for a person."""
        return self._call("rules.get", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def list(
        self,
        input: Optional[RulesListInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> RulesListOutput:
        """List rules. Newest first. Filter by status, unit, event or part of the name. `counts` says how many rules each status has under the other filters."""
        return self._call("rules.list", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def pause(
        self,
        input: Optional[RulesPauseInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> RulesPauseOutput:
        """Pause a rule. Stops a live rule at once: nothing is given or taken while it is paused. Keys and agents can pause. Starting it again needs an owner or admin, in person, with `POST /v1/rules/{id}/resume`. See [Rules](/rules)."""
        return self._call("rules.pause", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def preview(
        self,
        input: Optional[RulesPreviewInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> RulesPreviewOutput:
        """Preview a rule. Replays up to 20,000 recorded events from the past `days` (1 to 90, default 30) through the real engine and says what the rule would have given. Nothing is given. Send `definition` to try an unsaved edit. Schedule and balance rules get a forecast, not a replay. An estimate: see `notes`."""
        return self._call("rules.preview", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def publish(
        self,
        input: Optional[RulesPublishInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> RulesPublishOutput:
        """Take a rule live. Takes the newest version live. Only an owner or admin, in person. Agents and keys get `approval_required` and should create a proposal. Only the project's first live rule also puts the Overview dashboard on Home when nothing is there."""
        return self._call("rules.publish", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def resume(
        self,
        input: Optional[RulesResumeInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> RulesResumeOutput:
        """Start a paused rule again. The rule runs again on the version it was running. A paused rule going live is a go-live, so only an owner or admin, in person."""
        return self._call("rules.resume", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def stats(
        self,
        input: Optional[RulesStatsInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> RulesStatsOutput:
        """Get what a rule did. From the receipts: how many times the rule changed something, for how many people, and how much it gave or took per unit, plus how often it did not apply and why, and the ten people it reached most. Skips are kept for 30 days."""
        return self._call("rules.stats", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def update(
        self,
        input: Optional[RulesUpdateInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> RulesUpdateOutput:
        """Update a rule. Saves a new version of the newest, with the parts you send replaced. A live rule keeps its version until a person takes the new one live. `name` alone renames, no new version. Saving `effects` (not available yet) gets a key `approval_required`, as does renaming a rule with them. [Rules](/rules)."""
        return self._call("rules.update", {**(input or {}), **fields}, options)  # type: ignore[arg-type]


class TemplatesResource:
    def __init__(self, call: Call) -> None:
        self._call = call

    def get(
        self,
        input: Optional[TemplatesGetInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> TemplatesGetOutput:
        """Get a template. One template: what it adds (units, and rules that arrive as drafts) with its default settings, the settings a person can change, and when it was added to this project."""
        return self._call("templates.get", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def install(
        self,
        input: Optional[TemplatesInstallInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> TemplatesInstallOutput:
        """Add a template. Adds a template's units, views and rules; the rules are drafts and a person takes each live. Existing units and views are reused. Refused if the template is already added, a unit exists with other settings, or a rule key belongs to another rule. To change settings, remove and re-add."""
        return self._call("templates.install", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def list(
        self,
        input: Optional[TemplatesListInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> TemplatesListOutput:
        """List templates. The kits that add units and rules in one go, in the catalog's order, with whether each is available, or already added to this project (`in_use`). `filter: in_use` shows what this project has added."""
        return self._call("templates.list", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def plan(
        self,
        input: Optional[TemplatesPlanInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> TemplatesPlanOutput:
        """Plan a template. What adding a template with these settings would do, and a test week: a fixed, made-up week of visits, orders and sign-ups run through the real engine against the template's own rules. Nothing is written. Say what already exists (it is reused, not added again) and what to check."""
        return self._call("templates.plan", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def remove(
        self,
        input: Optional[TemplatesRemoveInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> TemplatesRemoveOutput:
        """Take a template back. Removes the rules the template added **that are still drafts**, and forgets that it was added. Rules that went live or were paused, the units, and everything people earned stay, and are counted in `kept`. A draft that was never live has no receipts, so the ledger is untouched."""
        return self._call("templates.remove", {**(input or {}), **fields}, options)  # type: ignore[arg-type]


class TrustedIssuersResource:
    def __init__(self, call: Call) -> None:
        self._call = call

    def activate(
        self,
        input: Optional[TrustedIssuersActivateInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> TrustedIssuersActivateOutput:
        """Activate a trusted issuer. Not available yet: sign-in is staging only. Turns a checked, healthy, paused issuer on. Its last check must be at the current revision and at most 24 hours old, or it is refused: check again. Owner or admin in person; a key or agent gets `approval_required`."""
        return self._call("trusted_issuers.activate", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def archive(
        self,
        input: Optional[TrustedIssuersArchiveInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> TrustedIssuersArchiveOutput:
        """Archive a trusted issuer. Not available yet: sign-in is staging only. Retires an issuer for good: no credential can use it; bindings and receipts stay, and its address can be set up again as a new issuer. Cannot be undone. Owner or admin in person; a key or agent gets `approval_required`."""
        return self._call("trusted_issuers.archive", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def check(
        self,
        input: Optional[TrustedIssuersCheckInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> TrustedIssuersCheckOutput:
        """Check a trusted issuer's signing keys. Not available yet: sign-in is staging only. Fetches the issuer's signing keys now and saves what it found: key count, `key_ids_hash`, algorithms, any `problem`. Activation needs a check at the current revision. About 10 a minute per project, one fetch per issuer at a time (`rate_limited`)."""
        return self._call("trusted_issuers.check", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def create(
        self,
        input: Optional[TrustedIssuersCreateInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> TrustedIssuersCreateOutput:
        """Add a trusted issuer. Not available yet: sign-in is staging only. Saves a sign-in provider (Supabase, Clerk or OpenID Connect) a project would trust, paused. Its addresses come from the profile and cannot change. Up to 10 issuers not archived. Owner or admin in person; a key or agent gets `approval_required`."""
        return self._call("trusted_issuers.create", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def get(
        self,
        input: Optional[TrustedIssuersGetInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> TrustedIssuersGetOutput:
        """Get a trusted issuer. Not available yet: sign-in is staging only. One trusted issuer: profile, addresses, revision, status and the health of its signing keys. `can_activate` says whether it could be activated now."""
        return self._call("trusted_issuers.get", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def list(
        self,
        input: Optional[TrustedIssuersListInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> TrustedIssuersListOutput:
        """List trusted issuers. Not available yet: sign-in is staging only. Newest first. The sign-in providers this project has set up, paused or archived."""
        return self._call("trusted_issuers.list", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def pause(
        self,
        input: Optional[TrustedIssuersPauseInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> TrustedIssuersPauseOutput:
        """Pause a trusted issuer. Not available yet: sign-in is staging only. Stops an issuer's tokens from signing anyone in; bindings stay. A saved issuer is paused already. An archived issuer stays archived. Owner or admin in person; a key or agent gets `approval_required`."""
        return self._call("trusted_issuers.pause", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def test(
        self,
        input: Optional[TrustedIssuersTestInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> TrustedIssuersTestOutput:
        """Test whether a sign-in token would be accepted. Not available yet: sign-in is staging only. Tells whether this issuer would accept a sign-in token. Body only, never stored or logged; the answer never holds it, its claims or its subject. Owners, admins and developers only, not keys or agents; about 10 a minute each, 60 an hour per project."""
        return self._call("trusted_issuers.test", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def update(
        self,
        input: Optional[TrustedIssuersUpdateInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> TrustedIssuersUpdateOutput:
        """Rename a trusted issuer. Not available yet: sign-in is staging only. Renames a trusted issuer. Nothing else can be edited: a different address or profile is a new issuer. A rename does not change the revision; a stale `expected_revision` changes nothing."""
        return self._call("trusted_issuers.update", {**(input or {}), **fields}, options)  # type: ignore[arg-type]


class UnitsResource:
    def __init__(self, call: Call) -> None:
        self._call = call

    def create(
        self,
        input: Optional[UnitsCreateInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> UnitsCreateOutput:
        """Create a unit. Sets up a unit: a name, a group and switches for what it can do (goes down, cap, supply, expiry, spend, use, send). The key defaults to a slug of the name and must be new. Owners, admins and developers, or a project key. [Units](/units)"""
        return self._call("units.create", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def get(
        self,
        input: Optional[UnitsGetInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> UnitsGetOutput:
        """Get a unit. By ID or key: its settings and what it holds across everyone."""
        return self._call("units.get", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def give(
        self,
        input: Optional[UnitsGiveInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> UnitsGiveOutput:
        """Give a unit to people by hand. Gives each of up to 200 people the same amount of one unit, one receipt each. A person the unit's settings stop is skipped with a reason; the rest still get theirs. Owners and admins, in the dashboard. [Giving by hand](/units#giving-by-hand)"""
        return self._call("units.give", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def give_preview(
        self,
        input: Optional[UnitsGivePreviewInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> UnitsGivePreviewOutput:
        """Preview giving a unit by hand. Shows what giving a unit by hand would do, without doing it: who would get it, who is skipped and why, who matched nobody, and what is left of a rule's budget (`count_against`). `users` are `usr_…` or your own IDs, up to 200. Writes nothing. [Giving by hand](/units#giving-by-hand)"""
        return self._call("units.give_preview", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def leaderboard(
        self,
        input: Optional[UnitsLeaderboardInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> UnitsLeaderboardOutput:
        """Get who holds the most of a unit. The top of one unit: up to 10 people, most first, with rank, `usr_…` ID and amount; equal amounts share a rank. The unit may be left out: the oldest unit someone holds. Never carries your own identifier for a person or an email. [Leaderboard](/units#the-leaderboard)"""
        return self._call("units.leaderboard", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def list(
        self,
        input: Optional[UnitsListInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> UnitsListOutput:
        """List units. Newest first, with what each holds across everyone, how many hold it, and what was added and taken in the last 30 days. `counts` says how many units each group has."""
        return self._call("units.list", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def send(
        self,
        input: Optional[UnitsSendInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> UnitsSendOutput:
        """Send a unit from one person to another. Moves an amount of one unit between two people as two receipts, all or nothing. The unit needs `sendable` on and must go down; the daily limit is `rate_limited`. Unknown person or unit: `not_found`. Owners and admins, or a project key; never an agent. [Sending](/units#sending-between-people)"""
        return self._call("units.send", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def spend(
        self,
        input: Optional[UnitsSpendInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> UnitsSpendOutput:
        """Take a unit from a person for something. Takes an amount of a unit from a person, all or nothing (`insufficient_balance`). The unit needs `spendable` on. A `reference` is used once per unit (`reference_used`). Unknown person or unit: `not_found`. Owners and admins, or a project key; never an agent. [Spending](/units#spending-and-using)"""
        return self._call("units.spend", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def update(
        self,
        input: Optional[UnitsUpdateInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> UnitsUpdateOutput:
        """Change a unit. Changes what you send. A setting applies to changes from now on and changes nobody's balance: lowering a cap below what people hold leaves their balances, and stops further additions."""
        return self._call("units.update", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def use(
        self,
        input: Optional[UnitsUseInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> UnitsUseOutput:
        """Use something a person holds. Redeems an amount (one by default) of a unit a person holds, all or nothing. The unit needs `usable` on. A `reference` is used once per unit. Fires `unit.used`. Unknown person or unit: `not_found`. Owners and admins, or a project key; never an agent. [Using](/units#spending-and-using)"""
        return self._call("units.use", {**(input or {}), **fields}, options)  # type: ignore[arg-type]


class UsersResource:
    def __init__(self, call: Call) -> None:
        self._call = call

    def alias(
        self,
        input: Optional[UsersAliasInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> UsersAliasOutput:
        """Add an alias to a person. Says another identifier, e.g. a pre-sign-in visitor ID, was this person too, so their history shows its events and receipts. It need not have sent events. Repeating an alias answers as it is. No chains, max 20, the shared anonymous ID refused. [Aliases](/guides/people#aliases-who-a-visitor-was)"""
        return self._call("users.alias", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def block(
        self,
        input: Optional[UsersBlockInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> UsersBlockOutput:
        """Block a person's device credentials. Blocks a person's device credentials on their next request. Blocking a merged-away person blocks the person kept. Needs an owner or admin in person; keys and agents get `approval_required`. Device sign-in is not available yet, so a block changes nothing about who may do what."""
        return self._call("users.block", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def erase(
        self,
        input: Optional[UsersEraseInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> UsersEraseOutput:
        """Erase a person. Not available yet: it answers `unavailable` until erasure is switched on. Starts erasing a person's profile, handles, links and event properties, and those of the people merged into them; their ID, balances and receipts stay. No undo. Owners and admins only, by `usr_…` ID."""
        return self._call("users.erase", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def export(
        self,
        input: Optional[UsersExportInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> UsersExportOutput:
        """Export people as CSV. Exports the people Lurk has heard of, newest first, as a CSV: identifier, first seen, email, name, handles and a column for each unit held. `search` narrows it as on the people list. Up to 10,000 people, then `truncated` is true. Owners and admins only; each export is audited."""
        return self._call("users.export", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def get(
        self,
        input: Optional[UsersGetInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> UsersGetOutput:
        """Get a person. Gets one person by `usr_…` ID or by your own identifier: holdings, profile, status (new, returning, lapsing), last activity, time zone and receipt count. A person merged into another returns `not_found`. [People](/guides/people)"""
        return self._call("users.get", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def history(
        self,
        input: Optional[UsersHistoryInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> UsersHistoryOutput:
        """Get a person's history. A person's events and receipts, newest first, including merged people's and aliases' (`seen_as`). `event` also returns the receipts it caused, and a page filtered by it can hold fewer than `limit` items, even none, and still have `has_more`. [People](/guides/people#a-persons-history)"""
        return self._call("users.history", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def list(
        self,
        input: Optional[UsersListInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> UsersListOutput:
        """List people. Lists people, newest first (`sort`), with holdings, profile and new/returning/lapsing status. `search` takes one whole value: a `usr_…` ID, your identifier, or an email or handle (any case); no partial match. Also `audience` (key or ID), `status`, `include=total`. [People](/guides/people)"""
        return self._call("users.list", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def merge(
        self,
        input: Optional[UsersMergeInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> UsersMergeOutput:
        """Merge one person into another. Merges `from` into `into`: what `from` holds moves to `into` as receipts, and `from`'s later events count for `into`. Needs an owner or admin in person; keys and agents get `approval_required`. Looking up `from` afterwards returns `not_found`. [Merging](/guides/people#merging-existing-people)"""
        return self._call("users.merge", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def unalias(
        self,
        input: Optional[UsersUnaliasInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> UsersUnaliasOutput:
        """Remove an alias from a person. Removes an alias: the person's history stops reading that identifier's events and receipts, and nothing else changes. An identifier that is not this person's alias returns `not_found`. [Aliases](/guides/people#aliases-who-a-visitor-was)"""
        return self._call("users.unalias", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def unblock(
        self,
        input: Optional[UsersUnblockInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> UsersUnblockOutput:
        """Unblock a person's device credentials. Lifts the block on a person's device credentials. Unblocking a merged-away person unblocks the person kept. Needs an owner or admin in person; keys and agents get `approval_required`. Device sign-in is not available yet, so nothing signs anyone in, blocked or not."""
        return self._call("users.unblock", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def unmerge(
        self,
        input: Optional[UsersUnmergeInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> UsersUnmergeOutput:
        """Undo a merge. Gives a merged-away person back by reversing the merge's receipts with new ones. Refused if the person kept has spent what came or a cap would break. Needs an owner or admin in person; keys and agents get `approval_required`. [Merging people](/guides/people#merging-existing-people)"""
        return self._call("users.unmerge", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def update(
        self,
        input: Optional[UsersUpdateInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> UsersUpdateOutput:
        """Update a person's profile. Sets the profile of an existing person (for a new one, send `profile` with the event): email, name, picture, handles, language. Left out is kept, null clears. In `handles` an entry replaces that platform's, null removes it. `profile: null` erases all. [People](/guides/people#a-persons-profile)"""
        return self._call("users.update", {**(input or {}), **fields}, options)  # type: ignore[arg-type]


class ViewsResource:
    def __init__(self, call: Call) -> None:
        self._call = call

    def create(
        self,
        input: Optional[ViewsCreateInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> ViewsCreateOutput:
        """Create a view. Saves a question about the project: who, what, over which range, as which shape (number, chart, ranked list). A member, key, brand agent or Lurky may; not a viewer. Audience and units must exist. `key` defaults to a slug of the name (`view-` first if a digit leads). [Views](/views#save-a-view)"""
        return self._call("views.create", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def get(
        self,
        input: Optional[ViewsGetInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> ViewsGetOutput:
        """Get a view. A view and its answer: a number, a series over time, or a ranked list. `range` reads another range, `compare` adds the span of the same length just before, `audience` reads for another audience. Ranges and weeks (Monday to Sunday) follow the project's time zone. [Views](/views#read-a-view)"""
        return self._call("views.get", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def list(
        self,
        input: Optional[ViewsListInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> ViewsListOutput:
        """List views. The saved questions of the project, newest first. A view is typed data (who, what, over, shape), never SQL. Search matches a name or key."""
        return self._call("views.list", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def update(
        self,
        input: Optional[ViewsUpdateInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> ViewsUpdateOutput:
        """Update a view. Renames a view, changes its description, or replaces its whole definition. Send at least one change. Dashboards that show it show the new question. [Views](/views#list-and-change-views)"""
        return self._call("views.update", {**(input or {}), **fields}, options)  # type: ignore[arg-type]


class WebhookEndpointsResource:
    def __init__(self, call: Call) -> None:
        self._call = call

    def create(
        self,
        input: Optional[WebhookEndpointsCreateInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> WebhookEndpointsCreateOutput:
        """Add a webhook endpoint. Lurk sends the events you pick to this URL, signed with the secret in the response. The secret is shown once. A project can have up to 25 active endpoints; switched-off ones are not counted."""
        return self._call("webhook_endpoints.create", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def delete(
        self,
        input: Optional[WebhookEndpointsDeleteInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> WebhookEndpointsDeleteOutput:
        """Delete a webhook endpoint. Stops sending to it and removes its delivery history. This can't be undone."""
        return self._call("webhook_endpoints.delete", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def list(
        self,
        input: Optional[WebhookEndpointsListInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> WebhookEndpointsListOutput:
        """List webhook endpoints. Newest first. Shows where events go and whether each endpoint is still switched on."""
        return self._call("webhook_endpoints.list", {**(input or {}), **fields}, options)  # type: ignore[arg-type]


class Resources:
    """The groups of operations, one attribute each. `Lurk` is this with the transport behind it."""

    activity: ActivityResource
    agent_keys: AgentKeysResource
    api_keys: ApiKeysResource
    audiences: AudiencesResource
    budgets: BudgetsResource
    chat_directory: ChatDirectoryResource
    chat_mirrors: ChatMirrorsResource
    chat_settings: ChatSettingsResource
    client_events: ClientEventsResource
    clocks: ClocksResource
    dashboards: DashboardsResource
    erasures: ErasuresResource
    events: EventsResource
    exports: ExportsResource
    feedback: FeedbackResource
    holds: HoldsResource
    identity_links: IdentityLinksResource
    integrations: IntegrationsResource
    invites: InvitesResource
    issuer_identities: IssuerIdentitiesResource
    known_values: KnownValuesResource
    lurky: LurkyResource
    members: MembersResource
    organizations: OrganizationsResource
    projects: ProjectsResource
    promotions: PromotionsResource
    proposals: ProposalsResource
    rules: RulesResource
    templates: TemplatesResource
    trusted_issuers: TrustedIssuersResource
    units: UnitsResource
    users: UsersResource
    views: ViewsResource
    webhook_endpoints: WebhookEndpointsResource

    def __init__(self, call: Call) -> None:
        self.activity = ActivityResource(call)
        self.agent_keys = AgentKeysResource(call)
        self.api_keys = ApiKeysResource(call)
        self.audiences = AudiencesResource(call)
        self.budgets = BudgetsResource(call)
        self.chat_directory = ChatDirectoryResource(call)
        self.chat_mirrors = ChatMirrorsResource(call)
        self.chat_settings = ChatSettingsResource(call)
        self.client_events = ClientEventsResource(call)
        self.clocks = ClocksResource(call)
        self.dashboards = DashboardsResource(call)
        self.erasures = ErasuresResource(call)
        self.events = EventsResource(call)
        self.exports = ExportsResource(call)
        self.feedback = FeedbackResource(call)
        self.holds = HoldsResource(call)
        self.identity_links = IdentityLinksResource(call)
        self.integrations = IntegrationsResource(call)
        self.invites = InvitesResource(call)
        self.issuer_identities = IssuerIdentitiesResource(call)
        self.known_values = KnownValuesResource(call)
        self.lurky = LurkyResource(call)
        self.members = MembersResource(call)
        self.organizations = OrganizationsResource(call)
        self.projects = ProjectsResource(call)
        self.promotions = PromotionsResource(call)
        self.proposals = ProposalsResource(call)
        self.rules = RulesResource(call)
        self.templates = TemplatesResource(call)
        self.trusted_issuers = TrustedIssuersResource(call)
        self.units = UnitsResource(call)
        self.users = UsersResource(call)
        self.views = ViewsResource(call)
        self.webhook_endpoints = WebhookEndpointsResource(call)
