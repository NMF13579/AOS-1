# Governance Rules

```yaml
rule_id: GOV-001
rule_text: >
  BLOCKED status cannot be converted to PASS or COMPLETE
  through human decision alone.
  A separate explicit result
  COMPLETE_WITH_ACCEPTED_HISTORICAL_DEVIATIONS
  must be used, with documented rationale
  for each individual deviation.
applies_to: all future Build Steps
does_not_apply_retroactively: true
does_not_rewrite_existing_history: true
source_checkpoint: reports/human-checkpoints/governance-rule-001-checkpoint.md
authorized_by: project_owner
date: 2026-06-13
```
