# Evidence Report Template

## Task Reference
Identify the exact task and execution report that this evidence package supports. The reference should make it easy for a reviewer to connect evidence with the claimed work.

Placeholder:
`[Insert the task ID, task name, and linked execution report or task brief.]`

## Evidence Summary
Summarize what this evidence package is intended to prove or clarify. This section should give a reviewer a quick picture of the evidence scope without turning the summary into approval.

Placeholder:
`[Describe what the evidence is meant to confirm, challenge, or document.]`

## Proof Artifacts
List the concrete artifacts that act as proof, such as diffs, file snapshots, logs, screenshots, or report outputs. Each item should explain why it matters to the task result.

Placeholder:
`[List the proof artifacts and explain what each one demonstrates.]`

## Validation Outputs
Record the outputs of validation steps that actually ran. This section should separate factual outputs from interpretation so reviewers can examine both.

Placeholder:
`[Summarize the results of checks, reviews, or validations that produced output.]`

## Commands / Logs
Record commands and logs that support the evidence trail. Include enough explanation that a reviewer understands what each command or log contributes.

Placeholder:
`[List relevant commands or logs and explain their evidentiary value.]`

## Files Verified
List the files that were directly checked as part of evidence review. This section should help a reviewer see exactly which artifacts were inspected and confirmed.

Placeholder:
`[List the files that were inspected and explain what was verified in each file.]`

## NOT_RUN Items
List the checks, commands, or validations that did not run. This section must remain explicit so a missing check is never mistaken for a passing check.

Placeholder:
`[List every important NOT_RUN item and explain why it did not run.]`

## UNKNOWN Items
Record any evidence questions that remain unknown. UNKNOWN items should stay visible so unresolved uncertainty is not silently converted into a clean result.

Placeholder:
`[List unresolved or unverifiable items that still affect evidence confidence.]`

## Evidence Gaps
Describe where evidence is incomplete, missing, or weaker than desired. Evidence gaps help reviewers judge confidence and decide whether further work or human review is needed.

Placeholder:
`[Explain what proof is missing or incomplete and why that matters.]`

## Blockers
List anything that prevented complete evidence collection or validation. A blocker should show what exact missing artifact, access, or authorization stopped further confirmation.

Placeholder:
`[List the issues that prevented more complete evidence gathering.]`

## PASS / FAIL / WARNING Claims
Summarize the status claims supported by the evidence and explain their limits. This section should be factual and bounded, never using PASS or WARNING as a substitute for approval.

Placeholder:
`[State the supported PASS, FAIL, or WARNING claims and explain the boundary of each claim.]`

## Forbidden Claims
State what this evidence report must not claim. Evidence can support a human decision, but it must not pretend to be that decision.

Required reminders:
- Evidence ≠ approval.
- CI PASS ≠ approval.
- NOT_RUN ≠ PASS.
- UNKNOWN ≠ OK.

## Non-Approval Boundary
State clearly that this template is an evidence container only. The template itself does not authorize approval, lifecycle mutation, runtime, validator, Governance / Control Module, Code Assembly Pipeline, merge, or release.

Required invariants:
- PASS ≠ approval.
- Evidence ≠ approval.
- CI PASS ≠ approval.
- UNKNOWN ≠ OK.
- NOT_RUN ≠ PASS.
- Human approval cannot be simulated.
- Human Risk Profile assignment cannot be simulated.
- Template ≠ runtime.
- Template ≠ validator.
- Template ≠ Governance / Control Module.
- Template ≠ Code Assembly Pipeline.
