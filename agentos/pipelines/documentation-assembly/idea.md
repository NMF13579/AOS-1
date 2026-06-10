# Idea Template

## Title
Use this heading for the short working name of the idea. The name should let a human or agent quickly distinguish this idea from other proposals without reading the full document.

Placeholder:
`[Insert idea title that identifies the concept or opportunity.]`

## Idea Summary
Summarize the idea in 1-2 short paragraphs. Explain what is being proposed and why it matters at a high level, without turning this section into a full specification.

Placeholder:
`[Describe the core concept, the intended change, and the reason this idea is worth exploring.]`

## Problem / Opportunity
Describe the current problem, gap, or opportunity that makes this idea relevant. Include enough context so a reviewer understands what is unsatisfactory today or what new value could be created.

Placeholder:
`[Explain the pain point, missed opportunity, or operational need that this idea addresses.]`

## Target User
Identify the main user, operator, maintainer, or stakeholder affected by the idea. Clarify who benefits from the change and whose workflow or decision-making will be improved.

Placeholder:
`[Name the primary user or stakeholder and explain how this person or group relates to the idea.]`

## Desired Outcome
State what successful progress would look like if the idea is carried forward. Focus on the intended result, not on implementation details or approval claims.

Placeholder:
`[Describe the observable result that would show the idea solved the intended problem.]`

## Constraints
List the limits that shape the idea. Include scope, safety, repository, branch, time, authority, or dependency constraints that must be respected before later documents are written.

Placeholder:
`[Record the boundaries, exclusions, and required conditions that limit this idea.]`

## Unknowns
Record open questions that are still unresolved. Unknowns must stay visible so later documents do not quietly assume answers that were never verified.

Placeholder:
`[List unclear facts, missing decisions, or assumptions that still need confirmation.]`

## Blockers
List anything that currently prevents safe progression from idea to project brief. A blocker should describe a concrete missing input, missing authorization, or unresolved conflict.

Placeholder:
`[List the exact items that stop this idea from safely moving forward.]`

## Evidence / Source Notes
Capture the sources, reports, conversations, or observations that informed the idea. This section should help a reviewer trace where the idea came from without treating source notes as approval.

Placeholder:
`[Reference supporting files, reports, human messages, or repository observations relevant to this idea.]`

## Handoff to Project Brief
Explain what the next document, the Project Brief, should carry forward from this idea. This handoff should identify the problem framing, intended user, and key constraints that must remain visible.

Placeholder:
`[Summarize what must be transferred into the Project Brief without changing scope or inventing approval.]`

## Forbidden Claims
List claims that must not be made from this template alone. This protects later work from treating an early idea as if it were already approved, complete, or ready for execution.

Required reminders:
- Do not claim this idea is approved.
- Do not claim this idea is ready for execution by itself.
- Do not claim this idea creates runtime, validator, governance, or code implementation authority.

## Non-Approval Boundary
State the boundary clearly: this template captures an idea only. The template itself does not authorize execution, approval, lifecycle mutation, runtime, validator, Governance / Control Module, Code Assembly Pipeline, merge, or release.

Required invariants:
- PASS ≠ approval.
- Evidence ≠ approval.
- Template ≠ runtime.
- Template ≠ validator.
- Template ≠ Governance / Control Module.
- Template ≠ Code Assembly Pipeline.
- Template ≠ approval.
- Template ≠ lifecycle mutation.

## Build Step 3 Safety Alignment
This template must preserve the Build Step 3 safety floor exactly as written here. The idea record may describe an opportunity, but it must not quietly turn uncertainty, delay, or partial review into success or approval.

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
