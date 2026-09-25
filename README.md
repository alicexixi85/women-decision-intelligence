# Women Decision Intelligence · 女性高成就者决策智库

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Cases](https://img.shields.io/badge/cases-22-blue)](cases/)
[![YAML Validated](https://img.shields.io/badge/YAML-validated-green)](.github/workflows/validate.yml)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

> **An AI agent skill for real-world decision support, built on 22 panoramic life cases of women high-achievers.**
> 基于 22 位女性高成就者全景人生案例的 AI 决策智能 Skill：不默认男性成功路径可迁移，把生育窗口、照护责任、资本偏见、年龄与社会评价等女性特有结构性变量单独建模，输出严谨、可迁移、带风险边界的决策推演。

**不默认男性成功路径具有普遍可迁移性。必须把女性真实人生中的资源条件、社会结构、家庭关系、生育窗口、年龄、照护责任、婚姻/伴侣、财富积累、职业路径、社会评价、性别偏见、融资环境以及人生阶段等因素单独建模。用大量真实女性高成就者的完整人生案例，形成一个可以用于现实决策的案例型决策智库。**

Works with **Claude / Claude Code, Antigravity, and any AI agent** that supports skill files.

---

## Why this exists · 为什么需要它

Traditional career and business decision models have three fatal flaws:

1. **Male-as-Default Bias（男性常模偏差）**：默认创业者拥有无休止的时间精力、默认没有无偿家务与生育哺乳负担、默认社会人脉网络与权力背书天然开放。
2. **Chicken-Soup Degeneration（女性主义口号化）**：把系统性困境降维成心理激励（"要勇敢、要有野心、拒绝内耗"），既无操作抓手，又遮蔽真实的结构性成本。
3. **Context Flattening（商业成功单一化）**：把女性人生扁平化为"估值"或"融资额"，隐去关键决策背后的真实年龄、生育窗口、婚姻变故、老人照护、健康透支与终身代价。

**This skill's goal**: a decision intelligence system grounded in panoramic real-life cases of women, modeling women-specific structural variables explicitly — outputting rigorous, transferable strategy options with clear risk boundaries. Not success stories. Decision infrastructure.

---

## What's inside · 内容一览

| 模块 | 内容 | 规模 |
|---|---|---|
| `SKILL.md` | Skill 主定义：触发条件、8 步决策工作流、核心防线原则 | 1 |
| `cases/` | 女性全息案例 YAML 档案（公开事实 + 决策结构 + 可迁移性判定 + 证据分级） | **22** |
| `frameworks/` | 核心约束与推演理论模型（约束/人生阶段/资本/家庭/职业/可迁移性） | 6 |
| `categories/` | 8 大领域深度决策逻辑（创业/财富/投资/科技/媒体/消费/领导力/重构） | 8 |
| `playbooks/` | 6 大场景化实操行动指南（转轨/创业/财富/重启/投资/IP） | 6 |
| `decision_rules.md` | 严密推理逻辑与质检守则（推理铁律） | 1 |
| `evaluation/` | 验证基准：典型决策场景实测集 + 真实案例平行推演沙盘 | 2 |
| `rubric.json` | 决策系统评估标准打分卡 | 1 |

每份案例档案统一包含 14 个结构化字段：`identity`（身份）· `background`（出身与起点）· `life_stage`（人生阶段）· `constraints`（十维约束）· `career`（职业与资本路径）· `key_decisions`（关键决策：情境/备选项/风险/动因/结果）· `failures`（失败）· `turning_points`（转折点）· `relationships_and_power`（关系与权力）· `wealth`（财富结构）· `decision_patterns`（可复用决策模式）· `anti_patterns`（反模式）· `transferability`（三级可迁移性判定）· `evidence`（信源与证据分级：documented fact / attributed statement / interpretation / inference）。

---

## Case library · 案例库（22）

| # | 人物 | 一句话标签 | 类型 |
|---|---|---|---|
| 1 | Sara Blakely | Spanx 创始人：5000 美元白手起家，零外部融资，100% 所有权 | 正面 |
| 2 | Estée Lauder（雅诗·兰黛） | 美妆帝国：线下触点式销售、品牌心智沉淀、家族传承 | 正面 |
| 3 | Oprah Winfrey（奥普拉） | 传媒帝国：极低起点逆袭，收回所有权（Harpo），版权即权力 | 正面 |
| 4 | Melanie Perkins | Canva 创始人：澳洲年轻女性，经历 100+ 次 VC 拒绝，产品先行 | 正面 |
| 5 | Whitney Wolfe Herd | Bumble 创始人：职场危机后绝地反击，女性友好型社交产品 | 正面 |
| 6 | Rihanna（蕾哈娜） | Fenty Beauty：娱乐顶流向百亿实业跃迁，包容性美妆颠覆品类 | 正面 |
| 7 | Madam C.J. Walker | 首位非裔女性百万富翁：零资源起步，建立数万女性代理网络 | 正面 |
| 8 | Arianna Huffington | 55 岁创办赫芬顿邮报，严重倦怠后创立 Thrive Global | 正面 |
| 9 | 董明珠 | 格力：36 岁单亲妈妈南下做销售，销售回款铁律，权力掌控 | 正面 |
| 10 | 陶华碧 | 老干妈：42 岁不识字寡母起步，零负债、强现金流壁垒 | 正面 |
| 11 | 张茵 | 玖龙纸业：借款 3 万元起步，废纸原料控制，穿越周期 | 正面 |
| 12 | Diane Hendricks | ABC Supply：单亲妈妈起步，危机后独掌百亿集团 | 正面 |
| 13 | Cathie Wood（凯茜·伍德） | ARK Invest：58 岁遭遇职场瓶颈后创立，主题投资与极高争议 | 正面 |
| 14 | Muriel Siebert | 首位纽交所女性会员，单挑华尔街全男性封闭俱乐部 | 正面 |
| 15 | 李飞飞（Fei-Fei Li） | ImageNet：移民贫困起步，学术破局，斯坦福 AI 与创业 | 正面 |
| 16 | 苏姿丰（Lisa Su） | AMD CEO：半导体技术领袖，带领破产边缘的 AMD 逆风翻盘 | 正面 |
| 17 | Indra Nooyi | 百事 CEO：跨国巨头掌舵，传统母职期待与商业权力的撕扯代价 | 正面 |
| 18 | J.K. Rowling | 单亲贫困救济金起步，严格守住版权控制权实现财富跨越 | 正面 |
| 19 | 李子柒（Li Ziqi） | 农村低起点顶流：遭遇 MCN 股权与品牌控制权断裂、重组 | 正面 |
| 20 | Coco Chanel（可可·香奈儿） | 孤儿院底层起步，借力阶层网络重构女性服饰，品牌权力控制 | 正面 |
| 21 | 何巧女 | 东方园林疯狂加杠杆，PPP 概念陷阱导致债务崩塌 | 警示 |
| 22 | Elizabeth Holmes | Theranos 技术造神与欺诈，迎合权贵虚妄预期的代价 | 警示 |

> 案例覆盖不同年代、国别、阶层与资本路径，并刻意纳入反面警示案例——决策智库的价值一半在"什么路走得通"，一半在"什么坑不能踩"。

---

## Quick start · 快速上手

### 方式一：作为 Claude / Claude Code Skill 使用

```bash
git clone https://github.com/alicexixi85/women-decision-intelligence.git
# 放到你的 skills 目录（Claude Code 默认读取 ~/.claude/skills/）
cp -r women-decision-intelligence ~/.claude/skills/women-decision-intelligence
```

之后直接对 AI 提问，Skill 会自动激活 8 步决策工作流。

### 方式二：Antigravity / 其他 AI Agent

把 `SKILL.md` 作为 system prompt 或 skill 文件导入，并将 `cases/`、`frameworks/`、`playbooks/` 目录作为知识库挂载即可。仓库根目录的 `SKILL.md` 即完整 Skill 定义。

### 方式三：直接阅读研究

`cases/*.yaml` 是独立可读的结构化档案，`frameworks/` 是理论模型，`playbooks/` 是场景行动指南——不需要跑 Agent 也可作为研究资料使用。

---

## Architecture · 六层决策架构

```text
┌─────────────────────────────────────────────────────────────┐
│ Layer 6: Decision Playbook (战略推演与选项沙盘 Option A/B/C) │
├─────────────────────────────────────────────────────────────┤
│ Layer 5: Decision Comparison & Transferability (可迁移性矩阵) │
├─────────────────────────────────────────────────────────────┤
│ Layer 4: Multi-Dimensional Case Retrieval (多维情境匹配) │
├─────────────────────────────────────────────────────────────┤
│ Layer 3: Decision & Anti-Patterns (真实规律与致命陷阱提炼) │
├─────────────────────────────────────────────────────────────┤
│ Layer 2: Female-Specific Constraint Model (女性特有约束建模) │
├─────────────────────────────────────────────────────────────┤
│ Layer 1: Female Case Knowledge Base (全景真实人物 YAML 档案)│
└─────────────────────────────────────────────────────────────┘
```

- **Layer 1 · 真实案例知识层**：22 份女性 YAML 全息档案（含正面与反面警示案例），严格标注信源级别。
- **Layer 2 · 女性特有约束模型**：生育/生物窗口、家庭无偿照护、资本偏见与防御型提问、年龄与性别双重社会评价作为显性变量。
- **Layer 3 · 决策模式与反模式**：提炼"兼职启动验证""以造血抗风险""所有权控制权闭环"等模式，建立反面警示。
- **Layer 4 · 多维情境检索**：按用户年龄、家庭负荷、流动资产、行业属性做相似情境交叉检索，而非按名气检索。
- **Layer 5 · 决策对照与可迁移性**：9 维对照表，划分高度可迁移 / 环境依赖型 / 不可迁移要素。
- **Layer 6 · 决策行动剧本**：输出含显性收益、隐性牺牲、前置条件与止损边界的多元路径，交由用户自主决策。

核心防线（详见 `SKILL.md` 与 `decision_rules.md`）：**男性案例隔离原则**（不默认男性路径可迁移）· **反鸡汤协议**（禁空洞口号，只谈事实与权衡）· **证据分级与隐私克制**（事实/引言/分析/推论四级标注，家庭变量仅在有可靠公开信源且直接影响决策时纳入）。

---

## Example prompts · 典型提问

- *"我今年 38 岁，在传统大厂担任中层，有两个小孩需要照顾，手里有 100 万现金，想辞职做独立品牌但担心现金流和精力崩盘——历史上有相似处境的女性吗？"*
- *"45 岁遭遇职业断崖，如何在中年重新积累财富？有哪些真实女性走通过这条路？"*
- *"女性在科技和硬件领域融资，常被投资人问防御性问题（风险控制而非市场规模），如何破局？"*
- *"没有伴侣或家庭的资金人脉支持，白手起家有哪些真正被验证过的路径？"*

系统将启动 8 步工作流：情境参数提取 → 约束建模 → 案例检索 → 模式对照 → 可迁移性判定 → 多路径推演 → 风险边界 → 行动剧本。

---

## Roadmap · 路线图

- [] 案例库从 22 扩充至 50+（增加东南亚、拉美、非洲女性创业者；增加普通高成就女性样本，不止名人富豪）
- [] 每个案例的关键决策从 2 个扩充至 5–8 个，信源从书目级细化到可核查引文（页码/链接）
- [] `evaluation/` 实测集扩充为可运行的 regression suite
- [] 多语言：英文版案例摘要（cases/en/）
- [] 提交 awesome-claude-skills 等 Skill 目录收录

---

## Contributing · 参与贡献

欢迎提交新的女性案例档案（请严格遵循 `cases/` 现有 14 字段 schema 与 `evidence` 四级证据标注），或补充 frameworks / playbooks。详见 [CONTRIBUTING.md](CONTRIBUTING.md)。所有 YAML/JSON 提交都会经过 CI 自动校验（`.github/workflows/validate.yml`）。

## License · 协议

[MIT License](LICENSE) — 可自由使用、修改、分发，含商业用途。

## Citation · 引用

```bibtex
@misc{women-decision-intelligence,
title = {Women Decision Intelligence: an AI agent skill for real-world
decision support based on women high-achievers' life cases},
author = {alicexixi85},
year = {2026},
url = {https://github.com/alicexixi85/women-decision-intelligence}
}
```

---

*Built for women facing real decisions — not success stories, but decision infrastructure.*
*为面临真实抉择的女性而建：不要成功学，要决策基础设施。*
