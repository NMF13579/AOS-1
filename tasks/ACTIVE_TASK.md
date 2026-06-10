# ACTIVE TASK

```yaml
active_task_id: ""
active_task_path: ""
status: NOT_ACTIVE
execution_allowed: false
human_authorized_current_task_only: false
agent_may_execute_backlog: false
approval_created: false
next_task_started: false
```

## Execution Authority

No task is currently active.

Agent may read `tasks/backlog/` as context only.

Agent must not execute any backlog task.

Agent must not auto-select a task.

Agent must not auto-proceed to the next task.

Agent must not create approval.

Agent must not simulate human checkpoint.
