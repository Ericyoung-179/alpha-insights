"""Stage 1: Briefing 验证器"""

from .common import ValidationResult, file_exists, file_contains_keyword, file_line_count


def validate(workspace):
    r = ValidationResult(1)
    f = "user_brief.md"

    if not file_exists(workspace, f):
        r.fail(f"{f} 不存在")
        return r
    r.pass_check(f"{f} 存在")

    # 必须含议题
    has_topic = (
        file_contains_keyword(workspace, f, "议题")
        or file_contains_keyword(workspace, f, "研究问题")
        or file_contains_keyword(workspace, f, "topic")
        or file_contains_keyword(workspace, f, "question")
    )
    if has_topic:
        r.pass_check("含议题关键词")
    else:
        r.fail("未检测到议题/研究问题")

    # 必须含档位
    has_tier = (
        file_contains_keyword(workspace, f, "Tier")
        or file_contains_keyword(workspace, f, "档位")
        or file_contains_keyword(workspace, f, "tier")
    )
    if has_tier:
        r.pass_check("含档位信息")
    else:
        r.fail("未检测到档位(Tier)信息")

    # WARN: 背景描述行数
    lines = file_line_count(workspace, f)
    if lines < 3:
        r.warn(f"文件仅 {lines} 行，背景描述可能不充分")

    return r
