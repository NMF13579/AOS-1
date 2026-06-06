# Task 2.1 — Legacy Capability Map

## 1. Machine-Readable Summary

```yaml
task_id: "2.1"
task_name: "Legacy Capability Mapping"
stage: "Stage 2"
mode: "read-only/evidence-collection/report-only"
report_path: "reports/task-2-1-legacy-capability-map.md"

human_authorization_verified: true
task_1_5_report_available: true
task_2_0_proposal_available: true
task_2_0_1_authorization_report_available: true
planning_proposal_accepted_by_human: true
legacy_read_only_mapping_authorized_by_human: true

legacy_repository_url: "https://github.com/NMF13579/AgentOS"
pinned_legacy_commit_sha: "e3a60a92fbd5e78e583cddb519d39527583f3433"
legacy_access_method: "temporary_clone"
temporary_directory_used: true
temporary_directory_removed: true
legacy_accessed_at_pinned_commit: true
legacy_moving_branch_used_as_evidence: false
legacy_files_copied: false
legacy_content_copied_into_report: false
large_legacy_implementation_content_reproduced: false
legacy_imported_as_authority: false

capabilities_found: 10
capabilities_classified_candidate_for_admission: 4
capabilities_classified_candidate_for_deferral: 4
capabilities_classified_candidate_for_rejection: 2
capabilities_classified_unknown: 0

any_capability_admitted: false
any_legacy_file_copied: false
any_legacy_content_imported: false

source_of_truth_impact_assessed: true
context_growth_impact_assessed: true
do_not_import_findings_present: true
parking_lot_reviewed: true

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

open_human_decision_count: 6
final_status: "TASK_2_1_MAP_READY_FOR_HUMAN_REVIEW"
```

## 2. Executive Summary

Human authorization for Task 2.1 was verified before any legacy access.

The legacy repository was read only at the pinned commit:
- repository: `https://github.com/NMF13579/AgentOS`
- pinned commit: `e3a60a92fbd5e78e583cddb519d39527583f3433`

This task found a large, structured legacy system with clear capability groups:
- governed bootstrap and routing
- human approval markers and approval boundary rules
- task lifecycle control around `active-task`
- unified validation and evidence tooling
- spec/UX to task generation
- manual queue and task health
- context selection and indexing
- execution-session and readiness runner
- template preparation/materialization
- memory-bank and lesson storage

This report does not admit any capability.
It records candidates only for later human decisions.

## 3. Human Authorization Review

Required authorization artifacts present:
- `reports/task-1-5-stage-2-planning-authorization.md`
- `reports/task-2-0-stage-2-planning-proposal.md`
- `reports/task-2-0-1-stage-2-planning-proposal-acceptance-and-legacy-mapping-authorization.md`

Confirmed from Task 2.0.1:
- Task 2.0 planning proposal accepted by human: `true`
- Task 2.1 read-only legacy mapping at pinned commit authorized by human: `true`
- Stage 2 execution authorized: `false`
- Stage 2 started: `false`

No `TASK_BLOCKER: HUMAN_AUTHORIZATION_MISSING` was triggered.

## 4. Repository State Review

- `repository_path`: `/Users/muhammednazyrov/Documents/GitHub/AOS-1`
- `current_branch`: `dev`
- `current_head_commit`: `c1e273be0d227c6b53df627eade398f4a0842fae`
- `latest_commits`:
  - `c1e273b — docs: add Stage 2 planning and authorization evidence`
  - `fd81667 — docs: record Stage 1 human review decision`
  - `36f6d29 — docs: add Stage 1 clean readiness evidence`
  - `8b9ba4e — chore: add active source pack baseline`
- `git_status_short`: clean
- `untracked_files_if_any`: none

## 5. Legacy Pointer Verification

Read from `Адреса проектов.txt`:
- `legacy_repository_url`: `https://github.com/NMF13579/AgentOS`
- `pinned_legacy_commit_sha`: `e3a60a92fbd5e78e583cddb519d39527583f3433`
- `legacy_role`: `reference_only`
- `access_mode`: `read_only_at_pinned_commit`
- `agent_may_import_as_authority`: `false`
- `agent_may_copy_files`: `false`

The moving legacy branch head was not used as evidence.

## 6. Legacy Access Method

- `legacy_access_method`: `temporary_clone`
- `temporary_directory_used`: `true`
- `temporary_directory_path`: `/private/tmp/aos-legacy-full.3YD8jN`
- `temporary_directory_removed`: `true`
- `legacy_accessed_at_pinned_commit`: `true`
- `legacy_moving_branch_used_as_evidence`: `false`
- `legacy_files_copied`: `false`
- `legacy_imported_as_authority`: `false`
- `large_legacy_implementation_content_reproduced`: `false`

Method summary:
- a temporary clone was created outside `AOS-1`
- the legacy repository was checked out in detached mode at the pinned commit only
- findings below are based on file paths, short summaries, and brief inspections

## 7. Legacy Capability Inventory

### CAP-001
- `capability_id`: `CAP-001`
- `name`: `Canonical bootstrap and routing`
- `description`: legacy has one startup path and five canonical rule modules that separate authority areas
- `found_in_legacy`: `true`
- `file_paths`:
  - `llms.txt`
  - `ROUTES-REGISTRY.md`
  - `core-rules/MAIN.md`
  - `state/MAIN.md`
  - `workflow/MAIN.md`
  - `quality/MAIN.md`
  - `security/MAIN.md`
- `short_evidence_summary`: startup order and module ownership are explicitly documented
- `status`: `PRESENT`
- `candidate_classification`: `CANDIDATE_FOR_ADMISSION`
- `rationale`: closely matches the new architecture goal of one clear authority route
- `do_not_import`: `false`

### CAP-002
- `capability_id`: `CAP-002`
- `name`: `Human approval marker and approval boundary`
- `description`: legacy separates evidence from approval and uses explicit approval marker files
- `found_in_legacy`: `true`
- `file_paths`:
  - `docs/HUMAN-APPROVAL-BOUNDARY.md`
  - `approvals/approval-task-20260426-brief-readiness-check-execution.md`
  - `scripts/validate-approval-marker.py`
  - `scripts/agentos-human-gate.py`
- `short_evidence_summary`: approval is file-based, scope-bound, and validated before sensitive lifecycle steps
- `status`: `PRESENT`
- `candidate_classification`: `CANDIDATE_FOR_ADMISSION`
- `rationale`: strong fit with the current rule that human approval cannot be simulated
- `do_not_import`: `false`

### CAP-003
- `capability_id`: `CAP-003`
- `name`: `Active task lifecycle gating`
- `description`: legacy has controlled commands to activate a task and prepare completion without automatic lifecycle mutation
- `found_in_legacy`: `true`
- `file_paths`:
  - `tasks/active-task.md`
  - `scripts/activate-task.py`
  - `scripts/complete-active-task.py`
  - `scripts/apply-transition.py`
  - `tools/state/ACTIVATE-TASK.md`
  - `tools/completion/COMPLETE-ACTIVE-TASK.md`
- `short_evidence_summary`: activation, readiness, and completion are broken into separate guarded steps
- `status`: `PRESENT`
- `candidate_classification`: `CANDIDATE_FOR_ADMISSION`
- `rationale`: fits Stage 2 goals around task control and non-automatic transitions
- `do_not_import`: `false`

### CAP-004
- `capability_id`: `CAP-004`
- `name`: `Unified validation and evidence wrapper`
- `description`: legacy has a single validation entry command that groups many checks and keeps evidence semantics explicit
- `found_in_legacy`: `true`
- `file_paths`:
  - `scripts/agentos-validate.py`
  - `tools/validation/AGENTOS-VALIDATE.md`
  - `quality/MAIN.md`
  - `reports/`
- `short_evidence_summary`: validation is orchestrated centrally but still described as evidence, not approval
- `status`: `PRESENT`
- `candidate_classification`: `CANDIDATE_FOR_ADMISSION`
- `rationale`: useful as a candidate pattern for future evidence collection and verification
- `do_not_import`: `false`

### CAP-005
- `capability_id`: `CAP-005`
- `name`: `Spec and UX to task generation`
- `description`: legacy can turn approved spec or UX inputs into candidate task contracts
- `found_in_legacy`: `true`
- `file_paths`:
  - `scripts/generate-tasks-from-spec.py`
  - `scripts/generate-tasks-from-ux.py`
  - `scripts/generate-task-contract.py`
  - `tools/contract-validator/VALIDATE-CONTRACT-DRAFT.md`
  - `tasks/drafts/`
- `short_evidence_summary`: generators exist, but they create candidate contracts rather than active execution directly
- `status`: `PRESENT`
- `candidate_classification`: `CANDIDATE_FOR_DEFERRAL`
- `rationale`: promising, but broad and likely too early before Stage 2 classification rules are finalized
- `do_not_import`: `false`

### CAP-006
- `capability_id`: `CAP-006`
- `name`: `Manual queue and task health`
- `description`: legacy has a manual queue model and a small health report for briefs, reviews, traces, and queue gaps
- `found_in_legacy`: `true`
- `file_paths`:
  - `tasks/queue/QUEUE.md`
  - `tools/task-queue/MANAGE-QUEUE.md`
  - `scripts/task-health.py`
  - `tools/task-health/TASK-HEALTH.md`
- `short_evidence_summary`: queue selection stays manual and health reporting is read-only
- `status`: `PRESENT`
- `candidate_classification`: `CANDIDATE_FOR_DEFERRAL`
- `rationale`: useful, but secondary to core authority and lifecycle boundaries
- `do_not_import`: `false`

### CAP-007
- `capability_id`: `CAP-007`
- `name`: `Context selection and index layer`
- `description`: legacy has context indexing, selection, and generated context data for task-relevant retrieval
- `found_in_legacy`: `partial`
- `file_paths`:
  - `scripts/select-context.py`
  - `scripts/build-context-index.py`
  - `data/context-index.json`
  - `schemas/context-index.schema.json`
- `short_evidence_summary`: context tooling exists, but it introduces extra derived artifacts and larger context surfaces
- `status`: `PARTIAL`
- `candidate_classification`: `CANDIDATE_FOR_DEFERRAL`
- `rationale`: likely useful later, but it carries context-growth risk and should not be rushed into the new core
- `do_not_import`: `false`

### CAP-008
- `capability_id`: `CAP-008`
- `name`: `Execution readiness and session records`
- `description`: legacy can check whether task execution would be allowed and can create execution-session evidence records
- `found_in_legacy`: `true`
- `file_paths`:
  - `scripts/run-active-task.py`
  - `scripts/check-execution-readiness.py`
  - `tools/execution/RUN-ACTIVE-TASK.md`
  - `reports/execution/`
- `short_evidence_summary`: runner start is separated from actual implementation execution and writes session evidence
- `status`: `PRESENT`
- `candidate_classification`: `CANDIDATE_FOR_DEFERRAL`
- `rationale`: potentially useful, but close to execution and should remain behind later human checkpoints
- `do_not_import`: `false`

### CAP-009
- `capability_id`: `CAP-009`
- `name`: `Template preparation and physical materialization`
- `description`: legacy includes scripts and template trees that physically prepare clean templates and runtime directories
- `found_in_legacy`: `true`
- `file_paths`:
  - `scripts/prepare-clean-template.py`
  - `templates/agentos-minimal/`
  - `templates/agentos-full/`
  - `scripts/check-template-integrity.py`
- `short_evidence_summary`: the legacy system contains real file-materialization behavior for template preparation
- `status`: `PRESENT`
- `candidate_classification`: `CANDIDATE_FOR_REJECTION`
- `rationale`: current AOS source pack explicitly separates planning from physical skeleton creation
- `do_not_import`: `true`
- `do_not_import_reason`: `conflicts with AgentOS invariant`

### CAP-010
- `capability_id`: `CAP-010`
- `name`: `Memory-bank and project memory store`
- `description`: legacy keeps project memory, lessons, and handoff materials outside the canonical rule modules
- `found_in_legacy`: `true`
- `file_paths`:
  - `memory-bank/README.md`
  - `memory-bank/project-status.md`
  - `lessons/`
  - `handoff/`
  - `project/PROJECT.md`
- `short_evidence_summary`: a non-runtime memory layer exists, but it still increases the number of places humans must track
- `status`: `PRESENT`
- `candidate_classification`: `CANDIDATE_FOR_REJECTION`
- `rationale`: current architecture is highly sensitive to hidden authority and source-of-truth drift
- `do_not_import`: `true`
- `do_not_import_reason`: `creates new source of truth`

## 8. Source-of-Truth Impact Assessment

Assessed for `CANDIDATE_FOR_ADMISSION` items only.

| capability_id | would admitting this add a new source of truth | conflict with Архитектура.txt | conflict with Скелет архитектуры.txt | require changing active source pack |
| --- | --- | --- | --- | --- |
| `CAP-001` | no | no | no | yes |
| `CAP-002` | no | no | no | yes |
| `CAP-003` | no | no | no | yes |
| `CAP-004` | no | no | no | yes |

Assessment summary:
- none of the four admission candidates appears to require a second authority source by design
- all four would still need future re-expression in the new AOS documents before any use

## 9. Context-Growth Impact Assessment

| capability_id | context tokens impact | document sprawl risk | bootstrap context growth |
| --- | --- | --- | --- |
| `CAP-001` | low | low | low |
| `CAP-002` | low | low | low |
| `CAP-003` | medium | medium | low |
| `CAP-004` | medium | medium | low |
| `CAP-005` | medium | high | medium |
| `CAP-006` | medium | medium | low |
| `CAP-007` | high | high | high |
| `CAP-008` | medium | high | medium |
| `CAP-009` | medium | high | medium |
| `CAP-010` | high | high | high |

Summary:
- biggest context-growth risk comes from the context layer itself and from memory/project notes
- smallest growth risk comes from clear authority routing and explicit approval boundary patterns

## 10. Do-Not-Import Findings

Capabilities marked `do_not_import: true`:

### CAP-009 — Template preparation and physical materialization
- reason: `conflicts with AgentOS invariant`
- explanation: the current AOS source pack says skeleton planning is allowed, but physical creation needs separate approval later

### CAP-010 — Memory-bank and project memory store
- reason: `creates new source of truth`
- explanation: even when described as non-authoritative, this layer adds more places where meaning and status may drift

## 11. Parking Lot Relevance

| parking_lot_item | is_it_present_in_legacy | does_this_map_finding_change_priority | does_this_map_finding_change_admission_recommendation | notes |
| --- | --- | --- | --- | --- |
| `F-20 Git Context Controller / GCC` | no | no | no | no direct legacy implementation found |
| `F-21 Letta git-backed memory` | partial | no | no | legacy has `memory-bank/`, but no Letta-based implementation was found |
| `F-31 Adaptive compute / voting` | no | no | no | no concrete implementation found |
| `F-32 Hotswap small→large model` | no | no | no | no concrete implementation found |
| `F-33 Fine-tuning on AgentOS data` | no | no | no | no concrete implementation found |
| `F-34 Multi-agent debate` | partial | no | no | term appears as idea in legacy reports, not as mapped capability |
| `F-35 AgentOps Replay` | no | no | no | no concrete implementation found |
| `F-43 Cross-repo sync` | partial | no | no | term appears as scope idea only, not as implemented capability |

No parking lot item is admitted by this report.

## 12. Open Questions and Blockers

Blockers:
- none

Open questions:
- should `CAP-001` through `CAP-004` be reviewed first as the smallest, lowest-risk legacy candidates?
- should `CAP-007` context tooling be kept out of the near-term core because of context-growth risk?
- should `CAP-009` and `CAP-010` be rejected fully or only rejected as core defaults?
- does the human want Stage 2.2 to focus first on approval/lifecycle patterns or on validation orchestration?

## 13. Forbidden Actions Boundary

Confirmed:
- No capability admitted.
- No legacy file copied.
- No legacy content imported as authority.
- No large legacy implementation content reproduced.
- No write to legacy repository.
- No legacy checkout inside AOS-1.
- No source pack modified.
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

## 14. Human Decision Items

- `DECISION_2_1_A`: Review this capability map for completeness and accuracy.
- `DECISION_2_1_B`: For each `CANDIDATE_FOR_ADMISSION`: admit, defer, or reject.
- `DECISION_2_1_C`: For each `CANDIDATE_FOR_DEFERRAL`: confirm deferral or promote.
- `DECISION_2_1_D`: For each `CANDIDATE_FOR_REJECTION`: confirm rejection.
- `DECISION_2_1_E`: For each `UNKNOWN`: provide direction.
- `DECISION_2_1_F`: Review do-not-import findings and confirm.

## 15. Final Status

`TASK_2_1_MAP_READY_FOR_HUMAN_REVIEW`
