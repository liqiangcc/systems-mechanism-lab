# System Mechanism White-box Learning Framework

> Status: **normative**  
> Scope: repository-wide  
> Detailed protocols: [`LEARNING_MECHANISM.md`](./LEARNING_MECHANISM.md) and [`LEARNING_BRANCH_WORKFLOW.md`](./LEARNING_BRANCH_WORKFLOW.md)

## 1. Purpose

本框架的目标不是最大化阅读量，而是把系统知识转换为可长期依赖的认知资产：

- 可以解释内部对象、状态、规则和因果链；
- 可以对条件变化做出预测；
- 可以通过来源和运行时现象进行验证；
- 可以被反例或更强证据修正；
- 可以追溯“为什么开始相信这条结论”；
- 可以迁移到其他系统，同时保留差异和边界。

最终产物不是章节摘要，而是**有来源、有证据、有边界、有状态的 Mechanism Unit**。

## 2. Non-goals

本仓库不把以下事项作为完成标准：

- 读完一本书或一个章节；
- 收集大量命令、API 或术语；
- 保存无法追溯来源的 AI 解释；
- 用一次演示性输出“证明”唯一机制；
- 为追求产出而把未验证猜测合入 `main`；
- 为同一规则维护多份相互漂移的简化规范。

## 3. Canonical sources of truth

仓库级规则只在以下位置定义：

| 文件 | 单一职责 |
| --- | --- |
| 本文件 | 框架总览、工件边界、状态模型、可追溯关系 |
| `LEARNING_MECHANISM.md` | 认知建立与验证协议 |
| `LEARNING_BRANCH_WORKFLOW.md` | Git 生命周期、commit 和 merge gate |
| `templates/*.md` | 将规范转为实际填写和审查的合同 |

`framework-review.md` 只记录某次审查及修复，不覆盖规范。

任何新规则必须进入对应权威文件；不得再创建平行的 `learning-workflow.md`、`merge-gate.md` 或 `mechanism-unit-spec.md`。

## 4. Knowledge architecture

### 4.1 Coverage Index：正交的导航索引

Coverage Map 回答：

- 来源读到哪里；
- 哪个章节或 section 已审阅；
- 是否已把来源映射到候选 Mechanism Unit；
- 哪些来源仍待处理。

Coverage 不属于证据层，不承载最终机制结论。

允许的 Coverage status：

```text
not-started
→ in-progress
→ source-reviewed
→ mapped
```

这些状态只描述来源处理进度。

### 4.2 Source Layer：模型依据

Source Layer 保存可追溯来源，而不是复制整章笔记。

每条来源至少记录：

- Source ID，例如 `S1`；
- 标题、作者或维护者；
- 版本、发布日期、edition 或 commit；
- chapter / section / page / stable URL 等 locator；
- 它支持或反驳的 Claim ID；
- 必要时记录实现适用范围。

优先级通常为：

1. 标准、原始论文、官方文档；
2. 官方源码和实现说明；
3. 经典教材；
4. 高质量二手解释。

AI 生成文本可以帮助提问和推理，但不能充当 Source Evidence。

### 4.3 Mechanism Layer：可检验模型

Mechanism Unit 是长期知识的核心。它描述：

- Problem 和约束；
- 对象、状态、状态转换和规则；
- invariants；
- competing hypotheses；
- causal chain；
- observables；
- trade-offs；
- boundaries / counterexamples；
- dependencies 和 transfer。

Mechanism Unit 必须拆成可审计的 Claim。推荐编号：

```text
C1, C2, C3, ...
```

结论段落不能只给一段整体叙述；关键结论应能回到具体 Claim ID。

### 4.4 Evidence Layer：支持、限制或推翻 claim

Evidence Layer 包含两类证据：

- Source Evidence：`S1`, `S2`, ...
- Runtime Evidence：`E1`, `E2`, ...，通常来自实验、trace、measurement、状态快照或源码路径验证。

实验本身推荐编号：

```text
EXP-001, EXP-002, ...
```

证据不是“附件堆积”。每条 evidence 必须连接到至少一个 Claim ID，并标明它是支持、限制还是反驳。

### 4.5 Claim–Evidence traceability

最低可追溯结构：

```text
Mechanism Unit
  ├─ C1 ── S1
  │      └─ E1 (from EXP-001)
  ├─ C2 ── S2
  └─ C3 ── unresolved
```

Mechanism Unit 中必须维护 Claim-Evidence Matrix：

| Claim | Status | Source evidence | Runtime evidence | Boundary |
| --- | --- | --- | --- | --- |
| C1 | cross-validated | S1 | E1 | Linux 6.x implementation |
| C2 | source-confirmed | S2 | — | experiment not currently observable |
| C3 | hypothesis | — | — | unresolved |

没有 evidence 的 claim 必须显式保持 `hypothesis`，不能被结论语气伪装成事实。

## 5. State models

### 5.1 Mechanism Unit lifecycle

Unit status 描述整个工件的工作阶段：

| Status | 含义 |
| --- | --- |
| `draft` | 问题和范围已创建，模型尚不完整 |
| `investigating` | 正在阅读、实验和修正 |
| `review-ready` | 作者认为已达到 merge gate，等待独立检查 |
| `learned` | merge gate 通过，已进入 `main` |
| `falsified` | 核心假设被推翻，但反例或修正具有长期价值 |
| `abandoned` | 范围错误、价值不足或当前无法形成可靠结论 |

### 5.2 Claim epistemic status

Claim status 描述单条命题的证据水平：

| Status | 含义 |
| --- | --- |
| `hypothesis` | 当前可证伪猜测 |
| `source-confirmed` | 可追溯权威来源支持，尚无运行时交叉验证 |
| `observed` | 运行时现象支持，但来源或替代解释仍不充分 |
| `cross-validated` | 来源与运行时证据相互支持 |
| `falsified` | 已被实验、来源或反例推翻 |

Unit status、Claim status 和 Coverage status 是三个不同维度，禁止互相代替。

## 6. Standard workflow

```text
1. Navigate source through Coverage Map
2. Read section for context
3. Extract one mechanism question
4. Define scope, dependencies and competing hypotheses
5. Build source model
6. Split important statements into Claim IDs
7. Design the smallest falsifiable experiment
8. Preserve raw evidence
9. Separate observation from inference
10. Update Claim-Evidence Matrix
11. Write the minimal conclusion
12. Add boundaries, counterexamples and transfer
13. Complete Merge Review
14. Merge durable knowledge to main
15. Update coverage in a separate commit when needed
```

Reading and mechanism extraction have different outputs:

```text
Reading output     = source understanding + candidate questions
Mechanism output   = model + claims + dependencies
Experiment output  = raw evidence + observations
Review output      = accepted, rejected, or explicitly unresolved knowledge
```

## 7. Repository artifact contract

Recommended layout:

```text
topics/<system>/
  README.md                         # Mechanism Map
  coverage.md                       # Source Coverage Map
  mechanisms/<mechanism>/
    README.md                       # copied from MECHANISM_UNIT.md
    MERGE_REVIEW.md                 # copied from MERGE_REVIEW.md
    experiments/
      EXP-001.md                    # copied from EXPERIMENT.md
      raw/
        <immutable evidence files>
```

### Mechanism Map

`topics/<system>/README.md` records:

- Mechanism ID/path；
- problem summary；
- dependencies；
- Unit status；
- evidence summary；
- link to the unit。

它不重复 Mechanism Unit 正文。

### Raw evidence

原始输出应尽量保持原样。允许：

- 小型输出直接放进 experiment 文件；
- 大型 trace、log 或 measurement 放到 `raw/`；
- 对外部不可提交内容记录稳定位置、生成命令和必要 checksum。

不得只保留经过人工改写的摘要而丢失原始观察。

## 8. Branch and merge contract

Mechanism learning branch：

```text
learn/<system>/<mechanism>
```

Repository-level framework maintenance：

```text
docs/<scope>
```

一个 `learn/*` 分支只建立一个 Mechanism Unit。Coverage 变更使用独立 commit。进入 `main` 前必须完成：

- Mechanism Unit；
- 必要 experiment / raw evidence；
- Claim-Evidence Matrix；
- `MERGE_REVIEW.md`；
- repository validation。

详细规则见 `LEARNING_BRANCH_WORKFLOW.md`。

## 9. Merge acceptance criteria

关键结论进入 `main` 前，至少满足：

1. Scope 单一，边界明确；
2. 模型能解释对象、状态、规则和因果链；
3. 关键 claim 有可追溯 evidence，或明确保持 unresolved；
4. 可实验的重要 claim 至少有一个可重复实验；
5. observation 与 inference 分离；
6. falsification criteria 在看到结果前定义；
7. 至少一个 boundary、异常路径或 counterexample；
8. dependency 不隐藏关键前提；
9. coverage、unit 和 claim 状态没有混用；
10. review 能回答“哪些证据支持哪条结论”。

`cross-validated` 是关键 claim 的默认目标，但不是伪造实验的理由。实验不可行时，可以保留 `source-confirmed`，前提是写明原因和限制。

## 10. Minimum learning session

一次会话不必完成整个机制，但至少留下：

```text
1 explicit question
+ 1 current hypothesis/model
+ 1 source locator or runtime observation
+ 1 claim status update
+ 1 unresolved question
```

这样中断后仍保留认知状态，而不是只留下聊天记录。

## 11. AI role

AI 可以帮助：

- 从原文提取候选 claim；
- 生成 competing hypotheses；
- 设计区分假设的实验；
- 检查 observation 与 inference 是否混淆；
- 寻找反例、边界和替代解释；
- 审查 conclusion 是否超出 evidence；
- 建立跨系统机制对照。

AI 不得：

- 把自身回答登记为 evidence；
- 在缺少 locator 时伪造来源；
- 在实验后倒写 hypothesis；
- 用流畅解释替代可追溯证据；
- 把“与模型一致”改写为“唯一原因已证明”。

## 12. Framework change policy

为了避免规范漂移：

1. 规则只能修改对应 canonical document；
2. 模板必须与规则同步；
3. review record 只描述发现和决议；
4. 新增状态或目录约定时，同时更新 validator；
5. 任何删除、重命名或状态变更都必须通过 repository validation；
6. 框架维护完成后，优先用真实 Mechanism Unit 验证可执行性，而不是继续扩写抽象规则。
