# Minimal Code Assembly Flow

## Purpose
Определяет минимальный manual-first flow для Task 5.1 без runtime enforcement, validator authority и auto-approval.

## Scope
Этот flow покрывает только:
- Task Brief intake
- Code Execution Package intake
- scope reflection
- baseline verification
- scoped change handling
- changed-path recording
- diff capture
- authorized checks recording
- Execution Report creation
- Evidence Report creation
- Human Review handoff

## Preconditions
Перед исполнением должны быть подтверждены:
- correct repository
- correct branch
- human-assigned Risk Profile
- execution authorization
- exact allowed write paths
- monitored paths readable
- known workspace state

## Flow Steps
1. Read Task Brief.
2. Read Code Execution Package.
3. Verify repository, branch, baseline commit and monitored paths.
4. Reflect scope against exact allowed paths and forbidden paths.
5. Apply only scoped code changes inside the allowed write list.
6. Record changed paths.
7. Capture diff.
8. Run only authorized checks.
9. Create Execution Report.
10. Create Evidence Report.
11. Create Human Review handoff.

## Fail-Closed Rules
- Unknown scope -> stop.
- Branch mismatch -> stop.
- Missing authorization -> stop.
- Unexpected monitored-path change -> `CONCURRENT_CHANGE_BLOCKED`.
- Forbidden path write -> stop.
- `NOT_RUN` must be recorded explicitly.
- PASS does not equal approval.
- Evidence does not equal approval.

## Output Artifacts
This flow expects:
- Execution Report
- Evidence Report
- Human Review handoff

## Non-Goals
This flow does not:
- approve work
- assign Risk Profile
- commit
- push
- merge
- release
- start Task 5.2
- implement validator
- implement runtime enforcement
