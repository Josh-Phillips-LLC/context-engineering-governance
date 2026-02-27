# Protected Path Policy Map

This document defines protected path ownership and enforcement controls for split Context-Engineering repositories.

## Protected Paths (Executive Sponsor approval required before merge)

### Governance Repository (`context-engineering-governance`)

- `governance.md`
- `context-flow.md`
- `00-os/**`
- `10-templates/review-checklists/**`
- `10-templates/compliance-officer-pr-review-brief.md`
- `10-templates/agent-prompts/compliance-officer-pr-review-checklist.md`
- `contracts/**`

### Implementation Repository (`context-engineering-implementation`)

- `.context-engineering/governance.yml`
- `00-os/**`
- `10-templates/**`
- `.github/workflows/**`
- `contracts/**`
- `CONTRACT_BOUNDARY.md`
- `BOUNDARY_GATES.md`

## Enforcement Baseline

The following controls are required on `main` for both split repositories:

1. CODEOWNERS file present and maintained (`.github/CODEOWNERS`)
2. Required pull request reviews enabled with:
   - at least one approval
   - stale review dismissal
   - code-owner review requirement enabled
3. Required status checks set to strict mode
4. Required conversation resolution enabled

Baseline required status checks:

- `context-engineering-governance`
  - `Validate Governance Boundary Gates`
  - `Validate machine-readable PR metadata`
- `context-engineering-implementation`
  - `Validate Implementation Boundary Gates`

## Break-Glass Override Policy (Emergency Only)

Admin override is permitted only for urgent production/governance continuity incidents when standard controls block critical remediation.

Required audit evidence for every override:

1. PR comment from Executive Sponsor describing emergency reason and risk acceptance
2. Linked remediation issue opened in `context-engineering-governance` within the same change window
3. Post-merge comment documenting:
   - what control was bypassed
   - why bypass was required
   - rollback/containment plan
   - follow-up control-hardening action owner and due date

## Rationale

These paths define policy authority, architecture decision governance, contract boundaries, and deterministic review gates. Unauthorized changes can alter approval boundaries or compliance behavior across all role and implementation systems.
