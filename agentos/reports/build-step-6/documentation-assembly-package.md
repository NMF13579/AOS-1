# Documentation Assembly Package: CANDIDATE-1-GITIGNORE

## Package Control
- **Trial ID**: `TRIAL-BS6-DOGFOOD-1`
- **Candidate ID**: `CANDIDATE-1-GITIGNORE`
- **Candidate Title**: Add Python coverage exclusions to .gitignore
- **Repository**: `NMF13579/AOS-1`
- **Branch/Commit**: `build/assembly-first`
- **Baseline Commit**: `defecbf69be7d025867002e68c846eea66e5e220`
- **Task 6.2 Reference**: FINAL_RESPONSE_ONLY (Template Source Decision)
- **Task 6.3 Reference**: FINAL_RESPONSE_ONLY (Candidate Admission)
- **Task 6.4 Reference**: FINAL_RESPONSE_ONLY (Human Selection)
- **Assigned Candidate Risk Profile**: `MEDIUM_RISK_GUIDED`
- **Risk Profile Assignment Reference**: Task 6.4 Explicit Human Prompt ("MEDIUM_RISK_GUIDED")
- **Authorized Template Sources**: Verified against branch `build/assembly-first` (commit: `defecbf69be7d025867002e68c846eea66e5e220`)
- **Code Assembly Contract Reference**: `agentos/pipelines/code-assembly/code-assembly-pipeline-contract.md` (SHA-256: `91dd76e5ce92678cfe2109fec254aa824ce63d8ea4b6c393fa80fd4927089f40`)
- **Package Status**: `DRAFT`
- **Code Execution Authorized**: `false`
- **Human Review Required**: `true`
- **Warnings Do Not Authorize Execution**: `true`

---

## 1. Idea
- **Observed Problem**: `.gitignore` lacks entries for Python test coverage artifacts (`.coverage`, `htmlcov/`), causing them to clutter git status during local testing.
- **Proposed Minimal Change**: Add `.coverage` and `htmlcov/` to the root `.gitignore`.
- **Expected Value**: Cleaner working tree after running tests, preventing accidental commits of coverage artifacts.
- **Source Evidence Reference**: Identified in Task 6.3 Repository Candidate Search.

---

## 2. Project Brief
- **Problem**: Python test coverage artifacts are currently untracked instead of ignored.
- **User or Stakeholder**: Developers / Agents running local Python tests.
- **Goal**: Ensure that git ignores `.coverage` and `htmlcov/`.
- **Expected Value**: Clean git status post-test execution.
- **Scope**: Modifications restricted strictly to `.gitignore`.
- **Constraints**: 
  - Must not alter any other ignore rules.
  - Must only add standard coverage paths.
- **Non-Goals**: 
  - Restructuring the entire `.gitignore`.
  - Adding ignore rules for other languages or tools.
- **Known Risks**: None identified.
- **Unknowns**: None.
- **Success Criteria**: 
  - `.coverage` and `htmlcov/` are explicitly listed in `.gitignore`.
  - The syntax is valid.
- **Source References**: Task 6.3 Candidate ID `CANDIDATE-1-GITIGNORE`.
- **Human Review Boundary**: This Brief does not permit execution. Task 6.6 Human Review is required.

---

## 3. Specification
- **Current Behavior**: Coverage artifacts (`.coverage`, `htmlcov/`) are not ignored.
- **Expected Behavior**: Coverage artifacts are ignored by git.
- **Functional Requirements**:
  1. `.gitignore` must include `.coverage`.
  2. `.gitignore` must include `htmlcov/`.
- **Non-Functional Constraints**: The file's existing format and order should be largely preserved, adding the new rules either at the end or in an appropriate section.
- **Inputs**: None.
- **Outputs**: Updated `.gitignore` file.
- **Edge Cases**: None.
- **Failure Behavior**: Fail-closed (do not change other git settings).
- **Acceptance Criteria**: `git status` does not show untracked `.coverage` or `htmlcov/` files when they exist.
- **Validation Requirements**: Manual verification or deterministic dry-run of git status.
- **Evidence Requirements**: Provide diff of `.gitignore`.
- **Unknowns**: None.
- **Human Review Boundary**: This Specification does not authorize execution.

---

## 4. Task Brief
- **Task ID and Name**: `TASK-DOGFOOD-1`: Update `.gitignore` for Python Coverage
- **Mode**: `SAFE_TASK_EXECUTION`
- **Repository**: `NMF13579/AOS-1`
- **Branch**: `build/assembly-first`
- **Context**: First dogfood execution under Assembly MVP.
- **Goal**: Add `.coverage` and `htmlcov/` to `.gitignore`.
- **Scope**: `.gitignore` only.
- **Allowed Changes**: Appending or inserting `.coverage` and `htmlcov/` into `.gitignore`.
- **Forbidden Changes**: Modifying other files, removing existing ignore rules.
- **Required Behavior**: Produce a valid `.gitignore`.
- **Non-Goals**: Reorganizing the entire file.
- **Validation**: Read-only validation by checking file contents.
- **Evidence Requirements**: A clear diff showing the added lines.
- **Expected Final Report**: An Execution Report showing the successful change.
- **Stop Conditions**: 
  - If `.gitignore` does not exist or is protected.
  - If any changes outside `.gitignore` are requested.
- **Final Boundary Rule**: Do not commit, push, merge, or release.

### Authorization Block
```yaml
human_authorization:
  authorized_by: project_owner
  authorization_source: "Task 6.4 Human Decision"
  authorized_task_id: "TASK-DOGFOOD-1"
  authorized_scope: ".gitignore only"

  assigned_risk_profile: "MEDIUM_RISK_GUIDED"
  risk_profile_assigned_by_human: false

  task_execution_authorized: false
  protected_canonical_changes_authorized: false
  destructive_operations_authorized: false
  scope_expansion_authorized: false

  commit_authorized: false
  push_authorized: false
  merge_authorized: false
  release_authorized: false

  result_approved_in_advance: false
  next_task_authorized: false
```

---

## 5. Execution Package
```yaml
execution_package:
  trial_id: "TRIAL-BS6-DOGFOOD-1"
  candidate_id: "CANDIDATE-1-GITIGNORE"

  task_brief_reference: "Inline Task Brief in this Package"
  task_brief_sha256: "To be calculated post-extraction if detached"

  code_assembly_contract_path: "agentos/pipelines/code-assembly/code-assembly-pipeline-contract.md"
  code_assembly_contract_commit: "defecbf69be7d025867002e68c846eea66e5e220"
  code_assembly_contract_sha256: "91dd76e5ce92678cfe2109fec254aa824ce63d8ea4b6c393fa80fd4927089f40"

  repository: "NMF13579/AOS-1"
  authorized_branch_or_commit: "build/assembly-first"

  authorized_paths:
    - ".gitignore"
  forbidden_paths:
    - "agentos/pipelines/**"
    - "agentos/approvals/**"
    - "agentos/reports/**"
    - "agentos/code-assembly/**"

  expected_behavior: "The .coverage file and htmlcov/ directory are ignored by git."
  validation_commands: "git status"
  manual_validation: "Visual inspection of .gitignore."
  evidence_requirements: "Provide file diff."
  stop_conditions: "If any path other than .gitignore is modified."

  code_execution_authorized: false
  execution_authorization_reference: ""
```

---

## 6. Cross-Document Consistency
All sections of this package enforce the strictly bounded `.gitignore` scope. The Risk Profile is uniformly `MEDIUM_RISK_GUIDED`. Execution permissions are universally `false`.

---

## 7. Warnings and Unknowns
- **Warning**: `T6.1-W1` (Origin: Task 6.2)
  - **Source**: Task 6.2
  - **Status**: OPEN
  - **Resolution Evidence**: None
  - **Package Impact**: None. (Earlier artifacts do not overlap with candidate paths).
  - **Blocks Task 6.6**: false
- **Warning**: `T6.1-W2` (Origin: Task 6.2)
  - **Source**: Task 6.2
  - **Status**: OPEN
  - **Resolution Evidence**: None
  - **Package Impact**: None. (Execution Package formulation explicitly bound to the contract version).
  - **Blocks Task 6.6**: false

---

## 8. Downstream Boundary
This Documentation Assembly Package is a `DRAFT`.
It does not authorize Task 6.6. It does not authorize execution. It does not authorize commits.

Status DOGFOOD_DOCUMENTATION_PACKAGE_DRAFTED_WITH_WARNINGS means that the documentation package exists as a DRAFT only and does not authorize preflight or code execution. Human Documentation Review (Task 6.6) is required before any execution authorization.
