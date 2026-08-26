"""
PydanticAI agent + typed MCP client for AnyDB Kaizen Commerce.

Two layers in one file:

1. ``AnyDBClient`` — async context manager that owns a stdio connection to
   the ``anydb-mcp-service`` binary. Exposes typed methods that take/return
   Phase 1 Pydantic models (see ``models.py``). Use this directly from
   scripts (e.g. LangExtract Workflow 3) when you don't need an LLM.

2. ``build_agent()`` — wires those typed methods up as PydanticAI tools so
   an LLM can drive them. Each tool has a proper Pydantic schema, so the
   model sees real enums and gets rejected locally before a bad update
   ever hits the network.

Fixed IDs (team / database, optional attach root) are configured in models.py;
callers never pass them.

Usage — direct (Workflow 3 style):

    async with AnyDBClient() as db:
        merchants = await db.list_records("Merchants")
        new_id = await db.create(
            Merchant(company_name="Quai du Vin",
                     client_status=MerchantClientStatus.PROSPECT),
            templatename="Merchants",
            name="Quai du Vin",
        )
        await db.update(Project(adoid=pid, status=ProjectStatus.IN_PROGRESS))

Usage — LLM-driven:

    async with AnyDBClient() as db:
        agent = build_agent(db)
        result = await agent.run("Mark the SGP project as In Progress.")
        print(result.output)
"""
from __future__ import annotations

import json
import os
from contextlib import AsyncExitStack
from typing import Any, Optional

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from pydantic import BaseModel, Field
from pydantic_ai import Agent, RunContext

from models import (
    ADBID,
    ROOTID,
    TEAMID,
    AnyDBRecord,
    Contact,
    Deal,
    Merchant,
    Project,
    Task,
)

# ---------- MCP server config ----------

ANYDB_BIN = os.environ.get("ANYDB_MCP_BIN", "/opt/homebrew/bin/anydb-mcp-service")
ANYDB_API_KEY = os.environ.get("ANYDB_DEFAULT_API_KEY", "")
ANYDB_USER_EMAIL = os.environ.get(
    "ANYDB_DEFAULT_USER_EMAIL", "operations@kaizencommerce.ca"
)
ANYDB_API_BASE_URL = os.environ.get(
    "ANYDB_API_BASE_URL", "https://app.anydb.com/api"
)
ANYDB_API_URL = os.environ.get("ANYDB_API_URL", ANYDB_API_BASE_URL)


def _server_params() -> StdioServerParameters:
    if not ANYDB_API_KEY:
        raise RuntimeError(
            "ANYDB_DEFAULT_API_KEY not set. Export it before starting the agent."
        )
    return StdioServerParameters(
        command=ANYDB_BIN,
        args=[],
        env={
            "ANYDB_DEFAULT_API_KEY": ANYDB_API_KEY,
            "ANYDB_DEFAULT_USER_EMAIL": ANYDB_USER_EMAIL,
            "ANYDB_API_URL": ANYDB_API_URL,
            "ANYDB_API_BASE_URL": ANYDB_API_BASE_URL,
            "PATH": "/opt/homebrew/bin:/usr/bin:/bin",
        },
    )


# ---------- Typed MCP client ----------


class AnyDBClient:
    """
    Async context-managed wrapper around the AnyDB MCP stdio server.

    Holds one long-lived session per instance. Caches ``templatename ->
    templateID`` so ``create()`` doesn't re-lookup every call.
    """

    def __init__(self) -> None:
        self._session: Optional[ClientSession] = None
        self._stack: Optional[AsyncExitStack] = None
        self._template_ids: dict[str, str] = {}

    # ----- lifecycle -----
    async def __aenter__(self) -> "AnyDBClient":
        self._stack = AsyncExitStack()
        read, write = await self._stack.enter_async_context(
            stdio_client(_server_params())
        )
        self._session = await self._stack.enter_async_context(
            ClientSession(read, write)
        )
        await self._session.initialize()
        return self

    async def __aexit__(self, exc_type, exc, tb) -> None:
        if self._stack is not None:
            await self._stack.aclose()
        self._stack = None
        self._session = None

    # ----- low-level -----
    async def _call(self, tool: str, args: dict[str, Any]) -> Any:
        if self._session is None:
            raise RuntimeError("AnyDBClient must be used as async context manager")
        res = await self._session.call_tool(tool, args)
        if res.isError:
            raise RuntimeError(f"{tool} failed: {res.content}")
        if not res.content:
            return None
        block = res.content[0]
        text = getattr(block, "text", None)
        if text is None:
            return None
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            return text

    async def _template_id(self, templatename: str) -> str:
        """Resolve (and cache) a template name to its MongoDB template ID."""
        if templatename in self._template_ids:
            return self._template_ids[templatename]
        data = await self._call(
            "list_records",
            {
                "teamid": TEAMID,
                "adbid": ADBID,
                "templatename": templatename,
                "pagesize": "1",
            },
        )
        items = (data or {}).get("items") or []
        if not items:
            raise RuntimeError(
                f"Cannot resolve template ID for {templatename!r}: no records exist "
                "yet. Create one manually in AnyDB first, or hardcode the ID."
            )
        tid = items[0].get("templateID")
        if not tid:
            raise RuntimeError(f"Record for {templatename!r} has no templateID field")
        self._template_ids[templatename] = tid
        return tid

    # ----- read -----
    async def list_records(
        self,
        templatename: Optional[str] = None,
        parentid: Optional[str] = None,
        pagesize: Optional[int] = None,
    ) -> list[dict[str, Any]]:
        args: dict[str, Any] = {"teamid": TEAMID, "adbid": ADBID}
        if templatename:
            args["templatename"] = templatename
        if parentid:
            args["parentid"] = parentid
        if pagesize:
            args["pagesize"] = str(pagesize)
        data = await self._call("list_records", args)
        return (data or {}).get("items") or []

    async def get_record(self, adoid: str) -> dict[str, Any]:
        data = await self._call(
            "get_record", {"teamid": TEAMID, "adbid": ADBID, "adoid": adoid}
        )
        return data or {}

    async def search_records(
        self, search: str, parentid: Optional[str] = None
    ) -> list[dict[str, Any]]:
        args: dict[str, Any] = {"teamid": TEAMID, "adbid": ADBID, "search": search}
        if parentid:
            args["parentid"] = parentid
        data = await self._call("search_records", args)
        if isinstance(data, list):
            return data
        if isinstance(data, dict):
            return data.get("items") or data.get("results") or []
        return []

    # ----- write -----
    async def update(self, record: AnyDBRecord) -> dict[str, Any]:
        """Update an existing record. ``record.adoid`` must be set."""
        payload = record.to_update_payload()
        if not payload["content"]:
            raise ValueError("No fields set on the model — nothing to update.")
        return await self._call("update_record", payload) or {}

    async def create(
        self,
        record: AnyDBRecord,
        templatename: str,
        name: str,
        attach: Optional[str] = None,
    ) -> dict[str, Any]:
        """
        Create a new record from a typed model.

        ``templatename`` is resolved to a template ID on first use and cached.
        ``attach`` defaults to the database root (top-level record); pass a
        parent adoid to nest (e.g. attach a Task under a Project).
        """
        if record.adoid:
            raise ValueError("create() requires a model with adoid unset")
        template_id = await self._template_id(templatename)
        args: dict[str, Any] = {
            "teamid": TEAMID,
            "adbid": ADBID,
            "name": name,
            "template": template_id,
            "content": record.to_content_payload(),
        }
        attach_target = attach or ROOTID
        if attach_target:
            args["attach"] = attach_target
        return await self._call("create_record", args) or {}


# ---------- PydanticAI agent ----------

_SYSTEM_PROMPT = """\
You are the AnyDB operations agent for Kaizen Commerce. You read from and write \
to the current Kaizen OS database via typed tools.

Rules:
- Fixed IDs (team, database) are already wired in — never ask for them and \
never try to pass them.
- Before every write, confirm the change in plain English: which record, \
which field, old value -> new value. Call a read tool first if you need to \
check the current value.
- Enum select fields must use the exact string values defined by the Pydantic \
models. Do not invent values. If the user's phrasing is ambiguous, ask.
- Dates: Projects' `actual_go_live`, Tasks'/Subtasks' `due_date`, Phases' \
dates use `YYYY-MM-DD` strings. `target_go_live`, `kickoff_date`, invoice \
dates, deal close dates, contact follow-up dates use Unix seconds (ints).
- For multi-field updates, send one tool call with every changed field — \
don't call `update_*` repeatedly.
- When creating a Deal or Contact for a new merchant, create the Merchant \
first, read back its adoid, then reference it in the Deal/Contact.
"""


class UpdateResult(BaseModel):
    ok: bool = True
    record_id: Optional[str] = None
    fields_updated: list[str] = Field(default_factory=list)
    note: Optional[str] = None


class CreateResult(BaseModel):
    ok: bool = True
    record_id: Optional[str] = None
    templatename: str
    name: str


def build_agent(
    client: AnyDBClient,
    model: str = "anthropic:claude-sonnet-4-5",
) -> Agent[AnyDBClient]:
    """
    Build a PydanticAI Agent wired to the given (already-entered) client.

    The agent exposes read tools (list/get/search) and typed write tools,
    one update + one create per template, so the LLM sees proper schemas
    (with enums) rather than a generic free-form content dict.
    """
    agent: Agent[AnyDBClient] = Agent(
        model,
        deps_type=AnyDBClient,
        system_prompt=_SYSTEM_PROMPT,
    )

    # ---- reads ----
    @agent.tool
    async def list_records(
        ctx: RunContext[AnyDBClient],
        templatename: Optional[str] = None,
        parentid: Optional[str] = None,
        pagesize: Optional[int] = None,
    ) -> list[dict[str, Any]]:
        """List records, optionally filtered by template or parent record."""
        return await ctx.deps.list_records(templatename, parentid, pagesize)

    @agent.tool
    async def get_record(
        ctx: RunContext[AnyDBClient], adoid: str
    ) -> dict[str, Any]:
        """Fetch a single record by its adoid."""
        return await ctx.deps.get_record(adoid)

    @agent.tool
    async def search_records(
        ctx: RunContext[AnyDBClient],
        search: str,
        parentid: Optional[str] = None,
    ) -> list[dict[str, Any]]:
        """Keyword-search records across the database."""
        return await ctx.deps.search_records(search, parentid)

    # ---- updates (one per template, typed) ----
    async def _do_update(
        ctx: RunContext[AnyDBClient], record: AnyDBRecord
    ) -> UpdateResult:
        await ctx.deps.update(record)
        return UpdateResult(
            record_id=record.adoid,
            fields_updated=list(record.to_content_payload().keys()),
        )

    @agent.tool
    async def update_merchant(
        ctx: RunContext[AnyDBClient], record: Merchant
    ) -> UpdateResult:
        """Update fields on an existing Merchant. `record.adoid` required."""
        return await _do_update(ctx, record)

    @agent.tool
    async def update_deal(
        ctx: RunContext[AnyDBClient], record: Deal
    ) -> UpdateResult:
        """Update fields on an existing Deal. `record.adoid` required."""
        return await _do_update(ctx, record)

    @agent.tool
    async def update_contact(
        ctx: RunContext[AnyDBClient], record: Contact
    ) -> UpdateResult:
        """Update fields on an existing Contact. `record.adoid` required."""
        return await _do_update(ctx, record)

    @agent.tool
    async def update_project(
        ctx: RunContext[AnyDBClient], record: Project
    ) -> UpdateResult:
        """Update fields on an existing Project. `record.adoid` required."""
        return await _do_update(ctx, record)

    @agent.tool
    async def update_task(
        ctx: RunContext[AnyDBClient], record: Task
    ) -> UpdateResult:
        """Update fields on an existing Task. `record.adoid` required."""
        return await _do_update(ctx, record)

    # ---- creates (one per template) ----
    async def _do_create(
        ctx: RunContext[AnyDBClient],
        record: AnyDBRecord,
        templatename: str,
        name: str,
        attach: Optional[str],
    ) -> CreateResult:
        res = await ctx.deps.create(record, templatename, name, attach)
        rid = None
        if isinstance(res, dict):
            rid = res.get("adoid") or (res.get("meta") or {}).get("adoid")
        return CreateResult(record_id=rid, templatename=templatename, name=name)

    @agent.tool
    async def create_merchant(
        ctx: RunContext[AnyDBClient], record: Merchant, name: str
    ) -> CreateResult:
        """Create a new Merchant. `name` is the top-level record label."""
        return await _do_create(ctx, record, "Merchants", name, None)

    @agent.tool
    async def create_deal(
        ctx: RunContext[AnyDBClient], record: Deal, name: str
    ) -> CreateResult:
        """Create a new Deal. Link to an existing Merchant via `record.merchant_account`."""
        return await _do_create(ctx, record, "Deals", name, None)

    @agent.tool
    async def create_contact(
        ctx: RunContext[AnyDBClient], record: Contact, name: str
    ) -> CreateResult:
        """Create a new Contact. Link to a Merchant via `record.company`."""
        return await _do_create(ctx, record, "Contacts", name, None)

    @agent.tool
    async def create_project(
        ctx: RunContext[AnyDBClient],
        record: Project,
        name: str,
        attach_merchant_adoid: Optional[str] = None,
    ) -> CreateResult:
        """Create a new Project, optionally attached under a Merchant."""
        return await _do_create(ctx, record, "Projects", name, attach_merchant_adoid)

    @agent.tool
    async def create_task(
        ctx: RunContext[AnyDBClient],
        record: Task,
        name: str,
        attach_project_adoid: Optional[str] = None,
    ) -> CreateResult:
        """Create a new Task, optionally attached under a Project."""
        return await _do_create(ctx, record, "Tasks", name, attach_project_adoid)

    return agent


__all__ = [
    "AnyDBClient",
    "build_agent",
    "UpdateResult",
    "CreateResult",
]
