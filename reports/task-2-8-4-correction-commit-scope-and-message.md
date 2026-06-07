# Task 2.8.4-Correction — Commit Scope and Message Correction

## 1. Task Metadata

- task_id: `2.8.4-Correction`
- mode: `correction task / one new commit / no push / no source-pack mutation`
- repository: `NMF13579/AOS-1`
- branch: `dev`
- correction_target_commit: `69cd7af850c74ab78a09b58377164e1fc591a0d5`
- report_path: `reports/task-2-8-4-correction-commit-scope-and-message.md`

## 2. Preconditions

- current_branch: `dev`
- local_branch_behind_upstream: `false`
- task_2_8_2_report_present: `true`
- architecture_txt_present: `true`
- skeleton_txt_present: `true`
- working_tree_status_interpretation: `only_allowed_uncommitted_task_2_8_3_file_present`

## 3. Task 2.8.4 Deviation Record

```yaml
task_2_8_4_deviation_record:
  actual_commit_sha: 69cd7af850c74ab78a09b58377164e1fc591a0d5
  actual_commit_message: "docs: apply CAP-002 approved source-pack mutations (§5.1, §6.1)"
  expected_commit_message: "docs: add CAP-002 human approval boundary to source pack"
  message_matches_expected: false
  actual_committed_files:
    - Архитектура.txt
    - Скелет архитектуры.txt
    - reports/task-2-8-2-cap-002-controlled-source-pack-mutation.md
  expected_committed_files:
    - Архитектура.txt
    - Скелет архитектуры.txt
    - reports/task-2-8-2-cap-002-controlled-source-pack-mutation.md
    - reports/task-2-8-3-cap-002-diff-review-and-commit-authorization.md
  missing_file: reports/task-2-8-3-cap-002-diff-review-and-commit-authorization.md
  amend_forbidden: true
  reason: commit already pushed to upstream
```

## 4. Task 2.8.3 File Status

```yaml
task_2_8_3_file_status:
  file_path: reports/task-2-8-3-cap-002-diff-review-and-commit-authorization.md
  status: found_locally_uncommitted
  included_in_correction_commit: true
```

The file exists locally and was not rewritten by this correction task.

## 5. Correction Action

```yaml
correction_action:
  amend_performed: false
  rebase_performed: false
  new_commit_created: true
  commit_message: "docs: record Task 2.8.4 correction — missing diff review and commit scope fix"
  committed_files:
    - reports/task-2-8-3-cap-002-diff-review-and-commit-authorization.md
    - reports/task-2-8-4-correction-commit-scope-and-message.md
  source_pack_files_modified: false
```

## 6. Staging and Commit Boundary

```yaml
staging_and_commit_boundary:
  files_staged:
    - reports/task-2-8-3-cap-002-diff-review-and-commit-authorization.md
    - reports/task-2-8-4-correction-commit-scope-and-message.md
  files_outside_scope_staged: false
  push_performed: false
  task_2_8_5_started: false
```

## 7. Forbidden Claims Check

```yaml
forbidden_claims_check:
  cap_002_runtime_implemented: false
  source_pack_modified_by_correction: false
  commit_amended: false
  rebase_performed: false
  push_performed: false
  task_2_8_5_started: false
  task_2_8_5_artifacts_created: false
  human_approval_simulated: false
```

## 8. Validation

- existing_task_2_8_3_file_reused_without_rewrite: `true`
- correction_report_created: `true`
- source_pack_files_untouched_by_correction: `true`
- push_performed: `false`
- commit_message_for_correction_prepared: `true`

## 9. Final Status

`TASK_2_8_4_CORRECTION_COMMITTED`
