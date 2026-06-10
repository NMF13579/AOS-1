# Project Brief Template

## Project Name
Use this section for the working project name or initiative label. The name should match the idea being carried forward and remain stable enough for later documents to reference it.

Placeholder:
`[Insert the project name used in downstream specification and task documents.]`

## Source Idea Reference
Point to the Idea document or idea record that this brief is based on. Explain which upstream concept is being formalized so a reviewer can trace the origin of the brief.

Placeholder:
`[Reference the relevant idea document, report, or human decision that this brief expands.]`

## Project Purpose
Explain why the project should exist and what value it is meant to create. This section should capture the business, operational, or product purpose without turning into detailed implementation rules.

Placeholder:
`[Describe the purpose of the project and why it matters now.]`

## User / Stakeholder
Name the primary user, operator, or stakeholder group. Explain whose needs the project serves and whose review may matter later when success is evaluated.

Placeholder:
`[Identify the main user or stakeholder and explain their relationship to the project.]`

## Scope Summary
Describe what the project covers at a high level. Keep the summary bounded so later documents can expand details without widening scope by accident.

Placeholder:
`[State what is in scope and what type of output or improvement is expected.]`

## Non-Goals
Record what this brief explicitly does not attempt to do. Non-goals reduce confusion by showing which adjacent ideas, features, or implementation areas are intentionally excluded.

Placeholder:
`[List what this project brief does not cover or authorize.]`

## Success Criteria
Describe the conditions that would show the project brief has been translated correctly into a later specification or task. These should be measurable or reviewable outcomes, not approval shortcuts.

Placeholder:
`[List the criteria a reviewer would use to say the project direction is adequately defined.]`

## Constraints
List authority, repository, safety, timeline, dependency, and scope limits that must be preserved. This section should help downstream authors stay within permitted boundaries.

Placeholder:
`[Record the limitations that shape the project and must remain visible later.]`

## Unknowns
List material questions that are still unresolved at the brief level. Unknowns should stay explicit rather than being silently converted into assumptions in the specification.

Placeholder:
`[List unclear facts, pending decisions, or open concerns still affecting the project.]`

## Blockers
Describe the items that prevent safe movement from Project Brief to Specification. A blocker should be concrete enough that a reviewer can see what needs to be resolved.

Placeholder:
`[List the exact issues that currently stop the brief from safely progressing.]`

## Evidence / Source Notes
Summarize the reports, human messages, and source materials that support this brief. Evidence notes help with traceability, but they must not be treated as approval by themselves.

Placeholder:
`[List the upstream sources or repository evidence that inform this brief.]`

## Handoff to Specification
Explain what the Specification must inherit from this brief. Carry forward the purpose, scope, success criteria, and constraints without inventing technical authority that does not yet exist.

Placeholder:
`[Summarize what the Specification must preserve and elaborate.]`

## Forbidden Claims
List the claims this document must not make. A Project Brief is not allowed to declare execution, approval, merge permission, or implementation completion.

Required reminders:
- Do not claim the project is approved.
- Do not claim the project is ready for code execution by itself.
- Do not claim the brief authorizes runtime, validator, governance, or pipeline implementation.

## Non-Approval Boundary
State clearly that this template supports project framing only. The template itself does not authorize execution, approval, lifecycle mutation, runtime, validator, Governance / Control Module, Code Assembly Pipeline, merge, or release.

Required invariants:
- PASS ≠ approval.
- Evidence ≠ approval.
- UNKNOWN ≠ OK.
- Template ≠ runtime.
- Template ≠ validator.
- Template ≠ Governance / Control Module.
- Template ≠ Code Assembly Pipeline.
- Template ≠ approval.

## Build Step 3 Safety Alignment
This template must preserve the Build Step 3 safety floor exactly as written here. A project brief may frame work, but it must not silently widen scope or treat postponed, missing, or unverified items as success.

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
