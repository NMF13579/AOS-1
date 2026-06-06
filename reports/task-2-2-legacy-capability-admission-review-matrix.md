# Task 2.2 — Legacy Capability Admission Review Matrix

## 1. Machine-Readable Summary

```yaml
task_id: "2.2"
task_name: "Legacy Capability Admission Review Matrix"
stage: "Stage 2"
mode: "read-only/admission-review-preparation/report-only"
report_path: "reports/task-2-2-legacy-capability-admission-review-matrix.md"

task_2_1_report_available: true
task_2_1_final_status: "TASK_2_1_MAP_READY_FOR_HUMAN_REVIEW"
task_2_1_commit_expected: "fab8da1"
task_2_1_commit_observed: "fab8da1"

capabilities_reviewed: 10
candidate_for_admission_count: 4
candidate_for_deferral_count: 4
candidate_for_rejection_count: 2
unknown_candidate_count: 0

human_admission_decisions_recorded_by_this_task: false
capabilities_admitted_by_this_task: 0
capabilities_deferred_by_this_task: 0
capabilities_rejected_by_this_task: 0
capabilities_requiring_human_decision: 10

source_of_truth_risk_reviewed: true
context_growth_risk_reviewed: true
do_not_import_reviewed: true
parking_lot_cross_checked: true

legacy_repository_accessed: false
legacy_files_copied: false
legacy_content_imported: false
large_legacy_implementation_content_reproduced: false

active_source_pack_modified: false
previous_reports_modified: false
files_staged: false
commit_created: false
push_performed: false

approval_created: false
stage_2_execution_authorized: false
stage_2_started: false
skeleton_materialized: false
validators_created: false
schemas_created: false
runtime_implemented: false

open_human_decision_count: 10

final_status: "TASK_2_2_ADMISSION_REVIEW_MATRIX_READY_FOR_HUMAN_DECISION"
```

## 2. Executive Summary

This report turns the `Task 2.1` map into a human decision table.

It does three things:
- keeps the evidence from `Task 2.1`
- keeps the candidate labels from `Task 2.1`
- adds empty decision fields for the human

It does not admit any capability.
It does not reject any capability as a human decision.
It does not defer any capability as a human decision.

## 3. Input Evidence Review

Reviewed input:
- `report_path`: `reports/task-2-1-legacy-capability-map.md`
- `present`: `true`
- `final_status`: `TASK_2_1_MAP_READY_FOR_HUMAN_REVIEW`
- `capabilities_found`: `10`
- `candidate_for_admission_count`: `4`
- `candidate_for_deferral_count`: `4`
- `candidate_for_rejection_count`: `2`
- `unknown_candidate_count`: `0`
- `any_capability_admitted`: `false`
- `do_not_import_findings_count`: `2`

No `TASK_BLOCKER: TASK_2_1_NOT_READY_FOR_ADMISSION_REVIEW` was triggered.

## 4. Repository State Review

- `repository_path`: `/Users/muhammednazyrov/Documents/GitHub/AOS-1`
- `current_branch`: `dev`
- `current_head_commit`: `fab8da1e57fedfb55f6c41afbbdae400261d1109`
- `latest_commits`:
  - `fab8da1 — docs: add legacy capability map`
  - `c1e273b — docs: add Stage 2 planning and authorization evidence`
  - `fd81667 — docs: record Stage 1 human review decision`
  - `36f6d29 — docs: add Stage 1 clean readiness evidence`
  - `8b9ba4e — chore: add active source pack baseline`
- `git_status_short`: clean

## 5. Capability Admission Matrix

| capability_id | name | task_2_1_candidate_classification | task_2_1_status | short_evidence_summary | source_paths_summary | source_of_truth_impact | context_growth_impact | do_not_import | do_not_import_reason | recommended_human_decision_options | agent_final_decision | human_decision_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `CAP-001` | Canonical bootstrap and routing | `CANDIDATE_FOR_ADMISSION` | `PRESENT` | One startup path and five canonical rule modules were found | `llms.txt`, `ROUTES-REGISTRY.md`, canonical modules | no new source of truth; no direct conflict seen; source pack change would still be needed | low | false | none | `ADMIT`, `DEFER`, `REJECT`, `REQUEST_CLARIFICATION` | none | `PENDING` |
| `CAP-002` | Human approval marker and approval boundary | `CANDIDATE_FOR_ADMISSION` | `PRESENT` | Explicit approval files and approval boundary rules were found | approval docs, approval marker, approval validation scripts | no new source of truth; no direct conflict seen; source pack change would still be needed | low | false | none | `ADMIT`, `DEFER`, `REJECT`, `REQUEST_CLARIFICATION` | none | `PENDING` |
| `CAP-003` | Active task lifecycle gating | `CANDIDATE_FOR_ADMISSION` | `PRESENT` | Controlled activation and completion-preparation flow was found | `tasks/active-task.md`, activation/completion scripts, lifecycle tool docs | no new source of truth; no direct conflict seen; source pack change would still be needed | medium | false | none | `ADMIT`, `DEFER`, `REJECT`, `REQUEST_CLARIFICATION` | none | `PENDING` |
| `CAP-004` | Unified validation and evidence wrapper | `CANDIDATE_FOR_ADMISSION` | `PRESENT` | One main validation entry command and evidence-focused verification layer were found | validation wrapper, validation tool docs, reports | no new source of truth; no direct conflict seen; source pack change would still be needed | medium | false | none | `ADMIT`, `DEFER`, `REJECT`, `REQUEST_CLARIFICATION` | none | `PENDING` |
| `CAP-005` | Spec and UX to task generation | `CANDIDATE_FOR_DEFERRAL` | `PRESENT` | Generators turn approved inputs into candidate task contracts | generation scripts, contract draft validator, drafts folder | unknown until future design choice | high | false | none | `ADMIT`, `DEFER`, `REJECT`, `REQUEST_CLARIFICATION` | none | `PENDING` |
| `CAP-006` | Manual queue and task health | `CANDIDATE_FOR_DEFERRAL` | `PRESENT` | Manual queue and read-only task-health reporting were found | queue docs, queue files, task-health script | unknown until future design choice | medium | false | none | `ADMIT`, `DEFER`, `REJECT`, `REQUEST_CLARIFICATION` | none | `PENDING` |
| `CAP-007` | Context selection and index layer | `CANDIDATE_FOR_DEFERRAL` | `PARTIAL` | Context indexing and selection exist, but they expand the context surface | context scripts, generated context data, schema | unknown; likely sensitive | high | false | none | `ADMIT`, `DEFER`, `REJECT`, `REQUEST_CLARIFICATION` | none | `PENDING` |
| `CAP-008` | Execution readiness and session records | `CANDIDATE_FOR_DEFERRAL` | `PRESENT` | Execution-readiness check and session evidence writing were found | runner scripts, execution docs, execution reports | unknown until future design choice | high | false | none | `ADMIT`, `DEFER`, `REJECT`, `REQUEST_CLARIFICATION` | none | `PENDING` |
| `CAP-009` | Template preparation and physical materialization | `CANDIDATE_FOR_REJECTION` | `PRESENT` | Real file/materialization behavior for templates was found | template prep script, template trees, template checker | yes; conflicts with current planning-only boundary | high | true | conflicts with AgentOS invariant | `ADMIT`, `DEFER`, `REJECT`, `REQUEST_CLARIFICATION` | none | `PENDING` |
| `CAP-010` | Memory-bank and project memory store | `CANDIDATE_FOR_REJECTION` | `PRESENT` | Separate memory and project-note layer was found | `memory-bank/`, `lessons/`, `handoff/`, `project/PROJECT.md` | yes; adds a likely extra source of truth | high | true | creates new source of truth | `ADMIT`, `DEFER`, `REJECT`, `REQUEST_CLARIFICATION` | none | `PENDING` |

## 6. Source-of-Truth Risk Review

For each capability:

| capability_id | add a new source of truth | conflict with Архитектура.txt | conflict with Скелет архитектуры.txt | require changing active source pack | requires_human_review_before_admission |
| --- | --- | --- | --- | --- | --- |
| `CAP-001` | no | no | no | yes | true |
| `CAP-002` | no | no | no | yes | true |
| `CAP-003` | no | no | no | yes | true |
| `CAP-004` | no | no | no | yes | true |
| `CAP-005` | unknown | unknown | unknown | unknown | true |
| `CAP-006` | unknown | unknown | unknown | unknown | true |
| `CAP-007` | unknown | unknown | unknown | unknown | true |
| `CAP-008` | unknown | unknown | unknown | unknown | true |
| `CAP-009` | yes | yes | yes | yes | true |
| `CAP-010` | yes | yes | unknown | yes | true |

Review summary:
- even the lowest-risk items still need human review because future adoption would require source-pack updates
- the two strongest source-of-truth risks are `CAP-009` and `CAP-010`

## 7. Context-Growth Risk Review

For each capability:

| capability_id | context tokens impact | document sprawl risk | bootstrap context growth | requires_human_review_before_admission |
| --- | --- | --- | --- | --- |
| `CAP-001` | low | low | low | false |
| `CAP-002` | low | low | low | false |
| `CAP-003` | medium | medium | low | false |
| `CAP-004` | medium | medium | low | false |
| `CAP-005` | medium | high | medium | true |
| `CAP-006` | medium | medium | low | false |
| `CAP-007` | high | high | high | true |
| `CAP-008` | medium | high | medium | true |
| `CAP-009` | medium | high | medium | true |
| `CAP-010` | high | high | high | true |

Review summary:
- biggest context-growth risks are `CAP-007` and `CAP-010`
- smallest context-growth risks are `CAP-001` and `CAP-002`

## 8. Do-Not-Import Review

Findings carried forward from `Task 2.1`:

| capability_id | name | do_not_import_reason | human_decision_required | agent_may_override |
| --- | --- | --- | --- | --- |
| `CAP-009` | Template preparation and physical materialization | conflicts with AgentOS invariant | true | false |
| `CAP-010` | Memory-bank and project memory store | creates new source of truth | true | false |

Boundary:
- these findings were not weakened
- these findings were not removed

## 9. Parking Lot Cross-Check

| parking_lot_item | legacy_presence_from_task_2_1 | admitted_by_this_task | requires_explicit_human_admission | notes |
| --- | --- | --- | --- | --- |
| `F-20 Git Context Controller / GCC` | no | false | true | no direct legacy implementation was mapped |
| `F-21 Letta git-backed memory` | partial | false | true | legacy has memory-like layer, but not Letta-based implementation |
| `F-31 Adaptive compute / voting` | no | false | true | no concrete legacy capability was mapped |
| `F-32 Hotswap small→large model` | no | false | true | no concrete legacy capability was mapped |
| `F-33 Fine-tuning on AgentOS data` | no | false | true | no concrete legacy capability was mapped |
| `F-34 Multi-agent debate` | partial | false | true | appears only as idea-level mention |
| `F-35 AgentOps Replay` | no | false | true | no concrete legacy capability was mapped |
| `F-43 Cross-repo sync` | partial | false | true | appears only as idea-level mention |

Boundary:
- no parking lot item was admitted by this report
- parking lot remains an input for later human decisions only

## 10. Human Decision Matrix

Human decision table:

| capability_id | name | candidate_classification | human_decision | allowed_decisions | human_notes |
| --- | --- | --- | --- | --- | --- |
| `CAP-001` | Canonical bootstrap and routing | `CANDIDATE_FOR_ADMISSION` | `PENDING` | `ADMIT`, `DEFER`, `REJECT`, `REQUEST_CLARIFICATION` | empty |
| `CAP-002` | Human approval marker and approval boundary | `CANDIDATE_FOR_ADMISSION` | `PENDING` | `ADMIT`, `DEFER`, `REJECT`, `REQUEST_CLARIFICATION` | empty |
| `CAP-003` | Active task lifecycle gating | `CANDIDATE_FOR_ADMISSION` | `PENDING` | `ADMIT`, `DEFER`, `REJECT`, `REQUEST_CLARIFICATION` | empty |
| `CAP-004` | Unified validation and evidence wrapper | `CANDIDATE_FOR_ADMISSION` | `PENDING` | `ADMIT`, `DEFER`, `REJECT`, `REQUEST_CLARIFICATION` | empty |
| `CAP-005` | Spec and UX to task generation | `CANDIDATE_FOR_DEFERRAL` | `PENDING` | `ADMIT`, `DEFER`, `REJECT`, `REQUEST_CLARIFICATION` | empty |
| `CAP-006` | Manual queue and task health | `CANDIDATE_FOR_DEFERRAL` | `PENDING` | `ADMIT`, `DEFER`, `REJECT`, `REQUEST_CLARIFICATION` | empty |
| `CAP-007` | Context selection and index layer | `CANDIDATE_FOR_DEFERRAL` | `PENDING` | `ADMIT`, `DEFER`, `REJECT`, `REQUEST_CLARIFICATION` | empty |
| `CAP-008` | Execution readiness and session records | `CANDIDATE_FOR_DEFERRAL` | `PENDING` | `ADMIT`, `DEFER`, `REJECT`, `REQUEST_CLARIFICATION` | empty |
| `CAP-009` | Template preparation and physical materialization | `CANDIDATE_FOR_REJECTION` | `PENDING` | `ADMIT`, `DEFER`, `REJECT`, `REQUEST_CLARIFICATION` | empty |
| `CAP-010` | Memory-bank and project memory store | `CANDIDATE_FOR_REJECTION` | `PENDING` | `ADMIT`, `DEFER`, `REJECT`, `REQUEST_CLARIFICATION` | empty |

The agent did not fill any human decision field with a final decision.

## 11. Open Questions and Blockers

Blockers:
- none

Open questions:
- Which `CANDIDATE_FOR_ADMISSION` capabilities should be admitted?
- Which `CANDIDATE_FOR_DEFERRAL` capabilities should remain deferred?
- Which `CANDIDATE_FOR_REJECTION` capabilities should be confirmed as rejected?
- Do any do-not-import findings require stronger blocking?
- Should any parking lot item be moved into future planning?
- Which admitted capabilities, if any, require source-pack update before implementation?
- Should `CAP-001` and `CAP-002` be reviewed first as the least risky pair?
- Should `CAP-007`, `CAP-009`, and `CAP-010` be treated as high-risk by default?

## 12. Forbidden Actions Boundary

Confirmed:
- No capability admitted.
- No capability deferred as final human decision.
- No capability rejected as final human decision.
- No legacy repository accessed.
- No legacy file copied.
- No legacy content imported.
- No large legacy implementation content reproduced.
- No active source pack modified.
- No previous report modified.
- No files staged.
- No commit created.
- No push performed.
- No skeleton materialized.
- No validators created.
- No schemas created.
- No runtime implemented.
- No approval created.
- No Stage 2 execution authorized.
- No Stage 2 started.
- Human decision remains open.

## 13. Proposed Next-Step Options

- Human may review this admission matrix.
- Human may provide explicit `ADMIT` / `DEFER` / `REJECT` / `REQUEST_CLARIFICATION` decisions for each capability.
- A later task may record human admission decisions.
- A later task may prepare source-of-truth impact updates only after human admission decisions.
- Human may reject the entire capability set.

## 14. Final Status

`TASK_2_2_ADMISSION_REVIEW_MATRIX_READY_FOR_HUMAN_DECISION`
