# Learning Mechanism

本文件定义如何把一个系统从黑盒 API 拆成可解释、可观察、可证伪和可迁移的机制认知。

框架总览与术语边界见 [`WHITEBOX_LEARNING_FRAMEWORK.md`](./WHITEBOX_LEARNING_FRAMEWORK.md)。Git 分支与 merge gate 见 [`LEARNING_BRANCH_WORKFLOW.md`](./LEARNING_BRANCH_WORKFLOW.md)。

## 1. Definition of understanding

对一个机制真正掌握，至少应做到：

1. **Explain**：说明它解决什么问题、由哪些对象和规则组成。
2. **Predict**：给定输入、故障或条件变化，预测行为。
3. **Observe**：知道哪些系统调用、状态、指标、文件、日志或事件能暴露它。
4. **Test**：设计最小实验区分 competing hypotheses。
5. **Bound**：说明结论的版本、实现、并发、故障和资源边界。
6. **Trace**：把关键 Claim ID 连接到 Source Evidence 和 Runtime Evidence。
7. **Transfer**：比较相同约束在其他系统中的设计差异。

> “读过”不是完成；“模型能做出预测，并由可追溯证据约束”才接近完成。

## 2. Three organization principles

### 2.1 Chapters navigate

书籍、文档和论文的章节用于保证来源覆盖率。章节是输入顺序，不是最终知识结构。

每读一个 section，先问：

- 它试图解释哪些机制？
- 哪些内容只是背景、API 或术语？
- 哪些陈述可以改写成可证伪 claim？
- 哪些机制依赖其他机制？
- 哪些观察能区分不同解释？

阅读结果写入 Coverage Map 或来源 locator；不要把整章摘要复制成 Mechanism Unit。

### 2.2 Mechanisms organize

长期知识以 Mechanism Unit 为核心。一个 unit 至少包含：

- Problem / constraints；
- Core Question；
- scope / non-goals；
- dependencies；
- competing hypotheses；
- objects / states / transitions / rules；
- invariants；
- causal chain；
- observables；
- claims；
- evidence；
- boundaries / counterexamples；
- trade-offs；
- transfer。

一个 unit 只解决一个可以独立解释、独立实验和独立审查的机制问题。

### 2.3 Evidence constrains

实验不是命令演示，也不是为了“证明我原来是对的”。它用于区分假设并限制结论。

好的实验必须提前回答：

> 如果 H1 正确会看到什么？如果 H2 正确会看到什么？什么结果会推翻当前首选解释？

Evidence 分为：

- Source Evidence：标准、论文、官方文档、源码、经典教材；
- Runtime Evidence：实验输出、trace、measurement、状态快照、代码路径观察。

每条 evidence 都要连接到 Claim ID。

## 3. Status separation

### Coverage status

```text
not-started | in-progress | source-reviewed | mapped
```

只描述来源处理进度。

### Mechanism Unit status

```text
draft | investigating | review-ready | learned | falsified | abandoned
```

描述整个工件的生命周期。

### Claim status

```text
hypothesis | source-confirmed | observed | cross-validated | falsified
```

描述单条命题的证据水平。

三者禁止混用。“章节已读”不能把 unit 改成 `learned`；一次实验也不能自动让所有 claims 变成 `cross-validated`。

## 4. Standard learning loop

```text
Question
  ↓
Competing Hypotheses
  ↓
Source Model
  ↓
Claims
  ↓
Experiment
  ↓
Raw Evidence
  ↓
Observation
  ↓
Inference
  ↓
Claim Status Update
  ↓
Conclusion
  ↓
Boundary / Counterexample
  ↓
Transfer
```

### Step 1 — Question

不要从“这一章有哪些知识点”开始，而要形成 why / how / under what conditions 问题，例如：

- `fork()` 后父子进程为什么能看到近似相同的地址空间？
- 文件描述符继承后，为什么文件偏移量可能共享？
- Kafka 为什么需要 ISR，而不只看副本数？
- MySQL MVCC 为什么同时需要版本与可见性规则？

问题必须足够小，能落到一个 Mechanism Unit。

### Step 2 — Competing Hypotheses

先写当前解释，再观察结果。不要事后倒写 hypothesis。

```text
H1: fork 后立即复制所有物理页。
H2: fork 后最初共享物理页，写入时通过 COW 分离。
```

同时写明区分它们的观察。

### Step 3 — Source Model

优先从权威来源提取：

- objects；
- states；
- transitions；
- rules；
- invariants；
- preconditions；
- exceptional paths；
- implementation/version boundaries。

每条来源分配 Source ID，例如 `S1`，并记录稳定 locator。来源提供模型依据，不免除验证。

### Step 4 — Claims

把重要叙述拆成可以独立检查的 Claim：

```text
C1: fork 返回后，父子进程具有独立的虚拟地址空间视图。
C2: 初始物理页可通过 COW 共享。
C3: 某页首次写入会触发私有副本建立。
```

避免一个大段 conclusion 同时包含多个证据水平不同的命题。

### Step 5 — Experiment

实验尽量只改变一个关键变量，并记录：

- linked Claim ID / Hypothesis ID；
- manipulated / controlled / observed variables；
- environment / version；
- commands / inputs；
- expected outcomes；
- falsification criteria；
- raw evidence destination。

优先选择最接近机制的观察：

- system-call trace；
- `/proc`、虚拟文件系统、内核暴露状态；
- file descriptor / inode / socket state；
- process / thread / scheduler state；
- network packet；
- database lock / transaction / execution plan；
- Kafka offset / replica / ISR；
- performance counter；
- source-code path。

### Step 6 — Raw Evidence

原始输出和解释分开保存。

错误：

```text
因为是 COW，所以内存没有复制。
```

正确：

```text
E1 Raw evidence: fork 后 RSS 未立即近似翻倍；对子进程目标页写入后 Private_Dirty 增加。
Observation: 写入前后该页的私有脏页统计发生变化。
Inference: 现象与按页写时复制模型一致，但单独这一观察不排除所有替代解释。
```

Raw evidence 要可重现或可定位；不能只保存人工摘要。

### Step 7 — Claim-Evidence Matrix

在 Mechanism Unit 中维护：

| Claim | Status | Source evidence | Runtime evidence | Boundary |
| --- | --- | --- | --- | --- |
| C1 | source-confirmed | S1 | — | POSIX semantics |
| C2 | cross-validated | S2 | E1 | tested on Linux version X |
| C3 | hypothesis | — | — | unresolved |

更新规则：

- 只有来源支持：`source-confirmed`；
- 只有运行时观察支持：`observed`；
- 二者交叉支持：`cross-validated`；
- 被证据推翻：`falsified`；
- 没有证据：保持 `hypothesis`。

### Step 8 — Conclusion

结论回答“为什么”，并只包含 matrix 支持到的强度。

推荐因果链：

```text
constraint/problem
→ mechanism design
→ state transition
→ observable behavior
→ cost/trade-off
```

结论引用 Claim ID，而不是重新写一组无法追踪的陈述。

### Step 9 — Boundary / Counterexample

每条关键 claim 继续追问：

- 所有版本都成立吗？
- 是规范语义还是具体实现？
- 并发、故障、资源不足时怎样？
- 哪个反例最容易推翻模型？
- 观察工具本身是否改变或隐藏行为？
- 还有哪些替代解释没有排除？

没有边界的结论通常是过度概括。

### Step 10 — Transfer

迁移不是强行类比，而是比较：

- 相同约束；
- 相同状态或规则；
- 不同假设；
- 不同 failure model；
- 为什么最终设计不同。

示例：

- OS page cache ↔ database buffer pool；
- WAL ↔ Kafka log / replicated log；
- OS scheduler ↔ application work queue；
- file descriptor ↔ capability / handle；
- MVCC ↔ immutable versions / snapshots。

## 5. Chapter-driven learning without chapter-shaped knowledge

教材轨道默认按章节推进，流程是：

```text
section pre-read
→ source questions
→ candidate mechanisms
→ source model
→ mechanism branches
→ experiments / evidence
→ claim updates
→ coverage update
```

仓库维护两张独立地图：

1. Coverage Map：来源处理到哪里；
2. Mechanism Map：有哪些机制、依赖和 Unit status。

一个章节可以映射多个机制；一个机制也可以跨多个章节。Coverage 更新不能替代 Mechanism Unit。

## 6. Experiment quality

实验至少满足：

### Reproducible

记录环境、版本、命令、输入、权限、前置状态和清理步骤。

### Minimal

一个实验优先区分一个关键假设；复杂场景拆成多个 experiment。

### Falsifiable

执行前记录预期和反驳条件。

### Observation separated from inference

Raw evidence、observation、inference、conclusion 分栏保存。

### Alternative explanations retained

未排除的解释写入 Limits，不因结果符合预期就删除。

### Appropriate certainty

“与模型一致”不等于“唯一原因已证明”。

## 7. Definition of Learned

Mechanism Unit 标记为 `review-ready` 前，应大部分回答“是”：

- [ ] Problem、scope 和 non-goals 清楚；
- [ ] dependencies 已记录；
- [ ] objects、states、transitions 和 invariants 可解释；
- [ ] causal chain 能预测至少一个条件变化后的行为；
- [ ] 关键叙述已拆成 Claim IDs；
- [ ] 每个关键 claim 有 evidence 或明确保持 unresolved；
- [ ] 至少一个重要 claim 经过可重复实验，或写明实验不可行原因；
- [ ] raw evidence 与 interpretation 分离；
- [ ] 至少一个 boundary、异常路径或 counterexample；
- [ ] trade-off 已说明；
- [ ] 至少进行一次跨系统比较；
- [ ] `MERGE_REVIEW.md` 已完成；
- [ ] repository validator 通过。

若只能回答“API 怎么调用”，仍属于 black-box knowledge。

## 8. Recommended directory layout

```text
topics/
  unix/
    README.md
    coverage.md
    mechanisms/
      process-creation/
        README.md
        MERGE_REVIEW.md
        experiments/
          EXP-001.md
          raw/
  kafka/
    README.md
    coverage.md
    mechanisms/
```

职责分离：

- `coverage.md`：学到哪里；
- system `README.md`：机制地图；
- mechanism `README.md`：理解了什么；
- `experiments/`：观察了什么；
- `MERGE_REVIEW.md`：为什么允许进入 `main`。

## 9. Minimum session closure

一次学习会话至少留下：

```text
1 explicit question
+ 1 current hypothesis/model
+ 1 source locator or runtime observation
+ 1 claim status update
+ 1 unresolved question
```

会话可以中断，但认知状态必须可恢复。

## 10. AI role

AI 可以帮助提取 claim、生成 competing hypotheses、设计实验、解释现象、寻找反例和审查 evidence overreach。

AI 的回答本身不作为最终证据。最终链路应回到：

```text
source / experiment
→ raw evidence
→ observation
→ reasoning
→ claim status
→ bounded conclusion
```
