# Task Brief Template

## Task ID / Name
Use this section for the exact task identifier and human-readable task name. The identifier should match the reporting chain so execution and evidence artifacts can refer back to the same task without confusion.

Placeholder:
`[Insert the exact task ID and task name for the scoped work.]`

## Mode
Describe the operating mode for the task, such as report-only, template creation, review, or implementation. The mode should tell both a human and an agent what kind of work is allowed and what kind is forbidden.

Placeholder:
`[State the execution mode and explain what that mode allows.]`

## Repository
Identify the repository or workspace where the task may operate. This section should make the physical work area explicit so write boundaries can be checked later.

Placeholder:
`[Name the repository and describe any repository-specific boundary that matters.]`

## Branch
Record the required branch and any branch-scope limitation. This helps ensure the task does not drift to an unauthorized branch or treat branch eligibility as approval.

Placeholder:
`[State the required branch and explain any restrictions on branch use.]`

## Context
Summarize the upstream reports, approvals, or conditions that make the task relevant. This section should give enough orientation that the task can be understood without re-reading the whole history.

Placeholder:
`[Explain the upstream status, prior reports, and important conditions for this task.]`

## Goal
State the concrete outcome the task is expected to produce. The goal should be specific enough that a reviewer can tell whether the task stayed in scope.

Placeholder:
`[Describe the exact outcome the task must achieve.]`

## Scope
Define what work is included in the task and what boundaries keep the task narrow. Scope should reduce ambiguity and prevent accidental expansion into adjacent work.

Placeholder:
`[Describe the exact work area and what kinds of changes are inside scope.]`

## Allowed Write Paths
List the exact files or directories that the task is allowed to create or edit. This section should be precise enough for later evidence review to check compliance.

Placeholder:
`[List the permitted file paths and explain why each is allowed.]`

## Forbidden Write Paths
List the files, directories, or artifact classes that must not be touched. This section should explicitly call out protected areas, deferred files, and out-of-scope work products.

Placeholder:
`[List the paths and artifact categories that remain forbidden.]`

## Required Behavior / Content
Describe the required output quality, mandatory sections, invariants, or behavioral limits for the task. This section should tell the performer what must appear in the result and what semantic boundaries must be preserved.

Placeholder:
`[Explain the required output structure, quality bar, and non-negotiable rules.]`

## Non-Goals
Record what the task is not trying to do. Non-goals prevent the performer from treating helpful adjacent work as authorized work.

Placeholder:
`[List the activities or outcomes that are explicitly outside this task.]`

## Validation
Describe how the task result should be checked after the work is done. Validation may include file review, status checks, or scope checks, but it must not be confused with approval.

Placeholder:
`[Explain what review or verification steps should confirm the task stayed within scope.]`

## Expected Final Report
Name the report or evidence artifact that should summarize the result. This section helps the performer know how completion must be recorded for later review.

Placeholder:
`[State which report should be produced and what it must summarize.]`

## Execution Package Handoff Notes
Acknowledge the relationship to Execution Package without creating or authorizing `execution-package.md`. This section should say what future execution packaging would need, while making clear that the Execution Package remains deferred.

Required note:
- Execution Package is acknowledged as a later handoff artifact.
- Execution Package is deferred here.
- This template does not create or authorize `agentos/pipelines/documentation-assembly/execution-package.md`.

Placeholder:
`[Describe what a future execution package would need to receive from this task.]`

## Unknowns
List unresolved task-level questions that still matter to safe execution. Unknowns should stay visible so a performer does not silently convert them into assumptions.

Placeholder:
`[List open issues, missing clarifications, or unverified conditions affecting this task.]`

## Blockers
Describe the items that prevent safe execution or safe completion reporting. A blocker should be concrete enough that a reviewer can tell what action or decision is missing.

Placeholder:
`[List the exact issues that currently stop the task from proceeding safely.]`

## Forbidden Claims
List claims that the task output must not make. This section should explicitly prevent approval claims, merge claims, release claims, and simulated human decisions.

Required reminders:
- Do not claim approval from task completion.
- Do not claim execution permission from plan acceptance alone.
- Do not claim runtime, validator, governance, or code pipeline behavior from a documentation template.

## Final Rule
State the hard boundaries that always apply. This section should end the document with explicit reminders that a task brief is a control artifact, not an approval artifact.

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
- Template ≠ approval.
- Template ≠ lifecycle mutation.

## Build Step 3 Safety Alignment
This template must preserve the Build Step 3 safety floor exactly as written here. A task brief may define allowed work, but it must not silently widen scope, soften safety rules, or convert delay or uncertainty into readiness.

Required safety reminders:
- `PASS ≠ approval.`
- `Evidence ≠ approval.`
- `CI PASS ≠ approval.`
- `Metrics ≠ approval.`
- `UNKNOWN ≠ OK.`
- `NOT_RUN ≠ PASS.`
- `BLOCKED ≠ PASS.`
- `DEFERRED ≠ PASS.`
- `DEFERRED ≠ approval.`
- `DEFERRED ≠ completion.`
- Human approval cannot be simulated.
- Human Risk Profile assignment cannot be simulated.
- Scope must not expand without explicit human permission.
- Protected/canonical changes require human checkpoint.
- Destructive operations are forbidden by default.
- Skeleton ≠ implementation.
- Template creation or template update is not runtime.
- Template creation or template update is not validator.
- Template creation or template update is not Governance / Control Module implementation.
- Template creation or template update is not Code Assembly Pipeline implementation.
- Template creation or template update is not lifecycle mutation.
