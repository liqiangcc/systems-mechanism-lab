# Mechanism Unit Template

> 一个机制单元只解决一个相对独立的机制问题。不要把整章摘要塞进这里。

## Metadata

- System:
- Mechanism:
- Status: `hypothesis | source-confirmed | observed | cross-validated | falsified`
- Related chapters/docs:
- Dependencies:

## 1. Problem

这个机制要解决什么问题？如果没有它，会发生什么？

## 2. Core Question

用一句可验证的问题描述本单元。

## 3. Competing Hypotheses

- H1:
- H2:

什么观察结果能区分它们？

## 4. Source Model

### Objects

- 

### States

- 

### State transitions

```text
state A
→ trigger
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

## 5. Observables

现实系统中可以观察什么来判断这个机制是否真的发生？

- 

## 6. Experiments

| Experiment | Hypothesis | Expected observation | Result |
| --- | --- | --- | --- |
| | | | |

详细实验放到 `experiments/`。

## 7. Evidence

### Source evidence

- Source:
- Claim supported:

### Runtime evidence

- Experiment:
- Observation:
- Raw evidence location:

## 8. Conclusion

当前最小、不过度外推的结论是什么？

## 9. Boundaries / Counterexamples

- 成立条件：
- 已知边界：
- 可能反例：
- 版本/实现相关性：

## 10. Transfer

在哪些其他系统中存在相似问题或机制？

| System | Similarity | Important difference |
| --- | --- | --- |
| | | |

## 11. Open Questions

- 

## 12. Definition of Learned

- [ ] 能解释 problem
- [ ] 能描述对象、状态和转换
- [ ] 能解释因果链
- [ ] 能预测条件变化后的行为
- [ ] 知道可观察点
- [ ] 至少完成一个关键实验
- [ ] 关键结论有证据
- [ ] 找到边界或反例
- [ ] 能说明 trade-off
- [ ] 能进行一次跨系统比较
