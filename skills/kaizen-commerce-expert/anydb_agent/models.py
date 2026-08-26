"""
Pydantic v2 write-safety models for AnyDB Kaizen Commerce.

Scope (Phase 1): highest-impact editable templates for daily ops + LangExtract
Workflow 3 (deal_brief.json -> AnyDB): Merchants, Deals, Contacts, Projects, Tasks.

Source of truth: skills/anydb-kaizen/SKILL.md. Field codes, types, and enum
values below are copied verbatim from that file. Do not edit without checking
SKILL.md first — AnyDB will silently accept unknown field codes but the value
won't show up in the UI, and wrong enum strings will reject the update.

Usage:
    p = Project(adoid="69ab1f7c6c0b7ee2f0755807",
                status=ProjectStatus.IN_PROGRESS,
                actual_go_live="2026-04-15")
    payload = p.to_update_payload()   # ready for update_record
"""
from __future__ import annotations

import os
import re
from datetime import date
from enum import Enum
from typing import Any, ClassVar, Optional

from pydantic import BaseModel, Field, field_validator


# ---------- Fixed IDs ----------
#
# Defaults come from the current Kaizen OS URL:
# https://app.anydb.com/69a206b4a3eaf1244c2a1831/6a04b2e1bf8f55f1cb0b73ea
#
# ROOTID is intentionally optional. AnyDB's create_record tool accepts `attach`
# as optional, so top-level creates should omit it unless a verified parent/root
# record is configured.
TEAMID = os.environ.get("KAIZEN_ANYDB_TEAMID", "69a206b4a3eaf1244c2a1831")
ADBID = os.environ.get("KAIZEN_ANYDB_ADBID", "6a04b2e1bf8f55f1cb0b73ea")
ROOTID = os.environ.get("KAIZEN_ANYDB_ROOTID", "")


# ---------- Value shapes ----------
class RefValue(BaseModel):
    """AnyDB reference field value — points at another record by adoid."""
    adoid: str


class UserRef(BaseModel):
    """AnyDB user field value."""
    userid: str



# ---------- Enums (select fields) ----------
class ProjectStatus(str, Enum):
    SCOPING = "🔵 Scoping"
    IN_PROGRESS = "🟡 In Progress"
    BLOCKED = "🟠 Blocked"
    COMPLETE = "🟢 Complete"
    ARCHIVED = "⚫ Archived"


class ProjectPackageTier(str, Enum):
    SILVER = "Silver"
    GOLD = "Gold"
    DIAMOND = "Diamond"
    CUSTOM = "Custom"


class ProjectType(str, Enum):
    POS_MIGRATION = "POS Migration"
    ANYDB_BACKOFFICE = "AnyDB Back-Office"
    B2B_SHOPIFY = "B2B Shopify Setup"
    RETAINER_SUPPORT = "Retainer Support"


class ServiceLine(str, Enum):
    DATA_MIGRATION = "Data migration"
    IMPLEMENTATION = "Implementation"
    TRAINING = "Training"
    CUSTOM_APP = "Custom App"
    CUSTOM_WEBSITE = "Custom website"
    SYSTEM_INTEGRATION = "System integration"


class TaskStatus(str, Enum):
    BACKLOG = "📥 Backlog"
    IN_PROGRESS = "🔄 In Progress"
    BLOCKED = "🚫 Blocked"
    DONE = "✅ Done"


class TaskPriority(str, Enum):
    CRITICAL = "🔴 Critical"
    HIGH = "🟠 High"
    NORMAL = "🟡 Normal"
    LOW = "🟢 Low"


class TaskPhase(str, Enum):
    BLUEPRINT = "Blueprint"
    DATA_EXTRACTION = "Data Extraction"
    DATA_MAPPING = "Data Mapping"
    SANITIZATION = "Sanitization"
    SHOPIFY_CONFIG = "Shopify Config"
    HARDWARE = "Hardware"
    TESTING = "Testing"
    TRAINING = "Training"
    GO_LIVE = "Go-Live"
    POST_LIVE_SUPPORT = "Post-Live Support"


class DealSalesStage(str, Enum):
    DISCOVERY = "🔍 Discovery"
    BLUEPRINT_SCOPING = "📋 Blueprint Scoping"
    PROPOSAL_SENT = "📄 Proposal Sent"
    NEGOTIATION = "🤝 Negotiation"
    CLOSED_WON = "✅ Closed Won"
    CLOSED_LOST = "❌ Closed Lost"


class DealType(str, Enum):
    NEW_CLIENT = "New Client"
    EXPANSION = "Expansion (add locations)"
    RETAINER_RENEWAL = "Retainer Renewal"
    CUSTOM_BUILD = "Custom Build"


class DealPackageTier(str, Enum):
    SILVER = "Silver ($5k+)"
    GOLD = "Gold ($10k+)"
    DIAMOND = "Diamond ($35k+)"
    CUSTOM = "Custom"


class DealLostReason(str, Enum):
    PRICE = "Price"
    COMPETITOR = "Competitor"
    NO_BUDGET = "No Budget"
    NO_DECISION = "No Decision"
    BAD_FIT = "Bad Fit"


class MerchantLegacyPOS(str, Enum):
    LIGHTSPEED = "Lightspeed"
    SQUARE = "Square"
    HEARTLAND = "Heartland"
    SHOPIFY_UPGRADE = "Shopify (upgrade)"
    VEND = "Vend"
    OTHER = "Other"


class MerchantClientStatus(str, Enum):
    PROSPECT = "🟡 Prospect"
    BLUEPRINT = "🔵 Blueprint"
    ACTIVE = "🟢 Active Client"
    PAST = "⚫ Past Client"
    LOST = "🔴 Lost"


class MerchantIndustry(str, Enum):
    RETAIL = "Retail"
    FASHION = "Fashion"
    FOOD_BEVERAGE = "Food & Beverage"
    HOME_GOODS = "Home Goods"
    HEALTH_BEAUTY = "Health & Beauty"
    SPORTING_GOODS = "Sporting Goods"
    OTHER = "Other"


class ContactRole(str, Enum):
    DECISION_MAKER = "Decision Maker"
    IT_TECHNICAL = "IT/Technical"
    FINANCE = "Finance"
    OPERATIONS = "Operations"
    STAFF_TRAINER = "Staff Trainer"
    OTHER = "Other"


# ---------- Shared validators ----------
_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def _check_date_str(v: Optional[str]) -> Optional[str]:
    if v is None:
        return v
    if not _DATE_RE.match(v):
        raise ValueError(f"expected 'YYYY-MM-DD', got {v!r}")
    date.fromisoformat(v)  # rejects 2026-13-40 etc.
    return v


def _check_unix_seconds(v: Optional[int]) -> Optional[int]:
    if v is None:
        return v
    if not isinstance(v, int):
        raise ValueError(f"timestamp must be int seconds, got {type(v).__name__}")
    if v < 0:
        raise ValueError(f"timestamp cannot be negative: {v}")
    if v > 10_000_000_000:
        raise ValueError(
            f"timestamp {v} looks like milliseconds — AnyDB expects seconds"
        )
    return v


# ---------- Base record ----------
def _unwrap(val: Any) -> Any:
    """Serialize enums / sub-models / lists to JSON-safe primitives."""
    if isinstance(val, Enum):
        return val.value
    if isinstance(val, BaseModel):
        return val.model_dump(exclude_none=True)
    if isinstance(val, list):
        return [_unwrap(v) for v in val]
    return val


class AnyDBRecord(BaseModel):
    """
    Base for writable AnyDB templates.

    Subclasses declare optional attributes for each editable field and a
    class-level ``_field_map`` mapping attribute name -> (pos_code, human_key).
    """

    # attribute name -> (AnyDB pos code, human-readable "key" string)
    _field_map: ClassVar[dict[str, tuple[str, str]]] = {}

    adoid: Optional[str] = Field(
        default=None,
        description="Record ID. Required for update; omitted for create.",
    )

    def to_content_payload(self) -> dict[str, dict[str, Any]]:
        """Build the AnyDB `content` dict from non-None editable fields."""
        out: dict[str, dict[str, Any]] = {}
        for attr, (pos, key) in self._field_map.items():
            val = getattr(self, attr, None)
            if val is None:
                continue
            out[pos] = {"pos": pos, "key": key, "value": _unwrap(val)}
        return out

    def to_update_payload(self) -> dict[str, Any]:
        """Full update_record payload. Requires adoid."""
        if not self.adoid:
            raise ValueError("adoid is required to build an update payload")
        return {
            "meta": {"adoid": self.adoid, "adbid": ADBID, "teamid": TEAMID},
            "content": self.to_content_payload(),
        }

    # create_record is built in the agent layer: the MCP tool needs a flat
    # `{adbid, teamid, name, template(ID), attach?, content}` payload, and
    # resolving a template *name* to its MongoDB ID requires a live session.
    # Use `to_content_payload()` here and let the agent assemble the rest.


# ---------- Merchants ----------
class Merchant(AnyDBRecord):
    """Merchants template — client master records."""

    company_name: Optional[str] = None
    legacy_pos: Optional[MerchantLegacyPOS] = None
    notes: Optional[str] = None  # rich text / HTML
    client_status: Optional[MerchantClientStatus] = None
    total_revenue: Optional[float] = None  # CAD
    industry: Optional[MerchantIndustry] = None
    account_owner: Optional[UserRef] = None
    shopify_store_url: Optional[str] = None
    website: Optional[str] = None
    num_locations: Optional[int] = None

    _field_map: ClassVar[dict[str, tuple[str, str]]] = {
        "company_name":      ("A3", "Company Name"),
        "legacy_pos":        ("A4", "Legacy POS System"),
        "notes":             ("A5", "Notes"),
        "client_status":     ("B4", "Client Status"),
        "total_revenue":     ("B9", "Total Revenue"),
        "industry":          ("C3", "Industry"),
        "account_owner":     ("C4", "Account Owner"),
        "shopify_store_url": ("D3", "Shopify Store URL"),
        "website":           ("D4", "Website"),
        "num_locations":     ("E3", "# of Locations"),
    }


# ---------- Deals ----------
class Deal(AnyDBRecord):
    """Deals template — sales pipeline."""

    deal_name: Optional[str] = None
    sales_stage: Optional[DealSalesStage] = None
    deal_type: Optional[DealType] = None
    package_tier: Optional[DealPackageTier] = None
    blueprint_booked: Optional[bool] = None
    service_lines: Optional[list[ServiceLine]] = None  # multi-select
    merchant_account: Optional[RefValue] = None
    deal_value: Optional[float] = None  # CAD
    lost_reason: Optional[DealLostReason] = None
    primary_contact: Optional[RefValue] = None
    close_probability: Optional[float] = None  # 0.0–1.0
    owner: Optional[UserRef] = None
    expected_close_date: Optional[int] = None  # unix seconds

    _field_map: ClassVar[dict[str, tuple[str, str]]] = {
        "deal_name":           ("A2", "Deal Name"),
        "sales_stage":         ("A3", "Sales Stage"),
        "deal_type":           ("A4", "Deal Type"),
        "package_tier":        ("B3", "Package Tier"),
        "blueprint_booked":    ("B4", "Blueprint Booked"),
        "service_lines":       ("B5", "Service Line(s)"),
        "merchant_account":    ("C2", "Merchant Account"),
        "deal_value":          ("C3", "Deal Value"),
        "lost_reason":         ("C4", "Lost Reason"),
        "primary_contact":     ("D2", "Primary Contact"),
        "close_probability":   ("D3", "Close Probability %"),
        "owner":               ("E2", "Owner"),
        "expected_close_date": ("E3", "Expected Close Date"),
    }

    @field_validator("expected_close_date")
    @classmethod
    def _v_unix(cls, v):
        return _check_unix_seconds(v)

    @field_validator("close_probability")
    @classmethod
    def _v_prob(cls, v):
        if v is None:
            return v
        if not 0.0 <= v <= 1.0:
            raise ValueError(f"close_probability must be 0.0–1.0, got {v}")
        return v


# ---------- Contacts ----------
class Contact(AnyDBRecord):
    """Contacts template — people at merchants."""

    full_name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    company: Optional[RefValue] = None
    job_title: Optional[str] = None
    primary_contact: Optional[bool] = None
    linkedin: Optional[str] = None
    role: Optional[ContactRole] = None
    assigned_to: Optional[UserRef] = None
    follow_up_date: Optional[int] = None  # unix seconds
    notes: Optional[str] = None  # rich text

    _field_map: ClassVar[dict[str, tuple[str, str]]] = {
        "full_name":       ("B2", "Full Name"),
        "email":           ("A3", "Email"),
        "phone":           ("B3", "Phone"),
        "company":         ("C2", "Company"),
        "job_title":       ("D2", "Job Title"),
        "primary_contact": ("D3", "Primary Contact"),
        "linkedin":        ("C3", "LinkedIn"),
        "role":            ("E2", "Role"),
        "assigned_to":     ("A4", "Assigned To"),
        "follow_up_date":  ("E3", "Follow-Up Date"),
        "notes":           ("A5", "Notes"),
    }

    @field_validator("follow_up_date")
    @classmethod
    def _v_unix(cls, v):
        return _check_unix_seconds(v)


# ---------- Projects ----------
class Project(AnyDBRecord):
    """Projects template — active client delivery."""

    project_name: Optional[str] = None
    status: Optional[ProjectStatus] = None
    target_go_live: Optional[int] = None  # unix seconds
    package_tier: Optional[ProjectPackageTier] = None
    actual_go_live: Optional[str] = None  # YYYY-MM-DD
    open_blockers: Optional[str] = None
    project_manager: Optional[UserRef] = None
    waiting_on_merchant: Optional[str] = None
    migration_specialist: Optional[UserRef] = None
    num_locations: Optional[int] = None
    project_type: Optional[ProjectType] = None
    kickoff_date: Optional[int] = None  # unix seconds
    service_line_primary: Optional[ServiceLine] = None

    _field_map: ClassVar[dict[str, tuple[str, str]]] = {
        "project_name":         ("A3",  "Project Name"),
        "status":               ("A4",  "Status"),
        "target_go_live":       ("A5",  "Target Go-Live Date"),
        "package_tier":         ("B4",  "Package Tier"),
        "actual_go_live":       ("B5",  "Actual Go-Live Date"),
        "open_blockers":        ("B19", "Open Blockers"),
        "project_manager":      ("C4",  "Project Manager"),
        "waiting_on_merchant":  ("C19", "Waiting On Merchant"),
        "migration_specialist": ("D4",  "Migration Specialist"),
        "num_locations":        ("D5",  "# of Locations"),
        "project_type":         ("E3",  "Project Type"),
        "kickoff_date":         ("E4",  "Kickoff Date"),
        "service_line_primary": ("F3",  "Service Line Primary"),
    }

    @field_validator("actual_go_live")
    @classmethod
    def _v_date_str(cls, v):
        return _check_date_str(v)

    @field_validator("target_go_live", "kickoff_date")
    @classmethod
    def _v_unix(cls, v):
        return _check_unix_seconds(v)


# ---------- Tasks ----------
class Task(AnyDBRecord):
    """Tasks template — work items under Projects/Phases."""

    task_name: Optional[str] = None
    priority: Optional[TaskPriority] = None
    blocker_notes: Optional[str] = None  # rich text
    assigned_to: Optional[UserRef] = None
    project: Optional[RefValue] = None
    due_date: Optional[str] = None  # YYYY-MM-DD
    phase: Optional[TaskPhase] = None
    depends_on: Optional[RefValue] = None
    status: Optional[TaskStatus] = None
    client_visible: Optional[bool] = None

    _field_map: ClassVar[dict[str, tuple[str, str]]] = {
        "task_name":      ("A2", "Task Name"),
        "priority":       ("A3", "Priority"),
        "blocker_notes":  ("A5", "Blocker Notes"),
        "assigned_to":    ("B3", "Assigned To"),
        "project":        ("C2", "Project"),
        "due_date":       ("C3", "Due Date"),
        "phase":          ("D2", "Phase"),
        "depends_on":     ("D3", "Depends On"),
        "status":         ("E2", "Status"),
        "client_visible": ("E3", "Client Visible"),
    }

    @field_validator("due_date")
    @classmethod
    def _v_date_str(cls, v):
        return _check_date_str(v)


__all__ = [
    "TEAMID", "ADBID", "ROOTID",
    "RefValue", "UserRef",
    "AnyDBRecord",
    "Merchant", "Deal", "Contact", "Project", "Task",
    "ProjectStatus", "ProjectPackageTier", "ProjectType", "ServiceLine",
    "TaskStatus", "TaskPriority", "TaskPhase",
    "DealSalesStage", "DealType", "DealPackageTier", "DealLostReason",
    "MerchantLegacyPOS", "MerchantClientStatus", "MerchantIndustry",
    "ContactRole",
]
