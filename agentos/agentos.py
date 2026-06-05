#!/usr/bin/env python3
import json
import sys

ALLOWED_COMMANDS = {"start", "status", "next", "help", "explain-blocker"}

BLOCKED_CAPABILITIES = [
    "runtime_implementation",
    "validation_authority",
    "execution",
    "repair",
    "install_update",
    "template_export",
    "approval_witness_handling",
    "cross_repo_behavior",
]


def emit_blocked(status, message, **extra):
    result = {
        "schema_version": 1,
        "result": "BLOCKED",
        "status": status,
        "runtime_ready": False,
        "execution_ready": False,
        "validation_ready": False,
        "clean_pass": False,
        "message": message,
        "next_safe_action": "implement_preflight_contract",
        "boundary": {
            "skeleton_is_not_implementation": True,
            "blocked_is_not_pass": True,
            "pass_is_not_approval": True,
        },
    }
    result.update(extra)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    sys.exit(1)


def main():
    if len(sys.argv) < 2:
        emit_blocked(
            "AGENTOS_COMMAND_MISSING_BLOCKED",
            "AgentOS command is missing. Use one of: start, status, next, help, explain-blocker.",
            allowed_skeleton_commands=sorted(ALLOWED_COMMANDS),
        )

    command = sys.argv[1]

    if command not in ALLOWED_COMMANDS:
        emit_blocked(
            "COMMAND_BLOCKED_IN_SKELETON",
            "This command is blocked because AgentOS is currently a skeleton and runtime behavior is not implemented.",
            blocked_command=command,
            blocked_capabilities=BLOCKED_CAPABILITIES,
            allowed_skeleton_commands=sorted(ALLOWED_COMMANDS),
        )

    emit_blocked(
        "A4_0_GR_SKELETON_ONLY",
        "AgentOS A4.0-GR skeleton exists. Runtime, execution, and validation are not implemented.",
        command=command,
    )


if __name__ == "__main__":
    main()
