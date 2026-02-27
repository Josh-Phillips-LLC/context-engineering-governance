# Split Issue Intake and Routing Policy

Effective date: 2026-02-27  
Parent tracking: https://github.com/Josh-Phillips-LLC/context-engineering-governance/issues/1

## Policy

- New change requests must be opened in split repositories, not legacy `Context-Engineering`.
- `Context-Engineering` remains transition-only for migration records and emergency fallback controls.
- Every PR must use a primary tracked issue in the correct split repository.

## Deterministic Routing Criteria

Route by the first matching criterion:

1. **Governance policy/control change** -> `Josh-Phillips-LLC/context-engineering-governance`
   - governance policy (`governance.md`, `context-flow.md`)
   - ADR schema/lifecycle (`00-os/adr/**`)
   - governed repo ownership state/markers (`00-os/governed-repos.yml`, `.context-engineering/governance.yml`)
   - governance review requirements, protected-path rules, metadata policy
2. **Execution/tooling/runtime change** -> `Josh-Phillips-LLC/context-engineering-implementation`
   - templates, generators, sync scripts, workstation/container runtime, implementation workflows
   - role output generation and implementation-side contract consumption
3. **Mixed governance + implementation change**
   - Open a governance parent issue in `context-engineering-governance` for decision/control scope.
   - Open linked implementation child issue(s) in `context-engineering-implementation` for execution.

## Legacy Issue Migration Rule

For open issues in legacy `Context-Engineering`:

1. If work has not started, recreate in the correct split repo and close legacy issue with migration link.
2. If work is already in progress, create a split-repo tracking issue, link both directions, and keep legacy issue open only until active work closes.
3. New PRs must use split-repo issues as the primary tracked issue; legacy issues may be referenced as secondary context only.

## Review Enforcement

- Compliance review must verify routing against this policy.
- If routing is incorrect, reviewer requests changes unless an Executive Sponsor-approved routing exception is documented in the PR.
