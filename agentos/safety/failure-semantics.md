# Failure Semantics and Status Mapping

## Title
Failure Semantics and Status Mapping Contract for AOS-1 / AgentOS Next.

## Purpose
This contract defines how AOS-1 maps unsafe, incomplete, unverifiable, missing, ambiguous, deferred, contradictory, or human-dependent states to explicit statuses. Its job is to make later tasks fail closed instead of silently treating incomplete or unsafe states as success.

## Source Authority
Authority order for this contract:
- `00_AOS_Core_Control.md`
- `01_AOS_Assembly_Pipelines_and_Build_Roadmap.md`
- `02_AOS_Governance_Control_Module_and_Safety_Rules.md`
- `03_AOS_Future_and_Legacy_Reference_OPTIONAL.md` as reference only

If `01_AOS_Assembly_Pipelines_and_Build_Roadmap.md` and `02_AOS_Governance_Control_Module_and_Safety_Rules.md` conflict on safety/control semantics, `02_AOS_Governance_Control_Module_and_Safety_Rules.md` wins unless `00_AOS_Core_Control.md` explicitly says otherwise. If `00_AOS_Core_Control.md` is missing, unreadable, internally conflicting, or cannot provide a stable control interpretation, the result must be `UNKNOWN_BLOCKED`.

## Scope of Applicability
This contract applies to Documentation Assembly Pipeline, future Code Assembly Pipeline, reports, Evidence, checkpoints, future validators, future runtime, future Governance / Control Module work, and downstream readiness decisions. It defines how statuses behave and how unsafe states propagate.

## Non-Goals
This contract is not runtime implementation, validator implementation, Governance / Control Module implementation, Code Assembly Pipeline implementation, branch protection, CI required checks, merge, release, approval, or lifecycle mutation. It does not review, rewrite, invalidate, approve, reject, or mutate prior Build Step 2 artifacts.

## Relationship to Minimal Safety Floor
This contract operationalizes the Minimal Safety Floor without weakening it. It expands the floor into explicit status mapping rules, but it does not replace or redefine the invariants already established in `agentos/safety/minimal-safety-floor.md`.

## Core Failure Semantics
If a required safety, source, scope, evidence, authorization, approval, lifecycle, protected/canonical, status propagation, deferred, or write-boundary state cannot be proven safe, complete, and authorized, the result must fail closed. Depending on what is wrong, the allowed fail-closed outputs are `BLOCKED`, `UNKNOWN_BLOCKED`, `NOT_RUN`, or `HUMAN_REVIEW_REQUIRED`.

## Status Taxonomy
This contract defines the following statuses:
- `PASS`
- `PASS_WITH_WARNINGS`
- `BLOCKED`
- `UNKNOWN_BLOCKED`
- `NOT_RUN`
- `HUMAN_REVIEW_REQUIRED`
- `DEFERRED`
- `REJECTED`
- `ACCEPTED`

Each status is scoped and must not be expanded by inference beyond its stated decision boundary.

## PASS Semantics
`PASS` means a defined check or task condition passed within its declared scope. `PASS` is not approval, is not lifecycle mutation, does not authorize merge, release, next task, next Build Step, protected/canonical change, destructive operation, runtime, validator, Governance / Control Module, or Code Assembly Pipeline.

## PASS_WITH_WARNINGS Semantics
`PASS_WITH_WARNINGS` means required conditions passed within declared scope, but non-blocking warnings were preserved. It is not clean `PASS`, is not approval, and must keep warning details visible. Warnings must not hide missing required invariants, missing authorization, unknown source authority, forbidden writes, lifecycle mutation, missing Evidence, or incomplete execution.

## BLOCKED Semantics
`BLOCKED` means execution, completion, readiness, or forward movement is stopped by a known unmet requirement. `BLOCKED` is not `PASS`, is not approval, is not completion, and must preserve blocking reasons.

## UNKNOWN_BLOCKED Semantics
`UNKNOWN_BLOCKED` means execution, completion, readiness, or forward movement is stopped because a required state is unknown, ambiguous, unreadable, conflicting, unverifiable, or cannot be safely classified. `UNKNOWN_BLOCKED` is not `PASS`, is not approval, is not completion, and must fail closed.

## NOT_RUN Semantics
`NOT_RUN` means a required check, validation, review, command, or execution step was not run. `NOT_RUN` is not `PASS`, is not Evidence of success, cannot satisfy validation, cannot support completion, and must be reported explicitly.

## HUMAN_REVIEW_REQUIRED Semantics
`HUMAN_REVIEW_REQUIRED` means a required decision, checkpoint, review, authorization, Risk Profile assignment, protected/canonical classification, or approval needs human action. It is not approval, not rejection, and not `PASS`. The agent must not resolve `HUMAN_REVIEW_REQUIRED` by inference.

## DEFERRED Semantics
`DEFERRED` means a decision or action is intentionally postponed. It is not approval, not rejection, not completion, not `PASS`, and not execution authorization. A deferred state must preserve what was deferred, who may decide it later, and what remains blocked or allowed. If the deferred item is required for downstream work, downstream work must remain blocked until the deferred item is resolved by explicit allowed decision.

## REJECTED Semantics
`REJECTED` means an explicit human decision rejected a plan, artifact, checkpoint, or proposed action. `REJECTED` must not be assigned by agent inference. It is scoped and may block downstream work if the rejected item is required.

## ACCEPTED Semantics
`ACCEPTED` means an explicit human decision accepted a plan, artifact, checkpoint, or proposed action within declared scope. `ACCEPTED` must not be assigned by agent inference. It is scoped and is not automatic execution authorization, merge authorization, release authorization, or lifecycle mutation unless the human decision explicitly says so.

## Missing Evidence Mapping
Required evidence missing maps to `BLOCKED`. An evidence path that is missing maps to `BLOCKED` or `UNKNOWN_BLOCKED` depending on whether the path absence is known or unreadable. Declared-but-unreadable evidence maps to `UNKNOWN_BLOCKED`, declared-but-empty evidence maps to `BLOCKED`, and declared-but-not-traceable evidence maps to `BLOCKED`.

## Invalid Evidence Mapping
Evidence that contradicts a claim maps to `BLOCKED`. Evidence format that is invalid maps to `BLOCKED` or `UNKNOWN_BLOCKED`. Evidence scope mismatch maps to `BLOCKED`. Evidence from a disallowed source maps to `BLOCKED`. Evidence integrity that cannot be determined maps to `UNKNOWN_BLOCKED`.

## Contradictory Evidence Mapping
Internal report conflict maps to `BLOCKED` or `UNKNOWN_BLOCKED`. A source conflict on safety semantics maps to `UNKNOWN_BLOCKED`. A conflict between `01_AOS_Assembly_Pipelines_and_Build_Roadmap.md` and `02_AOS_Governance_Control_Module_and_Safety_Rules.md` on safety semantics is resolved by `02_AOS_Governance_Control_Module_and_Safety_Rules.md` unless `00_AOS_Core_Control.md` explicitly says otherwise. If `00_AOS_Core_Control.md` is missing, unreadable, internally conflicting, or cannot stably interpret the conflict, the result is `UNKNOWN_BLOCKED`. Human decision conflict maps to `HUMAN_REVIEW_REQUIRED` or `UNKNOWN_BLOCKED`. Status field conflict maps to `BLOCKED` or `UNKNOWN_BLOCKED`.

## Unknown Result Mapping
Missing, unreadable, or ambiguous result state maps to `UNKNOWN_BLOCKED`. If the result conflicts with evidence, the outcome is `BLOCKED` or `UNKNOWN_BLOCKED` depending on whether the contradiction is known or cannot be safely resolved.

## Unknown Scope Mapping
Unknown task scope, file scope, authorization scope, lifecycle scope, or protected/canonical scope maps to `UNKNOWN_BLOCKED`. Unclear scope must fail closed.

## Unknown File Change Mapping
Unknown changed files or unknown write boundary maps to `UNKNOWN_BLOCKED`. Known forbidden write maps to `BLOCKED`. Uncertain forbidden write maps to `UNKNOWN_BLOCKED`. Detected partial write maps to `BLOCKED`. Unknown write completion state maps to `UNKNOWN_BLOCKED`.

## Unknown Flow Class Mapping
Unknown documentation flow, code flow, runtime flow, approval flow, or lifecycle flow maps to `UNKNOWN_BLOCKED`. If the agent cannot classify the flow safely, downstream readiness must fail closed.

## Human-Unavailable Mapping
Unavailable required human approval, checkpoint, Risk Profile assignment, or authorization maps to `HUMAN_REVIEW_REQUIRED`. Conflicting required human decisions map to `HUMAN_REVIEW_REQUIRED` or `UNKNOWN_BLOCKED`. The agent may not simulate human decisions.

## Warning Semantics
Warning means a non-blocking issue was detected and preserved. Warning is not clean `PASS` and is not approval. Warning must not hide required missing conditions. Warning must not downgrade `BLOCKED` to `PASS_WITH_WARNINGS`, must not downgrade `UNKNOWN_BLOCKED` to `PASS_WITH_WARNINGS`, must not convert `NOT_RUN` to `PASS_WITH_WARNINGS`, and must not convert required deferred decisions into `PASS_WITH_WARNINGS`. Warnings are allowed only when all required safety, source, scope, authorization, Evidence, write-boundary, deferred-dependency, and lifecycle conditions are already satisfied.

## Status Propagation Rules
Upstream `BLOCKED` blocks downstream. Upstream `UNKNOWN_BLOCKED` blocks downstream. Upstream `NOT_RUN` does not satisfy downstream. Upstream `DEFERRED` blocks downstream if the deferred item is required. Upstream `DEFERRED` preserves deferred scope and is not completion. Upstream `PASS` is not approval. Upstream `PASS_WITH_WARNINGS` preserves warnings. Upstream `ACCEPTED` is scoped to the human decision. Readiness does not start the next task. If the agent cannot determine whether a deferred item is required for downstream work, the downstream result must be `UNKNOWN_BLOCKED`.

## BLOCKED vs UNKNOWN_BLOCKED Boundary
`BLOCKED` means a known unmet requirement. Examples include required checkpoint missing, required authorization missing, required Risk Profile not assigned, forbidden write detected, required invariant missing, required Evidence absent, required upstream decision deferred, or required upstream artifact deferred. `UNKNOWN_BLOCKED` means the state is unknown, ambiguous, unreadable, conflicting, or unverifiable. Examples include required source unreadable, `00_AOS_Core_Control.md` internally conflicting, ambiguous checkpoint meaning, undetermined protected/canonical status, undetermined changed files, conflicting status fields, unverifiable evidence integrity, unknown deferred-item scope, or uncertainty whether a deferred item is required. If the agent cannot choose safely between the two, it must choose `UNKNOWN_BLOCKED`.

## ACCEPTED / REJECTED Human-Decision Boundary
`ACCEPTED` and `REJECTED` are human decision states unless a canonical source explicitly defines a non-human status with those exact names. The agent must not infer `ACCEPTED` or `REJECTED` from `PASS`, Evidence, CI PASS, Metrics, readiness, report creation, or `DEFERRED`. `ACCEPTED` requires explicit human decision evidence and remains scoped. `REJECTED` requires explicit human decision evidence and remains scoped. `DEFERRED` is neither `ACCEPTED` nor `REJECTED`.

## Retroactive Applicability Operational Boundary
Minimal Safety Floor applies conceptually from Build Step 0, but this contract does not automatically invalidate, rewrite, approve, reject, or mutate lifecycle for prior artifacts. Prior artifacts may be reviewed under the floor only by an authorized review task. Task 3.2 does not itself review prior Build Step artifacts and does not decide whether existing Build Step 2 artifacts violate the newly formalized semantics.

## Spec-Level Self-Verification Note
Task 3.2 verifies that all required status mappings are present only as a spec-level self-check against the required mapping lists. This self-check is not runtime enforcement, not validator execution, not independent audit, and not human approval.

## Machine-Readable Status Mapping

```yaml
failure_semantics_contract:
  artifact: "agentos/safety/failure-semantics.md"
  build_step: 3
  task_id: "3.2"
  contract_type: "failure_semantics_and_status_mapping"
  created_or_updated_by_task: "3.2"

  source_authority:
    primary_control_source: "00_AOS_Core_Control.md"
    roadmap_source: "01_AOS_Assembly_Pipelines_and_Build_Roadmap.md"
    safety_control_source: "02_AOS_Governance_Control_Module_and_Safety_Rules.md"
    optional_reference: "03_AOS_Future_and_Legacy_Reference_OPTIONAL.md"

  primary_source_00_mapping:
    primary_source_00_unreadable_or_missing: UNKNOWN_BLOCKED
    primary_source_00_internal_conflict: UNKNOWN_BLOCKED
    agent_may_resolve_00_internal_conflict_by_inference: false

  core_mappings:
    unknown_result_fails_closed: true
    unknown_scope_fails_closed: true
    unknown_file_change_fails_closed: true
    unknown_flow_class_fails_closed: true
    missing_evidence_blocks: true
    invalid_evidence_blocks_or_unknown_blocks: true
    contradictory_evidence_blocks_or_unknown_blocks: true
    validation_not_run_maps_to_not_run: true
    not_run_is_pass: false
    warning_is_clean_pass: false
    blocked_is_pass: false
    unknown_is_ok: false
    deferred_is_completion: false
    deferred_is_approval: false
    human_unavailable_requires_human_review_or_blocked: true

  status_boundaries:
    pass_is_not_approval: true
    pass_with_warnings_is_not_clean_pass: true
    blocked_is_not_pass: true
    unknown_blocked_is_not_pass: true
    not_run_is_not_pass: true
    deferred_is_not_pass: true
    deferred_is_not_completion: true
    deferred_is_not_approval: true
    deferred_required_item_blocks_downstream: true
    human_review_required_is_not_approval: true
    deferred_is_not_accepted: true
    deferred_is_not_rejected: true
    accepted_requires_human_decision: true
    rejected_requires_human_decision: true

  status_propagation_rules:
    upstream_blocked_blocks_downstream: true
    upstream_unknown_blocked_blocks_downstream: true
    upstream_not_run_does_not_satisfy_downstream: true
    upstream_deferred_blocks_downstream_if_required: true
    upstream_deferred_preserves_deferred_scope: true
    upstream_deferred_is_not_completion: true
    upstream_pass_is_not_approval: true
    upstream_pass_with_warnings_preserves_warnings: true
    upstream_accepted_is_scoped_to_human_decision: true
    readiness_does_not_start_next_task: true

  retroactive_applicability_operational_boundary:
    applies_from_build_step_0: true
    automatic_prior_artifact_invalidation: false
    automatic_prior_artifact_rewrite: false
    automatic_lifecycle_mutation: false
    prior_artifact_review_requires_authorized_review_task: true
    task_3_2_reviews_prior_artifacts: false

  boundary_assertions:
    this_contract_is_not_runtime: true
    this_contract_is_not_validator: true
    this_contract_is_not_governance_control_module_implementation: true
    this_contract_is_not_code_assembly_pipeline: true
    this_contract_is_not_lifecycle_mutation: true
    this_contract_is_not_approval: true
    this_contract_does_not_start_task_3_3: true
    this_contract_does_not_start_build_step_4: true

  self_verification:
    all_required_status_mappings_present_verified_by_agent_self_check: true
    self_verification_is_spec_level_only: true
    self_verification_is_not_runtime_enforcement: true
    self_verification_is_not_validator_execution: true
    self_verification_is_not_human_approval: true
```

## Final Rule
This contract defines fail-closed status behavior and must not be weakened by later automation, templates, reports, validators, runtime, or governance logic. If a later task cannot prove readiness and safety, it must fail closed rather than reinterpret unsafe states as PASS, approval, completion, or authorization.
