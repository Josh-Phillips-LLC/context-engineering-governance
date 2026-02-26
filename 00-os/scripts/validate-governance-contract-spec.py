#!/usr/bin/env python3

import json
import re
import sys
from pathlib import Path

CONTRACT_PATH = Path("contracts/governance-implementation-contract.json")
VERSION_RE = re.compile(r"^\d+\.\d+\.\d+$")

REQUIRED_TOP_LEVEL = [
    "contract_id",
    "version",
    "status",
    "authority",
    "compatibility",
    "governance_authoritative_paths",
    "implementation_consumes",
    "change_rules",
    "references",
]


def fail(message: str) -> int:
    print(f"Contract validation failed: {message}", file=sys.stderr)
    return 1


def main() -> int:
    if not CONTRACT_PATH.exists():
        return fail(f"missing contract file: {CONTRACT_PATH}")

    try:
        document = json.loads(CONTRACT_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return fail(f"invalid JSON in {CONTRACT_PATH}: {exc}")

    for key in REQUIRED_TOP_LEVEL:
        if key not in document:
            return fail(f"missing required key '{key}'")

    version = document.get("version", "")
    if not isinstance(version, str) or VERSION_RE.fullmatch(version) is None:
        return fail("'version' must be semantic version format X.Y.Z")

    authority = document.get("authority", {})
    if not isinstance(authority, dict):
        return fail("'authority' must be an object")

    for key in ("governance_repo", "implementation_repo"):
        if key not in authority or not isinstance(authority[key], str) or not authority[key]:
            return fail(f"'authority.{key}' must be a non-empty string")

    compatibility = document.get("compatibility", {})
    if not isinstance(compatibility, dict):
        return fail("'compatibility' must be an object")

    if compatibility.get("semver") is not True:
        return fail("'compatibility.semver' must be true")

    supported_major = compatibility.get("supported_major_for_current_impl")
    if not isinstance(supported_major, int) or supported_major < 0:
        return fail("'compatibility.supported_major_for_current_impl' must be a non-negative integer")

    for list_key in ("governance_authoritative_paths", "implementation_consumes"):
        value = document.get(list_key)
        if not isinstance(value, list) or not value:
            return fail(f"'{list_key}' must be a non-empty array")
        if not all(isinstance(item, str) and item for item in value):
            return fail(f"'{list_key}' must contain non-empty strings")

    print("Governance contract spec validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
