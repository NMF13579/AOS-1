# Raw Execution Evidence Bundle

```yaml
raw_evidence_bundle:
  trial_id: "TRIAL-BS6-DOGFOOD-1"
  candidate_id: "CANDIDATE-1-GITIGNORE"

  authorization_reference: "Task 6.6 Human Decision"
  package_reference: "agentos/reports/build-step-6/documentation-assembly-package.md"
  package_sha256: "37b2c61533f6224cc28e55420fc9ac0e9889610929ac3636ba7af526a9dc96cc"

  baseline_commit: "defecbf69be7d025867002e68c846eea66e5e220"
  working_tree_before: "Clean with untracked agentos/reports/build-step-6/"
  working_tree_after: "M .gitignore"

  authorized_paths:
    - ".gitignore"
  forbidden_paths:
    - "agentos/pipelines/**"
    - "agentos/approvals/**"
    - "agentos/reports/**"
    - "agentos/code-assembly/**"
  changed_paths:
    - ".gitignore"

  pre_change_hashes:
    - path: ".gitignore"
      sha256: "838fa69eabe5507048791975a67700c32d5ec1808144c3038dcac8e5411475db"
  post_change_hashes:
    - path: ".gitignore"
      sha256: "57da111d4c40a95d6dbe6f3b7163ab1b5f3974caf838b8fbc83375d8160e4ebe"
  diff_reference: "Inline Diff Below"

  performed_actions:
    - "Appended .coverage and htmlcov/ to .gitignore"
    - "Generated dummy .coverage and htmlcov/ files"
    - "Ran validation command (git status)"
    - "Removed dummy coverage files"
  commands:
    - "shasum -a 256 .gitignore"
    - "git diff .gitignore"
    - "touch .coverage && mkdir htmlcov && touch htmlcov/index.html && git status --short && rm -rf .coverage htmlcov"
  exit_codes:
    - 0

  validation_results:
    - command: "git status"
      result: "PASS"
  not_run_items: []
  unknowns: []
  warnings: []
  blockers: []

  scope_conflict_detected: false
  stop_record_present: false
  rollback_performed: false

  evidence_capture_status: "COMPLETE"
```

## Inline Diff
```diff
diff --git a/.gitignore b/.gitignore
index e17f6d5..3c2b7db 100644
--- a/.gitignore
+++ b/.gitignore
@@ -12,3 +12,7 @@
 __pycache__/
 *.pyc
 .DS_Store
+
+# Test coverage
+.coverage
+htmlcov/
```
