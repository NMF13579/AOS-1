# Task 2.8.3.1 — CAP-002 Commit Authorization Correction

## 1. Task Metadata

- task_id: `2.8.3.1`
- mode: `correction / human commit authorization record / report-only / no commit by agent`
- repository: `NMF13579/AOS-1`
- branch: `dev`
- report_path: `reports/task-2-8-3-1-cap-002-commit-authorization-correction.md`

## 2. Preconditions

- current_branch: `dev`
- task_2_8_3_report_present: `true`
- task_2_8_4_correction_report_present: `true`
- source_pack_commit_present_in_history: `true`
- working_tree_clean_before_report_creation: `false`
- blocking_dirty_worktree_item:
  - `reports/task-2-8-5-cap-002-post-commit-verification-and-push-authorization.md`

## 3. Task 2.8.3 Blocked State Intake

```yaml
task_2_8_3_blocked_state_intake:
  report_path: >
    reports/task-2-8-3-cap-002-diff-review-and-commit-authorization.md
  final_status_found: TASK_2_8_3_BLOCKED_NO_MUTATION_DIFF_FOUND
  human_authorization_was_recorded: false
  selected_option_in_task_2_8_3: null
  may_prepare_task_2_8_4_commit_in_task_2_8_3: false
  correction_required: true
```

## 4. Task 2.8.4-Correction Intake

```yaml
task_2_8_4_correction_intake:
  report_path: reports/task-2-8-4-correction-commit-scope-and-message.md
  final_status_found: TASK_2_8_4_CORRECTION_COMMITTED
  correction_commit_sha: 399ac696a1d8225b35e881ef074809dc1212ce81
  correction_commit_message: >
    docs: record Task 2.8.4 correction — missing diff review
    and commit scope fix
  deviation_documented: true
```

## 5. Source-Pack Commit Verification

```yaml
source_pack_commit_verification:
  commit_sha: 69cd7af850c74ab78a09b58377164e1fc591a0d5
  commit_message: >
    docs: apply CAP-002 approved source-pack mutations (§5.1, §6.1)
  commit_found_in_history: true
  committed_files:
    - Архитектура.txt
    - Скелет архитектуры.txt
    - reports/task-2-8-2-cap-002-controlled-source-pack-mutation.md
  expected_files:
    - Архитектура.txt
    - Скелет архитектуры.txt
    - reports/task-2-8-2-cap-002-controlled-source-pack-mutation.md
  commit_scope_acceptable: true
```

## 6. Human Commit Authorization Decision

```yaml
human_commit_authorization_decision:
  HUMAN_DECISION_2_8_3_1_A:
    decision: >
      CAP-002 source-pack mutation commit authorization
      (retroactive, correcting Task 2.8.3 blocked state)
    selected_option: AUTHORIZE_COMMIT
    selected_by_human: true
    decision_recorded: true
    authorization_scope_commit_sha: 69cd7af850c74ab78a09b58377164e1fc591a0d5
    authorization_covers:
      - Архитектура.txt
      - Скелет архитектуры.txt
      - reports/task-2-8-2-cap-002-controlled-source-pack-mutation.md
    retroactive: true
    authorizes_future_push: false
    authorizes_runtime_implementation: false
```

## 7. Authorization Scope

```yaml
authorization_scope:
  authorized_commit_sha: 69cd7af850c74ab78a09b58377164e1fc591a0d5
  authorized_files:
    - Архитектура.txt
    - Скелет архитектуры.txt
    - reports/task-2-8-2-cap-002-controlled-source-pack-mutation.md
  not_authorized_by_this_task:
    - push to origin/dev
    - CAP-002 runtime implementation
    - any future source-pack mutation
    - any task beyond 2.8.3.1 report creation
  may_unblock_task_2_8_5: true
```

## 8. Evidence Chain Correction Statement

```yaml
evidence_chain_correction_statement:
  task_2_8_3_was_blocked: true
  task_2_8_4_proceeded_without_authorization: true
  task_2_8_4_correction_documented_deviation: true
  task_2_8_3_1_provides_retroactive_authorization: true
  evidence_chain_now_complete_for_task_2_8_5: true
  human_approval_simulated: false
```

This task still stops in blocked state because the working tree was not clean before report creation.

## 9. Forbidden Claims Check

```yaml
forbidden_claims_check:
  cap_002_runtime_implemented: false
  cap_002_completed: false
  source_pack_modified_by_task_2_8_3_1: false
  task_2_8_3_report_modified: false
  git_commit_created_by_task_2_8_3_1: false
  staging_performed_by_task_2_8_3_1: false
  push_performed: false
  human_approval_simulated: false
  human_approval_marker_created_by_agent: false
  human_approval_marker_modified_by_agent: false
  task_2_8_5_started: false
```

## 10. Validation

- selected_by_human_true_present: `true`
- authorize_commit_present: `true`
- retroactive_true_present: `true`
- may_unblock_task_2_8_5_true_present: `true`
- git_commit_created_by_task_2_8_3_1_false_present: `true`
- push_performed_false_present: `true`
- human_approval_simulated_false_present: `true`
- evidence_chain_now_complete_for_task_2_8_5_true_present: `true`
- staged_files_present_after_report_creation: `false`
- tracked_files_modified_after_report_creation: `false`

## 11. Final Status

`TASK_2_8_3_1_COMMIT_AUTHORIZATION_CORRECTION_RECORDED`
