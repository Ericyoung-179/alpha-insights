"""Stage 2: Framing 验证器"""

from .common import ValidationResult, file_exists, file_contains_keyword, count_pattern, load_state


def validate(workspace):
    r = ValidationResult(2)
    f = "research_definition.md"

    if not file_exists(workspace, f):
        r.fail(f"{f} 不存在")
        return r
    r.pass_check(f"{f} 存在")

    # 必须含子问题
    has_subq = (
        file_contains_keyword(workspace, f, "子问题")
        or file_contains_keyword(workspace, f, "sub-question")
        or file_contains_keyword(workspace, f, "Q1")
    )
    if has_subq:
        r.pass_check("含子问题")
    else:
        r.fail("未检测到子问题")

    # 必须含透镜分配
    has_lens = (
        file_contains_keyword(workspace, f, "透镜")
        or file_contains_keyword(workspace, f, "lens")
        or file_contains_keyword(workspace, f, "分析透镜")
    )
    if has_lens:
        r.pass_check("含透镜分配")
    else:
        r.fail("未检测到透镜分配（分析透镜 / lens）")

    # WARN: 框架数量
    framework_count = count_pattern(workspace, f, r"(?:框架|framework|模型|model)")
    if framework_count < 2:
        r.warn(f"框架/模型提及仅 {framework_count} 次，建议至少 2 个框架")

    # WARN: IQR 复核（从 _state.json 读取，不从 deliverable 文件搜索）
    state = load_state(workspace)
    if state and state.get("iqr_results"):
        iqr_data = state["iqr_results"].get("2")
        if iqr_data:
            result = iqr_data.get("result", "unknown")
            if result == "BLOCK":
                r.fail("IQR 复核阻断（BLOCK）— 需修复后重新提交")
            elif result in ("PASS", "REVISE"):
                r.pass_check(f"IQR 复核已执行（{result}）")
            else:
                r.warn(f"IQR 复核结果异常: {result}")
        else:
            r.warn("未检测到 Stage 2 IQR 复核记录（建议执行独立质量复核）")
    else:
        r.warn("未检测到 IQR 复核记录（建议执行独立质量复核）")

    return r
