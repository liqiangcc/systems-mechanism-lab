# Learning Branch Workflow

本规范定义 `systems-mechanism-lab` 的 Git 工作流。目标是让 Git 历史表达认知如何从假设经过证据约束，最终成为可长期保留的机制模型。

配套规范：

- [`WHITEBOX_LEARNING_FRAMEWORK.md`](./WHITEBOX_LEARNING_FRAMEWORK.md)
- [`LEARNING_MECHANISM.md`](./LEARNING_MECHANISM.md)
- [`../templates/MERGE_REVIEW.md`](../templates/MERGE_REVIEW.md)

## 1. Branch responsibilities

### `main`

`main` 是 canonical knowledge base，保存：

- 已通过 merge gate 的 Mechanism Unit；
- 可重复 experiment 和 raw evidence；
- Claim-Evidence Matrix；
- 明确的 boundaries、counterexamples 和 unresolved claims；
- 事实性的 Coverage Map 与 Mechanism Map；
- 仓库级权威规范和模板。

`main` 允许保留未知，但未知必须显式标记，不能伪装成已验证结论。

### `learn/<system>/<mechanism>`

所有新机制学习默认从最新 `main` 创建：

```text
learn/<system>/<mechanism-slug>
```

例如：

```text
learn/unix/process-creation
learn/unix/file-open-description
learn/mysql/mvcc-visibility
learn/kafka/isr-membership
```

一个 `learn/*` 分支只建立一个 Mechanism Unit。

### `docs/<scope>`

仓库级框架、模板和非机制文档维护使用：

```text
docs/<scope>
```

例如：

```text
docs/whitebox-framework
docs/experiment-template
```

不要把 repository-level 规范维护伪装成某个系统机制。

## 2. Branch boundary equals mechanism boundary

当前分支必须能用一句话描述：

```text
验证 fork 后地址空间复制的机制及其可观察证据。
```

出现以下情况时应拆分：

- 包含第二个可独立解释和实验的机制；
- 同时跨越多个不相关 failure model；
- 需要独立 reviewer 才能判断；
- 文件开始按章节堆积而不是按 claim 组织；
- branch goal 中出现多个互不依赖的“以及”。

分支寿命由机制闭环决定，不按固定天数决定。达到 gate 后合并；范围错误时关闭。

## 3. Coverage and mechanism separation

Coverage Map 回答：

```text
source read to where?
which section is source-reviewed?
which section has been mapped to mechanisms?
```

Mechanism Unit 回答：

```text
what is the internal model?
which claims are supported?
what evidence and boundaries exist?
```

强制规则：

1. `coverage.md` 不承载机制正文；
2. Coverage status 只能是 `not-started | in-progress | source-reviewed | mapped`；
3. Claim status 不能写入 coverage table；
4. “章节完成”不自动产生 `learned` unit；
5. 一个章节中的多个机制进入不同 `learn/*` 分支；
6. 一个跨章节机制只维护一个 unit；
7. coverage 更新使用独立 `coverage(...)` commit；
8. Mechanism Map 只链接和索引 unit，不复制正文。

## 4. Standard branch lifecycle

```text
main
  │
  ├─ create learn/<system>/<mechanism>
  │
  ├─ draft Mechanism Unit
  ├─ define claims and competing hypotheses
  ├─ collect source evidence
  ├─ run experiments
  ├─ preserve raw evidence
  ├─ update Claim-Evidence Matrix
  ├─ write bounded conclusion
  ├─ record counterexamples / transfer
  ├─ complete MERGE_REVIEW.md
  ├─ run repository validator
  │
  └─ merge → main → delete branch
```

### Step 1 — Start from current `main`

```bash
git switch main
git pull --ff-only
git switch -c learn/unix/process-creation
```

### Step 2 — Create the artifacts

```text
topics/<system>/mechanisms/<mechanism>/
  README.md
  MERGE_REVIEW.md
  experiments/
```

从模板复制，不手写另一套结构。

### Step 3 — Record hypotheses before results

至少先记录：

- Core Question；
- H1 / H2；
- distinguishing observation；
- falsification criteria。

### Step 4 — Let commits express epistemic change

Commit 应描述认知状态变化，而不是会话活动。

### Step 5 — Move Unit status to `review-ready`

只有作者完成 self-review、Claim-Evidence Matrix 和 validator 后，才能标记 `review-ready`。

### Step 6 — Independent merge review

Reviewer 使用 `MERGE_REVIEW.md` 检查范围、证据、边界和状态语义。未通过就继续留在 branch。

### Step 7 — Merge and close

通过后进入 `main`，Unit status 改为 `learned`，删除短生命周期 branch。

后续新证据推翻结论时，创建新的 `learn/*` branch 修正，不复活旧 branch。

## 5. Commit convention

推荐格式：

```text
<type>(<system>/<mechanism>): <epistemic change>
```

Repository-level docs 可以省略 system/mechanism：

```text
docs(framework): separate coverage and claim states
```

### Types

| type | 含义 |
| --- | --- |
| `learn` | 建立问题、scope、hypothesis 或初始模型 |
| `experiment` | 新增或修正可重复实验 |
| `evidence` | 保存来源证据、raw evidence 或 observation |
| `mechanism` | 更新 claim、因果链、边界或最终模型 |
| `coverage` | 只更新来源覆盖状态 |
| `docs` | 仓库级规范、模板、validator |
| `review` | 记录独立审查结论 |

示例：

```text
learn(unix/process-creation): define competing memory hypotheses
experiment(unix/process-creation): observe page changes after child write
evidence(unix/process-creation): record proc memory evidence E1
mechanism(unix/process-creation): cross-validate C2 within Linux boundary
coverage(unix): map process-creation sections
review(unix/process-creation): accept claim-evidence traceability
docs(framework): add executable merge review
```

禁止默认使用：

```text
update notes
study chapter 24
more learning
fix docs
wip
```

### Atomicity

一个 commit 尽量只表达一种状态变化：

- coverage 不与 mechanism 混合；
- raw evidence 不与后验解释伪装成同一步；
- 格式化不与 claim 变化混合；
- 被证伪时保留“旧假设 → evidence → 新状态”的历史；
- framework rule 和对应 template 应在同一完整变更中保持一致。

## 6. Merge Gate

每个 mechanism directory 必须包含已填写的 `MERGE_REVIEW.md`。

### Gate A — Scope

- [ ] 只有一个 Mechanism Unit；
- [ ] Problem、scope 和 non-goals 明确；
- [ ] 没有无关重构、整章摘录或临时文件；
- [ ] dependencies 已记录。

### Gate B — Model

- [ ] objects、states、transitions、rules 足以解释行为；
- [ ] causal chain 引用关键 Claim IDs；
- [ ] invariants 和 trade-offs 已记录（适用时）；
- [ ] conclusion 没有引入 matrix 外的新 claim。

### Gate C — Traceability

- [ ] 关键叙述已拆为 Claim IDs；
- [ ] Source IDs 有版本和 locator；
- [ ] Runtime Evidence IDs 能回到 experiment / raw evidence；
- [ ] 每个关键 claim 有 evidence 或明确保持 unresolved；
- [ ] 没有把 AI 回答登记为 evidence。

### Gate D — Falsifiability and evidence

- [ ] competing hypotheses 在结果前记录；
- [ ] falsification criteria 明确；
- [ ] observation 与 inference 分离；
- [ ] 可实验的重要 claim 至少有一个可重复 experiment；
- [ ] `source-confirmed` 但无实验的 claim 写明原因；
- [ ] 不把“与模型一致”写成“唯一原因已证明”。

### Gate E — Boundaries

- [ ] 至少一个 boundary、exceptional path 或 counterexample；
- [ ] version / implementation applicability 明确；
- [ ] 未排除的 alternative explanations 保留；
- [ ] 没有把实现细节无条件泛化成系统 invariant。

### Gate F — State semantics

- [ ] Coverage、Unit 和 Claim status 没有混用；
- [ ] Unit status 当前为 `review-ready`；
- [ ] falsified claims 没有从历史中静默删除；
- [ ] unresolved claims 不影响已接受结论的最小范围，或已阻止合并。

### Gate G — Reproducibility

- [ ] environment、version、commands、inputs 完整；
- [ ] raw evidence 存在或有稳定 locator；
- [ ] 复现实验所需权限和前置状态已说明；
- [ ] 清理步骤或副作用已记录。

### Gate H — Repository quality

- [ ] branch 基于足够新的 `main`；
- [ ] 路径符合目录合同；
- [ ] Mechanism Map 已更新（如需）；
- [ ] coverage 更新使用独立 commit（如有）；
- [ ] `python3 scripts/validate_framework.py` 通过；
- [ ] commit history 能回答“为什么开始相信这条结论”。

## 7. Merge strategy

默认保留有学习价值的 commit 历史。

如果 commit 已按“hypothesis → experiment → evidence → claim update”组织，可使用普通 merge 或 rebase merge。若存在大量无意义 WIP，应先整理。

判断标准不是 commit 数量，而是：

> 合并后的历史是否帮助未来的人或 AI 重建证据链？

## 8. Outcomes

### Learned

Gate 通过，进入 `main`。

### Falsified

核心假设被推翻，但反例、实验或修正模型具有长期价值。整理为明确知识后可以合并。

### Abandoned

问题边界错误、当前不可验证或没有长期价值。关闭并删除 branch，不为“有产出”强行合并。

## 9. Example: chapter to branches

阅读 Unix 进程章节后识别：

```text
process creation
file-open-description sharing
copy-on-write memory
```

不要创建一个巨型章节 branch。应分别建立：

```text
learn/unix/process-creation
learn/unix/file-open-description-sharing
learn/unix/copy-on-write
```

Coverage Map 只记录来源是否 `source-reviewed` 或 `mapped`。

## 10. Minimum rules

1. `main` 保存可审计的长期认知；
2. 新机制使用 `learn/<system>/<mechanism>`；
3. repository-level 规范维护使用 `docs/<scope>`；
4. 一个 branch 一个 Mechanism Unit；
5. coverage、unit、claim 三类状态分离；
6. 每个关键 claim 连接 evidence；
7. merge 前填写 `MERGE_REVIEW.md` 并运行 validator；
8. 通过后合并并删除 learning branch。
