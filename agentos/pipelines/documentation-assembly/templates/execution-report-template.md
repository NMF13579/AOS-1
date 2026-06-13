# Execution Report Template

## Document Control
- Document status:
- Report purpose: record what the agent planned, what the agent actually did, and where the work stopped
- Non-approval reminder: this report is not approval

## Task Reference
Record the exact task being reported.

Guidance:
- Include task ID, task name, and relevant task brief reference.
- Keep the reference exact.

## Execution Authority Reflection
Describe the authority the agent relied on.

Guidance:
- Name the human authorization source.
- Separate execution authority from approval.

## Repository Baseline
Record the starting repository facts.

Guidance:
- Include branch, baseline commit, and relevant working tree notes.
- Make unknown baseline facts explicit.

## Planned Actions
List the intended actions before execution.

Guidance:
- Keep planned work separate from performed work.
- Use this section to show original intent.

## Performed Actions
List the actions actually taken.

Guidance:
- Record only what was actually done.
- If an action was skipped, keep it out of this section.

## Changed Paths
List the exact files changed.

Guidance:
- Use exact paths.
- If no files changed, state that directly.

## Commands
Record the commands actually run.

Guidance:
- Each command should include an exit code or `NOT_RUN`.
- If no shell command was used for a step, say so plainly.

## Checks and Tests
List the checks that ran.

Guidance:
- Describe what each check was meant to confirm.
- Do not treat a check result as approval.

## NOT_RUN Register
List expected checks or actions that did not run.

Guidance:
- Keep every important `NOT_RUN` item visible.
- `NOT_RUN` is not `PASS`.

## Unknown Register
List unknowns still affecting the report.

Guidance:
- Keep unknowns explicit.
- `UNKNOWN` is not `OK`.

## Warnings
List non-blocking concerns.

Guidance:
- Keep warnings visible.
- A warning is not a clean pass.

## Blockers
List anything that blocked full completion.

Guidance:
- Explain what blocked progress.
- Name the missing input, approval, or fact when possible.

## Stop Record
Describe why execution stopped.

Guidance:
- Name the exact stopping condition.
- Keep this factual and bounded.

## Scope Compliance
Describe whether the work stayed inside scope.

Guidance:
- Compare performed actions against allowed changes.
- If scope compliance cannot be proven, say so.

## Rollback Status
Describe whether any rollback happened.

Guidance:
- State `not performed` if rollback did not happen.
- Do not imply rollback authority if it was never granted.

## Agent Result Claim
State the agent's result claim.

Guidance:
- This claim is not evidence by itself.
- Keep claim wording narrower than approval wording.

## Downstream Boundary
State what this report does not authorize.

Guidance:
- No approval, merge, release, automatic next-task start, or lifecycle mutation.
