# Evidence Report Template

## Document Control
- Document status:
- Report purpose: record proof artifacts and evidence quality for one scoped task
- Non-approval reminder: evidence does not equal approval

## Task Reference
Record the exact task this evidence supports.

Guidance:
- Link it to the task brief and execution report.
- Keep references exact.

## Repository Baseline
Record the repository facts the evidence depends on.

Guidance:
- Include baseline commit, branch, and any working tree note relevant to interpretation.
- Make missing facts visible.

## Evidence Inventory
List the exact proof artifacts.

Guidance:
- Use exact references to files, diffs, commands, or outputs.
- Do not describe evidence in vague categories only.

## Changed File List
List the exact changed files.

Guidance:
- Use exact paths.
- If no files changed, say so directly.

## Diff Evidence
Describe the diff evidence available.

Guidance:
- Name where the change proof can be inspected.
- If diff evidence is missing, say so.

## Command Evidence
List command outputs that support the record.

Guidance:
- Keep factual command references separate from interpretation.
- Include enough detail to trace the evidence.

## Checks and Tests Evidence
List evidence from checks and tests that actually ran.

Guidance:
- Keep `NOT_RUN` items out of this section.
- Describe what the evidence shows, not what you hope it shows.

## Exit Codes
Record exit codes for commands and checks.

Guidance:
- Use exact exit codes where available.
- If something did not run, record `NOT_RUN` instead of guessing.

## NOT_RUN Evidence
List important checks or commands that did not run.

Guidance:
- `NOT_RUN` does not count as `PASS`.
- Explain why each item did not run.

## Unknown Evidence
List evidence gaps that remain unknown.

Guidance:
- `UNKNOWN` does not count as `OK`.
- Keep missing proof visible.

## Warnings
List non-blocking evidence concerns.

Guidance:
- Warnings may lower confidence.
- Warnings are not approval blockers unless explicitly stated.

## Blockers
List evidence blockers.

Guidance:
- Name missing artifacts, blocked checks, or unresolved authority issues.
- Keep blocker wording concrete.

## Stop Evidence
Describe the evidence showing why the task stopped where it did.

Guidance:
- Point to the exact source of the stop condition.
- Keep this separate from human decision.

## Rollback Evidence
Describe whether any rollback evidence exists.

Guidance:
- If rollback did not happen, say so directly.
- Do not imply rollback approval.

## Scope Comparison
Compare the evidence against the scoped task.

Guidance:
- Show whether evidence matches allowed changes.
- If scope cannot be proven from evidence, say so.

## Evidence Completeness
```yaml
evidence_completeness:
  status:
  missing_evidence:
  impact:
```

Guidance:
- Allowed `status` values: `COMPLETE`, `INCOMPLETE_BUT_USABLE`, `INSUFFICIENT`.
- `INSUFFICIENT` blocks a positive claim.

## Claim Boundary
State what the evidence can support and what it cannot.

Guidance:
- Evidence may support review.
- Evidence does not create approval.

## Human Review Boundary
State what still requires human review.

Guidance:
- Keep human decision separate from evidence sufficiency.
- Do not pre-fill approval outcomes.
