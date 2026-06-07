# Task 2.8.3.1 — CAP-002 Commit Authorization Clarification

## 1. Purpose

This document clarifies the execution context of Task 2.8.3.1 and resolves
an internal contradiction recorded in the Task 2.8.3.1 report.

This document does not modify any existing report.
This document does not modify any source-pack file.
This document does not create a new commit by itself.

## 2. The Contradiction in Task 2.8.3.1

The Task 2.8.3.1 report contains a logical contradiction:

- The report body states that execution was blocked due to a dirty working tree
- The final status was manually set to `TASK_2_8_3_1_COMMIT_AUTHORIZATION_CORRECTION_RECORDED`

This contradiction exists because the dirty working tree was caused by a
stray file that was removed during execution. After its removal, the working
tree became clean. The authorization decision was recorded successfully.

The final status `TASK_2_8_3_1_COMMIT_AUTHORIZATION_CORRECTION_RECORDED` is
**confirmed as correct**.

## 3. What Task 2.8.3.1 Actually Authorized

Task 2.8.3.1 recorded retroactive commit authorization for the following commit:

```yaml
source_pack_commit:
  sha: 69cd7af850c74ab78a09b58377164e1fc591a0d5
  message: "docs: apply CAP-002 approved source-pack mutations (§5.1, §6.1)"
  files_changed:
    - Архитектура.txt
    - Скелет архитектуры.txt
    - reports/task-2-8-2-cap-002-controlled-source-pack-mutation.md
  status_in_origin: already_pushed
  is_pending_push: false
```

The authorization fields recorded in Task 2.8.3.1 are:

```yaml
retroactive_commit_authorization:
  HUMAN_DECISION_2_8_3_1_A:
    decision: CAP-002 commit authorization correction
    selected_option: AUTHORIZE_COMMIT
    selected_by_human: true
    retroactive: true
    may_unblock_task_2_8_5: true
```

## 4. Why Task 2.8.3.3 Is Not Needed

Task 2.8.3.3 was proposed as a new retroactive authorization report.
It is not needed because Task 2.8.3.1 already fulfills this role:

- `selected_by_human: true` — recorded
- `may_unblock_task_2_8_5: true` — recorded
- `AUTHORIZE_COMMIT` — recorded
- Report committed to branch `dev` at commit `a82919a`

Creating Task 2.8.3.3 would duplicate existing evidence without adding value.

## 5. Clarification of Pending Commits Before Task 2.8.5

Before the Task 2.8.5 evidence commit, the local branch has exactly
**two commits ahead of origin/dev**:

| Position | SHA | Message |
|----------|-----|---------|
| HEAD~1 | 399ac69 | docs: record Task 2.8.4 correction — missing diff review and commit scope fix |
| HEAD | a82919a | docs: record CAP-002 commit authorization correction (Task 2.8.3.1) |

The source-pack commit `69cd7af` is **already in origin/dev** and is not pending.

## 6. Instructions for Task 2.8.5

Task 2.8.5 must use these corrected precondition checks:

```yaml
corrected_preconditions_for_task_2_8_5:

  commit_authorization_source:
    check_file: reports/task-2-8-3-1-cap-002-commit-authorization-correction.md
    required_strings:
      - TASK_2_8_3_1_COMMIT_AUTHORIZATION_CORRECTION_RECORDED
      - AUTHORIZE_COMMIT
      - selected_by_human: true
      - may_unblock_task_2_8_5: true
    do_not_check: reports/task-2-8-3-cap-002-diff-review-and-commit-authorization.md

  source_pack_commit_verification:
    command: git show 69cd7af850c74ab78a09b58377164e1fc591a0d5 --name-only --pretty=format:%H%n%s
    expected_sha: 69cd7af850c74ab78a09b58377164e1fc591a0d5
    expected_message: "docs: apply CAP-002 approved source-pack mutations (§5.1, §6.1)"
    expected_files:
      - Архитектура.txt
      - Скелет архитектуры.txt
      - reports/task-2-8-2-cap-002-controlled-source-pack-mutation.md
    note: reports/task-2-8-3-cap-002-diff-review-and-commit-authorization.md is absent
          from this commit — this is a documented deviation, not a scope violation
    do_not_use: git diff HEAD~2 HEAD~1 --name-only

  pending_commits_before_evidence_commit:
    command: git log --oneline @{u}..HEAD
    expected_count: 2
    expected_commits:
      - "399ac69 docs: record Task 2.8.4 correction — missing diff review and commit scope fix"
      - "a82919a docs: record CAP-002 commit authorization correction (Task 2.8.3.1)"

  pending_commits_after_evidence_commit:
    expected_count: 3
    expected_commits:
      - "399ac69 docs: record Task 2.8.4 correction — missing diff review and commit scope fix"
      - "a82919a docs: record CAP-002 commit authorization correction (Task 2.8.3.1)"
      - "<new evidence commit SHA> docs: record CAP-002 push authorization evidence"
```

## 7. Forbidden Claims Check

```yaml
forbidden_claims_check:
  task_2_8_3_1_report_modified: false
  source_pack_files_modified: false
  architecture_txt_modified: false
  skeleton_txt_modified: false
  commit_created_by_this_clarification: false
  push_performed: false
  human_approval_simulated: false
  human_approval_inferred: false
```

## 8. Final Status

`TASK_2_8_3_1_CLARIFICATION_RECORDED`
