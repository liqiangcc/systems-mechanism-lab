# Experiment Template

> 实验的目标是区分假设并约束 claim，不是“跑一下命令”或证明唯一原因。

## Metadata

- Experiment ID: `EXP-001`
- Unit ID: `<system>/<mechanism>`
- Linked Claim IDs:
- Linked Hypothesis IDs:
- Date:
- Author:
- Environment:
- OS / kernel / product version:
- Hardware / container / VM:
- Required privileges:
- Raw evidence path:

## 1. Question

本实验要回答什么问题？它为什么能区分 linked hypotheses？

## 2. Pre-registered Hypotheses

| Hypothesis | Expected observation if true | Expected observation if false |
| --- | --- | --- |
| H1 | | |
| H2 | | |

必须在执行实验前填写。

## 3. Falsification Criteria

- 当前首选解释：
- 什么结果会推翻它：
- 什么结果只能说明“与模型一致”，不能排除替代解释：
- 哪些结果会让实验变成 inconclusive：

## 4. Variables

- Manipulated variables:
- Controlled variables:
- Observed variables:
- Known uncontrolled variables:

## 5. Preconditions and Safety

- Initial state:
- Required data / fixtures:
- Permissions:
- Side effects:
- Cleanup / rollback:

## 6. Procedure

```bash
# exact commands or reproducible steps
```

命令需要包含关键参数、输入和顺序。不要只写“运行程序并观察”。

## 7. Expected Evidence Manifest

| Evidence ID | Expected artifact | Collection method | Linked claims |
| --- | --- | --- | --- |
| E1 | | | |

## 8. Raw Evidence

只放未经解释的输出、日志、trace、measurement、状态快照或其稳定路径。

```text
raw output
```

大型文件放入 `experiments/raw/`。外部证据需记录 locator、生成命令，必要时记录 checksum。

## 9. Observations

只描述实际看到的事实。

| Evidence ID | Observation | Time / condition |
| --- | --- | --- |
| E1 | | |

## 10. Interpretation

| Claim / hypothesis | Supported, limited or falsified? | Reasoning from evidence | Alternative explanation |
| --- | --- | --- | --- |
| | | | |

注意：

- `observed` 是直接事实；
- `inferred` 是由事实推导的解释；
- “符合预期”不等于“唯一机制已证明”。

## 11. Conclusion

本实验最多支持到什么程度？明确要更新的 Claim status：

| Claim ID | Previous status | New status | Justification |
| --- | --- | --- | --- |
| | | | |

## 12. Reproducibility Check

- [ ] 在同一环境重复执行
- [ ] 结果是否稳定
- [ ] 命令和输入完整
- [ ] raw evidence 已保存
- [ ] 清理步骤已验证

重复次数与差异：

## 13. Limits

- Environment limits:
- Version limits:
- Measurement blind spots:
- Uncontrolled variables:
- Alternative explanations not excluded:
- Generalization limits:

## 14. Next Smallest Experiment

为了进一步排除替代解释，下一步最小实验是什么？
