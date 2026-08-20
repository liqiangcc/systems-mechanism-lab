# Learning Branch Workflow

本规范定义 `systems-mechanism-lab` 的 Git 学习工作流。目标是让 Git 历史表达**认知如何从假设经过证据验证，最终成为可长期保留的机制模型**，而不是把仓库变成按会话堆积的笔记集合。

它与 [`LEARNING_MECHANISM.md`](./LEARNING_MECHANISM.md) 配套：学习机制定义“怎样建立和验证认知”，本文定义“这些认知怎样通过分支、commit 和 merge gate 进入 `main`”。

---

## 1. 核心原则

### 1.1 `main` 保存已验证的长期认知

`main` 是仓库的 canonical knowledge base。

允许进入 `main` 的内容应当是：

- 已满足 merge gate 的 Mechanism Unit；
- 可重复的实验及其原始观察；
- 能支持结论的 evidence；
- 明确记录边界、反例和不确定性的结论；
- 事实性的 coverage 元数据。

以下内容不应作为机制结论直接留在 `main`：

- 尚未验证的猜测；
- 只有 AI 解释、没有可追溯来源或实验支持的结论；
- 临时探索记录；
- 失败且没有学习价值的中间产物；
- 将“读完章节”误写成“机制已掌握”的状态。

`main` 的含义不是“从不出现未知”，而是：**未知必须被显式标记，不能伪装成已验证认知。**

### 1.2 `learn/*` 用于机制学习

所有新的机制学习默认从 `main` 创建 `learn/*` 分支。

命名格式：

```text
learn/<system>/<mechanism-slug>
```

例如：

```text
learn/unix/process-creation
learn/unix/file-descriptor-sharing
learn/mysql/mvcc-visibility
learn/kafka/isr-membership
```

分支名称描述**机制**，而不是章节、日期或学习会话。

不推荐：

```text
learn/chapter-24
learn/2026-08-20
learn/today-notes
```

### 1.3 一个 Mechanism Unit 一个短生命周期分支

一个 `learn/*` 分支只解决一个 Mechanism Unit。

如果学习中发现第二个可以独立解释、独立实验、独立合并的机制，应拆出新的 `learn/*` 分支，而不是继续扩大当前分支。

短生命周期意味着：

- 范围足够小，可以独立验证；
- 达到 merge gate 后立即合并；
- 被证伪或方向错误时可以直接关闭；
- 不把长期未解决问题持续堆积在一个巨型 learning branch 中。

分支寿命由“一个机制是否形成闭环”决定，而不是人为规定固定天数。

---

## 2. Branch Responsibilities

| 分支 | 职责 | 可以包含 | 不应包含 |
| --- | --- | --- | --- |
| `main` | 保存长期、可复用、已验证状态 | validated mechanism、evidence、reproducible experiment、coverage metadata | 未验证机制结论、临时探索 |
| `learn/<system>/<mechanism>` | 建立并验证一个 Mechanism Unit | hypothesis、source model、experiment、observation、evidence、boundary、final mechanism | 第二个独立机制、大范围章节笔记、无关重构 |

原则：

> **branch boundary = mechanism boundary**

Git 分支本身就是学习范围控制器。

---

## 3. Coverage 与 Mechanism 必须分离

Coverage 和 Mechanism 是两种不同状态，不能互相替代。

### Coverage 回答

```text
我读到哪里？
哪些章节 / 文档 / 论文已经覆盖？
哪些来源仍未处理？
```

对应文件通常是：

```text
topics/<system>/coverage.md
```

### Mechanism 回答

```text
我真正理解并验证了什么？
机制的状态、规则、因果链和边界是什么？
证据是什么？
```

对应目录通常是：

```text
topics/<system>/mechanisms/<mechanism>/
```

### 分离规则

1. `coverage.md` 不承载机制正文或最终因果解释。
2. mechanism 文件不以“读到第几章”作为完成条件。
3. 章节完成不自动意味着任何 Mechanism Unit 已完成。
4. 一个机制跨多个章节时，只维护一个 Mechanism Unit。
5. 一个章节包含多个机制时，分别进入多个 `learn/*` 分支。
6. coverage 更新使用独立 commit，不与 mechanism/evidence 内容混在同一个 commit。
7. coverage 只能记录事实状态，例如 `read / mapped / pending`；不能用 coverage 状态代替 evidence 状态。

推荐关系：

```text
Source / Chapter
      │
      ├──> coverage.md        # navigation state
      │
      └──> Mechanism Unit     # durable knowledge
                │
                └──> experiments / evidence
```

---

## 4. 标准分支生命周期

```text
main
  │
  ├─ create learn/<system>/<mechanism>
  │
  ├─ Question / Hypothesis
  ├─ Source Model
  ├─ Experiment
  ├─ Observation
  ├─ Evidence
  ├─ Conclusion
  ├─ Boundary / Counterexample
  │
  ├─ Merge Gate
  │
  └─ merge → main
```

### Step 1 — 从最新 `main` 建分支

```bash
git switch main
git pull --ff-only
git switch -c learn/unix/process-creation
```

### Step 2 — 建立单一 Mechanism Unit

优先从 `templates/MECHANISM_UNIT.md` 创建机制目录。

当前分支必须能够用一句话描述目标：

```text
验证 fork 后地址空间复制的真实机制及其可观察证据。
```

如果一句话中开始出现多个互不依赖的“以及”，通常意味着应该拆分。

### Step 3 — 先写假设，再做实验

不要在知道结果后伪造 hypothesis。

至少记录：

- 当前问题；
- 竞争假设；
- 哪个观察可以区分它们。

### Step 4 — 让 commit 表达认知推进

commit 不按“今天做了什么”组织，而按**认知状态变化**组织。

### Step 5 — 满足 Merge Gate

未达到 gate 就继续留在 `learn/*`，或者明确关闭为 falsified / abandoned；不要为了“保持进度”提前进入 `main`。

### Step 6 — 合并后删除学习分支

Mechanism Unit 合并后，`learn/*` 已完成使命，应删除。

后续如果出现新证据推翻原结论，创建新的 `learn/*` 分支修正，而不是复活旧分支。

---

## 5. Commit 规范

推荐格式：

```text
<type>(<system>/<mechanism>): <epistemic change>
```

### 类型

| type | 含义 |
| --- | --- |
| `learn` | 建立问题、假设或初始模型 |
| `experiment` | 新增或修正可重复实验 |
| `evidence` | 记录来源证据或运行时观察 |
| `mechanism` | 更新经过证据支持的机制结论 / 边界 |
| `coverage` | 只更新来源覆盖状态 |
| `docs` | 仓库级学习规范、模板等维护 |

示例：

```text
learn(unix/process-creation): define competing fork memory hypotheses
experiment(unix/process-creation): observe private pages after child write
evidence(unix/process-creation): record proc memory observations
mechanism(unix/process-creation): conclude copy-on-write boundary
coverage(unix): map TLPI process-creation sections
docs(workflow): define learning branch merge gate
```

禁止使用低信息量提交作为默认习惯：

```text
update notes
study chapter 24
more learning
fix docs
wip
```

### Commit 原子性

一个 commit 应尽量只表达一种状态变化。

特别要求：

- `coverage(...)` 不与 `mechanism(...)` 混合；
- 原始 observation 不和后验解释伪装成同一步；
- 大量格式化 / 重构不和机制结论混合；
- 修正被证伪假设时，应让历史能够看出“旧模型 → 证据 → 新模型”。

Git history 应能够回答：

> **我们为什么开始相信这个结论？**

---

## 6. Merge Gate

`learn/*` 合入 `main` 前，至少检查以下 gate。

### Gate A — Scope

- [ ] 当前分支只有一个 Mechanism Unit。
- [ ] 没有混入第二个独立机制。
- [ ] 没有无关重构、大段章节摘录或临时文件。

### Gate B — Model

- [ ] Problem 清楚。
- [ ] 关键对象、状态、规则或状态转换已描述。
- [ ] 关键 causal chain 能解释观察到的行为。
- [ ] 重要 invariant / trade-off 已记录（适用时）。

### Gate C — Evidence

- [ ] 关键结论有可追溯 source evidence 或 runtime evidence。
- [ ] 对可实验的重要结论，默认至少有一个可重复实验。
- [ ] observation 与 interpretation 分开记录。
- [ ] evidence 状态明确，不把 `hypothesis` 写成事实。
- [ ] 关键结论优先达到 `cross-validated`；若实验不可行，仅 `source-confirmed` 时必须明确原因和限制。

### Gate D — Falsifiability & Boundary

- [ ] 写明什么结果会推翻当前模型，或已经记录竞争假设如何被排除。
- [ ] 至少记录一个边界条件、异常路径或反例。
- [ ] 没有把实现细节无条件泛化成系统不变量。

### Gate E — Reproducibility

- [ ] 实验包含必要环境 / 版本信息。
- [ ] 命令、输入、观察方法足够让之后重新执行。
- [ ] 原始输出与人工解释可区分。

### Gate F — Separation

- [ ] coverage 与 mechanism 使用不同文件职责。
- [ ] coverage 更新若存在，使用独立 commit。
- [ ] “章节已读完”没有被当成 mechanism learned 的证据。

### Gate G — Repository Quality

- [ ] 分支基于足够新的 `main`，没有未处理冲突。
- [ ] 文件路径符合仓库结构。
- [ ] 没有明显重复 Mechanism Unit。
- [ ] commit message 能说明认知状态变化。

只有 gate 通过后，Mechanism Unit 才进入 `main`。

---

## 7. Merge 策略

默认推荐 **保留有学习价值的 commit 历史**。

如果分支中的 commit 已按“假设 → 实验 → 证据 → 结论”组织，可以使用普通 merge 或 rebase merge，让认知演化仍可追踪。

如果分支充满临时修正、噪声 commit，应在合并前整理历史；不要让 `main` 永久保存大量无意义 WIP。

是否 squash 不是绝对规则，判断标准是：

> **合并后的历史是否仍能帮助未来的人或 AI 重建证据链？**

不要为了 commit 数量少而 squash 掉真正有解释价值的认知演化。

---

## 8. 失败学习也要有明确出口

并非每个 `learn/*` 都必须合并。

可能结果：

### Validated

机制达到 merge gate，合并到 `main`。

### Falsified

原假设被推翻，但实验或反例本身具有长期价值。

此时可以把**被证伪的命题、证据和正确边界**整理成可验证知识后再合并。

### Abandoned

问题定义错误、没有长期价值或当前无法验证。

直接关闭并删除分支，不为了“有产出”强行合并。

因此：

> **关闭一个错误分支也是成功的范围控制。**

---

## 9. 示例：从章节到多个机制分支

假设阅读 Unix 进程相关章节，识别出三个机制：

```text
process creation
file descriptor inheritance
copy-on-write memory
```

不要创建：

```text
learn/unix/chapter-processes
```

然后把三个机制全部堆进去。

应拆成：

```text
learn/unix/process-creation
learn/unix/fd-inheritance
learn/unix/copy-on-write
```

coverage 仍然只负责记录章节是否完成映射：

```text
topics/unix/coverage.md
```

三个机制分别完成各自实验、证据链和 merge gate 后进入 `main`。

这样即使以后换成 Kafka、MySQL、Redis 或 JVM，Git 工作流仍然保持一致：

```text
source navigation != knowledge structure
chapter != mechanism
branch boundary = mechanism boundary
main = validated durable state
```

---

## 10. 最小执行规则

如果只记住六条：

1. `main` 只保留可长期依赖的已验证状态。
2. 新机制从 `learn/<system>/<mechanism>` 开始。
3. 一个 Mechanism Unit 一个短生命周期分支。
4. Coverage 与 Mechanism 分离，coverage 使用独立 commit。
5. commit 描述认知变化，而不是学习时间或会话活动。
6. 通过 merge gate 后才进入 `main`，合并后删除 `learn/*`。

这套规则的最终目标不是制造 Git 流程，而是让仓库本身成为一张**可审计、可复现、可证伪的系统认知图谱**。
