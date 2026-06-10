# ACTIVE TASK TEMPLATE

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

Agent may read `tasks/backlog/` as context.

Agent may execute only the task referenced in `active_task_path`.

Agent must not execute any other backlog task.

Agent must not auto-proceed to the next task.

Agent must not create approval.

Agent must not simulate human checkpoint.

After completion, agent must create the required report and stop.
