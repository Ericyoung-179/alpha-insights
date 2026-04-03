# Changelog

## V2.0.5 (2026-04-03)

> **五层深度审计 + 全量修复**：对 75 文件执行 L-A 术语一致性 / L-B 框架结构一致性 / L-C 执行流模拟 / L-D 脚本健壮性 / L-E 缺失内容审计，共识别 42 项问题（8 HIGH + 27 MEDIUM + 7 LOW），全部修复。

### 修复：执行可靠性

- `state_manager.py` / `dashboard.py` — `_load_state()` 增加 `json.JSONDecodeError` 容错，损坏的 `_state.json` 不再导致流程崩溃
- `report_helper.py` — `_to_js()` 字符串转义补充 `\r` / `\t`，修复含特殊字符的图表标签渲染异常
- ReportBuilder 状态文件路径从 `/tmp/rpt_{project}.json` 改为 `{ws}/_rpt_state.json`，解决跨平台 + 重启后状态丢失

### 修复：执行一致性

- SKILL.md Stage 6 自检项数 5→7，与 `report_standards.md` 对齐
- Track A+B 并行写入保护：Subagent 结果统一返回主 Session 写入 `evidence_base.md`
- Agent/Subagent 不可用时的降级路径：主 Session 串行执行
- 红蓝队 Subagent 增加 Agent 工具不可用时的 fallback 说明

### 新增：交付物模板 & 边缘情况

- SKILL.md 补充 `user_brief.md` / `research_definition.md` 结构模板，Stage 1-2 交付物格式可追溯
- 边缘情况表新增 5 条：用户否决全部洞察、中途换议题、`_state.json` 损坏恢复、Agent 不可用降级、Bash 不可用降级
- `judgment_rules.md` 四维评分表补 3 分锚点（具体性/独特性/可执行性/影响力）
- `judgment_rules.md` Step 2 用户否决洞察回退机制
- `research_engine.md` 空结果处理规则（扩展关键词重试 → 标注证据缺口）

### 修复：内容补全

- `methodology/mece.md` 补「输出格式」章节，与其他方法论文件结构对齐
- `report_standards.md` 补洞察分级说明（A 类 18-20 分 / B 类 16-17 分），与 Stage 5 `insights.md` 对齐
- `research_engine.md` 修复「知识库搜索搜索」重复词 typo

---

## V2.0 (2026-04-01)

> **核心升级理念**：Harness Engineering — 不过度投资 prompt，投资执行环境。通过脚本验证 + 状态机 + Hook 自动化 + 上下文压缩，从外部约束执行质量，把"AI 应该做"变成"系统保证做"。

### 新增：Harness 执行引擎（`scripts/harness/`）

**状态管理**
- `state_manager.py` — Workspace 初始化 + `_state.json` 状态机，追踪研究阶段、档位、框架加载、访谈状态等全流程元数据

**六阶段验证器**（`validators/stage1-6.py`）
- 每个 Stage 的交付物自动验证，PASS/FAIL/WARN 三级判定
- Tier 感知：Tier 2+ 对红蓝队审查、ECharts 图表数量等执行更严格的 FAIL 级校验
- Stage 5 验证器最为完善：评分检测 + 红蓝队审查 + 实质挑战 + So What 链深度 + Pre-mortem + SMART + 用户确认 + 关键变量 + 行动建议（共 13 项检查）

**Context 管理**
- `context_budget.py` — 估算 workspace 产物总 token 占用，预警 70%/90% 阈值
- `compress_stage.py` — 按 Stage 压缩产物（保留 A/B 级证据摘要），释放上下文空间

**质量仪表盘**
- `dashboard.py` — Stage 5→6 转场前，汇总 S2-S5 四阶段质量指标，一屏呈现

**会话恢复**
- `resume_check.py` — SKILL 加载时自动扫描进行中的研究 workspace，提示用户继续而非重新开始

### 新增：Hook 自动化系统

SKILL.md frontmatter 声明 4 个 Hook，平台自动执行：

| Hook | 触发时机 | 功能 |
|------|---------|------|
| `html_write_guard.py` | PreToolUse:Write | 阻止 Write 工具直接输出 HTML（必须用 Bash+Python） |
| `context_budget_hook.py` | PreToolUse:Read/Bash/Grep/Glob/Edit | 上下文预算实时预警，>90% 自动阻断 |
| `stage_gate_hook.py` | PostToolUse:Write | 写入交付物后自动运行门控验证 |
| `progress_logger.py` | PostToolUse:* | 异步记录工具调用日志（`_hook_log.jsonl`） |

共享模块：`_workspace_finder.py` — 从 cwd 智能定位 workspace 目录，支持多种回退策略。

### 新增：独立质量复核（IQR）

- `resources/quality_review.md` — Stage 2/4/6 三阶段 IQR 模板
- 独立 Subagent 评审，按 PASS/REVISE/BLOCK 处理
- Tier 2+ 自动触发

### 新增：ReportBuilder 分步生成器

- `scripts/report_helper.py` — `ReportBuilder` 类，分步构建 HTML 报告
- 自动生成封面、目录、章节头、尾页、ECharts 初始化代码
- `values→data` 自动映射，绕过模型输出层对 `data` 关键字的过滤
- 解决一次性生成大 HTML 的超时/截断问题

### 改进：SKILL.md V2.0 重构

**Stage 转场协议**
- 每个 Stage 开始时强制执行：Workspace 路径恢复 + Context 恢复 + 位置播报
- 每个 Stage 结束时强制输出标准化转场块
- 全阶段门控条件表（FAIL 阻断 + WARN 提示）

**Stage 1**
- 新增背景预研究（2-3 次快速搜索）+ 一句话结论播报（禁止展示原始搜索结果）
- 三档产出档位（Tier 1/2/3）正式纳入工作流，影响后续所有 Stage

**Stage 3**
- Q→H 映射规则：每个假设标注对应子问题，无假设的子问题注明原因
- 访谈决策纳入确认流程（不可跳过）

**Stage 4**
- 框架分析结论独立产出（新增检查项）
- 访谈催收检查点（Stage 3.5 激活时自动触发）
- 轨道跳过必须告知用户原因

**Stage 5**
- 深度门控：So What 链 ≥3 层 + Red-Team 必须产出 ≥1 个 Substantive 级挑战
- 逐规则播报（禁止黑箱合并执行）
- 用户确认前置到规则 7 后、红蓝队前

**Stage 6**
- HTML 必须通过 Bash+Python 生成（硬性规则，Hook 自动阻断 Write .html）
- ReportBuilder 分步生成（每步 1-2 章，避免超时）
- Tier 2+ 要求 ≥3 个 ECharts 交互图表（FAIL 级校验）

**Stage 7B 收尾**
- 精简收尾模板：议题 + 档位 + 报告路径 + 核心发现 + Star/Issue 链接
- 语雀使用记录自动追加（`doc_id: 532511097`），静默执行不打扰用户

### 改进：数据源与搜索

- `resources/research_engine.md` — Track 标签统一修正（A→G），执行顺序明确
- XHS 脚本端点迁移（`check_topics.js`、`search_notes.js`、`get_note.js`）
- 语雀 Track D 搜索集成

### 改进：洞察质量

- `resources/judgment_rules.md` — insights.md 产出模板标准化，评分格式统一为 `= XX 分`
- 红蓝队 Subagent 模板细化，挑战分级（Fatal/Substantive/Weak/Addressable）

### 架构原则

- **优雅降级**：Bash 不可用时（如 Openclaw 环境），所有 Harness 功能回退到 V1 纯指令行为，不阻断工作流
- **Fail Open**：所有 Hook 和验证脚本在异常时静默放行
- **自包含**：禁止调用外部 SKILL，Alpha Insights 必须独立可用

### 文件清单

```
scripts/harness/
├── state_manager.py          # 状态机
├── stage_gate.py             # 验证器统一入口
├── context_budget.py         # 上下文预算分析
├── compress_stage.py         # 产物压缩
├── dashboard.py              # 质量仪表盘
├── resume_check.py           # 会话恢复
├── validators/
│   ├── __init__.py
│   ├── common.py             # 共享工具 + ValidationResult
│   ├── stage1.py ~ stage6.py # 六阶段验证器
└── hooks/
    ├── __init__.py
    ├── _workspace_finder.py  # 共享 workspace 定位
    ├── html_write_guard.py   # HTML 写入防护
    ├── context_budget_hook.py# 上下文预警
    ├── stage_gate_hook.py    # 自动门控
    └── progress_logger.py    # 进度日志

scripts/report_helper.py      # ReportBuilder + build_report()

resources/quality_review.md   # IQR 模板（新增）
```

---

## V1.0 (2026-03-26)

初始发布。七阶段工作流 + 19 框架 + 9 方法论 + 8 条判断力规则 + 三档产出 + HTML 报告。详见 [GitHub Release](https://github.com/Ericyoung-183/alpha-insights)。
