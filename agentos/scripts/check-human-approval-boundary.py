import sys
import json
import os

def print_result(json_mode, result_code, exit_code, **kwargs):
    if json_mode:
        output = {
            "result": result_code,
            "exit_code": exit_code,
            "approval_file": kwargs.get("approval_file"),
            "decision": kwargs.get("decision"),
            "actor_type": kwargs.get("actor_type"),
            "selected_by_human": kwargs.get("selected_by_human"),
            "agent_generated": kwargs.get("agent_generated"),
            "allowed": result_code == "CAP002_APPROVAL_BOUNDARY_PASS",
            "blocked_reason": result_code if result_code != "CAP002_APPROVAL_BOUNDARY_PASS" else None,
            "human_approval_simulated": False
        }
        print(json.dumps(output, indent=2))
    else:
        print(result_code)
    sys.exit(exit_code)

def main():
    json_mode = "--json" in sys.argv
    
    if "--approval-file" not in sys.argv:
        print_result(json_mode, "CAP002_APPROVAL_BOUNDARY_ERROR", 2)
        
    try:
        idx = sys.argv.index("--approval-file")
        approval_file = sys.argv[idx + 1]
    except (ValueError, IndexError):
        print_result(json_mode, "CAP002_APPROVAL_BOUNDARY_ERROR", 2)

    if not os.path.exists(approval_file):
        print_result(json_mode, "CAP002_APPROVAL_BOUNDARY_BLOCKED_MISSING_APPROVAL", 1, approval_file=approval_file)

    try:
        with open(approval_file, "r") as f:
            content = f.read()
            
            def dict_raise_on_duplicates(ordered_pairs):
                d = {}
                for k, v in ordered_pairs:
                    if k in d:
                        raise ValueError("duplicate key")
                    d[k] = v
                return d
            
            data = json.loads(content, object_pairs_hook=dict_raise_on_duplicates)

    except ValueError as e:
        if "duplicate key" in str(e):
            print_result(json_mode, "CAP002_APPROVAL_BOUNDARY_BLOCKED_AMBIGUOUS_APPROVAL", 1, approval_file=approval_file)
        print_result(json_mode, "CAP002_APPROVAL_BOUNDARY_BLOCKED_MALFORMED_APPROVAL", 1, approval_file=approval_file)
    except Exception:
        print_result(json_mode, "CAP002_APPROVAL_BOUNDARY_BLOCKED_MALFORMED_APPROVAL", 1, approval_file=approval_file)

    if not isinstance(data, dict):
        print_result(json_mode, "CAP002_APPROVAL_BOUNDARY_BLOCKED_MALFORMED_APPROVAL", 1, approval_file=approval_file)

    required_fields = [
        "approval_id", "task_id", "capability_id", "decision", 
        "actor_type", "selected_by_human", "human_decision_reference", "agent_generated"
    ]
    for field in required_fields:
        if field not in data:
            print_result(json_mode, "CAP002_APPROVAL_BOUNDARY_BLOCKED_MISSING_REQUIRED_FIELD", 1, approval_file=approval_file)
            
    actor_type = data.get("actor_type")
    selected_by_human = data.get("selected_by_human")
    agent_generated = data.get("agent_generated")
    decision = data.get("decision")
    
    kwargs = {
        "approval_file": approval_file,
        "decision": decision,
        "actor_type": actor_type,
        "selected_by_human": selected_by_human,
        "agent_generated": agent_generated
    }

    if actor_type != "human":
        print_result(json_mode, "CAP002_APPROVAL_BOUNDARY_BLOCKED_NON_HUMAN_ACTOR", 1, **kwargs)

    if selected_by_human is not True:
        print_result(json_mode, "CAP002_APPROVAL_BOUNDARY_BLOCKED_NOT_SELECTED_BY_HUMAN", 1, **kwargs)

    if agent_generated is not False:
        print_result(json_mode, "CAP002_APPROVAL_BOUNDARY_BLOCKED_AGENT_GENERATED", 1, **kwargs)

    if decision != "APPROVED":
        print_result(json_mode, "CAP002_APPROVAL_BOUNDARY_BLOCKED_DECISION_NOT_APPROVED", 1, **kwargs)
        
    print_result(json_mode, "CAP002_APPROVAL_BOUNDARY_PASS", 0, **kwargs)

if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except Exception:
        json_mode = "--json" in sys.argv
        print_result(json_mode, "CAP002_APPROVAL_BOUNDARY_ERROR", 2)
