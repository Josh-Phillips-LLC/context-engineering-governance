# Governance Registries and Validators

## Overview

This directory contains:
- **governed-repos.yml**: Canonical source of truth for repository governance state
- **protected-path-policy-map.md**: Canonical protected governance path definitions
- **scripts/**: Governance validation scripts (ADR, PR metadata, boundary, and ownership)

## Purpose

- Maintains canonical governance ownership declarations and adoption state.
- Enforces deterministic validation of governance artifacts in CI.

## Usage

After modifying governance ownership files:

```bash
# Validate governance ownership artifacts
python3 00-os/scripts/validate-governance-ownership.py
```

This validates:
- `00-os/governed-repos.yml`
- `.context-engineering/governance.yml`

## Registry Schema

See `governed-repos.yml` for repository governance ownership state.

## Related Artifacts

- Local marker schema: `.context-engineering/governance.yml`
- Governance policy section: `governance.md#repository-governance-adoption-model-ownership-states`
