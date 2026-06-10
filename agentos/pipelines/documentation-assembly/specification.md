# Specification Template

## Specification Title
Use this heading for the formal name of the specification. The title should match the project brief context closely enough that downstream task briefs can cite it without ambiguity.

Placeholder:
`[Insert the specification title that describes the scoped behavior or document package.]`

## Project Brief Reference
Reference the Project Brief that this specification expands. Explain which brief is being translated into requirements so reviewers can follow the document chain.

Placeholder:
`[Link or name the source Project Brief and summarize its relevance.]`

## Functional Requirements
Describe the required behaviors, document outputs, or workflow capabilities that must exist if the specification is followed. Keep each requirement reviewable and framed as expected behavior, not as approval.

Placeholder:
`[List the required functions, outputs, or documented behaviors that the project must support.]`

## Non-Functional Requirements
Describe quality expectations such as clarity, traceability, maintainability, safety wording, or usability of the documents. These requirements should shape how the output is produced, even when they do not define direct behavior.

Placeholder:
`[List the quality, readability, safety, or maintainability requirements that apply.]`

## Safety / Governance Requirements
Record the safety rules, authority boundaries, and non-approval rules that the specification must respect. This is where the specification acknowledges project-control boundaries without turning into an implementation of control logic.

Placeholder:
`[List the safety, risk, review, and authority rules that later work must respect.]`

## Data / Inputs / Outputs
Describe the key inputs this specification relies on and the outputs it is expected to produce. Include document inputs, human decisions, and evidence references where relevant.

Placeholder:
`[Explain what information comes in, what artifacts come out, and how they relate.]`

## Dependencies
List upstream documents, decisions, files, or process checkpoints required before the specification can be used safely. Dependencies should show what must already exist or be confirmed.

Placeholder:
`[Record the required upstream sources, reports, or decisions this specification depends on.]`

## Constraints
List the constraints that narrow how this specification can be fulfilled. Include repository limits, branch rules, forbidden work, and any relevant scope or review boundaries.

Placeholder:
`[Describe the limitations that downstream task briefs or document batches must obey.]`

## Unknowns
Record unresolved questions that still affect the specification. Unknowns must remain visible so downstream tasks do not treat them as settled facts.

Placeholder:
`[List open issues, missing clarifications, or assumptions that still need resolution.]`

## Blockers
Describe anything that prevents safe handoff from Specification to Task Brief. Blockers should point to missing approvals, unresolved scope questions, or unverified dependencies.

Placeholder:
`[List the exact issues that stop the specification from safely moving into task execution planning.]`

## Evidence / Source Notes
Summarize the evidence, canonical sources, and human decisions that support the specification. This section supports traceability and review, but it must not be mistaken for approval.

Placeholder:
`[List the source materials or reports that justify the specification.]`

## Handoff to Task Brief
Explain what the Task Brief must carry forward from this specification. Focus on scope, write boundaries, required behavior, and validation expectations that a task author must preserve.

Placeholder:
`[Summarize the instructions and boundaries the Task Brief must inherit.]`

## Forbidden Claims
List the claims that are forbidden at the specification stage. This template must not imply code approval, merge permission, release readiness, or simulated human authorization.

Required reminders:
- Do not claim the specification is execution approval.
- Do not claim the specification is human approval.
- Do not claim the specification enables lifecycle mutation by itself.

## Non-Approval Boundary
State clearly that this specification is a structured requirements document only. The template itself does not authorize execution, approval, lifecycle mutation, runtime, validator, Governance / Control Module, Code Assembly Pipeline, merge, or release.

Required invariants:
- PASS ≠ approval.
- Evidence ≠ approval.
- CI PASS ≠ approval.
- UNKNOWN ≠ OK.
- Human approval cannot be simulated.
- Human Risk Profile assignment cannot be simulated.
- Template ≠ runtime.
- Template ≠ validator.
- Template ≠ Governance / Control Module.
- Template ≠ Code Assembly Pipeline.

## Build Step 3 Safety Alignment
This template must preserve the Build Step 3 safety floor exactly as written here. A specification may define requirements, but it must not reinterpret safety states as permission, completion, or approval.

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
