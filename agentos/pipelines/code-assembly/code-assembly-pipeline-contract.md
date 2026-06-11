# Code Assembly Pipeline Contract

**Pipeline ID:** `code-assembly`
**Contract Version:** 1.0.0
**Status:** `DRAFT — PENDING_TASK_4_2_REVIEW`
**Branch:** `build/assembly-first`
**Created by Task:** 4.1 — Code Assembly Pipeline Contract
**Human Authorization:** Build Step 4 / Task 4.1 — granted 2026-06-11
**Write Mode:** `create_new`

---

## 1. Purpose

The Code Assembly Pipeline defines the authorized sequence of steps by which agent-executable code artifacts are assembled, validated, and prepared for human review prior to any merge, release, or runtime activation.

This contract specifies:
- Pipeline identity, scope, and boundary
- Authorized input and output artifacts
- Step definitions and sequencing
- Gate conditions and failure semantics
- Safety invariants applicable to this pipeline
- What this pipeline does NOT do

---

## 2. Scope and Boundary

### 2.1 In Scope

| Item | Notes |
|------|-------|
| Assembly of code artifacts from approved skeleton and architecture sources | Skeleton ≠ implementation; assembly populates structure with governed content |
| Per-step validation gates | Each step must pass its gate before the next step is permitted |
| Artifact state tracking | Input SHA, output SHA, and status are recorded per step |
| Failure-closed behavior on gate failures | Any gate failure halts the pipeline; no continuation |
| Human checkpoint emission | Pipeline emits a checkpoint report before protected or canonical writes |

### 2.2 Out of Scope

| Item | Reason |
|------|--------|
| Test execution | Not permitted in Build Step 4; reserved for later Build Steps |
| Runtime execution | Forbidden; no code is run during assembly |
| Validator implementation | Reserved for Governance / Control Module |
| Merge, commit, push, release | Forbidden; all lifecycle mutations require separate human decision |
| Writes to `dev` branch | Explicitly forbidden in Task 4.1 authorization |
| Writes to `agentos/contracts/` | Not an authorized write target for this pipeline |
| Modifications to 00/01/02 control files | Protected; require separate human checkpoint |
| Modifications to architecture or skeleton artifacts | Protected; require separate human checkpoint |
| Modifications to Minimal Safety Floor or failure semantics | Protected; require separate human checkpoint |
| Modifications to Documentation Assembly Pipeline | Protected; require separate human checkpoint |
| Product code changes | Out of scope for contract artifact |
| Build Step 5 | Not authorized |
| Scope expansion | Any scope expansion requires new human authorization |

---

## 3. Safety Invariants

All AOS-1 core invariants apply without exception:

```
PASS ≠ approval
Evidence ≠ approval
CI PASS ≠ approval
UNKNOWN ≠ OK
NOT_RUN ≠ PASS
Human approval cannot be simulated
Skeleton ≠ implementation
Protected/canonical changes require human checkpoint
Destructive operations are forbidden by default
Agent may propose Risk Profile, but must not self-assign LOW_RISK_FAST
```

These invariants are non-negotiable and cannot be overridden by any pipeline step, gate result, or agent decision.

---

## 4. Authorized Source References

The following artifacts are the canonical input references for code assembly:

| Artifact | Path | Role |
|----------|------|------|
| Assembly Pipelines and Build Roadmap | `agentos/01_AOS_Assembly_Pipelines_and_Build_Roadmap.md` | Build sequence authority |
| Core Control | `agentos/00_AOS_Core_Control.md` | Governance authority (read-only reference) |
| Governance Control Module | `agentos/02_AOS_Governance_Control_Module_and_Safety_Rules.md` | Safety rules (read-only reference) |
| Minimal Safety Floor | `agentos/safety/minimal-safety-floor.md` | Safety floor constraints |
| Failure Semantics | `agentos/safety/failure-semantics.md` | Failure classification rules |
| Documentation Assembly Pipeline Contract | `agentos/pipelines/documentation-assembly/` | Structural precedent |

All source references are **read-only** within this pipeline. No write operations are permitted against these artifacts.

---

## 5. Pipeline Steps

### Step Overview

```
[GATE: Pre-Assembly Verification]
        ↓
  Step 1: Source Intake and Lock
        ↓
  [GATE: Source Lock Gate]
        ↓
  Step 2: Skeleton Expansion
        ↓
  [GATE: Expansion Integrity Gate]
        ↓
  Step 3: Content Population
        ↓
  [GATE: Content Completeness Gate]
        ↓
  Step 4: Safety Alignment Check
        ↓
  [GATE: Safety Alignment Gate]
        ↓
  Step 5: Human Checkpoint Emission
        ↓
  [HUMAN DECISION REQUIRED — pipeline halts here]
```

---

### Step 1: Source Intake and Lock

**Purpose:** Verify that all authorized source artifacts exist on the correct branch, record their SHAs, and lock them as the assembly baseline.

**Inputs:**
- Authorized source references (§4)
- Target branch: `build/assembly-first`

**Actions:**
- Read and record SHA for each source reference
- Verify no protected artifact has been modified since last human checkpoint
- Record pre-assembly repository state snapshot

**Outputs:**
- `source-intake-lock.yaml` — SHA registry of all source artifacts at assembly time

**Gate: Source Lock Gate**
- All source SHAs must be recorded
- No UNKNOWN source states permitted
- Any missing artifact → `PIPELINE_BLOCKED`

---

### Step 2: Skeleton Expansion

**Purpose:** Expand approved skeleton files into the target assembly structure. Skeleton provides shape; this step validates the shape is consistent with the architecture and roadmap.

**Inputs:**
- Skeleton artifacts (from `build/assembly-first`, confirmed present)
- Architecture artifacts (read-only)

**Actions:**
- Map skeleton paths to their corresponding assembly target paths
- Verify no skeleton path conflicts with protected/canonical boundaries
- Record expansion map

**Outputs:**
- `skeleton-expansion-map.yaml` — mapping of skeleton source → assembly target paths

**Gate: Expansion Integrity Gate**
- All skeleton paths must resolve to non-protected targets
- No overlap with forbidden write paths
- Structural consistency with architecture confirmed
- Any conflict → `PIPELINE_BLOCKED`

---

### Step 3: Content Population

**Purpose:** Populate assembly target files with content derived from authorized sources. Content must be traceable to a source reference.

**Inputs:**
- Skeleton expansion map (Step 2 output)
- Authorized source references (§4)

**Actions:**
- For each expansion target: derive content from source references
- Record source traceability for each populated field
- No content may be generated without a traceable source

**Outputs:**
- Populated assembly artifacts at target paths
- `content-population-manifest.yaml` — per-artifact source traceability record

**Gate: Content Completeness Gate**
- All target paths in expansion map must be populated
- No placeholder content permitted (`TODO`, `TBD`, `PLACEHOLDER`)
- Source traceability recorded for every artifact
- Any gap → `PIPELINE_BLOCKED`

---

### Step 4: Safety Alignment Check

**Purpose:** Verify that all populated artifacts comply with the Minimal Safety Floor and Failure Semantics rules. No assembled artifact may violate a safety invariant.

**Inputs:**
- Populated assembly artifacts (Step 3 outputs)
- `agentos/safety/minimal-safety-floor.md`
- `agentos/safety/failure-semantics.md`

**Actions:**
- Check each artifact against Minimal Safety Floor constraints
- Verify failure modes are classified per failure semantics
- Record alignment status per artifact

**Outputs:**
- `safety-alignment-report.yaml` — per-artifact safety alignment status

**Gate: Safety Alignment Gate**
- All artifacts must be `ALIGNED`
- Any `MISALIGNED` or `UNKNOWN` status → `PIPELINE_BLOCKED`
- No override of safety invariants permitted

---

### Step 5: Human Checkpoint Emission

**Purpose:** Emit a structured human review package containing all pipeline outputs, gate results, and a complete diff of proposed changes. **The pipeline halts here.** No writes to any protected or canonical path may occur without a new human authorization.

**Inputs:**
- All Step 1–4 outputs and gate results
- Pre-assembly repository state (Step 1)

**Actions:**
- Generate human checkpoint package
- Record `may_proceed_to_write: PENDING_HUMAN_DECISION`
- Pipeline status: `AWAITING_HUMAN_AUTHORIZATION`

**Outputs:**
- Human checkpoint report in `reports/human-checkpoints/`

**Gate: Human Decision Required**
- This gate cannot be passed by the pipeline
- Only explicit human authorization may unlock the next phase
- `PENDING_HUMAN_DECISION ≠ PASS`

---

## 6. Artifact Registry

| Artifact | Path | Write Mode | Step |
|----------|------|-----------|------|
| Source Intake Lock | `agentos/pipelines/code-assembly/source-intake-lock.yaml` | create_new | 1 |
| Skeleton Expansion Map | `agentos/pipelines/code-assembly/skeleton-expansion-map.yaml` | create_new | 2 |
| Content Population Manifest | `agentos/pipelines/code-assembly/content-population-manifest.yaml` | create_new | 3 |
| Safety Alignment Report | `agentos/pipelines/code-assembly/safety-alignment-report.yaml` | create_new | 4 |
| Human Checkpoint Report | `reports/human-checkpoints/build-step-4-code-assembly-human-checkpoint.md` | create_new | 5 |

All artifacts listed above require their own per-step human authorization before write. The contract itself (this file) does not authorize any step execution.

---

## 7. Failure Semantics

All failures in this pipeline are **fail-closed**:

| Condition | Status | Action |
|-----------|--------|--------|
| Any gate fails | `PIPELINE_BLOCKED` | Halt; emit blocker report; await human decision |
| Any UNKNOWN present | `PIPELINE_BLOCKED` | UNKNOWN ≠ OK; halt immediately |
| Any NOT_RUN gate at checkpoint | `PIPELINE_BLOCKED` | NOT_RUN ≠ PASS |
| Source SHA mismatch | `PIPELINE_BLOCKED` | Halt; do not proceed |
| Safety misalignment | `PIPELINE_BLOCKED` | Halt; do not proceed |
| Scope expansion attempt | `PIPELINE_BLOCKED` | Scope expansion requires new human authorization |
| Forbidden write attempt | `PIPELINE_BLOCKED` | Abort; record forbidden write attempt |

---

## 8. Risk Profile

**Proposed Risk Profile:** `MEDIUM` — new directory and contract file creation on feature branch; no protected artifacts modified; no runtime execution; no merge.

**Note:** Agent proposes this Risk Profile. Human must confirm or reassign. Agent must not self-assign `LOW_RISK_FAST`.

---

## 9. What This Contract Does NOT Authorize

This contract document is a specification. It does NOT:

- Authorize execution of any pipeline step
- Authorize any write beyond this contract file itself
- Authorize Task 4.2, Task 4.3, or Build Step 5
- Constitute approval of any artifact
- Simulate human decision for any gate
- Override any AOS-1 safety invariant

Each pipeline step requires its own per-step human authorization before execution.

---

## 10. Changelog

| Version | Date | Change | Authorized by |
|---------|------|--------|---------------|
| 1.0.0 | 2026-06-11 | Initial creation — Task 4.1 | Human — Build Step 4 Task 4.1 authorization |
