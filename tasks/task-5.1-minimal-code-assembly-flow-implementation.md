# Task 5.1 — Minimal Code Assembly Flow Implementation

## Task ID / Name

Task ID: `5.1`

Task name: `Minimal Code Assembly Flow Implementation`

## Mode

Implementation under human checkpoint `HCP-BS5-TASK51-001`.

This task may prepare the first minimal working code-assembly flow inside the exact allowed write list only.

## Repository

Repository: `NMF13579/AOS-1`

The task may operate only in this local repository on the approved branch.

## Branch

Required branch: `build/assembly-first`

Branch change is not authorized by this task.

## Context

Upstream basis:

- `reports/build-step-5-intake-and-mvp-scope-lock.md`
- `reports/human-checkpoints/build-step-5-task-5-0-authorization-checkpoint.md`
- `reports/human-checkpoints/build-step-5-task-5-1-implementation-checkpoint.md`
- `agentos/pipelines/code-assembly/code-assembly-pipeline-contract.md`
- `agentos/safety/minimal-safety-floor.md`
- `agentos/safety/failure-semantics.md`

Human checkpoint `HCP-BS5-TASK51-001` records:

- `human_decision: APPROVED`
- `risk_profile: HIGH_RISK_PROTECTED`
- `authorized_change_mode: create_new_only`
- `execution_permission_for_task_5_2: not granted`

Current workspace note:

- `workspace_clean_before_start: required` is written in the checkpoint
- current local workspace is still not clean because unrelated untracked files exist
- this task brief records that condition explicitly and does not treat it as solved

## Goal

Define and execute one minimal code-assembly flow in a fail-closed way, using only newly created files inside the exact allowed write list.

## Scope

In scope:

- create this Task Brief
- create one new implementation file for the minimal code-assembly flow
- create one Execution Report
- create one Evidence Report

Out of scope:

- editing existing canonical contract files
- editing templates
- editing `tasks/ACTIVE_TASK.md`
- commit, push, merge, release
- any product code change outside the exact allowed write list

## Allowed Write Paths

Exact allowed write paths for Task 5.1:

- `tasks/task-5.1-minimal-code-assembly-flow-implementation.md`
- `agentos/pipelines/code-assembly/minimal-code-assembly-flow.md`
- `reports/build-step-5-task-5-1-execution-report.md`
- `reports/build-step-5-task-5-1-evidence-report.md`

Allowed change mode for every path above:

- `create_new`

## Forbidden Write Paths

Forbidden paths include:

- `agentos/safety/`
- `agentos/pipelines/code-assembly/code-assembly-pipeline-contract.md`
- `reports/human-checkpoints/`
- `tasks/ACTIVE_TASK.md`
- `agentos/pipelines/documentation-assembly/templates/`
- any path not listed exactly in the allowed write list

Additional forbidden actions:

- overwrite existing files
- delete, move, rename, archive
- hidden partial write
- commit, push, merge, release without separate human authorization

## Required Behavior / Content

The task result must:

- preserve `PASS ≠ approval`
- preserve `Evidence ≠ approval`
- preserve `NOT_RUN ≠ PASS`
- preserve `UNKNOWN ≠ OK`
- keep all writes attributable to Task 5.1 only
- keep implementation readable in plain language
- record `NOT_RUN` explicitly for any check that is required but not run
- stop if an intended write path falls outside the exact allowed write list
- stop if workspace state prevents safe attribution of the new files

The implementation file must:

- describe the minimal code-assembly flow from Task Brief to Evidence Report
- preserve manual human review as mandatory
- preserve fail-closed behavior when scope, branch, authority, or write boundary is unclear

## Non-Goals

This task does not:

- modify the Code Assembly Pipeline Contract
- create validator logic
- create runtime enforcement
- create governance logic
- change lifecycle state
- authorize Task 5.2
- simulate human approval

## Validation

Validation after Task 5.1 work must include:

- `git status --short`
- changed-path check against the exact allowed write list
- readable diff review for the new files
- explicit `NOT_RUN` reporting for any non-executed checks
- human review of diff
- human review of Evidence Report

## Expected Final Report

Expected completion artifacts:

- `reports/build-step-5-task-5-1-execution-report.md`
- `reports/build-step-5-task-5-1-evidence-report.md`

Checkpoint `HCP-BS5-TASK51-001` also names:

- `reports/build-step-5-task-5-1-human-review-handoff.md`

That path is not included in the exact allowed write list above, so it remains blocked unless separately clarified by human.

## Execution Package Handoff Notes

- Execution Package is acknowledged as a later handoff artifact.
- Execution Package is deferred here.
- This task brief does not create or authorize `agentos/pipelines/documentation-assembly/execution-package.md`.

Future execution packaging for Task 5.1 should receive:

- exact allowed write paths
- checkpoint reference `HCP-BS5-TASK51-001`
- risk profile evidence
- branch context
- validation expectations
- evidence expectations

## Unknowns

- whether the dirty workspace must be cleaned first by a separate human-authorized action before any implementation write beyond this Task Brief
- whether `reports/build-step-5-task-5-1-human-review-handoff.md` should be added to the exact allowed write list by a later human clarification

## Blockers

- workspace is not currently clean, while checkpoint prerequisite says `workspace_clean_before_start: required`

## Forbidden Claims

- Do not claim approval from task completion.
- Do not claim execution permission from plan acceptance alone.
- Do not claim runtime, validator, governance, or code pipeline behavior beyond the exact created artifacts.

## Final Rule

- PASS ≠ approval.
- Evidence ≠ approval.
- CI PASS ≠ approval.
- UNKNOWN ≠ OK.
- NOT_RUN ≠ PASS.
- Human approval cannot be simulated.
- Human Risk Profile assignment cannot be simulated.
- Template ≠ runtime.
- Template ≠ validator.
- Template ≠ Governance / Control Module.
- Template ≠ Code Assembly Pipeline.
- Template ≠ approval.
- Template ≠ lifecycle mutation.

## Build Step 3 Safety Alignment

- `PASS ≠ approval.`
- `Evidence ≠ approval.`
- `CI PASS ≠ approval.`
- `Metrics ≠ approval.`
- `UNKNOWN ≠ OK.`
- `NOT_RUN ≠ PASS.`
- `BLOCKED ≠ PASS.`
- `DEFERRED ≠ PASS.`
- `DEFERRED ≠ approval.`
- `DEFERRED ≠ completion.`
- Human approval cannot be simulated.
- Human Risk Profile assignment cannot be simulated.
- Scope must not expand without explicit human permission.
- Protected/canonical changes require human checkpoint.
- Destructive operations are forbidden by default.
- Skeleton ≠ implementation.
- Template creation or template update is not runtime.
- Template creation or template update is not validator.
- Template creation or template update is not Governance / Control Module implementation.
- Template creation or template update is not Code Assembly Pipeline implementation.
- Template creation or template update is not lifecycle mutation.
