# System Mechanism White-box Learning Framework Review

> Review date: 2026-08-21  
> Branch: `learn/system-mechanism-framework`  
> Baseline commit: `cce2e3d12e2d08987f6c80b8a9a731c4d5779026`  
> Scope: every tracked file in the repository at the baseline

## 1. Review method

本次审查逐文件读取 baseline tree，并从以下角度检查：

- 规范是否只有一个 source of truth；
- Coverage、Mechanism、Evidence 的关注点是否分离；
- 状态是否有唯一语义；
- conclusion 是否可以追溯到具体 evidence；
- experiment 是否可证伪、可重复；
- merge gate 是否可以实际执行；
- 目录、模板和工作流是否互相一致；
- 框架是否能直接承载 Unix、Kafka、MySQL、Redis 和 JVM。

## 2. Findings

### F1 — Critical: parallel normative documents drifted

新增的 `learning-workflow.md`、`mechanism-unit-spec.md`、`merge-gate.md`、`experiment-evidence.md` 和 `source-linking.md` 与已有权威文档重复。

其中旧简版 branch convention 写成 `learn/<topic>-<mechanism>`，与正式规范 `learn/<system>/<mechanism>` 冲突；简版 workflow 还绕过了 boundary、claim audit 和完整 merge gate。

**Resolution:** 删除五份平行规范，新增唯一框架总览，并在 README 明确 canonical documents。

### F2 — High: Coverage status mixed navigation with evidence

`topics/unix/coverage.md` 原状态链包含 `experimented`、`cross-validated` 和 `learned`。这些属于机制或 claim 的证据状态，不属于章节覆盖状态，与 branch workflow 自身的 separation rule 矛盾。

**Resolution:** Coverage status 收敛为：

```text
not-started | in-progress | source-reviewed | mapped
```

### F3 — High: no claim-level evidence traceability

原模板只有整体 `Status` 和通用 Evidence 区域，无法回答某一条 conclusion 由哪条来源、哪个实验支持，也无法表达同一 unit 中不同 claim 的证据强度。

**Resolution:** 引入 Claim IDs、Source IDs、Evidence IDs 和 Claim-Evidence Matrix；整体 Unit lifecycle 与 Claim status 分离。

### F4 — High: merge gate was descriptive, not executable

原 gate 没有独立 review artifact，容易由作者直接宣称通过，也没有逐 claim 审计、raw evidence 检查和状态语义检查。

**Resolution:** 新增 `templates/MERGE_REVIEW.md`，并要求每个 Mechanism Unit 在进入 `main` 前填写。

### F5 — Medium: experiment language overstated certainty

旧文档把实验目的写成 “proving the mechanism model”，与主规范的可证伪和不伪造确定性原则冲突。

**Resolution:** 实验模板改为区分假设、保留替代解释，并使用 support / limit / falsify 语义。

### F6 — Medium: repository-level branch type was undefined

规范只定义 `learn/*`，导致框架维护也使用 learning branch 命名，模糊机制学习与仓库维护。

**Resolution:** 新增 `docs/<scope>` 作为 repository-level framework maintenance branch。当前 branch 是历史迁移分支，不在本次提交中强制改名。

### F7 — Medium: Mechanism Map was promised but absent

主规范要求 Coverage Map 与 Mechanism Map 分离，但 Unix topic 只有 coverage 文件。

**Resolution:** 新增 `topics/unix/README.md` 作为 Mechanism Map；当前明确记录尚无通过 gate 的 unit。

### F8 — Medium: no drift detection

文档重叠、状态混用和失效链接此前只能人工发现。

**Resolution:** 新增 `scripts/validate_framework.py` 与 GitHub Actions workflow，检查 canonical files、deprecated duplicates、模板合同、内部链接和 coverage status。

## 3. Resulting architecture

```text
Coverage Index       # where source reading is
      │
      ├─ Source Layer       # S1, S2, locators
      │
      └─ Mechanism Layer    # C1, C2, model, dependencies
                  │
                  └─ Evidence Layer  # E1, EXP-001, raw observations
                               │
                               └─ Merge Review
                                      │
                                      └─ main
```

三类状态独立：

```text
Coverage status ≠ Unit lifecycle ≠ Claim epistemic status
```

## 4. Files changed by remediation

Created:

- `docs/WHITEBOX_LEARNING_FRAMEWORK.md`
- `templates/MERGE_REVIEW.md`
- `topics/unix/README.md`
- `scripts/validate_framework.py`
- `.github/workflows/validate-framework.yml`

Reworked:

- `README.md`
- `docs/LEARNING_MECHANISM.md`
- `docs/LEARNING_BRANCH_WORKFLOW.md`
- `templates/MECHANISM_UNIT.md`
- `templates/EXPERIMENT.md`
- `topics/unix/coverage.md`

Removed as duplicate normative sources:

- `docs/experiment-evidence.md`
- `docs/learning-workflow.md`
- `docs/mechanism-unit-spec.md`
- `docs/merge-gate.md`
- `docs/source-linking.md`

## 5. Acceptance criteria

The remediation is acceptable only when:

- repository tree contains no deprecated parallel specifications；
- all internal Markdown links resolve；
- required templates expose the canonical fields；
- all coverage table statuses use the navigation-only enum；
- branch convention has one canonical form；
- local validator exits with code `0`；
- the committed branch is re-read and compared with `main` before review。

## 6. Verification evidence

Pre-commit reconstruction of the final tree:

```text
$ python3 scripts/validate_framework.py
Framework validation passed: 12 required files, 17 internal links, 70 coverage rows.
```

Additional checks:

- `python3 -m py_compile scripts/validate_framework.py` exited `0`;
- placeholder scan across README, docs, templates, topics, scripts and workflow found no unfinished markers;
- final tree contains only the 12 intended tracked files.

## 7. Final assessment

原框架方向正确：章节用于导航，机制用于组织，实验用于约束认知，`main` 保存长期状态。

本次修复解决的核心不是“再补几段说明”，而是把框架从多份描述性文档收敛为：

> **single-source, claim-traceable, state-separated, executable and regression-checked learning protocol**
