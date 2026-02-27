#!/usr/bin/env python3

import fnmatch
import sys
from pathlib import Path

RULES = [
    (
        "BND-GOV-001",
        ".devcontainer-workstation/**",
        "Implementation workstation/runtime assets are not allowed in governance repository.",
        "Move devcontainer/runtime assets to context-engineering-implementation.",
    ),
    (
        "BND-GOV-002",
        ".context-engineering/**",
        "Implementation-owned governance ownership config mirror is not allowed in governance repository.",
        "Keep governance ownership source in governance policy artifacts; remove implementation mirror directories.",
    ),
    (
        "BND-GOV-003",
        "00-os/scripts/generate-role-wiring.py",
        "Role wiring generator implementation is not allowed in governance repository.",
        "Move generator implementation to context-engineering-implementation.",
    ),
    (
        "BND-GOV-004",
        "00-os/scripts/ensure-role-repo-fork-first.sh",
        "Role-repo operational script is not allowed in governance repository.",
        "Move operational script to context-engineering-implementation.",
    ),
    (
        "BND-GOV-005",
        "00-os/scripts/exo-with-az-token.sh",
        "Execution automation script is not allowed in governance repository.",
        "Move execution automation script to context-engineering-implementation.",
    ),
    (
        "BND-GOV-006",
        "10-templates/repo-starters/**",
        "Generator template implementation assets are not allowed in governance repository.",
        "Keep only policy/governance templates here; move starter generators to implementation repo.",
    ),
    (
        "BND-GOV-007",
        ".github/workflows/sync-role-repos.yml",
        "Role sync pipeline workflow is not allowed in governance repository.",
        "Move role sync workflow to context-engineering-implementation.",
    ),
    (
        "BND-GOV-008",
        ".github/workflows/publish-role-workstation-images.yml",
        "Workstation image publishing workflow is not allowed in governance repository.",
        "Move image build/publish workflow to context-engineering-implementation.",
    ),
    (
        "BND-GOV-009",
        ".github/workflows/orchestrate-role-onboarding.yml",
        "Role onboarding orchestration workflow is not allowed in governance repository.",
        "Move onboarding orchestration workflow to context-engineering-implementation.",
    ),
]

ALLOWED_PATHS = {
    ".context-engineering/governance.yml",
}


def list_repo_files() -> list[str]:
    files: list[str] = []
    for path in Path(".").rglob("*"):
        if not path.is_file():
            continue
        relative = path.as_posix()
        if relative.startswith("./"):
            relative = relative[2:]
        if relative.startswith(".git/"):
            continue
        files.append(relative)
    return sorted(files)


def main() -> int:
    files = list_repo_files()
    violations: list[str] = []

    for file_path in files:
        if file_path in ALLOWED_PATHS:
            continue
        for rule_id, pattern, message, remediation in RULES:
            if fnmatch.fnmatch(file_path, pattern):
                violations.append(
                    f"{rule_id} error {file_path} {message} | remediation: {remediation}"
                )

    if violations:
        print("Governance boundary validation failed:", file=sys.stderr)
        for violation in sorted(violations):
            print(f"- {violation}", file=sys.stderr)
        return 1

    print("Governance boundary validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
