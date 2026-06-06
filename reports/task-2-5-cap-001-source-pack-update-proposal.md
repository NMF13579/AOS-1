# Task 2.5 — CAP-001 Source-Pack Update Proposal

## 1. Machine-Readable Summary

```yaml
task_id: "2.5"
task_name: "CAP-001 Source-Pack Update Proposal"
stage: "Stage 2"
mode: "read-only/source-pack-update-proposal/report-only"
report_path: "reports/task-2-5-cap-001-source-pack-update-proposal.md"

capability_in_scope: "CAP-001"

task_2_4_report_available: true
task_2_4_final_status: "TASK_2_4_SOURCE_PACK_IMPACT_REVIEW_READY_FOR_HUMAN_DECISION"
task_2_4_report_committed: true
task_2_4_commit_observed: "b4b163b"

task_2_4_1_report_available: true
task_2_4_1_final_status: "TASK_2_4_1_CAP_001_SOURCE_PACK_PLANNING_AUTHORIZED"
task_2_4_1_report_committed: true
task_2_4_1_commit_observed: "dfff865"

cap_001_source_pack_proposal_authorized_by_human: true
spu_001_proposal_authorized_by_human: true
spu_002_proposal_authorized_by_human: true

spu_candidates_in_scope:
  - "SPU-001"
  - "SPU-002"
spu_proposals_created: 2

only_cap_001_in_scope: true
only_spu_001_and_spu_002_in_scope: true

proposals_classified_minimal_conservative: true

source_pack_modified: false
source_pack_patch_created: false
source_pack_update_authorized_by_this_task: false

implementation_task_created: false
implementation_permission_created: false

legacy_repository_accessed: false
legacy_files_copied: false
legacy_content_imported: false

skeleton_materialized: false
validators_created: false
schemas_created: false
runtime_implemented: false
generated_indexes_created: false

files_staged: false
commit_created: false
push_performed: false

approval_created_by_agent: false
stage_2_execution_authorized: false
stage_2_started: false

approval_boundary_weakened: false
execution_boundary_weakened: false
new_source_of_truth_created: false
hidden_execution_enabled: false

open_human_decision_count: 3

final_status: "TASK_2_5_SOURCE_PACK_UPDATE_PROPOSAL_READY_FOR_HUMAN_DECISION"
```

## 2. Executive Summary

This report prepares proposal-only wording for `CAP-001` and only for two planned source-pack updates:
- `SPU-001`
- `SPU-002`

Nothing is applied here.
No project document is changed.
No implementation is authorized.

## 3. Preconditions Review

| report_path | present | final_status | evidence_status | observed_commit | notes |
| --- | --- | --- | --- | --- | --- |
| `reports/task-2-4-admitted-capability-source-pack-impact-review.md` | true | `TASK_2_4_SOURCE_PACK_IMPACT_REVIEW_READY_FOR_HUMAN_DECISION` | `committed` | `b4b163b` | confirms `CAP-001` impact review and lists `SPU-001`, `SPU-002` |
| `reports/task-2-4-1-cap-001-source-pack-planning-authorization.md` | true | `TASK_2_4_1_CAP_001_SOURCE_PACK_PLANNING_AUTHORIZED` | `committed` | `dfff865` | confirms proposal preparation only, not editing or execution |
| `reports/task-2-3-human-admission-decisions.md` | true | `TASK_2_3_HUMAN_DECISIONS_RECORDED` | `committed` | `b0a705c` | confirms `CAP-001` was admitted by the human |

Precondition confirmation:
- `CAP-001 source-pack proposal preparation authorized by human: true`
- `SPU-001 proposal preparation authorized by human: true`
- `SPU-002 proposal preparation authorized by human: true`
- `admitted capabilities processed as separate packages: true`
- `source-pack update authorized by Task 2.4.1: false`
- `Stage 2 execution authorized: false`

No `TASK_BLOCKER: CAP_001_SOURCE_PACK_PLANNING_NOT_AUTHORIZED` was triggered.

## 4. Repository State Review

- `repository_path`: `/Users/muhammednazyrov/Documents/GitHub/AOS-1`
- `current_branch`: `dev`
- `current_head_commit`: `dfff865068a23182d6df7386ecdeb72bf208c4c2`
- `latest_commits`:
  - `dfff865 — docs: record human authorization for CAP-001 source-pack planning (SPU-001, SPU-002)`
  - `b4b163b — docs: source-pack impact review for admitted capabilities CAP-001–004`
  - `b0a705c — docs: record human admission decisions for Stage 2 capabilities`
  - `4984ce7 — docs: add legacy capability admission review matrix`
  - `fab8da1 — docs: add legacy capability map`
  - `c1e273b — docs: add Stage 2 planning and authorization evidence`
- `git_status_short`: clean

No `TASK_BLOCKER: WRONG_BRANCH` was triggered.

## 5. CAP-001 Scope Confirmation

Confirmed:
- `CAP-001 is the only capability in scope.`
- `SPU-001 and SPU-002 are the only source-pack update proposals in scope.`
- `CAP-002 through CAP-010 are out of scope for this task.`

No `TASK_BLOCKER: OUT_OF_SCOPE_CAPABILITY_OR_SPU_INCLUDED` was triggered.

## 6. Active Source Pack — Current State Review

| file_name | read | relevant_excerpt_or_section | why_relevant_to_CAP_001 |
| --- | --- | --- | --- |
| `Архитектура.txt` | true | `llms.txt is bootstrap pointer. Registry maps. Pipeline routes. Resolver selects one next safe action.` | this is the closest current text that defines bootstrap, routing, and safe navigation meaning |
| `Архитектура.txt` | true | `Resolver returns one allowed next action and cannot execute commands...` | confirms routing must stay navigation-only and must not become hidden execution |
| `Скелет архитектуры.txt` | true | section `AgentOS directory groups` with `bootstrap/`, `registry/`, `pipelines/` | this is the closest current placement guidance for future structure |
| `Скелет архитектуры.txt` | true | group roles: `bootstrap/` = startup/preflight design, `registry/` = machine navigation registries, `pipelines/` = flow descriptions, not permission | gives the current meaning that the proposal must preserve |
| `Roadmap.txt` | true | Stage 2 purpose and forbidden actions | confirms this task stays proposal-only and not implementation |
| `Адреса проектов.txt` | true | legacy is `reference_only` | supports boundary that no legacy import is created here |
| `06_Stage_1_Source_Pack_Intake_and_Admission_Gate.txt` | true | feature admission needs evidence and must not silently admit | supports conservative proposal behavior |
| `08_Future_Feature_Candidates_Parking_Lot.txt` | true | parking lot is not implementation permission | supports narrow scope and no expansion beyond `CAP-001` |

## 7. SPU-001 Proposal — Архитектура.txt Clarification

### Current text

Nearest current lines from `Архитектура.txt`:

```text
llms.txt is bootstrap pointer.
Registry maps.
Pipeline routes.
Resolver selects one next safe action.
```

And the current boundary also says:

```text
Resolver returns one allowed next action and cannot execute commands, mutate files, create approval, complete task or start next stage.
```

### Proposed addition

PROPOSAL ONLY — NOT APPLIED

```text
Bootstrap route meaning:

Bootstrap only points the agent to the governed entry path and the current authority surfaces.
Registry only maps declared surfaces and does not grant approval, implementation permission or execution permission.
Pipeline only describes bounded route options and does not start execution by itself.
Resolver only selects one allowed next safe action and does not execute that action.

Therefore canonical bootstrap and routing are navigation and authority-orientation only.
They do not create approval.
They do not start execution.
They do not create implementation permission.
They do not bypass human checkpoints.
```

### Placement proposal

Target placement: `Архитектура.txt`, near `## 4. Главная формула` and the existing `Contract / Registry / State / Resolver / Pipeline` boundary section.

### Classification

- `type`: `clarification`
- `scope`: `minimal`
- `risk`: `medium`
- `breaks_existing_rules`: `false`
- `creates_new_source_of_truth`: `false`
- `weakens_approval_boundary`: `false`
- `weakens_execution_boundary`: `false`
- `enables_hidden_execution`: `false`
- `source_pack_update_authorized_now`: `false`
- `human_decision_required_before_apply`: `true`

## 8. SPU-002 Proposal — Скелет архитектуры.txt Alignment

### Current text

Nearest current lines from `Скелет архитектуры.txt`:

```text
agentos/
  architecture/
  bootstrap/
  governance/
  contracts/
  registry/
  state/
  pipelines/
```

And current role definitions:

```text
bootstrap/  | Startup/preflight design | Не execution без реализации
registry/   | Machine navigation registries | Не выше Markdown/YAML source
pipelines/  | Описания потоков | Не permission
```

### Proposed addition

PROPOSAL ONLY — NOT APPLIED

```text
Bootstrap / registry / pipeline alignment for canonical routing:

- bootstrap/ is the future home of startup orientation and preflight entry guidance only.
- registry/ is the future home of declared navigation maps only.
- pipelines/ is the future home of bounded route descriptions only.

These three groups may work together to orient the agent toward one safe next step, but this remains conceptual alignment only until separately implemented and approved.

This alignment does not authorize physical skeleton materialization.
This alignment does not authorize file creation.
This alignment does not authorize directory creation.
This alignment does not authorize execution, approval, or implementation.
```

### Placement proposal

Target placement: `Скелет архитектуры.txt`, near `## 5. AgentOS directory groups` and `## 6. Роли групп`.

### Classification

- `type`: `skeleton_alignment`
- `scope`: `minimal`
- `risk`: `medium`
- `breaks_existing_rules`: `false`
- `creates_new_source_of_truth`: `false`
- `weakens_approval_boundary`: `false`
- `weakens_execution_boundary`: `false`
- `enables_hidden_execution`: `false`
- `source_pack_update_authorized_now`: `false`
- `human_decision_required_before_apply`: `true`

## 9. Boundary Safety Review

For both proposals:

| proposal | approval_boundary_weakened | execution_boundary_weakened | implementation_permission_created | stage_2_execution_authorized | hidden_execution_enabled |
| --- | --- | --- | --- | --- | --- |
| `SPU-001` | false | false | false | false | false |
| `SPU-002` | false | false | false | false | false |

Reason:
- both proposals make the current safety border more explicit, not weaker
- both proposals say navigation only, not execution
- neither proposal creates permission by itself

## 10. Source-of-Truth Safety Review

For both proposals:

| proposal | new_source_of_truth_created | existing_source_pack_authority_preserved | architecture_priority_preserved | skeleton_architecture_remains_guidance_until_applied | proposal_is_not_applied_change |
| --- | --- | --- | --- | --- | --- |
| `SPU-001` | false | true | true | true | true |
| `SPU-002` | false | true | true | true | true |

Reason:
- `SPU-001` only clarifies an existing meaning already implied by the architecture
- `SPU-002` only aligns placement guidance already implied by the skeleton
- neither proposal introduces a second authority document or a hidden rule source

## 11. Forbidden Actions Boundary

Confirmed:
- No source pack modified.
- No source-pack patch created.
- No source-pack update authorized by this task.
- No implementation task created.
- No implementation permission created.
- No CAP-001 implementation performed.
- No legacy repository accessed.
- No legacy files copied.
- No legacy content imported.
- No skeleton materialized.
- No validators created.
- No schemas created.
- No runtime implemented.
- No generated indexes created.
- No files staged.
- No commit created.
- No push performed.
- No approval created by agent.
- No Stage 2 execution authorized.
- No Stage 2 started.

## 12. Human Decision Items

- `DECISION_2_5_A`: Approve, reject, or revise `SPU-001` proposed clarification for `Архитектура.txt`.
- `DECISION_2_5_B`: Approve, reject, or revise `SPU-002` proposed alignment for `Скелет архитектуры.txt`.
- `DECISION_2_5_C`: If both are approved, authorize or reject preparation of Task 2.6 to apply these edits to source pack files.

## 13. Proposed Next-Step Options

- Human may review Task 2.5 proposal.
- Human may approve `SPU-001`.
- Human may approve `SPU-002`.
- Human may reject or revise either proposal.
- A later Task 2.6 may apply approved edits only if explicitly authorized by human.

## 14. Final Status

`TASK_2_5_SOURCE_PACK_UPDATE_PROPOSAL_READY_FOR_HUMAN_DECISION`
