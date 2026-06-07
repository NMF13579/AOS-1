# Agent Autonomy Modes Policy

## 1. Purpose
This policy defines limited temporary development modes to reduce excessive task overhead while building the AgentOS system, while maintaining hard boundaries on critical actions.

## 2. Authority Boundary
Modes define permissible actions. No mode allows bypassing fundamental governance principles, protected core systems, or final stage-transition approvals.

## 3. Mode Summary
The system defines three core autonomy modes:
* `STRICT_GOVERNED_MODE`
* `DEV_SANDBOX_MODE`
* `CONTROLLED_WRITE_MODE`

## 4. STRICT_GOVERNED_MODE
The default mode. Requires explicit boundaries, approvals, and reports for all actions.

## 5. DEV_SANDBOX_MODE
A temporary mode used to accelerate development. DEV_SANDBOX_MODE expands development-time draft/scaffold/test/fixture/report freedom only. It does not expand approval authority, lifecycle authority, protected/canonical write authority, destructive-operation authority, commit authority, merge authority, or stage-transition authority.

## 6. CONTROLLED_WRITE_MODE
Allows scoped writes defined strictly by a prior explicit agreement or approval marker. Scope expansion requires a human checkpoint.

## 7. Default and Unknown Mode Rules
- `STRICT_GOVERNED_MODE` is the default.
- Missing mode means `STRICT_GOVERNED_MODE`.
- Unknown, ambiguous, deprecated, or unsupported mode must fail closed.

## 8. Protected / Canonical File Rule
No mode permits unilateral writes, deletes, or changes to canonical repository structural markers, architecture, or roadmap documents without explicit human approval.

## 9. Destructive Operation Rule
Any destructive operation requires a separate controlled cleanup flow and is forbidden in any standard autonomy mode by default.

## 10. Approval and Lifecycle Boundary
No mode authorizes creating approvals, mutating lifecycle, or executing stage transitions independently.

## 11. Temporary Mode Removal Strategy
`DEV_SANDBOX_MODE` is a temporary scaffold. Once system self-building capabilities reach sufficient maturity, the use of this mode will be restricted or removed through a formal lifecycle update.

## 12. Non-Goals
This policy does not:
* Activate DEV_SANDBOX_MODE.
* Update templates, schemas, validators, or runtime.
* Change roadmap, architecture, or skeleton.
* Grant agent approval authority.
* Authorize broader write access or cleanup.
* Start the next stage.
