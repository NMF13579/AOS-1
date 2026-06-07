---
schema_version: 1
artifact_type: skeleton
status: draft
implementation_status: not_implemented
runtime_authority: false
source_of_truth: false
blocks_execution: true
created_for: A4.0-GR
agent_autonomy_mode: STRICT_GOVERNED_MODE
allowed_write_paths: []
forbidden_operations:
  - approval
  - lifecycle_mutation
  - protected_file_change
  - delete
  - move
  - rename
  - archive
  - commit
  - merge
  - next_stage_start
human_checkpoint_required_for:
  - protected_file_change
  - canonical_doc_change
  - delete
  - move
  - rename
  - archive
  - scope_expansion
---
