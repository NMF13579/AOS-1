# Human Review Template

## Document Control
- Document status: `DRAFT`
- Review purpose: capture a human decision after reviewing scoped artifacts
- Non-approval reminder: this template is empty until a human fills it

## Reviewer Identity
Record who performed the review.

Guidance:
- Use the human reviewer's identity or trusted reference.
- Do not let the agent fill this as a human fact.

## Reviewed Artifacts
List the exact artifacts reviewed.

Guidance:
- Use exact file or report references.
- Keep the review scope explicit.

## Reviewed Artifact Hashes
List hashes or equivalent integrity markers when available.

Guidance:
- Use exact hashes if the review process requires them.
- If hashes are unavailable, say so instead of inventing them.

## Scope Review
Describe whether the reviewed work stayed within scope.

Guidance:
- Focus on allowed versus forbidden changes.
- Record uncertainty if scope proof is incomplete.

## Behavior Review
Describe whether the result behaves as expected.

Guidance:
- Compare against the task or specification.
- Keep behavior review separate from approval wording.

## Diff Review
Describe what the reviewed changes show.

Guidance:
- Focus on the actual change set.
- Note if diff evidence is missing or partial.

## Validation Review
Describe the status of checks and validations.

Guidance:
- Distinguish passed checks from checks not run.
- Validation is not approval.

## NOT_RUN Review
Describe how `NOT_RUN` items affect the review.

Guidance:
- `NOT_RUN` is not `PASS`.
- Note whether missing checks block decision-making.

## Unknown Review
Describe how unknowns affect the review.

Guidance:
- `UNKNOWN` is not `OK`.
- Record whether unknowns force deferral or changes.

## Evidence Completeness Review
Describe whether the evidence is enough for a human decision.

Guidance:
- Keep this separate from the decision itself.
- Name missing evidence if it matters.

## Protected/Canonical Review
Describe whether protected or canonical boundaries were respected.

Guidance:
- Note whether a checkpoint existed when required.
- Record any path-boundary concern directly.

## Destructive Operation Review
Describe whether destructive actions were attempted or avoided.

Guidance:
- If none occurred, say so.
- Keep this explicit even when the answer is negative.

## Warnings
List warnings the human reviewer wants to carry forward.

Guidance:
- Warnings do not automatically equal rejection.
- Keep warning meaning explicit.

## Requested Changes
List the changes the human wants before approval, if any.

Guidance:
- Use concrete, scoped requests.
- Avoid vague demands that silently expand scope.

## Human Decision
```yaml
human_decision:
  decision:
  reviewer_identity:
  decision_evidence:
  decision_timestamp_or_reference:
  agent_populated_fields: false
```

Guidance:
- Allowed `decision` values: `APPROVED`, `REJECTED`, `CHANGES_REQUESTED`, `HUMAN_REVIEW_REQUIRED`.
- Do not pre-fill any decision value.

## Decision Boundary
State what the human decision does and does not authorize.

Guidance:
- A human decision must remain scoped.
- Approval, rejection, or change request must not be simulated by the agent.
