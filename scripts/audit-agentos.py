import os
import re
import sys

def main():
    llms_path = 'llms.txt'
    all_passed = True
    errors = 0

    def print_check(msg, status):
        print(f"[CHECK] {msg} ... {status}")

    # 1. Check existence
    if os.path.exists(llms_path):
        print_check("llms.txt exists", "OK")
    else:
        print_check("llms.txt exists", "FAIL")
        print("AUDIT RESULT: FAIL")
        sys.exit(1)

    with open(llms_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 2. Check section present
    if "## Advisory Model Selection" in content:
        print_check("Advisory Model Selection section present", "OK")
    else:
        print_check("Advisory Model Selection section present", "FAIL")
        all_passed = False
        errors += 1

    # 3. Check duplicate headers
    header_count = content.count("## Advisory Model Selection")
    if header_count == 1:
        print_check("No duplicate headers", "OK")
    else:
        print_check("No duplicate headers", f"FAIL (found {header_count})")
        all_passed = False
        errors += 1

    # 4. Check invariant present
    if "PASS ≠ approval" in content or "PASS != approval" in content:
        print_check("PASS != approval invariant present", "OK")
    else:
        print_check("PASS != approval invariant present", "FAIL")
        all_passed = False
        errors += 1

    # 5. Check concrete model names
    concrete_models = ['gpt-4', 'gpt-3', 'claude', 'sonnet', 'opus', 'haiku', 'gemini', 'llama', 'openai', 'anthropic', 'mistral', 'deepseek']
    content_lower = content.lower()
    found_models = [m for m in concrete_models if m in content_lower]
    
    if not found_models:
        print_check("No concrete model names", "OK")
    else:
        print_check("No concrete model names", f"FAIL (found {', '.join(found_models)})")
        all_passed = False
        errors += 1

    if all_passed:
        print("AUDIT RESULT: PASS")
        sys.exit(0)
    else:
        print("AUDIT RESULT: FAIL")
        sys.exit(1)

if __name__ == '__main__':
    main()
