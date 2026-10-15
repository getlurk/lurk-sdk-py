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
    HoldsDecideInput,
    HoldsDecideOutput,
    HoldsGetInput,
    HoldsGetOutput,
    HoldsListInput,
    HoldsListOutput,
    IntegrationsHealthInput,
    IntegrationsHealthOutput,
    IntegrationsListInput,
    IntegrationsListOutput,
    InvitesAcceptInput,
    InvitesAcceptOutput,
    InvitesDeclineInput,
    InvitesDeclineOutput,
    InvitesListInput,
    InvitesListOutput,
    InvitesRevokeInput,
    InvitesRevokeOutput,
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
    UnitsCreateInput,
    UnitsCreateOutput,
    UnitsGetInput,
    UnitsGetOutput,
    UnitsGiveInput,
    UnitsGiveOutput,
    UnitsGivePreviewInput,
    UnitsGivePreviewOutput,
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
    UsersExportInput,
    UsersExportOutput,
    UsersGetInput,
    UsersGetOutput,
    UsersListInput,
    UsersListOutput,
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
        """Export receipts as CSV. The receipts that match, newest first, as a CSV file: one row for each unit a receipt changed. The same filters as the list. Up to 10,000 rows; past that the file stops and says so (`truncated`), so narrow the filters. Text a spreadsheet would run as a formula is written as text. Every export leaves an audit entry."""
        return self._call("activity.export", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def feed(
        self,
        input: Optional[ActivityFeedInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> ActivityFeedOutput:
        """List what happened and what didn't. One list, newest first, of receipts (`given`), rules that heard an event and did nothing (`skipped`, with the reason; kept 30 days) and changes waiting for a person (`held`). Filter by `kind`, person, rule, unit or time. A skip changed no unit, so filtering by unit leaves skips out. Once a held change is decided it is a receipt or a `hold_refused` skip, never both."""
        return self._call("activity.feed", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def list(
        self,
        input: Optional[ActivityListInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> ActivityListOutput:
        """List receipts. Newest first. Every receipt says who acted, through what, and each unit it changed with the balance after. Filter by person, rule, unit or time."""
        return self._call("activity.list", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def undo(
        self,
        input: Optional[ActivityUndoInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> ActivityUndoOutput:
        """Undo a receipt. Writes a new receipt that reverses the first, by the person, and both stay: a ledger never deletes. Refused when the receipt is itself an undo, was already undone, or the person's balance no longer allows taking it back (it would go below the unit's floor or past its cap). Only an owner or admin can. Limits a rule counted are not given back."""
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
        """Create an agent key. Only an owner or admin, in person. One key per agent: its name is what receipts and proposals say. The full key is in the response once; Lurk keeps only a hash and cannot show it again."""
        return self._call("agent_keys.create", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def list(
        self,
        input: Optional[AgentKeysListInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> AgentKeysListOutput:
        """List agent keys. Newest first. Shows each agent's name, the start of its key and its state; the full key is never shown again."""
        return self._call("agent_keys.list", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def revoke(
        self,
        input: Optional[AgentKeysRevokeInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> AgentKeysRevokeOutput:
        """Revoke an agent key. Only an owner or admin, in person. The agent stops working at once, on its next request. Revoking a revoked key changes nothing."""
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
        """Create a project API key. Only an owner or admin, in person. The full key is in the response once; Lurk keeps only a hash and cannot show it again."""
        return self._call("api_keys.create", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def list(
        self,
        input: Optional[ApiKeysListInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> ApiKeysListOutput:
        """List project API keys. Newest first. Shows each key's name, start and state; the full key is never shown again."""
        return self._call("api_keys.list", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def revoke(
        self,
        input: Optional[ApiKeysRevokeInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> ApiKeysRevokeOutput:
        """Revoke a project API key. Only an owner or admin, in person. The key stops working at once. Revoking a revoked key changes nothing."""
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
        """Create an audience. A list (people you add by hand or over the API) or a condition audience (kept up to date by its conditions: active on N days, first seen, inactive, holds at least N, a property total). A new condition audience is empty until the worker works it out, within five minutes. Rules can then read it in `if`."""
        return self._call("audiences.create", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def list(
        self,
        input: Optional[AudiencesListInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> AudiencesListOutput:
        """List audiences. The groups of people rules can read, newest first, with how many are in each and which rules read it. A condition audience's members are worked out every five minutes: `refreshed_at` says when, and a rule sees it as it stood then."""
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
        """Move a staging project's clock forward. Moves the project's time forward by days, hours or minutes, so a seven-day streak, a weekly schedule or an expiry can be tried without waiting. Staging projects only. Scheduled rules and expiries that come due run within a minute. Time only moves forward, except for a reset."""
        return self._call("clocks.advance", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def get(
        self,
        input: Optional[ClocksGetInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> ClocksGetOutput:
        """Read the project's clock. What time it is in this project, and whether it has been moved from real time. Only a staging project's clock can be moved; a production project always shows real time."""
        return self._call("clocks.get", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def reset(
        self,
        input: Optional[ClocksResetInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> ClocksResetOutput:
        """Put a staging project's clock back to real time. Ends the test clock: the project runs on real time again. This is the one way time goes back, so receipts made while the clock was ahead will look as if they come from the future until real time catches up. Staging projects only."""
        return self._call("clocks.reset", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def set(
        self,
        input: Optional[ClocksSetInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> ClocksSetOutput:
        """Move a staging project's clock to a time. Sets the time the project thinks it is, such as the Monday a schedule should run. It cannot be earlier than the project's time now; use a reset to start over. Staging projects only."""
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
        """Make a dashboard. A dashboard of views on the 12-column grid, up to 40 tiles. `unit` makes it that unit's own dashboard (one each). It is not shown on Home until `dashboards.update` says so."""
        return self._call("dashboards.create", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def get(
        self,
        input: Optional[DashboardsGetInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> DashboardsGetOutput:
        """Get a dashboard. One dashboard with its tiles: each tile is a view and a place on the 12-column grid. Use "home" for the one on Home, or "unit:<key>" for a unit's own. A tile's answer is `views.get`."""
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
        """Read a dashboard with every tile's answer. A dashboard and the answer of each of its tiles in one call, so a board is one read and not one for every tile. `range`, `compare` and `audience` apply to every tile as they do to `views.get`; the answers are by tile `id`. Use "home" for the one on Home, or "unit:<key>" for a unit's own."""
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
        """List the events this project has. Every event name that arrived in the last 30 days or that a rule listens for, once each, in name order: how many arrived, when the newest did, its property names (never values) and the rules listening."""
        return self._call("events.catalog", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def send(
        self,
        input: Optional[EventsSendInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> EventsSendOutput:
        """Send an event. Something a user did. Lurk runs your live rules on it and returns the receipts: what changed and the balance after."""
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
        """Stop an export. Stops a queued or running export. What it had written is thrown away. An export that has finished is not changed; to remove its file before the three days are up, it is deleted when it expires. Owners and admins only."""
        return self._call("exports.cancel", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def create(
        self,
        input: Optional[ExportsCreateInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> ExportsCreateOutput:
        """Start an export. Starts a file of receipts or people, made in the background, with the same filters as the quick export. It answers at once with a job to watch (`exports.get`); when it is ready, `exports.download` gives a link. It holds up to 1,000,000 rows, and the file is deleted three days after it is ready. Owners and admins only, 3 a person and 20 a project a day. Every export leaves an audit entry."""
        return self._call("exports.create", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def download(
        self,
        input: Optional[ExportsDownloadInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> ExportsDownloadOutput:
        """Get the link to an export's file. A link to the finished file, good for 5 minutes. Ask again for a new one. No link is given once the file's three days are up, even if it has not been deleted yet. Owners and admins only; every download leaves an audit entry."""
        return self._call("exports.download", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def get(
        self,
        input: Optional[ExportsGetInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> ExportsGetOutput:
        """See how an export is going. Whether the file is queued, being made (with the rows written so far), ready (with when it will be deleted), failed (with why) or gone. Owners and admins only."""
        return self._call("exports.get", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def list(
        self,
        input: Optional[ExportsListInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> ExportsListOutput:
        """List recent exports. The project's exports, newest first, with who asked and how each went. Owners and admins only."""
        return self._call("exports.list", {**(input or {}), **fields}, options)  # type: ignore[arg-type]


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
        """Give or refuse a hold. A person decides. Giving makes the rule's changes now, as one receipt, if the balance still allows them and the rule's budget for the window has room (giving spends it); if it doesn't, nothing changes and the hold stays for the person to refuse. Refusing changes nothing and is recorded. Only an owner or admin can (an owner only, if the project says so)."""
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


class IntegrationsResource:
    def __init__(self, call: Call) -> None:
        self._call = call

    def health(
        self,
        input: Optional[IntegrationsHealthInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> IntegrationsHealthOutput:
        """Check the integrations. What is wrong with the connectors this project has, and how to fix it. Without `key` it answers for the ones that are connected or need attention; with `key` it answers for that one, whatever its status. `needs_attention` counts them all, for the sidebar. A failing webhook endpoint is a problem; one a person turned off is not."""
        return self._call("integrations.health", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def list(
        self,
        input: Optional[IntegrationsListInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> IntegrationsListOutput:
        """List integrations. Every way events reach Lurk or state leaves it, in the order the dashboard shows them, with what this project has: `connected`, `needs_attention` (connected, but something is wrong), `not_connected`, or `later` (listed, but not available yet). Your app, MCP and webhooks are real today and their status is read from your keys and endpoints. `filter: connected` includes the ones that need attention."""
        return self._call("integrations.list", {**(input or {}), **fields}, options)  # type: ignore[arg-type]


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
        """Accept an invitation. Joins the organization with the invited role. Only the person who signed in with the invited address can; anything else answers not_found."""
        return self._call("invites.accept", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def decline(
        self,
        input: Optional[InvitesDeclineInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> InvitesDeclineOutput:
        """Decline an invitation. Turns an invitation down. Only the person who signed in with the invited address can."""
        return self._call("invites.decline", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def list(
        self,
        input: Optional[InvitesListInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> InvitesListOutput:
        """List the invitations to you. Open invitations to the email address you signed in with, newest first. Answers nothing until that address is verified."""
        return self._call("invites.list", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def revoke(
        self,
        input: Optional[InvitesRevokeInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> InvitesRevokeOutput:
        """Cancel an invitation. Withdraws an invitation that has not been answered. Owners and admins can."""
        return self._call("invites.revoke", {**(input or {}), **fields}, options)  # type: ignore[arg-type]


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
        """Yesterday in a line. What happened yesterday, in the project's time zone: how many people were active (and how that compares with the day before), how many were new, how many events came in and what was given, as a sentence and as the numbers behind it. No model is used, so it costs nothing. The sentence is null while the project has not heard anything yet."""
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
        """What Home suggests. The cards on Home, worked out from what the project has now: what needs a person (an approval, held receipts, a budget nearly used, a connector that needs attention), what changed (people drifting away, a paused rule) and one idea. At most six, most urgent first, without the ones this member put away. Each says why, in the project's own numbers. Nothing here uses a model, so it costs nothing."""
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
        """Invite someone to an organization. Invites an email address with a role (admin, developer or viewer) to an organization you own or administer. They join when they sign in with that address and accept. Inviting an address that already has an open invitation renews it; an address that is already a member is refused."""
        return self._call("members.invite", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def list(
        self,
        input: Optional[MembersListInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> MembersListOutput:
        """List an organization's team. The people in an organization and the invitations still open, newest first, with the total of both. An organization you are not in answers not_found, the same as one that does not exist."""
        return self._call("members.list", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def me(
        self,
        input: Optional[MembersMeInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> MembersMeOutput:
        """Who is signed in. The person behind the session and, when the request names a project, their membership and role in it."""
        return self._call("members.me", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def remove(
        self,
        input: Optional[MembersRemoveInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> MembersRemoveOutput:
        """Remove a member. Takes a member out of the organization. Owners and admins can; an owner cannot be removed, and nobody removes themselves."""
        return self._call("members.remove", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def update(
        self,
        input: Optional[MembersUpdateInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> MembersUpdateOutput:
        """Change a member's role. Gives a member another role (admin, developer or viewer). Owners and admins can; an owner's role does not change here."""
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
        """Create an organization. Starts a brand's account; you become its owner. Not idempotent: a repeated slug is refused, so list your organizations to see whether the first call went through."""
        return self._call("organizations.create", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def list(
        self,
        input: Optional[OrganizationsListInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> OrganizationsListOutput:
        """List your organizations. The organizations the signed-in person is a member of, newest first, with their role in each."""
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
        """What is left to set this project up. The steps to set the project up (a unit, a rule, an event, going live), which are done, and which parts of the dashboard they open. It is worked out from what the project has, so what an agent made through the API counts. Once a rule has been live the project is past setup and nothing is locked. The locks are advice for the dashboard: no operation is refused because of them."""
        return self._call("projects.setup", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def update(
        self,
        input: Optional[ProjectsUpdateInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> ProjectsUpdateOutput:
        """Update a project. Renames a project, sets its time zone, sets who says yes to proposals and held changes, or sets how many days a person is new and how many quiet days make them lapsing. An owner or admin can change the name, time zone and those two numbers; only an owner can change who says yes. Leave a field out to keep it."""
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
        """Copy rules and units into another project, for a person to approve. Proposes copying rules and units from one project of your organization into another, such as Staging into Production. Nothing is copied now: it makes a proposal in the project it copies into, and a person there approves it. Units are created if the project has none with the key; rules arrive as drafts (a new draft version if the key is there), and are taken live like any rule. The units a rule changes are copied with it if they are missing. You need to be in both projects."""
        return self._call("promotions.create", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def preview(
        self,
        input: Optional[PromotionsPreviewInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> PromotionsPreviewOutput:
        """See what copying into another project would do. Takes the same input as `promotions.create` and says what would be added, updated and left, without making a proposal or writing anything. `can_send` says whether `promotions.create` would go through; if not, `problem` says why. You need to be in both projects."""
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
        """The change card for a proposal. What a person is asked to approve, field by field: the proposal's own before and after for every change, made by the server. A card is applicable only while the proposal is open and every change shows something that would differ. Lurky shows this beside its words, and Apply decides the proposal by its ID."""
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
        """Create a rule as a draft. Rules start as drafts. A key or an agent can create and preview them; only a person takes one live."""
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
        """Pause a rule. Stops a live rule at once: nothing is given or taken while it is paused. Safe for an agent to do. Starting it again needs a person (`rules.resume`)."""
        return self._call("rules.pause", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def preview(
        self,
        input: Optional[RulesPreviewInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> RulesPreviewOutput:
        """Preview a rule. For a rule that starts on an event, replays up to 20,000 recorded events of the past days through the real rule engine, in memory, and says what the rule would have given. For a rule on a schedule, says when it runs next and how many people it reaches; for one that starts when a balance moves, which rules lead into it and how many people are already there. Nothing is given. Send `definition` to try an edit that is not saved yet. It is an estimate: see `notes`."""
        return self._call("rules.preview", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def publish(
        self,
        input: Optional[RulesPublishInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> RulesPublishOutput:
        """Take a rule live. Takes the newest version live. Only an owner or admin, in person. Agents and keys get `approval_required` and should create a proposal."""
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
        """What a rule did. From the receipts: how many times the rule changed something, for how many people, and how much it gave or took per unit, plus how often it did not apply and why, and the ten people it reached most. Skips are kept for 30 days."""
        return self._call("rules.stats", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def update(
        self,
        input: Optional[RulesUpdateInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> RulesUpdateOutput:
        """Edit a rule. Writes a new version from the newest one with the parts you send replaced. A live rule keeps running its live version until a person takes the new one live. Sending only `name` renames the rule without a new version."""
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
        """Add a template. Adds a template's units and views (one that already exists is reused as it is) and its rules **as drafts**; a person takes each rule live. Refused if the template is already added, can't run yet, or a rule it adds has the key of one that exists. A template is added once: remove it to change its settings."""
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
        """Plan adding a template. What adding a template with these settings would do, and a test week: a fixed, made-up week of visits, orders and sign-ups run through the real engine against the template's own rules. Nothing is written. Say what already exists (it is reused, not added again) and what to check."""
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
        """Create a unit. Sets up a unit: what it is called and what it allows. Only settings Lurk enforces are accepted: goes up, goes down, a cap per person, the lowest balance, whether the app shows it, a supply (the most that can ever be given in all) and an expiry (what is given is taken back after so many days). Sending between people comes later."""
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
        """Give a unit to people by hand. Gives each of up to 200 people the same amount of one unit, one receipt each, by the person and with an optional note. People are `usr_…` IDs or the brand's own IDs. The unit's own settings apply: someone it can't be given to is skipped with the reason and the others still get theirs. `count_against` names a rule with a budget in this unit: the give is counted in it, and if it would pass the budget nothing is given. Only an owner or admin can; use `units.give_preview` first."""
        return self._call("units.give", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def give_preview(
        self,
        input: Optional[UnitsGivePreviewInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> UnitsGivePreviewOutput:
        """Preview giving a unit by hand. What `units.give` would do with the same input, without doing it: who gets the unit, who is skipped and why (the unit's own settings), who matched nobody, and what is left of the budget when the give is counted in a rule. Nothing is written."""
        return self._call("units.give_preview", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

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
        """Send a unit from one person to another. Moves an amount of one unit from one person to another, as two receipts (`send` and `receive`, with the same `transfer` ID) that happen together or not at all. The sender must hold the amount above the unit's lowest balance (`insufficient_balance`), have sent less than the unit's daily limit today (`rate_limited`), and the receiver must be able to hold it (the unit's cap). What expires keeps its expiry: the receiver gets the sender's clock, not a new one. A send makes nothing: it is not counted as given or spent. The unit must allow it (`sendable`). Both people must already be known. Called by your server with a project key for a person, or by an owner or admin; never by an agent. Units cannot be bought, cashed out or given a money value."""
        return self._call("units.send", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def spend(
        self,
        input: Optional[UnitsSpendInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> UnitsSpendOutput:
        """Take a unit from a person for something. Takes an amount of one unit from one person, for a stated reason: a free coffee for 100 Beans. All or nothing: it is refused with `insufficient_balance` when the person holds less than the amount above the unit's lowest balance. What expires first is taken first. A `reference` (your own redemption or order ID) can be used once per unit; a second spend with it is refused with `reference_used`, and a retry of the same request returns the first answer. The unit must allow it (`spendable`). Called by your server with a project key, or by an owner or admin; never by an agent."""
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
        """Use something a person holds. Redeems an amount (one by default) of a unit a person holds: a coupon at the till, a ticket at the door. All or nothing: it is refused with `insufficient_balance` when the person holds less. What expires first is used first. A `reference` (your own scan or redemption ID) can be used once per unit; a second use with it is refused with `reference_used`, and a retry of the same request returns the first answer. The unit must allow it (`usable`). It fires the `unit.used` webhook as well as `activity.created`. Called by your server with a project key, or by an owner or admin; never by an agent."""
        return self._call("units.use", {**(input or {}), **fields}, options)  # type: ignore[arg-type]


class UsersResource:
    def __init__(self, call: Call) -> None:
        self._call = call

    def export(
        self,
        input: Optional[UsersExportInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> UsersExportOutput:
        """Export people as CSV. The people Lurk has heard of, newest first, as a CSV file: the brand's identifier, when Lurk first heard of them, and a column for each unit with what they hold. Up to 10,000 people; past that the file stops and says so (`truncated`). Text a spreadsheet would run as a formula is written as text. Every export leaves an audit entry."""
        return self._call("users.export", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def get(
        self,
        input: Optional[UsersGetInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> UsersGetOutput:
        """Get a person. By `usr_…` ID or by the brand's own identifier (the one events use): what they hold, their time zone, and how many receipts they have. Also whether they are new, returning or lapsing, and when they were last active."""
        return self._call("users.get", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def list(
        self,
        input: Optional[UsersListInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> UsersListOutput:
        """List people. The people Lurk has heard of in this project, newest first (or oldest first with `sort`), with what each holds. Search takes the brand's whole identifier: they are kept sealed, so there is no partial match. `audience` keeps only the people in one audience, `status` keeps only the new, returning or lapsing ones, and `include=total` adds how many people match across every page. Every person says which of the three they are."""
        return self._call("users.list", {**(input or {}), **fields}, options)  # type: ignore[arg-type]


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
        """Save a view. Saves a question about the project: who, what, over which range, as which shape (a number, a chart over time, or a ranked list). It only reads, so a member, a key or an agent can save one. The audience and units it names must exist."""
        return self._call("views.create", {**(input or {}), **fields}, options)  # type: ignore[arg-type]

    def get(
        self,
        input: Optional[ViewsGetInput] = None,
        /,
        *,
        options: Optional[RequestOptions] = None,
        **fields: Any,
    ) -> ViewsGetOutput:
        """Read a view. A view and its answer, computed from the project's data when asked: a number, a series over time, or a ranked list. Read it over another `range`, `compare` it with the span of the same length just before, or read it for another `audience`. Ranges and weeks are in the project's time zone (a week is Monday to Sunday)."""
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
        """Change a view. Renames a view, changes its description, or replaces its whole definition. Dashboards that show it show the new question."""
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
        """Add a webhook endpoint. Lurk sends the events you pick to this URL, signed with the secret in the response. The secret is shown once."""
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
    clocks: ClocksResource
    dashboards: DashboardsResource
    events: EventsResource
    exports: ExportsResource
    holds: HoldsResource
    integrations: IntegrationsResource
    invites: InvitesResource
    lurky: LurkyResource
    members: MembersResource
    organizations: OrganizationsResource
    projects: ProjectsResource
    promotions: PromotionsResource
    proposals: ProposalsResource
    rules: RulesResource
    templates: TemplatesResource
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
        self.clocks = ClocksResource(call)
        self.dashboards = DashboardsResource(call)
        self.events = EventsResource(call)
        self.exports = ExportsResource(call)
        self.holds = HoldsResource(call)
        self.integrations = IntegrationsResource(call)
        self.invites = InvitesResource(call)
        self.lurky = LurkyResource(call)
        self.members = MembersResource(call)
        self.organizations = OrganizationsResource(call)
        self.projects = ProjectsResource(call)
        self.promotions = PromotionsResource(call)
        self.proposals = ProposalsResource(call)
        self.rules = RulesResource(call)
        self.templates = TemplatesResource(call)
        self.units = UnitsResource(call)
        self.users = UsersResource(call)
        self.views = ViewsResource(call)
        self.webhook_endpoints = WebhookEndpointsResource(call)
