# Task 2.0 — Stage 2 Planning Proposal

## 1. Machine-Readable Summary

```yaml
task_id: "2.0"
task_name: "Stage 2 Planning Proposal"
stage: "Stage 2 planning"
mode: "read-only/planning-proposal/report-only"
report_path: "reports/task-2-0-stage-2-planning-proposal.md"

planning_authorization_verified: true
task_1_5_report_available: true
task_1_5_final_status: "TASK_1_5_STAGE_2_PLANNING_PREPARATION_AUTHORIZED_BY_HUMAN"
task_1_5_evidence_status: "local_uncommitted"

source_pack_files_read: 6
legacy_pointer_read: true
pinned_legacy_reference_read: true
legacy_repository_accessed_directly: false
legacy_capabilities_mapped_in_this_task: false
parking_lot_reviewed: true

proposed_task_count: 7
future_legacy_mapping_task_proposed: true

stage_2_execution_started: false
stage_2_approved_by_this_task: false
stage_2_execution_authorized_by_this_task: false
skeleton_materialized: false
validators_created: false
schemas_created: false
runtime_implemented: false
legacy_imported: false
legacy_files_copied: false
approval_created: false

active_source_pack_modified: false
previous_reports_modified: false
files_staged: false
commit_created: false
push_performed: false

open_human_decision_count: 5

final_status: "TASK_2_0_PROPOSAL_READY_FOR_HUMAN_REVIEW"
```

## 2. Executive Summary

This report proposes a Stage 2 planning sequence for human review.

Planning authorization is confirmed from `reports/task-1-5-stage-2-planning-authorization.md`, but that authorization currently exists as local uncommitted evidence, not committed evidence. This does not block the proposal, but it is recorded clearly.

This task read the active source pack, the legacy pointer, and the pinned legacy reference from `Адреса проектов.txt`. It did not access the legacy repository directly, did not read legacy capabilities, and did not admit any feature automatically.

## 3. Planning Authorization Review

Reviewed authorization evidence:
- `reports/task-1-5-stage-2-planning-authorization.md`

Confirmed from Task 1.5:
- `TASK_1_5_STAGE_2_PLANNING_PREPARATION_AUTHORIZED_BY_HUMAN`
- `stage_2_started: false`
- `stage_2_execution_authorized: false`
- `approval_created_by_agent: false`

Authorization result:
- planning authorization verified: `true`
- Task 1.5 evidence status: `local_uncommitted`

No `PROPOSAL_BLOCKER: PLANNING_NOT_AUTHORIZED` was triggered.

## 4. Repository State Review

- `repository_path`: `/Users/muhammednazyrov/Documents/GitHub/AOS-1`
- `current_branch`: `dev`
- `current_head_commit`: `fd81667a3bba5ed28ab505d507dbc94590e63c8d`
- `latest_commits`:
  - `fd81667 — docs: record Stage 1 human review decision`
  - `36f6d29 — docs: add Stage 1 clean readiness evidence`
  - `8b9ba4e — chore: add active source pack baseline`
- `git_status_short`: `?? reports/task-1-5-stage-2-planning-authorization.md`
- `task_1_5_evidence_status`: `local_uncommitted`

Local artifacts:
- `reports/task-1-5-stage-2-planning-authorization.md` is present as local report evidence only

## 5. Source Pack Reading Summary

| file_name | read | key_findings relevant to Stage 2 planning | notes |
| --- | --- | --- | --- |
| `Архитектура.txt` | true | Architecture keeps safety, approval, lifecycle, and source-of-truth boundaries above automation | Stage 2 planning must preserve these invariants |
| `Скелет архитектуры.txt` | true | Skeleton is planning guidance only and does not authorize physical materialization | Stage 2 proposal must avoid file creation/materialization work |
| `Roadmap.txt` | true | Stage 2 is legacy mapping and feature-admission alignment, not implementation | Main source for Stage 2 purpose and evidence categories |
| `Адреса проектов.txt` | true | Legacy repository is reference-only and pinned legacy commit is recorded | Proposal may reference pointer and pinned snapshot only |
| `06_Stage_1_Source_Pack_Intake_and_Admission_Gate.txt` | true | Stage 1 ended as intake/evidence, not approval | Stage 2 proposal must keep human checkpoint boundary explicit |
| `08_Future_Feature_Candidates_Parking_Lot.txt` | true | Parking lot stores future candidates but does not admit them | Stage 2 may consider them as inputs for review only |

All six required source-pack files were readable.

## 6. Stage 2 Goal From Roadmap

Verbatim from `Roadmap.txt`:

Purpose:

```text
map useful legacy capabilities to the target architecture without importing old implementation by default.
```

Required evidence categories:

```text
- candidate legacy capabilities;
- admitted/deferred/rejected classification;
- source-of-truth impact;
- context-growth impact;
- parity expectations where needed;
- do-not-import findings;
- blockers and unresolved human decisions.
```

Forbidden from `Roadmap.txt`:

```text
- direct copy-paste as authority;
- runtime implementation;
- automatic feature admission;
- project transfer completion claim.
```

Planning note:
- Roadmap states the Stage 2 purpose and evidence categories, but does not define exact task filenames or field layouts.

## 7. Legacy Pointer and Pinned Reference Summary

Read only from `Адреса проектов.txt`:
- `pinned_legacy_commit_sha`: `e3a60a92fbd5e78e583cddb519d39527583f3433`
- `legacy_repository_url`: `https://github.com/NMF13579/AgentOS/tree/dev`
- `legacy_role`: `reference_only`
- `future_task_may_request_read_only_legacy_mapping`: `true`
- `agent_may_access_legacy_repository_in_this_task`: `false`
- `agent_may_read_legacy_capabilities_in_this_task`: `false`
- `agent_may_import_as_authority`: `false`
- `agent_may_copy_files`: `false`

Boundary result:
- legacy pointer was read
- pinned legacy reference was read
- legacy repository was not accessed directly
- legacy capabilities were not mapped in this task

## 8. Proposed Task List

### Task 2.1 — Stage 2 Scope Lock and Boundary Definition
- `task_id`: `2.1`
- `task_name`: `Stage 2 Scope Lock and Boundary Definition`
- `goal`: define exact Stage 2 scope, non-goals, decision boundaries, and success criteria before any legacy mapping
- `inputs`: `Архитектура.txt`, `Roadmap.txt`, `06_Stage_1_Source_Pack_Intake_and_Admission_Gate.txt`, `reports/task-1-5-stage-2-planning-authorization.md`
- `allowed_outputs`: one Stage 2 scope/boundary report or task brief draft for human review
- `forbidden_actions`: no legacy repository access, no runtime work, no feature admission, no project transfer, no skeleton materialization
- `estimated_scope`: `narrow`
- `human_checkpoint_required`: `true`
- `depends_on`: `Task 1.5 human authorization record`

### Task 2.2 — Legacy Pointer and Pinned Reference Review
- `task_id`: `2.2`
- `task_name`: `Legacy Pointer and Pinned Reference Review`
- `goal`: restate and validate which legacy repository pointer and pinned reference are in scope for later read-only mapping
- `inputs`: `Адреса проектов.txt`, `Архитектура.txt`, `Roadmap.txt`
- `allowed_outputs`: one evidence report confirming exact legacy reference boundaries
- `forbidden_actions`: no capability reading, no repository import, no file copying, no feature admission
- `estimated_scope`: `narrow`
- `human_checkpoint_required`: `true`
- `depends_on`: `Task 2.1`

### Task 2.3 — Read-Only Legacy Capability Mapping Request
- `task_id`: `2.3`
- `task_name`: `Read-Only Legacy Capability Mapping Request`
- `goal`: request permission and define contract for a future read-only legacy capability mapping task
- `inputs`: `Roadmap.txt`, `Адреса проектов.txt`, `Архитектура.txt`, `reports/task-1-5-stage-2-planning-authorization.md`
- `allowed_outputs`: one request/report specifying what future mapping may inspect and what it must not do
- `forbidden_actions`: no direct capability mapping in this task, no import, no copying, no admission, no implementation
- `estimated_scope`: `narrow`
- `human_checkpoint_required`: `true`
- `depends_on`: `Task 2.1`, `Task 2.2`

### Task 2.4 — Admission Classification Design
- `task_id`: `2.4`
- `task_name`: `Admission Classification Design`
- `goal`: define how admitted, deferred, rejected, blocked, and requires-human-decision outcomes will be recorded during Stage 2
- `inputs`: `Архитектура.txt`, `Roadmap.txt`, `06_Stage_1_Source_Pack_Intake_and_Admission_Gate.txt`, `08_Future_Feature_Candidates_Parking_Lot.txt`
- `allowed_outputs`: one classification design report or template proposal
- `forbidden_actions`: no automatic feature admission, no runtime work, no project transfer, no legacy import
- `estimated_scope`: `medium`
- `human_checkpoint_required`: `true`
- `depends_on`: `Task 2.1`

### Task 2.5 — Source-of-Truth Impact Assessment Design
- `task_id`: `2.5`
- `task_name`: `Source-of-Truth Impact Assessment Design`
- `goal`: define how each future legacy capability candidate will be checked for source-of-truth drift risk
- `inputs`: `Архитектура.txt`, `Roadmap.txt`, `Скелет архитектуры.txt`
- `allowed_outputs`: one assessment design report with required review fields
- `forbidden_actions`: no implementation, no feature admission, no source-of-truth mutation, no skeleton materialization
- `estimated_scope`: `medium`
- `human_checkpoint_required`: `true`
- `depends_on`: `Task 2.1`, `Task 2.4`

### Task 2.6 — Context-Growth Impact Review Design
- `task_id`: `2.6`
- `task_name`: `Context-Growth Impact Review Design`
- `goal`: define how Stage 2 will evaluate prompt/context growth risk from any future admitted capability
- `inputs`: `Архитектура.txt`, `Roadmap.txt`, `08_Future_Feature_Candidates_Parking_Lot.txt`
- `allowed_outputs`: one design report for context-growth evaluation criteria
- `forbidden_actions`: no runtime work, no admission, no legacy import, no Stage 2 execution
- `estimated_scope`: `medium`
- `human_checkpoint_required`: `true`
- `depends_on`: `Task 2.1`, `Task 2.4`

### Task 2.7 — Stage 2 Approval Boundary and Non-Execution Review
- `task_id`: `2.7`
- `task_name`: `Stage 2 Approval Boundary and Non-Execution Review`
- `goal`: define the explicit review gate that prevents Stage 2 planning from being mistaken for execution or approval
- `inputs`: `Архитектура.txt`, `Roadmap.txt`, `06_Stage_1_Source_Pack_Intake_and_Admission_Gate.txt`, `reports/task-1-5-stage-2-planning-authorization.md`
- `allowed_outputs`: one non-execution boundary report or gate proposal
- `forbidden_actions`: no Stage 2 start, no implementation permission, no approval creation, no project transfer
- `estimated_scope`: `narrow`
- `human_checkpoint_required`: `true`
- `depends_on`: `Task 2.1`, `Task 2.4`, `Task 2.5`, `Task 2.6`

Proposal summary:
- proposed task count: `7`
- future read-only legacy mapping task proposed: `true`

## 9. Parking Lot Review

Parking-lot items relevant to Stage 2 planning as review inputs only:
- `F-20 Git Context Controller / GCC`
- `F-35 AgentOps Replay`
- `F-43 Cross-repo sync`
- `F-21 Letta git-backed memory`
- `F-31 Adaptive compute / voting`
- `F-34 Multi-agent debate`

Parking-lot boundary confirmation:
- parking lot items are not automatically admitted
- parking lot items require explicit human admission decision
- no parking lot item becomes implementation permission by appearing in this report

No parking-lot item was classified as admitted in this task.

## 10. Risks and Open Questions

Risks:
- `legacy import boundary risk`: future mapping could be mistaken for permission to copy or adopt legacy content
- `scope creep risk`: Stage 2 planning could expand into implementation if task boundaries are not explicit
- `context growth risk`: capability mapping may pull too much legacy context into future tasks
- `source-of-truth drift risk`: future candidate capabilities may pressure canonical documents or derived artifacts to drift
- `planning mistaken for approval risk`: planning proposal could be misread as permission to execute
- `parking lot mistaken for roadmap risk`: listed future candidates could be mistaken for admitted Stage 2 work

Open questions for human review:
- Should future Stage 2 tasks be approved one by one, or as one small approved bundle?
- Should the future read-only legacy mapping task be limited to the pinned commit only, or may it also compare with legacy `dev` for context?
- What admission outcome vocabulary should be treated as the minimum required set for Stage 2?
- Which parking-lot items, if any, should be considered during Stage 2 review?
- Should parity expectations be required for every future admitted capability, or only for selected capabilities?

## 11. Forbidden Actions Boundary

Explicitly confirmed:
- Stage 2 not started.
- Stage 2 execution not authorized.
- Stage 2 not approved by this task.
- Skeleton not materialized.
- Validators not created.
- Schemas not created.
- Runtime not implemented.
- Legacy repository not accessed directly.
- Legacy capabilities not mapped in this task.
- Legacy files not imported.
- Legacy features not admitted.
- Parking lot items not admitted.
- Approval not created.
- Human decision not simulated.
- Files not staged.
- Commit not created.
- Push not performed.

## 12. Human Decision Items

- `DECISION_1`: Review and approve or reject this Stage 2 planning proposal.
- `DECISION_2`: Approve or reject each proposed task individually or as a group.
- `DECISION_3`: Decide whether a future read-only legacy capability mapping task may access the pinned legacy repository.
- `DECISION_4`: Decide admission status for each legacy capability only after a future mapping task, if authorized.
- `DECISION_5`: Decide which parking lot items, if any, should be considered for Stage 2.

These decisions remain open. This task does not answer them.

## 13. Proposed Next-Step Options

- Human may approve this planning proposal and authorize Task 2.1 preparation.
- Human may reject or revise this planning proposal.
- Human may approve individual tasks from the proposed list.
- Human may add, remove, or reorder proposed tasks.
- Human may authorize a future read-only legacy capability mapping task.
- Human must review any Stage 2 task brief before execution.

## 14. Final Status

`TASK_2_0_PROPOSAL_READY_FOR_HUMAN_REVIEW`
