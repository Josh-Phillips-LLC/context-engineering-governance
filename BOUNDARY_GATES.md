# Governance Boundary Gates

These CI gates prevent governance/implementation boundary drift.

## Enforced by CI

Workflow: `.github/workflows/validate-boundary-governance.yml`

Checks:
- Governance repo must not contain implementation runtime/tooling paths.
- Governance contract spec must remain structurally valid.
- Governance ownership artifacts (`00-os/governed-repos.yml` and `.context-engineering/governance.yml`) must validate and reconcile.

## Failure Remediation

If the boundary gate fails:

1. Move execution/runtime artifacts to `context-engineering-implementation`.
2. Keep governance repo scoped to policy authority and contract definitions.
3. Re-run CI and include remediation evidence in PR notes.
