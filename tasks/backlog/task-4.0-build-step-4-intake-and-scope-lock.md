# Task 4.0 - Build Step 4 Intake and Scope Lock

```yaml
task_id: "4.0"
task_name: "Build Step 3 Completion Intake and Build Step 4 Scope Lock"
repository: "NMF13579/AOS-1"
required_branch: "build/assembly-first"
risk_profile: "MEDIUM_RISK_GUIDED"
risk_profile_assigned_by_human: true
execution_authorization_reference: "HDP-BS4-RESET-001"
execution_allowed: true
rerun_authorization_reference: "HDP-BS4-RERUN-001"
```

## Purpose

Verify Build Step 3 completion and determine whether Task 4.1 may start under the updated authorization scope from `HDP-BS4-RERUN-001`.

## Allowed Actions

- Read repository files required for Task 4.0.
- Create `reports/build-step-4-intake-and-scope-lock-v2.md` using `create_new`.

## Required Checks

- Verify the current branch is `build/assembly-first`.
- Verify the Build Step 3 completion checkpoint.
- Review required authority and safety sources.
- Verify the human-assigned Risk Profile.
- Classify the planned Task 4.1 contract path and write mode.
- Determine the protected/canonical boundary.
- Verify whether the Task 4.1 contract already exists on the canonical target branch.
- Capture the pre-write repository state.
- Record blockers, unknowns, and checks that were not run.

## Task 4.1 Planned Contract

```yaml
path: "agentos/pipelines/code-assembly/code-assembly-pipeline-contract.md"
classification: "planned_active_contract_artifact"
initial_creation_is_protected_or_canonical_change: false
future_modification_requires_separate_review: true
planned_write_mode: "create_new"
authorized_directory_creation: "agentos/pipelines/code-assembly/"
```

## Forbidden Actions

- Do not rerun the old report path.
- Do not alter `reports/build-step-4-intake-and-scope-lock.md`.
- Do not modify protected or canonical files.
- Do not run tests, builds, runtime, or validators.
- Do not commit, push, merge, release, or start Build Step 5.
- Do not perform destructive operations or lifecycle mutation.

## Output

Create only:

`reports/build-step-4-intake-and-scope-lock-v2.md`

After creating and verifying the report, stop.
