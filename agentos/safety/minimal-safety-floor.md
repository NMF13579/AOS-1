# Minimal Safety Floor

## Title
Minimal Safety Floor Semantics Contract for AOS-1 / AgentOS Next.

## Purpose
This contract makes the minimum always-on safety rules explicit, traceable, and checkable. It documents the floor that all current and future documentation, code, evidence, review, validator, runtime, and governance artifacts must respect.

## Source Authority
Authority order for this contract:
- `00_AOS_Core_Control.md`
- `01_AOS_Assembly_Pipelines_and_Build_Roadmap.md`
- `02_AOS_Governance_Control_Module_and_Safety_Rules.md`
- `03_AOS_Future_and_Legacy_Reference_OPTIONAL.md` as reference only

If roadmap and safety/control semantics conflict, safety/control semantics from `02_AOS_Governance_Control_Module_and_Safety_Rules.md` win unless `00_AOS_Core_Control.md` explicitly says otherwise.

## Scope of Applicability
This contract applies to Documentation Assembly Pipeline, future Code Assembly Pipeline, Build Step reports, Evidence reports, human checkpoint packages, future validators, future runtime enforcement, and future Governance / Control Module work. The floor is always-on and is not optional for any later artifact that participates in scoped work, evidence, review, authorization, or lifecycle handling.

## Non-Goals
This contract is not runtime implementation, validator implementation, Governance / Control Module implementation, Code Assembly Pipeline implementation, approval, merge, release, lifecycle mutation, or a substitute for Task 3.2 failure semantics detail. It does not itself authorize any write outside its own creation scope.

## Core Safety Invariants
The following invariants are mandatory and must not be weakened by later work:
- PASS ≠ approval.
- Evidence ≠ approval.
- CI PASS ≠ approval.
- Metrics ≠ approval.
- UNKNOWN ≠ OK.
- NOT_RUN ≠ PASS.
- BLOCKED ≠ PASS.
- Human approval cannot be simulated.
- Human Risk Profile assignment cannot be simulated.
- Skeleton ≠ implementation.
- Scope must not expand without explicit human permission.
- Protected/canonical change requires human checkpoint.
- Destructive operation is forbidden by default.
- No auto-approval.
- No auto-completion.
- No auto-merge.
- No auto-commit.
- No hidden execution.
- No hidden lifecycle mutation.

## PASS Semantics
PASS means the defined check or task condition passed within its declared scope. PASS does not approve work, does not merge work, does not release work, does not mutate lifecycle, does not authorize the next Build Step, and does not replace human review.

## Evidence Semantics
Evidence is proof material or support for a claim. Evidence is not approval, is not human decision, is not lifecycle mutation, and cannot authorize merge, release, protected/canonical change, or destructive operation.

## CI PASS Semantics
CI PASS means configured CI checks passed. CI PASS is not approval, is not human review, is not merge authorization, is not release authorization, and is not lifecycle mutation.

## Metrics Semantics
Metrics are measurement signals. Metrics are not approval and are not Evidence unless linked to traceable measurement context. Metrics cannot authorize lifecycle mutation, merge, release, protected/canonical changes, or destructive operations.

## UNKNOWN Handling
UNKNOWN is not OK. UNKNOWN must not be treated as PASS, must not be treated as approval, and must not be silently converted to false, zero, clean, accepted, or complete. UNKNOWN in required safety, source, scope, authorization, approval, lifecycle, protected/canonical, or write-boundary fields must fail closed.

## NOT_RUN Handling
NOT_RUN is not PASS. NOT_RUN is not Evidence of success, cannot satisfy validation, cannot support completion, and must be reported explicitly.

## BLOCKED Handling
BLOCKED is not PASS, is not approval, and is not completion. BLOCKED must preserve the reason for blocking and must not be bypassed by agent assumption.

## Human Approval Boundary
Human approval cannot be simulated. Agent reports, Evidence, PASS, CI PASS, Metrics, readiness, or checkpoint package creation cannot replace human approval. Human approval must be explicit, scoped, and traceable.

## Human Risk Profile Assignment Boundary
Human Risk Profile assignment cannot be simulated. The agent may propose a Risk Profile, but the agent must not assign Risk Profile. If required Risk Profile assignment is unavailable, the result must be `BLOCKED` or `HUMAN_REVIEW_REQUIRED`.

## Scope Expansion Boundary
Scope must not expand without explicit human permission. Task scope, file scope, Build Step scope, lifecycle scope, and authorization scope must remain bounded. Unclear scope must fail closed.

## Protected/Canonical Boundary
Protected/canonical changes require human checkpoint. The agent must not self-declare protected/canonical files as non-canonical. Unknown protected/canonical status must fail closed.

## Destructive Operation Boundary
Destructive operations are forbidden by default. Deletion, move, rename, archive, overwrite, history rewrite, branch protection change, and irreversible cleanup require explicit human authorization and applicable checkpoint.

## Lifecycle Mutation Boundary
Lifecycle mutation requires explicit human authorization. Readiness does not mutate lifecycle. PASS does not mutate lifecycle. Evidence does not mutate lifecycle. CI PASS does not mutate lifecycle. The agent must not mark tasks, Build Steps, milestones, or releases complete without required human decision.

## Auto-Approval Prohibition
No artifact, report, validator, runtime, metric, or pipeline result may auto-approve work. Any design that would convert PASS, Evidence, or CI PASS into approval violates Minimal Safety Floor.

## Auto-Completion Prohibition
No artifact, report, validator, runtime, metric, or pipeline result may auto-complete work. Completion remains bounded by explicit human decision where the process requires it.

## Auto-Merge Prohibition
No automation may treat readiness, PASS, Evidence, CI PASS, or metrics as merge permission. Merge requires its own explicit human authorization.

## Auto-Commit Prohibition
No automation may silently commit changes outside explicitly authorized task scope. Future automation may enforce or check the floor, but must not redefine the floor or bypass scoped write authority.

## Hidden Execution Prohibition
No hidden execution is allowed. Execution and evidence-producing actions must remain visible, scoped, and attributable.

## Hidden Lifecycle Mutation Prohibition
No hidden lifecycle mutation is allowed. Status changes, completion signals, approval transitions, and next-step transitions must remain explicit and traceable.

## Skeleton vs Implementation Boundary
Skeleton is not implementation. Template is not implementation. Contract is not runtime. Specification is not validator. Documentation is not enforcement. The existence of a skeleton, template, or contract must not be misread as implemented behavior.

## Documentation Assembly Pipeline Applicability
Documentation Assembly Pipeline must obey Minimal Safety Floor from the first document through task, evidence, review, and checkpoint artifacts. Documentation artifacts may structure work, but they must not redefine approval, PASS, Evidence, UNKNOWN, NOT_RUN, lifecycle, or authorization semantics unsafely.

## Future Code Assembly Pipeline Applicability
Future Code Assembly Pipeline must operate within the same floor. Code diffs, checks, Execution Reports, and Evidence Reports must not reinterpret PASS as approval, readiness as merge permission, or evidence as lifecycle mutation.

## Future Validator Applicability
Future validators may check, enforce, or measure compliance with Minimal Safety Floor, but must not redefine the floor. Validator behavior must never weaken the invariants documented here.

## Future Runtime Applicability
Future runtime enforcement may physically block forbidden actions, but runtime is only an enforcement layer. Runtime must not redefine approval, Risk Profile assignment, lifecycle mutation, or authorization semantics without explicit human-approved protected/canonical change.

## Future Governance / Control Module Applicability
Future Governance / Control Module work may formalize gates, reviews, and controls, but it must not weaken Minimal Safety Floor. Governance logic may check or enforce the floor; it may not replace it with looser semantics.

## Status Mapping Reference Boundary
This contract defines the minimum semantic floor only. Detailed failure status mapping, blocked-state handling detail, and extended failure semantics belong to `agentos/safety/failure-semantics.md` in Task 3.2 and are not created or updated here.

## Retroactive Applicability Boundary
Minimal Safety Floor conceptually applies from Build Step 0. This contract does not decide operational consequences for already-created artifacts, does not retroactively approve, reject, rewrite, or invalidate prior artifacts, and does not decide whether earlier artifacts violate the floor. Operational mapping for retroactive applicability is delegated to Task 3.2 or a later authorized review task.

## Final Rule
Minimal Safety Floor is always-on from day one and is not optional. Future runtime, validator, Governance / Control Module, and Code Assembly Pipeline work may only enforce or check this floor; they must not weaken or redefine it without explicit human-approved protected/canonical change.

```yaml
minimal_safety_floor_contract:
  artifact: "agentos/safety/minimal-safety-floor.md"
  build_step: 3
  task_id: "3.1"
  contract_type: "minimal_safety_floor_semantics"
  applies_from: "Build Step 0"
  created_or_updated_by_task: "3.1"

  source_authority:
    primary_control_source: "00_AOS_Core_Control.md"
    roadmap_source: "01_AOS_Assembly_Pipelines_and_Build_Roadmap.md"
    safety_control_source: "02_AOS_Governance_Control_Module_and_Safety_Rules.md"
    optional_reference: "03_AOS_Future_and_Legacy_Reference_OPTIONAL.md"

  invariant_presence:
    pass_is_not_approval: true
    evidence_is_not_approval: true
    ci_pass_is_not_approval: true
    metrics_are_not_approval: true
    unknown_is_not_ok: true
    not_run_is_not_pass: true
    blocked_is_not_pass: true
    human_approval_cannot_be_simulated: true
    human_risk_profile_assignment_cannot_be_simulated: true
    skeleton_is_not_implementation: true
    scope_must_not_expand_without_explicit_human_permission: true
    protected_canonical_change_requires_human_checkpoint: true
    destructive_operation_forbidden_by_default: true
    no_auto_approval: true
    no_auto_completion: true
    no_auto_merge: true
    no_auto_commit: true
    no_hidden_execution: true
    no_hidden_lifecycle_mutation: true

  boundary_assertions:
    this_contract_is_not_runtime: true
    this_contract_is_not_validator: true
    this_contract_is_not_governance_control_module_implementation: true
    this_contract_is_not_code_assembly_pipeline: true
    this_contract_is_not_lifecycle_mutation: true
    this_contract_is_not_approval: true
    this_contract_does_not_start_task_3_2: true
    this_contract_does_not_start_build_step_4: true

  self_verification:
    all_required_invariants_present_verified_by_agent_self_check: true
    self_verification_is_spec_level_only: true
    self_verification_is_not_runtime_enforcement: true
    self_verification_is_not_validator_execution: true
    self_verification_is_not_human_approval: true

  retroactive_applicability_parking_lot:
    applies_from_build_step_0_requires_operational_mapping: true
    delegated_to: "Task 3.2 or later authorized review task"
    task_3_1_decides_operational_effect: false
```
