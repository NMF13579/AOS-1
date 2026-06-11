# Code Assembly Pipeline Contract

**Pipeline ID:** `code-assembly`  
**Contract Version:** `2.0.0`  
**Status:** `NORMATIVE_CONTRACT_READY_FOR_REVIEW`  
**Canonical Branch:** `build/assembly-first`  
**Current Task:** `Task 4.1 remediation`  
**Human Authorization:** `HDP-BS4-TASK41-REMEDIATION-001`  
**Write Mode For This Task:** `replace_existing`

## 1. Title

Code Assembly Pipeline Contract for AOS-1 / AgentOS Next.

This artifact defines the rules for how a scoped code task moves from a written task brief to human review without silently turning agent output into approval.

## 2. Purpose

The purpose of this contract is to define one controlled flow for code work:

`Scoped Task Brief -> eligibility review -> explicit execution authorization -> Code Execution Package -> scoped code change -> Code Diff -> checks / tests -> Execution Report -> Evidence Report -> Human Review -> separate Human Approval, Rejection, or Change Request`

This contract keeps each step visible, traceable, and fail-closed when a required condition is missing.

## 3. Source Authority

Authority order for this contract:
- `00_AOS_Core_Control.md`
- `01_AOS_Assembly_Pipelines_and_Build_Roadmap.md`
- `02_AOS_Governance_Control_Module_and_Safety_Rules.md`
- `agentos/safety/minimal-safety-floor.md`
- `agentos/safety/failure-semantics.md`

If roadmap wording and safety wording conflict, safety wording wins unless `00_AOS_Core_Control.md` explicitly says otherwise.

## 4. Repository Architecture and Skeleton Authority

This contract may use repository architecture and skeleton artifacts as read-only references, but it must not treat them as implementation authority by themselves.

Rules:
- `dev` remains a frozen baseline and must not be mutated by this pipeline.
- `build/assembly-first` is the working branch for scoped implementation.
- Skeleton is not implementation.
- Architecture references shape allowed placement, but do not authorize writes by themselves.

## 5. Scope of Applicability

This contract applies only to scoped code work that already has:
- a task brief,
- a human-assigned risk profile,
- explicit execution authorization,
- a declared write boundary,
- and a known repository branch context.

It governs contract-level code assembly behavior, not runtime behavior and not release behavior.

## 6. Non-Goals

This contract does not:
- implement runtime,
- implement a validator,
- implement the Governance / Control Module,
- approve work,
- merge work,
- release work,
- mutate lifecycle automatically,
- auto-start the next task,
- or expand scope automatically.

## 7. Relationship to Documentation Assembly Pipeline

Documentation Assembly Pipeline prepares the inputs for code work: project brief, specification, task brief, execution package, execution report template, and evidence expectations.

Code Assembly Pipeline starts only after that preparation exists. If the documentation layer is missing or unclear, the code layer must stop with `BLOCKED`, `UNKNOWN_BLOCKED`, or `HUMAN_REVIEW_REQUIRED`.

## 8. Relationship to Minimal Safety Floor

This contract inherits the Minimal Safety Floor without weakening it.

That means:
- `PASS != approval`
- `Evidence != approval`
- `CI PASS != approval`
- `UNKNOWN != OK`
- `NOT_RUN != PASS`
- `Human approval cannot be simulated`
- `Scope must not expand without explicit human permission`
- `Protected/canonical changes require human checkpoint`
- `Destructive operations are forbidden by default`

## 9. Safety Semantics Inheritance

This contract may restate safety rules for clarity, but it must not redefine or weaken:
- PASS semantics,
- Evidence semantics,
- approval boundary,
- failure semantics,
- protected/canonical handling,
- lifecycle boundary,
- Source of Truth authority.

If a later section appears to weaken these rules, that later section is invalid and the stricter rule wins.

## 10. Required Input Contract

Required inputs for any task using this pipeline:
- `00_AOS_Core_Control.md`
- `01_AOS_Assembly_Pipelines_and_Build_Roadmap.md`
- `02_AOS_Governance_Control_Module_and_Safety_Rules.md`
- `agentos/safety/minimal-safety-floor.md`
- `agentos/safety/failure-semantics.md`
- a scoped task brief,
- a human-assigned risk profile,
- explicit execution authorization,
- repository branch context,
- and a known write boundary.

Missing required input results in `BLOCKED`. Unknown input state results in `UNKNOWN_BLOCKED`.

## 11. Scoped Task Brief Eligibility

A Task Brief is eligible only if it defines:
- exact goal,
- exact allowed paths,
- forbidden paths,
- validation expectations,
- failure behavior,
- and stop conditions.

Task Brief does not equal execution authorization. A complete brief can still be blocked if execution authorization is absent.

## 12. Risk Profile Boundary

Risk Profile assignment must come from a human or a separately approved deterministic classifier. The agent may propose a profile but must not assign it.

Rules:
- missing human assignment -> `HUMAN_REVIEW_REQUIRED`
- unclear sufficiency of assigned profile -> `UNKNOWN_BLOCKED`
- profile lower than required for the task -> `BLOCKED`

Risk Profile assignment does not by itself authorize a write.

## 13. Execution Authorization Boundary

Explicit execution authorization is required before any code write.

Execution authorization must state:
- exact task scope,
- allowed write paths,
- write mode,
- branch boundary,
- and forbidden actions.

Execution authorization does not equal approval. It only permits scoped work.

## 14. Integrated Code Execution Package Contract

The Code Execution Package is the bundle of task inputs used for one scoped code task. It must include:
- task brief,
- source references,
- branch context,
- write boundary,
- risk profile evidence,
- execution authorization,
- and expected validations.

The package enables execution context. It does not approve, merge, or release work.

## 15. Repository and Branch Context

Before any write, the agent must confirm:
- repository matches the authorized repository,
- current branch matches the authorized branch,
- branch is not `dev`,
- and branch state is readable.

Branch mismatch results in `BLOCKED`. Unknown branch state results in `UNKNOWN_BLOCKED`.

## 16. Allowed File Paths

Allowed file paths must be exact, not broad patterns, unless a human decision explicitly authorizes a pattern.

For any given task, the task brief or execution authorization must name the exact writable paths. If an intended write path is not explicitly listed, the write is forbidden.

## 17. Forbidden File Paths

Forbidden paths include, unless separately authorized:
- control files `00/01/02/03`,
- `agentos/safety/`,
- `agentos/contracts/`,
- architecture artifacts,
- skeleton artifacts,
- protected reports,
- `dev` branch targets,
- and any path outside the approved write list.

Known forbidden write attempt results in `BLOCKED`.

## 18. Allowed Change Types

Allowed change types must be declared explicitly. Examples:
- `create_new`
- `replace_existing`
- `update_existing`

If the declared change type and actual repository state do not match, execution must fail closed. The agent must not silently switch from one mode to another.

## 19. Forbidden Change Types

Forbidden change types include unless explicitly authorized:
- delete,
- move,
- rename,
- archive,
- overwrite outside declared mode,
- hidden partial write,
- duplicate consolidation,
- and write boundary expansion.

Destructive operation remains forbidden by default.

## 20. Scope Expansion Handling

If the task appears to require more files, more branches, or more lifecycle actions than originally authorized, the agent must stop and report `HUMAN_REVIEW_REQUIRED` or `UNKNOWN_BLOCKED`.

Useful follow-on work is not a reason to expand scope automatically.

## 21. UNKNOWN Scope Handling

If the agent cannot prove:
- what is in scope,
- what is out of scope,
- what is writable,
- or which document has authority,

the result must be `UNKNOWN_BLOCKED`.

Unknown must not be converted into assumed permission.

## 22. Protected/Canonical Handling

Protected or canonical changes require separate human checkpoint.

The agent must not self-declare a path as non-protected if authority is unclear. If path classification is unknown, the result is `UNKNOWN_BLOCKED`. If protected status is known and separate authorization is missing, the result is `BLOCKED`.

## 23. Destructive Operation Handling

Destructive operations are forbidden by default.

This includes delete, rename, move, archive, history rewrite, and any irreversible cleanup. If a task seems to benefit from such a change but no explicit human authorization exists, the agent must not proceed.

## 24. Scoped Code Change Expectations

A scoped code change must:
- stay inside the exact allowed path list,
- stay within the allowed change mode,
- remain traceable to the task brief,
- preserve inherited safety semantics,
- and stop when the authorized goal is complete.

Useful adjacent cleanup must be reported, not applied automatically.

## 25. Code Diff Expectations

If code changes are made, the resulting diff must be:
- attributable to the scoped task,
- readable by a human reviewer,
- limited to the allowed paths,
- and explainable in plain language.

Code Diff does not equal approval.

## 26. Checks and Tests Flow

Checks and tests may run only if separately authorized by the task scope.

If checks are required but not authorized, they must be reported as `NOT_RUN`. If checks are authorized and fail, the result may become `BLOCKED` depending on task rules. Checks PASS still does not equal approval.

## 27. NOT_RUN Handling

`NOT_RUN` must be reported explicitly for any required validation that was not executed.

`NOT_RUN` is not PASS, is not Evidence of success, and cannot be silently omitted from the final report.

## 28. UNKNOWN Result Handling

If a required result cannot be safely determined, the task must use `UNKNOWN_BLOCKED`.

Unknown write state, unknown branch state, unknown SHA state, or unknown authority state must not be flattened into a clean result.

## 29. Partial Execution Handling

If a task starts but cannot prove whether the write completed fully and correctly, the task must fail closed.

Rules:
- known incomplete write -> `BLOCKED`
- unknown write completion state -> `UNKNOWN_BLOCKED`
- automatic retry of unknown write state is forbidden unless separately authorized

## 30. Warning Semantics

Warnings are allowed only for non-blocking issues that do not weaken safety and do not hide missing required conditions.

Warnings must not hide:
- missing section,
- missing authorization,
- unknown status,
- unexpected path change,
- partial write,
- safety conflict,
- or Source of Truth conflict.

## 31. Execution Report Requirements

Every executed task using this pipeline must produce an Execution Report that records:
- actual branch,
- actual changed paths,
- write mode used,
- pre-write and post-write state where required,
- blockers,
- unknowns,
- warnings,
- and final task status.

Execution Report is the agent claim. It is not proof by itself.

## 32. Evidence Report Requirements

If the task scope requires evidence, the Evidence Report must record the proof material used to support the execution claim:
- SHA values,
- diff summary,
- changed path list,
- output artifacts,
- and `NOT_RUN` items where applicable.

Evidence Report does not equal approval.

## 33. Agent Claim vs Evidence Boundary

The agent may claim what was done, but must separate that claim from the proof.

Examples:
- "file changed" is a claim,
- SHA comparison is proof,
- "all sections present" is a claim,
- counted section list is proof.

When claim and proof conflict, proof wins and the task must fail closed if the conflict matters.

## 34. Manual Human Review Requirement

Manual human review remains required before approval where the process demands it.

The pipeline may prepare review-ready artifacts, but it must not pretend that review already happened.

## 35. Human Approval Boundary

Human approval is a separate explicit decision.

The following are not approval:
- Task Brief,
- eligibility PASS,
- Risk Profile assignment,
- Code Execution Package,
- Code Diff,
- Execution Report,
- Evidence Report,
- checks PASS,
- CI PASS,
- readiness to start the next task.

## 36. Commit / Push / Merge / Release Boundary

Commit, push, merge, and release require separate explicit human authorization.

A code task may complete locally without any of those actions being authorized. Their absence must be stated in the final report instead of being assumed away.

## 37. Lifecycle Mutation Boundary

Lifecycle mutation, including marking a wider build phase complete or starting the next task automatically, requires separate human authorization.

`may_start_task_4_2: true` would only mean readiness from the report perspective. It would not authorize Task 4.2 execution.

## 38. Build Step 5 Boundary

This contract does not authorize Build Step 5, and no code task under this contract may auto-start Build Step 5.

If later work depends on Build Step 5 decisions, those decisions remain blocked until separately authorized by a human.

## 39. Machine-Readable Contract Summary

```yaml
code_assembly_pipeline_contract:
  artifact: "agentos/pipelines/code-assembly/code-assembly-pipeline-contract.md"
  contract_version: "2.0.0"
  branch_context: "build/assembly-first"
  contract_status: "NORMATIVE_CONTRACT_READY_FOR_REVIEW"

  source_authority:
    primary_control_source: "00_AOS_Core_Control.md"
    roadmap_source: "01_AOS_Assembly_Pipelines_and_Build_Roadmap.md"
    safety_control_source: "02_AOS_Governance_Control_Module_and_Safety_Rules.md"
    minimal_safety_floor: "agentos/safety/minimal-safety-floor.md"
    failure_semantics: "agentos/safety/failure-semantics.md"

  pipeline_flow:
    - "Scoped Task Brief"
    - "eligibility review"
    - "explicit execution authorization"
    - "Code Execution Package"
    - "scoped code change"
    - "Code Diff"
    - "checks / tests"
    - "Execution Report"
    - "Evidence Report"
    - "Human Review"
    - "separate Human Approval, Rejection, or Change Request"

  invariants:
    task_brief_is_not_execution_authorization: true
    eligibility_pass_is_not_execution_authorization: true
    risk_profile_assignment_is_not_write_authorization: true
    code_execution_package_is_not_approval: true
    code_execution_package_is_not_execution_evidence: true
    code_diff_is_not_approval: true
    execution_report_is_agent_claim: true
    execution_report_is_not_proof_by_itself: true
    evidence_report_is_not_approval: true
    checks_pass_is_not_approval: true
    ci_pass_is_not_approval: true
    not_run_is_not_pass: true
    unknown_is_not_ok: true
    warning_is_not_clean_pass: true
    readiness_is_not_execution_authorization: true
    human_approval_cannot_be_simulated: true
    protected_canonical_changes_require_human_checkpoint: true
    destructive_operations_forbidden_by_default: true

  boundaries:
    allowed_change_types_must_be_explicit: true
    scope_expansion_requires_explicit_human_permission: true
    protected_or_canonical_unknown_fails_closed: true
    branch_mismatch_blocks_execution: true
    commit_push_merge_release_require_separate_authorization: true
    task_4_2_not_auto_started: true
    build_step_5_not_authorized: true
```

## 40. Final Rule

Task 4.1 defines the contract layer for Code Assembly Pipeline. It does not implement the pipeline itself, does not execute product work by itself, and does not weaken AOS-1 safety semantics.

If the pipeline cannot prove scope, authority, risk profile, write boundary, branch context, or safety preservation, it must fail closed with `BLOCKED`, `UNKNOWN_BLOCKED`, or `HUMAN_REVIEW_REQUIRED` rather than inventing a clean success state.
