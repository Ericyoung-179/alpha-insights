#!/usr/bin/env python3
"""Hook 1: PreToolUse on Read|Bash|Grep|Glob — context budget auto-warning.

Thresholds:
- >90% → block tool execution, demand compression first
- >70% → inject warning message, allow execution
- ≤70% → silent pass
"""

import json
import os
import sys

# Add harness parent dir to path so we can import sibling modules
_HARNESS_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _HARNESS_DIR not in sys.path:
    sys.path.insert(0, _HARNESS_DIR)

from hooks._workspace_finder import find_workspace  # noqa: E402


def main():
    try:
        data = json.loads(sys.stdin.read())
    except Exception:
        return  # malformed input → fail open

    cwd = data.get("cwd") or ""
    workspace = find_workspace(cwd)
    if not workspace:
        return  # no workspace found → nothing to check

    # Import analyze_workspace from harness/context_budget.py
    from context_budget import analyze_workspace  # noqa: E402

    result = analyze_workspace(workspace)
    pct = result.get("budget_pct", 0)

    if pct > 90:
        compress_stages = result.get("compress_stages", [])
        stages_str = ", ".join(str(s) for s in compress_stages)
        json.dump({
            "decision": "block",
            "reason": (
                f"🚨 Context 预算已用 {pct}%，严重超载！\n"
                f"必须先压缩 Stage {stages_str} 的产物再继续。\n"
                f"请执行: python3 scripts/harness/compress_stage.py "
                f"{workspace} --all"
            ),
        }, sys.stdout, ensure_ascii=False)
    elif pct > 70:
        compress_stages = result.get("compress_stages", [])
        stages_str = ", ".join(str(s) for s in compress_stages)
        json.dump({
            "decision": "allow",
            "message": (
                f"⚠️ Context 预算已用 {pct}%，建议尽快压缩 Stage {stages_str} 的产物。\n"
                f"当前总 token 估算: {result.get('estimated_tokens', 0):,} / "
                f"{result.get('budget_total', 0):,}"
            ),
        }, sys.stdout, ensure_ascii=False)
    # ≤70% → silent pass (no output)


if __name__ == "__main__":
    try:
        main()
    except Exception:
        sys.exit(0)  # fail open
