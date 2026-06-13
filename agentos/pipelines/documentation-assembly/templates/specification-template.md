# Specification Template

## Document Control
- Document status: `DRAFT`
- Document purpose: translate an approved brief into reviewable expected behavior and validation requirements
- Source of authority: scoped Project Brief plus governing sources
- Non-approval reminder: this specification does not authorize execution or approval

## Source Project Brief
Reference the exact Project Brief this specification expands.

Minimum guidance:
- Name the brief directly.
- Summarize the inherited goal and scope without expanding them.

## Current Behavior
Describe what happens now.

Minimum guidance:
- Separate observed evidence from assumptions.
- If current behavior is unknown, say so explicitly.

## Expected Behavior
Describe what should happen if the specification is followed.

Minimum guidance:
- Keep this tied to the source Project Brief.
- Avoid hidden scope growth.

## Functional Requirements
List the required behaviors or outputs.

Minimum guidance:
- Make each requirement testable or reviewable.
- Use clear statements that a reviewer can confirm.

## Non-Functional Constraints
List quality and boundary requirements.

Minimum guidance:
- Include clarity, traceability, safety wording, maintainability, or process constraints when relevant.
- Keep this separate from functional behavior.

## Inputs
List the inputs the specification expects.

Minimum guidance:
- Name exact upstream documents, human decisions, or facts.
- Mark missing inputs as unknown instead of inventing replacements.

## Outputs
List the outputs the specification expects.

Minimum guidance:
- Name the exact artifacts or results.
- Keep outputs consistent with the source brief.

## Edge Cases
List special or uncomfortable cases the design must still handle.

Minimum guidance:
- Include missing data, partial evidence, conflicting signals, or blocked states when relevant.
- Do not pretend edge cases are solved if they are not.

## Failure Behavior
Describe how the flow must fail safely.

Minimum guidance:
- Use fail-closed semantics.
- Keep `UNKNOWN`, `NOT_RUN`, and `BLOCKED` visible where applicable.

## Acceptance Criteria
List the reviewable conditions for saying the specification is complete enough for task writing.

Minimum guidance:
- Acceptance criteria are not approval.
- Keep them specific and bounded.

## Validation Requirements
Describe how the specification should be checked.

Minimum guidance:
- Name the checks, reviews, or comparisons expected later.
- Do not treat missing validation as pass.

## Evidence Requirements
Describe what proof must exist later.

Minimum guidance:
- Name the kinds of evidence required.
- Keep evidence separate from approval.

## Unknowns
List unresolved items still affecting the specification.

Minimum guidance:
- Preserve unknowns as unknowns.
- Do not hide gaps behind optimistic wording.

## Human Review Boundary
State what still requires human review.

Minimum guidance:
- Note any approval, scope, or risk decisions that remain human-only.
- Confirm that this specification does not authorize execution.
