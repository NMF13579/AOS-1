# Execution Report Template

## Task Reference
Identify the exact task, task brief, or build-step item this report refers to. The reference should be precise enough that a reviewer can match claims in this report to the original task boundary.

Placeholder:
`[Insert the task ID, task name, and any linked task brief or report path.]`

## Claimed Work Performed
Describe the work the agent claims to have completed. This section is for reported actions and outcomes, not for approval language or evidence conclusions by itself.

Placeholder:
`[Summarize the specific work claimed to be performed within the allowed scope.]`

## Files Created
List the files the agent claims to have created during the task. Include only files inside the authorized scope and describe why each file belongs in the result.

Placeholder:
`[List each created file and explain its role in the task outcome.]`

## Files Modified
List the files the agent claims to have modified during the task. Each entry should explain what changed at a high level and why the change stayed within scope.

Placeholder:
`[List each modified file and explain the purpose of the change.]`

## Files Not Touched
List the critical files or directories that were intentionally left unchanged. This helps later reviewers confirm that protected or deferred areas were respected.

Placeholder:
`[List important files or directories that remained untouched and explain why.]`

## Commands Run
Record the commands the agent actually ran, if any. Include enough context that a reviewer can understand why each command was used without treating command execution as approval.

Placeholder:
`[List the commands that were run and explain what each command checked or changed.]`

## Commands Not Run
List commands, checks, or tools that were intentionally not used. This section helps separate performed work from omitted work so a clean boundary remains visible.

Placeholder:
`[List important commands or checks that were not run and explain why.]`

## Validation Performed
Describe the validations that were performed after the claimed work. Validation here means checks or review steps, not approval or automatic acceptance.

Placeholder:
`[Describe what was checked after the work and what those checks were meant to verify.]`

## Validation Not Run
List validations that were expected but not run, or that were intentionally skipped. This section must remain explicit so NOT_RUN items are not misread as PASS.

Placeholder:
`[List any validation steps that did not run and explain the reason.]`

## Unknowns
Record any unknowns that remained after the claimed work. Unknowns should stay explicit so the report does not imply clean certainty where uncertainty remains.

Placeholder:
`[List unresolved facts, ambiguous results, or unanswered questions remaining after the work.]`

## Blockers
Describe any blocker that prevented full execution or clean completion. A blocker should show what stopped progress and what would be needed to continue safely.

Placeholder:
`[List the exact blockers that limited completion or verification.]`

## Deviations
Document any deviation from the original task brief or plan, even if the deviation was minor. This helps a reviewer see where execution differed from expectation and decide whether follow-up is needed.

Placeholder:
`[Describe any differences between the planned task and the work actually performed.]`

## Evidence References
Point to the supporting evidence that can confirm or challenge the claims in this report. This section should help the reader find proof artifacts without treating the report itself as proof.

Placeholder:
`[Reference the related evidence report, logs, diffs, or verification artifacts.]`

## Forbidden Claims
State what this report must not claim. The report may summarize actions, but it must not present itself as approval, final proof, or a simulated human decision.

Required reminders:
- Execution Report records agent claims.
- Execution Report is not Evidence by itself.
- Execution Report is not approval.

## Non-Approval Boundary
State the boundary clearly: this template records execution claims only. The template itself does not authorize approval, lifecycle mutation, runtime, validator, Governance / Control Module, Code Assembly Pipeline, merge, or release.

Required invariants:
- PASS ≠ approval.
- Evidence ≠ approval.
- CI PASS ≠ approval.
- NOT_RUN ≠ PASS.
- Template ≠ runtime.
- Template ≠ validator.
- Template ≠ Governance / Control Module.
- Template ≠ Code Assembly Pipeline.
- Template ≠ approval.
- Template ≠ lifecycle mutation.
