# Task Brief Template

## Task ID and Name
- Task ID:
- Task name:

Guidance:
- Use the exact task identifier.
- Use a name that matches the scoped work only.

## Mode
- Execution mode:

Guidance:
- Describe what kind of work is allowed in simple words.
- Do not imply execution authority if it was not explicitly granted.

## Repository
- Repository:

Guidance:
- Name the exact repository or workspace.
- Keep repository context separate from branch context.

## Branch
- Required branch:

Guidance:
- Name the exact branch.
- Branch eligibility is not approval by itself.

## Human Authorization
```yaml
human_authorization:
  authorized_by:
  authorization_source:
  authorized_task_id:
  task_execution_authorized: false
  authorized_scope:
  assigned_risk_profile:
  risk_profile_assigned_by_human: false

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

Guidance:
- Keep blank fields blank until a human supplies exact values.
- Do not copy current task values into this template by default.

## Context
Describe the background needed to understand the task.

Guidance:
- Summarize only the relevant upstream state.
- Keep unknowns visible if context is incomplete.

## Goal
State the single task outcome.

Guidance:
- Make it concrete and reviewable.
- Do not combine multiple unrelated goals.

## Scope
Describe what work is inside the task.

Guidance:
- Keep scope narrow and explicit.
- Name the allowed work area clearly.

## Allowed Changes
List the exact files, folders, or artifact types that may change.

Guidance:
- Prefer exact paths over broad categories.
- If a path is not listed, treat it as forbidden.

## Forbidden Changes
List what must not change.

Guidance:
- Include protected, deferred, out-of-scope, and destructive actions as needed.
- Make boundaries hard to misunderstand.

## Required Behavior
Describe the output and safety behavior expected from the task.

Guidance:
- Name required sections, content rules, and boundary rules.
- Keep approval separate from execution and evidence.

## Non-Goals
List what this task does not do.

Guidance:
- Use this section to block adjacent scope expansion.
- Keep it consistent with Scope.

## Validation
Describe how the result must be checked.

Guidance:
- Name the checks or review steps.
- `NOT_RUN` must stay visible if something was not checked.

## Evidence Requirements
Describe what evidence must be produced.

Guidance:
- Name the exact proof artifacts expected.
- Evidence does not equal approval.

## Expected Final Report
Describe the final report that must be produced.

Guidance:
- Name the target report or report structure.
- Keep the reporting requirement inside the task boundary.

## Stop Conditions
Describe when the agent must stop instead of continuing.

Guidance:
- Stop on unknown scope, unknown path authority, missing required approval, or blocked validation.
- Do not continue through assumption.

## Final Boundary Rule
State what this task cannot do even if work appears successful.

Guidance:
- Completion is not approval.
- The task must not auto-start the next task, merge, release, or simulate a human decision.
