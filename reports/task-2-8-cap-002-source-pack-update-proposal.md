# Task 2.8 — CAP-002 Source-Pack Update Proposal

## 1. Task Metadata

```yaml
task_id: "2.8"
task_name: "CAP-002 Source-Pack Update Proposal"
stage: "Stage 2"
mode: "Source-pack update proposal / report-only"
repository: "NMF13579/AOS-1"
branch_required: "dev"
branch_observed: "dev"
capability_id: "CAP-002"
capability_name: "Human approval marker and approval boundary"
task_2_7_1_human_decisions_verified: true
task_2_7_2_evidence_repair_verified: true
source_pack_mutation_performed: false
human_approval_required_before_mutation: true
final_status: "TASK_2_8_SOURCE_PACK_UPDATE_PROPOSAL_CREATED"
```

## 2. Preconditions

- `git branch --show-current`: `dev`
- `reports/task-2-7-cap-002-decision-consolidation.md`: present
- `reports/task-2-7-1-cap-002-human-decisions.md`: present
- `reports/task-2-7-2-evidence-content-verification-repair.md`: present
- `Архитектура.txt`: present
- `Скелет архитектуры.txt`: present
- `TASK_2_7_1_HUMAN_DECISIONS_RECORDED`: confirmed
- `DECISION_2_7_A = ADMIT_FOR_SOURCE_PACK_UPDATE`: confirmed
- `DECISION_2_7_B = ARCHITECTURE_AND_SKELETON`: confirmed
- `DECISION_2_7_C = MAY_PREPARE_TASK_2_8`: confirmed
- `may_prepare_task_2_8: true`: confirmed
- `TASK_2_7_2_PATH_MISMATCH_CONTENT_VERIFIED`: confirmed

Precondition result: passed.

## 3. Task 2.7.1 Intake

Task 2.7.1 records human direction to:

- admit CAP-002 for source-pack update proposal preparation;
- cover both `Архитектура.txt` and `Скелет архитектуры.txt`;
- allow preparation of Task 2.8.

These decisions authorize proposal preparation only. They do not approve CAP-002 and do not authorize source-pack mutation.

## 4. Task 2.7.2 Evidence Repair Intake

- report: `reports/task-2-7-2-evidence-content-verification-repair.md`
- final status: `TASK_2_7_2_PATH_MISMATCH_CONTENT_VERIFIED`
- evidence content verified: `true`
- human-resolved canonical Task 2.4 path accepted: `true`

## 5. Source-Pack Reading Log

```yaml
source_pack_reading_log:
  architecture_txt:
    file_exists: true
    sections_read:
      - "## 5. Базовые инварианты AgentOS"
      - "## 16. Validation / Evidence / Approval"
    relevant_existing_invariants_found:
      - "PASS ≠ approval."
      - "Evidence ≠ approval."
      - "CI PASS ≠ approval."
      - "Human approval нельзя симулировать."
      - "Human approval is separate and higher than PASS/evidence/CI."
    selected_anchor: "§5.1 Human Approval Boundary, as a proposed subsection under ## 5. Базовые инварианты AgentOS"
    read_method: "grep of headings and approval terms; sed -n '1,120p'; sed -n '120,220p'; sed -n '540,610p'"

  skeleton_architecture_txt:
    file_exists: true
    sections_read:
      - "## 5. AgentOS directory groups"
      - "## 6. Роли групп"
    approvals_group_found: true
    selected_anchor: "§6.1 Human Approval Marker and Approval Boundary, as a proposed extension after the approvals/ role in ## 6. Роли групп"
    read_method: "grep of headings and approval terms; sed -n '1,140p'; sed -n '140,180p'"
```

## 6. CAP-002 Requirement Summary

CAP-002 is:

`Human approval marker and approval boundary`

CAP-002 protects against:

- agent-simulated approval;
- agent-inferred approval;
- agent-created approval marker;
- agent-modified approval marker;
- PASS treated as approval;
- evidence treated as approval;
- CI PASS treated as approval;
- completion review treated as approval;
- readiness treated as approval.

Human approval must be explicit, traceable, and outside ordinary agent self-claims.

Required boundaries:

- PASS ≠ approval.
- Evidence ≠ approval.
- CI PASS ≠ approval.
- Completion review ≠ approval.
- Readiness ≠ approval.
- Human approval cannot be simulated.
- Missing approval evidence must fail closed.
- Ambiguous approval evidence must fail closed.

## 7. Architecture Anchor Review

```yaml
architecture_anchor_candidates:
  option_1:
    anchor: "§5 / §5.1 Базовые инварианты"
    rationale: "CAP-002 is a governance invariant and approval boundary."
    recommended: true

  option_2:
    anchor: "§16 / §16.1 Validation / Evidence / Approval"
    rationale: "CAP-002 also affects validation/evidence mechanics."
    recommended: false
```

The existing section 5 already contains the non-equivalence rules for PASS, evidence, CI, decision records, and human approval. Section 16 explains how validation and evidence behave, but it is downstream of the core invariant.

```yaml
selected_architecture_anchor:
  candidate_id: CAP002_SPU_001
  target_file: "Архитектура.txt"
  selected_anchor: "§5.1 Human Approval Boundary"
  rejected_anchor: "§16.1"
  selection_reason: "Approval boundary is a core governance invariant, not only validation mechanics."
  status: PROPOSED_ONLY
```

## 8. Skeleton Anchor Review

The current skeleton already declares an `approvals/` group with the role `Human approval evidence` and the boundary `Human-owned boundary`. Extending that role in section 6 is structurally consistent.

```yaml
selected_skeleton_anchor:
  candidate_id: CAP002_SPU_002
  target_file: "Скелет архитектуры.txt"
  selected_anchor: "§6.1 Human Approval Marker and Approval Boundary"
  selection_reason: "Existing approvals-related structure is appropriate for Human Approval Marker and Approval Boundary Check."
  status: PROPOSED_ONLY
```

## 9. Source-Pack Update Candidate Register

```yaml
source_pack_update_candidates:
  CAP002_SPU_001:
    target_file: "Архитектура.txt"
    target_anchor: "§5.1 Human Approval Boundary"
    candidate_type: ARCHITECTURE_INVARIANT_UPDATE
    status: PROPOSED_ONLY
    source_pack_mutation_performed: false
    human_approval_required_before_mutation: true

  CAP002_SPU_002:
    target_file: "Скелет архитектуры.txt"
    target_anchor: "§6.1 Human Approval Marker and Approval Boundary"
    candidate_type: SKELETON_APPROVAL_STRUCTURE_UPDATE
    status: PROPOSED_ONLY
    source_pack_mutation_performed: false
    human_approval_required_before_mutation: true
```

## 10. Architecture Update Candidate

### Proposed Architecture Text

§5.1 Human Approval Boundary

Human Approval Boundary is a core governance invariant of AOS-1.

AOS-1 must treat human approval as an explicit, traceable, human-originated decision.

Agent-generated PASS is not approval.

Agent-generated evidence is not approval.

Agent-generated completion review is not approval.

CI PASS is not approval.

Readiness is not approval.

An agent must not create, modify, simulate, infer, backfill, or silently replace human approval.

If approval evidence is missing, ambiguous, contradictory, or agent-generated, the system must fail closed.

A human approval marker must be outside ordinary agent self-claims and must reference a traceable human decision record.

Machine-readable approval boundary metadata, if inserted, must use explicit fenced YAML block formatting, not 4-space indentation.

```yaml
human_approval_boundary:
  cap_002_approval_granted: false
  source_pack_mutation_authorized: false
  architecture_txt_mutation_authorized: false
  skeleton_txt_mutation_authorized: false
  human_approval_required_before_mutation: true
  agent_may_create_human_approval_marker: false
  agent_may_modify_human_approval_marker: false
  agent_may_infer_human_approval: false
```

The YAML block must not be inserted as 4-space indented text.

Boundary statements preserved by this candidate:

- PASS ≠ approval.
- Evidence ≠ approval.
- CI PASS ≠ approval.
- Completion review ≠ approval.
- Readiness ≠ approval.
- Human approval cannot be simulated.
- Missing approval evidence must fail closed.
- Ambiguous approval evidence must fail closed.

## 11. Skeleton Update Candidate

### Proposed Skeleton Text

§6.1 Human Approval Marker and Approval Boundary

Required structural elements:

- Human Approval Marker
- Approval Boundary Check
- Approval Evidence Reference
- Approval Pending State
- Approval Rejection / Deferral State
- Non-Simulation Rule
- Fail-Closed Missing Approval Rule
- Fail-Closed Ambiguous Approval Rule
- Forbidden Approval Claim Check

The approval boundary structure must ensure:

- agents cannot create human approval markers;
- agents cannot modify human approval markers;
- agents cannot infer human approval from PASS, evidence, CI, readiness, or completion review;
- missing approval evidence blocks mutation or lifecycle advancement;
- ambiguous approval evidence blocks mutation or lifecycle advancement.

Boundary statements preserved by this candidate:

- PASS ≠ approval.
- Evidence ≠ approval.
- CI PASS ≠ approval.
- Completion review ≠ approval.
- Readiness ≠ approval.
- Human approval cannot be simulated.
- Missing approval evidence must fail closed.
- Ambiguous approval evidence must fail closed.

## 12. Markdown Safety Review

```yaml
markdown_safety_review:
  nested_fenced_blocks_present: false
  machine_readable_yaml_uses_explicit_fenced_yaml_block: true
  yaml_inserted_as_4_space_indented_text: false
  proposed_text_safe_for_direct_insertion: true
  proposed_text_contains_required_boundaries: true
```

The architecture proposal is not wrapped in an outer fenced block. Its machine-readable metadata uses one explicit fenced YAML block, so no nested fence is created.

## 13. Human Approval Boundary

```yaml
human_approval_boundary:
  cap_002_approval_granted: false
  source_pack_mutation_authorized: false
  architecture_txt_mutation_authorized: false
  skeleton_txt_mutation_authorized: false
  task_2_8_1_started: false
  human_approval_required_before_mutation: true
  agent_may_create_human_approval_marker: false
  agent_may_modify_human_approval_marker: false
  agent_may_infer_human_approval: false
```

## 14. Downstream Use Rule

Future CAP-002 human review or mutation tasks must use `CAP002_SPU_001` and `CAP002_SPU_002` from Task 2.8.

Task 2.8 does not approve the proposed candidates.

Task 2.8 only prepares proposed candidates for human review.

## 15. Forbidden Claims Check

```yaml
forbidden_claims_check:
  cap_002_implemented: false
  cap_002_approved: false
  cap_002_execution_started: false
  cap_002_source_pack_mutation_performed: false
  cap_002_source_pack_mutation_authorized: false
  architecture_txt_modified: false
  skeleton_txt_modified: false
  task_2_8_1_started: false
  task_2_8_1_artifacts_created: false
  human_approval_simulated: false
  human_approval_marker_created_by_agent: false
  human_approval_marker_modified_by_agent: false
```

## 16. Validation

Validation requirements:

- both proposal candidates are present;
- architecture anchor is `§5.1 Human Approval Boundary`;
- skeleton anchor is `§6.1 Human Approval Marker and Approval Boundary`;
- all required approval boundaries are present;
- machine-readable YAML uses an explicit fenced YAML block;
- YAML is not represented as 4-space indented text;
- nested fenced blocks are absent;
- source-pack files remain unchanged.

## 17. Final Status

`TASK_2_8_SOURCE_PACK_UPDATE_PROPOSAL_CREATED`
