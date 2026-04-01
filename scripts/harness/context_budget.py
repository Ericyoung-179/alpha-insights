#!/usr/bin/env python3
"""
Alpha Insights — Context Budget Estimator

估算当前 workspace 产物的 token 消耗，给出压缩建议。

用法:
    python3 context_budget.py <workspace>
"""

import json
import os
import sys

# 粗略估算：1 个中文字 ≈ 1.5 token，1 个英文词 ≈ 1.3 token
# 简化为：1 字符 ≈ 0.5 token（中英混合场景的经验值）
CHARS_PER_TOKEN = 2.0

# Claude 有效上下文预算（保守估计，给 SKILL 指令和对话留空间）
CONTEXT_BUDGET_TOKENS = 150000  # 约 150K token 可用于产物

# 各文件的权重和压缩策略
FILE_CONFIG = {
    "user_brief.md": {"stage": 1, "compress": "aggressive", "keep_summary": True},
    "research_definition.md": {"stage": 2, "compress": "aggressive", "keep_summary": True},
    "research_plan.md": {"stage": 3, "compress": "aggressive", "keep_summary": True},
    "evidence_base.md": {"stage": 4, "compress": "moderate", "keep_summary": True},
    "insights.md": {"stage": 5, "compress": "never", "keep_summary": False},
    "report.html": {"stage": 6, "compress": "skip", "keep_summary": False},
}


def estimate_tokens(text):
    return len(text) / CHARS_PER_TOKEN


def analyze_workspace(workspace):
    files = {}
    total_chars = 0
    total_tokens = 0

    for filename, config in FILE_CONFIG.items():
        path = os.path.join(workspace, filename)
        if os.path.isfile(path):
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            chars = len(content)
            tokens = estimate_tokens(content)
            files[filename] = {
                "exists": True,
                "chars": chars,
                "estimated_tokens": int(tokens),
                "stage": config["stage"],
                "compress_strategy": config["compress"],
            }
            total_chars += chars
            total_tokens += tokens
        else:
            files[filename] = {"exists": False, "stage": config["stage"]}

    budget_pct = (total_tokens / CONTEXT_BUDGET_TOKENS) * 100

    # 压缩建议
    recommendation = "none"
    compress_stages = []

    if budget_pct > 80:
        recommendation = "urgent"
        compress_stages = [1, 2, 3, 4]
    elif budget_pct > 60:
        recommendation = "recommended"
        compress_stages = [1, 2, 3]
    elif budget_pct > 40:
        recommendation = "optional"
        compress_stages = [1, 2]

    return {
        "total_chars": total_chars,
        "estimated_tokens": int(total_tokens),
        "budget_total": CONTEXT_BUDGET_TOKENS,
        "budget_pct": round(budget_pct, 1),
        "recommendation": recommendation,
        "compress_stages": compress_stages,
        "files": files,
    }


def main():
    if len(sys.argv) < 2:
        print("用法: python3 context_budget.py <workspace>")
        sys.exit(1)

    workspace = sys.argv[1]
    if not os.path.isdir(workspace):
        print(json.dumps({"error": f"目录不存在: {workspace}"}, ensure_ascii=False))
        sys.exit(1)

    result = analyze_workspace(workspace)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
