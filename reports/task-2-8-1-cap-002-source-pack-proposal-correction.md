# Task 2.8.1 — CAP-002 Source-Pack Proposal Correction

## 1. Task Metadata

```yaml
task_id: "2.8.1"
task_name: "CAP-002 Source-Pack Proposal Correction"
stage: "Stage 2"
mode: "Corrective proposal refinement / report-only"
repository: "NMF13579/AOS-1"
branch_required: "dev"
branch_observed: "dev"
task_2_7_2_evidence_repair_verified: true
task_2_8_proposal_available: true
task_2_8_proposal_committed: true
source_pack_mutation_performed: false
human_approval_required_before_mutation: true
final_status: "TASK_2_8_1_PROPOSAL_CORRECTION_CREATED"
```

## 2. Preconditions

- `git branch --show-current`: `dev`
- `git status --short` before task work: clean
- `reports/task-2-7-2-evidence-content-verification-repair.md`: present
- `TASK_2_7_2_PATH_MISMATCH_CONTENT_VERIFIED`: confirmed
- `reports/task-2-8-cap-002-source-pack-update-proposal.md`: present and committed
- `CAP002_SPU_001`: found
- `CAP002_SPU_002`: found
- `Архитектура.txt`: present
- `Скелет архитектуры.txt`: present

Precondition result: passed.

## 3. Task 2.7.2 Intake

- report: `reports/task-2-7-2-evidence-content-verification-repair.md`
- final status: `TASK_2_7_2_PATH_MISMATCH_CONTENT_VERIFIED`
- evidence repair verified: `true`

The evidence base is sufficient for corrective proposal review.

## 4. Task 2.8 Proposal Intake

- report: `reports/task-2-8-cap-002-source-pack-update-proposal.md`
- committed: `true`
- `CAP002_SPU_001`: read
- `CAP002_SPU_002`: read
- original architecture anchor: `§5.1 Human Approval Boundary`
- original skeleton anchor: `§6.1 Human Approval Marker and Approval Boundary`
- original proposal mutation performed: `false`

The corrective review preserves the valid anchor direction and replaces the original candidate identifiers with corrected identifiers for downstream use.

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
    selected_anchor: "§5.1 Human Approval Boundary, proposed under ## 5. Базовые инварианты AgentOS"
    read_method: "grep of approval terms and headings; sed -n '120,220p'; sed -n '540,610p'"

  skeleton_architecture_txt:
    file_exists: true
    sections_read:
      - "## 5. AgentOS directory groups"
      - "## 6. Роли групп"
    approvals_group_found: true
    selected_anchor: "§6.1 Human Approval Marker and Approval Boundary, proposed after the approvals/ role in ## 6. Роли групп"
    read_method: "grep of approval terms and headings; sed -n '96,180p'"
```

## 6. Architecture Anchor Re-Evaluation

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

Section 5 is the stronger anchor because it already defines the non-equivalence of PASS, evidence, CI results, decision records, and human approval. Section 16 explains validation mechanics but does not outrank the core invariant.

```yaml
corrected_architecture_anchor:
  candidate_id: CAP002_SPU_001_CORRECTED
  target_file: "Архитектура.txt"
  preferred_anchor: "§5.1 Human Approval Boundary"
  previous_anchor: "§5.1 Human Approval Boundary"
  rejected_alternative_anchor: "§16.1"
  correction_reason: "Approval boundary is a core governance invariant, not only validation mechanics. The Task 2.8 anchor direction is confirmed and carried forward under a corrected candidate identifier."
  status: PROPOSED_ONLY
```

## 7. Skeleton Anchor Re-Evaluation

The source content supports the existing skeleton direction:

- `approvals/` already exists in the target directory groups;
- its role is `Human approval evidence`;
- its boundary is `Human-owned boundary`.

```yaml
corrected_skeleton_anchor:
  candidate_id: CAP002_SPU_002_CORRECTED
  target_file: "Скелет архитектуры.txt"
  preferred_anchor: "§6.1 Human Approval Marker and Approval Boundary"
  previous_anchor: "§6.1 Human Approval Marker and Approval Boundary"
  correction_reason: "Existing approvals group is structurally appropriate for Human Approval Marker and Approval Boundary Check."
  status: PROPOSED_ONLY
```

## 8. Corrected Source-Pack Update Candidates

```yaml
corrected_source_pack_update_candidates:
  CAP002_SPU_001_CORRECTED:
    replaces_candidate: CAP002_SPU_001
    target_file: "Архитектура.txt"
    target_anchor: "§5.1 Human Approval Boundary"
    candidate_type: ARCHITECTURE_INVARIANT_UPDATE
    status: PROPOSED_ONLY
    source_pack_mutation_performed: false
    human_approval_required_before_mutation: true

  CAP002_SPU_002_CORRECTED:
    replaces_candidate: CAP002_SPU_002
    target_file: "Скелет архитектуры.txt"
    target_anchor: "§6.1 Human Approval Marker and Approval Boundary"
    candidate_type: SKELETON_APPROVAL_STRUCTURE_UPDATE
    status: PROPOSED_ONLY
    source_pack_mutation_performed: false
    human_approval_required_before_mutation: true
```

## 9. Corrected Architecture Proposed Text

### Corrected Architecture Proposed Text

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

Required boundaries preserved:

- PASS ≠ approval.
- Evidence ≠ approval.
- CI PASS ≠ approval.
- Completion review ≠ approval.
- Readiness ≠ approval.
- Human approval cannot be simulated.
- Missing approval evidence must fail closed.
- Ambiguous approval evidence must fail closed.

## 10. Corrected Skeleton Proposed Text

### Corrected Skeleton Proposed Text

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

Required boundaries preserved:

- PASS ≠ approval.
- Evidence ≠ approval.
- CI PASS ≠ approval.
- Completion review ≠ approval.
- Readiness ≠ approval.
- Human approval cannot be simulated.
- Missing approval evidence must fail closed.
- Ambiguous approval evidence must fail closed.

## 11. Markdown Safety Review

```yaml
markdown_safety_review:
  nested_fenced_blocks_present: false
  machine_readable_yaml_uses_explicit_fenced_yaml_block: true
  yaml_inserted_as_4_space_indented_text: false
  proposed_text_safe_for_direct_insertion: true
  proposed_text_contains_required_boundaries: true
```

The proposed architecture insertion is not enclosed in an outer fenced block. The machine-readable metadata uses one explicit fenced YAML block, so the report contains no nested fenced-block risk.

## 12. Human Approval Boundary

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

## 13. Downstream Use Rule

Future CAP-002 source-pack approval or mutation tasks must use `CAP002_SPU_001_CORRECTED` and `CAP002_SPU_002_CORRECTED`, not the original uncorrected `CAP002_SPU_001` and `CAP002_SPU_002` from Task 2.8.

Task 2.8.1 does not approve the corrected candidates.

Task 2.8.1 only prepares corrected candidates for human review.

## 14. Forbidden Claims Check

```yaml
forbidden_claims_check:
  cap_002_implemented: false
  cap_002_approved: false
  cap_002_execution_started: false
  source_pack_mutation_performed: false
  source_pack_mutation_authorized: false
  architecture_txt_modified: false
  skeleton_txt_modified: false
  task_2_8_2_started: false
  human_approval_simulated: false
  human_approval_marker_created_by_agent: false
  human_approval_marker_modified_by_agent: false
```

## 15. Validation

Validation requirements:

- both corrected candidate identifiers are present;
- architecture anchor is `§5.1 Human Approval Boundary`;
- skeleton anchor is `§6.1 Human Approval Marker and Approval Boundary`;
- approval non-equivalence and fail-closed boundaries are present;
- machine-readable YAML uses an explicit fenced YAML block;
- YAML is not represented as 4-space indented text;
- nested fenced blocks are absent;
- source-pack files remain unchanged.

## 16. Final Status

`TASK_2_8_1_PROPOSAL_CORRECTION_CREATED`
