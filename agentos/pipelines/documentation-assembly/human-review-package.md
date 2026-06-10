# Human Review Package Template

## Review Package Title
Use this section for the clear title of the review package. The title should identify the task or build-step decision being prepared for human review.

Placeholder:
`[Insert the review package title that clearly identifies the decision context.]`

## Task / Build Step Reference
Identify the exact task, build step, and upstream reports that the human is being asked to review. This section should make the review scope explicit before any decision fields appear.

Placeholder:
`[List the task ID, build step, and related report or template references.]`

## Inputs Reviewed
List the inputs the human reviewer is expected to examine. This helps separate the review package from the underlying evidence and keeps the decision context transparent.

Placeholder:
`[List the input reports, templates, evidence items, or files that should be reviewed.]`

## Execution Report Summary
Summarize the relevant claims from the Execution Report in plain language. This section should help the human reviewer understand what the agent says happened without treating the claims as proof by themselves.

Placeholder:
`[Summarize the important claimed work from the execution report.]`

## Evidence Report Summary
Summarize the relevant findings from the Evidence Report. This should help the reviewer understand what proof exists, what did not run, and what remains uncertain.

Placeholder:
`[Summarize the key supporting evidence, evidence gaps, and caution areas.]`

## Human Review Questions
List the specific questions the human reviewer should answer. These questions should focus attention on scope, correctness, safety, sufficiency of evidence, and whether the next step should proceed.

Placeholder:
`[List the concrete questions the human reviewer must answer before making a decision.]`

## Human Decision Fields
Provide the exact fields that a human decision should fill in. This section should make it easy to record explicit approval, rejection, deferral, scope limits, or Risk Profile decisions without ambiguity.

Placeholder:
`[List the decision fields the human must fill and explain what each field means.]`

## Approval Boundary
Describe the difference between review support and actual approval. This section must remind the reader that the package can prepare a decision but cannot create human approval on its own.

Placeholder:
`[Explain what later human action would count as approval and what this package cannot do.]`

## Rejection / Revision Options
List the options the human may choose if the work is not acceptable as-is. This helps the package support correction paths instead of forcing only binary acceptance.

Placeholder:
`[Describe how the human may reject, revise, narrow, or request changes.]`

## Deferred Decision Options
Describe when the human may defer a decision and what additional evidence or clarification might be needed. This section should keep “not ready yet” visible as a valid outcome.

Placeholder:
`[Explain how the human may defer the decision and what follow-up would be needed.]`

## Risk Profile Notes
Record any Risk Profile context the human should consider. This section may highlight the current assigned profile or note that only a human can assign or change it.

Placeholder:
`[Explain the current Risk Profile context and any risk-related decision the human may need to make.]`

## Unknowns
List unresolved questions that the human reviewer should know about before deciding. Unknowns help prevent false certainty during review.

Placeholder:
`[List the unresolved facts or open concerns that still affect the decision.]`

## Blockers
Describe issues that prevent a clean human decision right now. Blockers should point to missing evidence, unresolved scope, or missing required inputs.

Placeholder:
`[List the exact issues that stop the review from being complete or decisive.]`

## Forbidden Claims
State what this package must not claim. A Human Review Package can support a human review, but it must not impersonate a human decision or approval.

Required reminders:
- Human Review Package may support human review.
- Human Review Package is not approval by itself.
- Human approval cannot be simulated.
- Risk Profile assignment cannot be simulated.

## Final Human Decision Record
Provide the place where the final human decision can be copied verbatim once it exists. This section should support accurate recording of the human message without transforming it into an inferred summary.

Placeholder:
`[Insert the final human decision verbatim when it is actually provided.]`
