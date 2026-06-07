# Task 2.7.2 — Evidence Content Verification Repair

## 1. Task Metadata

```yaml
task_id: "2.7.2"
task_name: "Evidence Content Verification Repair"
stage: "Stage 2"
mode: "Corrective evidence verification / read-only report-only"
repository: "NMF13579/AOS-1"
branch_required: "dev"
branch_observed: "dev"
task_2_7_report_present: true
task_2_7_1_report_present: true
final_status: "TASK_2_7_2_PATH_MISMATCH_CONTENT_VERIFIED"
```

## 2. Preconditions

- `git branch --show-current`: `dev`
- `git status --short` before report creation: clean
- `test -f reports/task-2-7-cap-002-decision-consolidation.md`: passed
- `test -f reports/task-2-6-5-cap-001-source-pack-update-completion-review.md`: passed
- `test -f reports/task-2-6-4-post-commit-verification-cap-001-source-pack-edit.md`: passed
- `test -f reports/task-2-2-legacy-capability-admission-review-matrix.md`: passed
- `test -f reports/task-2-3-human-admission-decisions.md`: passed
- `test -f reports/task-2-4-source-pack-impact-review-for-admitted-capabilities.md`: failed
- human path resolution received:
  - expected path: `reports/task-2-4-source-pack-impact-review-for-admitted-capabilities.md`
  - canonical actual path: `reports/task-2-4-admitted-capability-source-pack-impact-review.md`
  - resolution: `PATH_MISMATCH_RESOLVED_BY_HUMAN`
  - `actual_file_is_canonical`: `true`
  - `read_and_verify_content`: `true`

Precondition result:

- Task 2.7 report exists.
- All five evidence roles are now readable for corrective review.
- The originally missing Task 2.4 mapped path was resolved by explicit human direction to the canonical actual path:
  `reports/task-2-4-admitted-capability-source-pack-impact-review.md`

## 3. Reason for Corrective Verification

Task 2.7 recorded `PATH_MISMATCH_CONTENT_FOUND` classifications, but the corrective review is required because content equivalence must be proven by reading actual evidence files, not inferred from filenames or prompt context.

## 4. Task 2.7 Intake

Task 2.7 claimed that five evidence items were usable under `PATH_MISMATCH_CONTENT_FOUND`.

This corrective task checks whether that claim is supported by real file reading:

- `cap_001_completion_review`
- `cap_001_post_commit_verification`
- `stage_2_admission_review_matrix`
- `stage_2_human_admission_decisions`
- `stage_2_source_pack_impact_review`

Task 2.7.1 was also read because it depends on Task 2.7’s evidence base.

## 5. Actual Evidence File Reading Log

```yaml
actual_evidence_file_reading_log:
  cap_001_completion_review:
    actual_path: reports/task-2-6-5-cap-001-source-pack-update-completion-review.md
    file_exists: true
    file_read: true
    lines_read: "1-214 of 214"
    read_method: "wc -l + sed -n '1,220p'"

  cap_001_post_commit_verification:
    actual_path: reports/task-2-6-4-post-commit-verification-cap-001-source-pack-edit.md
    file_exists: true
    file_read: true
    lines_read: "1-174 of 174"
    read_method: "wc -l + sed -n '1,220p'"

  stage_2_admission_review_matrix:
    actual_path: reports/task-2-2-legacy-capability-admission-review-matrix.md
    file_exists: true
    file_read: true
    lines_read: "1-255 of 255"
    read_method: "wc -l + sed -n '1,220p' + sed -n '221,255p'"

  stage_2_human_admission_decisions:
    actual_path: reports/task-2-3-human-admission-decisions.md
    file_exists: true
    file_read: true
    lines_read: "1-299 of 299"
    read_method: "wc -l + sed -n '1,220p' + sed -n '221,299p'"

  stage_2_source_pack_impact_review:
    actual_path: reports/task-2-4-admitted-capability-source-pack-impact-review.md
    file_exists: true
    file_read: true
    lines_read: "1-359 of 359"
    read_method: "human path resolution + wc -l + sed -n '1,220p' + sed -n '221,359p'"
```

Additional note:

- The human resolved the Task 2.4 path mismatch explicitly and confirmed that
  `reports/task-2-4-admitted-capability-source-pack-impact-review.md`
  is the canonical actual file for this evidence role.
- That canonical actual file was read in full and used for content verification.

## 6. Evidence Content Verification Matrix

```yaml
evidence_content_verification_matrix:
  cap_001_completion_review:
    expected_role: CAP-001 source-pack update completion review
    expected_path_from_task_2_7: reports/task-2-6-5-cap-001-completion-review.md
    actual_path: reports/task-2-6-5-cap-001-source-pack-update-completion-review.md
    task_id_or_title_found: "Task 2.6.5 — CAP-001 Source-Pack Update Completion Review"
    final_status_found: "TASK_2_6_5_CAP_001_SOURCE_PACK_UPDATE_COMPLETE"
    content_verification_status: CONTENT_VERIFIED
    path_mismatch_classification_supported: true

  cap_001_post_commit_verification:
    expected_role: CAP-001 post-commit verification
    expected_path_from_task_2_7: reports/task-2-6-4-1-cap-001-post-commit-verification.md
    actual_path: reports/task-2-6-4-post-commit-verification-cap-001-source-pack-edit.md
    task_id_or_title_found: "Task 2.6.4 — Post-Commit Verification of CAP-001 Source-Pack Edit"
    final_status_found: "TASK_2_6_4_POST_COMMIT_VERIFICATION_PASS"
    content_verification_status: CONTENT_VERIFIED
    path_mismatch_classification_supported: true

  stage_2_admission_review_matrix:
    expected_role: Stage 2 capability admission review matrix
    expected_path_from_task_2_7: reports/stage-2-capability-admission-review-matrix.md
    actual_path: reports/task-2-2-legacy-capability-admission-review-matrix.md
    task_id_or_title_found: "Task 2.2 — Legacy Capability Admission Review Matrix"
    final_status_found: "TASK_2_2_ADMISSION_REVIEW_MATRIX_READY_FOR_HUMAN_DECISION"
    content_verification_status: CONTENT_VERIFIED
    path_mismatch_classification_supported: true

  stage_2_human_admission_decisions:
    expected_role: Stage 2 human admission decisions
    expected_path_from_task_2_7: reports/stage-2-human-admission-decisions.md
    actual_path: reports/task-2-3-human-admission-decisions.md
    task_id_or_title_found: "Task 2.3 — Human Admission Decisions Record"
    final_status_found: "TASK_2_3_HUMAN_DECISIONS_RECORDED"
    content_verification_status: CONTENT_VERIFIED
    path_mismatch_classification_supported: true

  stage_2_source_pack_impact_review:
    expected_role: Stage 2 source-pack impact review for admitted capabilities
    expected_path_from_task_2_7: reports/stage-2-source-pack-impact-review.md
    actual_path: reports/task-2-4-admitted-capability-source-pack-impact-review.md
    task_id_or_title_found: "Task 2.4 — Admitted Capability Source-Pack Impact Review"
    final_status_found: "TASK_2_4_SOURCE_PACK_IMPACT_REVIEW_READY_FOR_HUMAN_DECISION"
    content_verification_status: CONTENT_VERIFIED
    path_mismatch_classification_supported: true
```

## 7. Corrected PATH_MISMATCH Classification Review

The Task 2.7 `PATH_MISMATCH_CONTENT_FOUND` classifications are now content-verified by corrective review.

Detailed result:

- All five classifications are now content-verified by corrective reading.
- For the Task 2.4 evidence role, verification depends on the explicit human resolution:
  - expected path: `reports/task-2-4-source-pack-impact-review-for-admitted-capabilities.md`
  - canonical actual path: `reports/task-2-4-admitted-capability-source-pack-impact-review.md`
  - resolution: `PATH_MISMATCH_RESOLVED_BY_HUMAN`

## 8. Impact on Task 2.7 and Task 2.7.1

```yaml
impact_review:
  task_2_7_original_report_modified: false
  task_2_7_original_path_mismatch_claim_corrected_by_supplemental_report: true
  task_2_7_1_human_decisions_invalidated: false
  cap_002_admission_direction_changed: false
  may_prepare_task_2_8_changed: false
```

Interpretation:

- Task 2.7 is not rewritten.
- This report supplements Task 2.7 by proving four path mismatches through actual reading.
- Task 2.7.1 remains valid as a human decision record.
- CAP-002 admission direction is unchanged.
- `may_prepare_task_2_8` is not changed by this corrective task.

## 9. Carry-Forward Items

```yaml
carry_forward:
  may_prepare_task_2_8_1_proposal_correction: true
  reason: Task 2.8 proposal still needs correction for architecture anchor and Markdown fenced-block safety.
```

## 10. Forbidden Claims Check

```yaml
forbidden_claims_check:
  cap_002_implemented: false
  cap_002_approved: false
  cap_002_execution_started: false
  source_pack_mutation_performed: false
  source_pack_mutation_authorized: false
  architecture_txt_modified: false
  skeleton_txt_modified: false
  task_2_8_1_started: false
  human_approval_simulated: false
```

## 11. Validation

Required validation markers included in this report:

- `CONTENT_VERIFIED`
- `PATH_MISMATCH_CONTENT_FOUND`
- `actual_evidence_file_reading_log:`
- `evidence_content_verification_matrix:`
- `task_2_7_original_report_modified: false`
- `cap_002_implemented: false`
- `source_pack_mutation_performed: false`
- `architecture_txt_modified: false`
- `skeleton_txt_modified: false`
- `human_approval_simulated: false`

Validation expectation:

- If any required validation command fails, final status must be `TASK_2_7_2_VALIDATION_FAILED`.

## 12. Final Status

`TASK_2_7_2_PATH_MISMATCH_CONTENT_VERIFIED`
