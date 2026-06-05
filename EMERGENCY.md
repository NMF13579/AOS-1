# Emergency Recovery

This file is human-readable recovery guidance only.

## Boundary

- EMERGENCY.md is not agent permission.
- EMERGENCY.md cannot authorize deletion.
- EMERGENCY.md cannot authorize approval.
- EMERGENCY.md cannot authorize merge, push, release, or scope expansion.
- EMERGENCY.md cannot authorize protected writes.

## Safe first steps

1. Stop automated execution.
2. Inspect `agentos/agentos.yaml`.
3. Inspect `agentos/architecture/invariants.md`.
4. Inspect latest `agentos/state/` and `agentos/reports/`.
5. Do not delete state, approvals, reports, or audit.
6. Use recovery flow when implemented.
