# Mechanism Unit Template

> 一个 Mechanism Unit 只解决一个可以独立解释、实验和审查的机制问题。不要把整章摘要塞进这里。

## Metadata

- Unit ID: `<system>/<mechanism>`
- System:
- Mechanism:
- Unit status: `draft | investigating | review-ready | learned | falsified | abandoned`
- Branch: `learn/<system>/<mechanism>`
- Last updated:
- Related coverage:
- Dependencies:
- Dependents (optional):

## 1. Problem

这个机制解决什么问题？如果没有它，会发生什么？

## 2. Core Question

用一句可验证的问题描述本单元。

## 3. Scope / Non-goals

### In scope

- 

### Out of scope

- 

## 4. Competing Hypotheses

| Hypothesis | Explanation | Distinguishing observation |
| --- | --- | --- |
| H1 | | |
| H2 | | |

在看到实验结果前写明当前首选解释和推翻条件。

## 5. Source Model

### Objects

- 

### States

- 

### State transitions

```text
state A
→ trigger / rule
→ state B
```

### Invariants

- 

### Causal chain

```text
constraint/problem
→ mechanism
→ state change
→ observable behavior
→ cost/trade-off
```

### Trade-offs

- 

## 6. Claims and Evidence

Claim status：

```text
hypothesis | source-confirmed | observed | cross-validated | falsified
```

| Claim ID | Claim | Status | Source evidence | Runtime evidence | Boundary |
| --- | --- | --- | --- | --- | --- |
| C1 | | hypothesis | | | |
| C2 | | hypothesis | | | |

规则：

- Conclusion 中的关键陈述必须引用 Claim ID；
- 没有 evidence 的 claim 保持 `hypothesis`；
- `source-confirmed`、`observed` 和 `cross-validated` 不互相替代；
- 被推翻的 claim 保留并标记 `falsified`，不要静默删除。

## 7. Source Evidence

| Source ID | Source / authority | Version / date / commit | Stable locator | Supported or falsified claims | Notes / applicability |
| --- | --- | --- | --- | --- | --- |
| S1 | | | | | |

不要把 AI 回答登记为 Source Evidence。

## 8. Observables

现实系统中可以观察什么来判断机制是否发生？

| Observable | Tool / location | Expected relation to claims | Blind spots |
| --- | --- | --- | --- |
| | | | |

## 9. Experiments

| Experiment ID | Linked claims / hypotheses | Expected distinction | Result | Evidence IDs |
| --- | --- | --- | --- | --- |
| EXP-001 | | | pending | |

详细实验放到 `experiments/EXP-001.md`，raw evidence 放到 `experiments/raw/` 或记录稳定 locator。

## 10. Observation and Inference

### Observations

只写实际看到的事实，并引用 Evidence ID。

- E1:

### Inferences

说明这些 observation 支持、限制或反驳哪些 claim；保留未排除的替代解释。

- 

## 11. Conclusion

写当前最小、不过度外推的结论，并引用 Claim ID，例如：

```text
C1 + C2 support the following bounded causal chain: ...
```

不要在本节引入 Claim-Evidence Matrix 中不存在的新命题。

## 12. Boundaries / Counterexamples

- Preconditions:
- Version / implementation boundary:
- Concurrency / failure boundary:
- Known counterexample:
- Alternative explanations not yet excluded:
- Observation-tool limitations:

## 13. Transfer

| System | Similar constraint | Similar mechanism | Important difference / non-transferable assumption |
| --- | --- | --- | --- |
| | | | |

## 14. Open Questions

| Question | Why unresolved | Required source / experiment | Blocks merge? |
| --- | --- | --- | --- |
| | | | yes / no |

## 15. Definition of Learned

- [ ] Problem、scope 和 non-goals 清楚
- [ ] dependencies 已记录
- [ ] objects、states、transitions、invariants 可解释
- [ ] causal chain 能预测行为
- [ ] 关键陈述已拆为 Claim IDs
- [ ] 每个关键 claim 有 evidence 或明确 unresolved
- [ ] 至少完成一个区分关键假设的 experiment，或说明不可行原因
- [ ] raw evidence、observation 和 inference 分离
- [ ] 找到 boundary、异常路径或 counterexample
- [ ] trade-off 已说明
- [ ] 完成一次跨系统比较
- [ ] Unit status 已更新为 `review-ready`
- [ ] `MERGE_REVIEW.md` 已完成
- [ ] repository validator 通过
