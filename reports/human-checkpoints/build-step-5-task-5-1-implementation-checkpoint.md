# reports/human-checkpoints/build-step-5-task-5-1-implementation-checkpoint.md

checkpoint_id: HCP-BS5-TASK51-001
checkpoint_type: task_execution_authorization
task: "Task 5.1 — Minimal Code Assembly Flow Implementation"
branch: build/assembly-first
date: 2026-06-13
authorized_by: human  # подпись человека обязательна

# ── Предусловия ──────────────────────────────────────────────────────────────

prerequisites:
  task_5_0_final_status: BUILD_STEP_5_INTAKE_READY_WITH_WARNINGS  # должен быть до execution
  task_5_0_report_committed: true
  task_5_0_checkpoint_committed: true
  task_5_0_checkpoint_path: >
    reports/human-checkpoints/build-step-5-task-5-0-authorization-checkpoint.md
  risk_profile_assigned_by_human: HIGH_RISK_PROTECTED
  workspace_clean_before_start: required

# ── Risk Profile ─────────────────────────────────────────────────────────────

risk_profile:
  assigned: HIGH_RISK_PROTECTED
  assigned_by: human
  rationale: >
    Task 5.1 создаёт первый рабочий Code Assembly Pipeline.
    Изменения затрагивают agentos/pipelines/ — область, граничащую
    с canonical contracts. Требуется human oversight на каждом шаге.

# ── Authorized scope ─────────────────────────────────────────────────────────

authorized_writes:
  - agentos/pipelines/code-assembly/  # только pre-authorized paths из CEP
  - tasks/                            # только Task Brief файл Task 5.1
  - reports/                          # только Execution Report и Evidence Report

authorized_change_mode: create_new_only  # не перезаписывать существующие файлы

# ── Forbidden ────────────────────────────────────────────────────────────────

forbidden:
  - agentos/safety/
  - agentos/pipelines/code-assembly/code-assembly-pipeline-contract.md
  - reports/human-checkpoints/
  - tasks/ACTIVE_TASK.md
  - любые product code файлы
  - templates/ без отдельного human checkpoint
  - commit / push / merge / release без отдельного human authorization

# ── Semantic invariants ───────────────────────────────────────────────────────

invariants_confirmed:
  pass_is_not_approval: true
  evidence_is_not_approval: true
  not_run_is_not_pass: true
  unknown_is_not_ok: true
  agent_claim_is_not_proof: true
  human_review_required: true
  validator_status_if_no_validator: NOT_RUN
  auto_commit_forbidden: true
  auto_push_forbidden: true
  auto_merge_forbidden: true

# ── Expected outputs Task 5.1 ─────────────────────────────────────────────────

expected_artifacts:
  - path: agentos/pipelines/code-assembly/  # implementation files
    type: implementation
  - path: reports/build-step-5-task-5-1-execution-report.md
    type: execution_report
  - path: reports/build-step-5-task-5-1-evidence-report.md
    type: evidence_report
  - path: reports/build-step-5-task-5-1-human-review-handoff.md
    type: human_review_handoff

# ── Human decision ────────────────────────────────────────────────────────────

human_decision: APPROVED

human_notes: ""  # опционально

# ── Boundaries ───────────────────────────────────────────────────────────────

post_execution_required:
  human_review_of_diff: true
  human_review_of_evidence_report: true
  separate_commit_authorization: true

this_checkpoint_is_not:
  - approval
  - execution_permission_for_task_5_2
  - lifecycle_mutation
  - merge_authorization
