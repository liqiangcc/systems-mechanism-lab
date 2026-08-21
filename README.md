# systems-mechanism-lab

A reusable laboratory for learning how computer systems actually work.

本仓库不是普通读书笔记集合。它把系统知识组织为**可以解释、预测、观察、实验、证伪、审计和迁移的机制模型**，适用于 Unix/Linux、Kafka、MySQL、Redis、JVM、网络、存储等主题。

## Core idea

> Chapters provide navigation. Mechanisms provide structure. Evidence justifies claims.

标准闭环：

```text
Source navigation
→ Mechanism question
→ Competing hypotheses
→ Source model
→ Experiment
→ Raw evidence
→ Observation / inference
→ Claim update
→ Boundary / counterexample
→ Merge review
→ durable knowledge in main
```

## Framework contract

以下三个文件是唯一的仓库级权威规范：

1. [`docs/WHITEBOX_LEARNING_FRAMEWORK.md`](docs/WHITEBOX_LEARNING_FRAMEWORK.md)：框架总览、分层、状态模型和工件边界。
2. [`docs/LEARNING_MECHANISM.md`](docs/LEARNING_MECHANISM.md)：如何从问题建立、验证和修正机制认知。
3. [`docs/LEARNING_BRANCH_WORKFLOW.md`](docs/LEARNING_BRANCH_WORKFLOW.md)：分支、commit、merge gate 和进入 `main` 的规则。

[`templates/`](templates/) 是这些规范的可执行合同。发现规范缺口时，应修改上述权威文件和模板，不再新增平行的简化版 workflow、merge gate 或 mechanism spec。

[`docs/framework-review.md`](docs/framework-review.md) 是审查记录，不是新的规范来源。

## Artifact boundaries

| Artifact | 回答的问题 | 典型位置 |
| --- | --- | --- |
| Coverage Map | 来源读到哪里、是否已映射 | `topics/<system>/coverage.md` |
| Mechanism Map | 已有哪些机制、依赖和生命周期状态 | `topics/<system>/README.md` |
| Mechanism Unit | 系统内部为什么这样工作 | `topics/<system>/mechanisms/<mechanism>/README.md` |
| Experiment / Evidence | 凭什么相信或推翻某条 claim | `.../experiments/` 与 raw evidence |
| Merge Review | 是否达到进入 `main` 的条件 | `.../MERGE_REVIEW.md` |

Coverage 是导航索引，不是证据层，也不能把“章节读完”转换成“机制已掌握”。

## State separation

三类状态不得混用：

- Coverage status：`not-started | in-progress | source-reviewed | mapped`
- Mechanism Unit status：`draft | investigating | review-ready | learned | falsified | abandoned`
- Claim status：`hypothesis | source-confirmed | observed | cross-validated | falsified`

## Repository structure

```text
docs/
  WHITEBOX_LEARNING_FRAMEWORK.md # authoritative framework overview
  LEARNING_MECHANISM.md          # epistemic learning protocol
  LEARNING_BRANCH_WORKFLOW.md    # Git workflow and merge gate
  framework-review.md            # non-normative review record
templates/
  MECHANISM_UNIT.md              # one mechanism and its claim graph
  EXPERIMENT.md                  # one falsifiable experiment
  MERGE_REVIEW.md                # executable merge-gate record
topics/
  <system>/
    README.md                    # Mechanism Map
    coverage.md                  # Source Coverage Map
    mechanisms/
      <mechanism>/
        README.md
        MERGE_REVIEW.md
        experiments/
scripts/
  validate_framework.py          # repository contract validation
```

## Start here

1. Read the framework overview.
2. Select a source section through the Coverage Map.
3. Create one `learn/<system>/<mechanism>` branch.
4. Copy the Mechanism Unit and Experiment templates.
5. Link every important conclusion claim to source evidence and/or runtime evidence.
6. Complete `MERGE_REVIEW.md` before proposing the branch for `main`.

Validate repository contracts locally with:

```bash
python3 scripts/validate_framework.py
```
