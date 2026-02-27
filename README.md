# Context Engineering Governance

Authoritative governance policy source for Context Engineering.

## Purpose

This repository contains policy, process, and architecture-governance artifacts that define how downstream implementation and role repositories operate.

Normative split direction:

- governance -> implementation -> role repositories

## Initial Bootstrap Scope

This bootstrap includes canonical governance artifacts migrated from `Josh-Phillips-LLC/Context-Engineering` to establish a reviewable governance baseline:

- `governance.md`
- `context-flow.md`
- `00-os/adr/`
- `00-os/role-charters/`
- governance review/checklist templates and PR policy contract artifacts

See `MIGRATION_PROVENANCE.md` for source commit references.

## Boundary Gates

Boundary drift is enforced by CI in:

- `BOUNDARY_GATES.md`
- `.github/workflows/validate-boundary-governance.yml`

## Change Management

- Issue-first workflow
- Split issue intake/routing policy (`00-os/intake-routing.md`)
- PR review required
- Executive Sponsor approval required for protected-path governance changes

See `governance.md` and `00-os/workflow.md` for the authoritative operating model.
