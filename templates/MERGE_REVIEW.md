# Mechanism Unit Merge Review

> 本文件是 merge gate 的执行记录。复制到 Mechanism Unit 目录并填写，不要只在聊天中口头宣称通过。

## Metadata

- Unit ID:
- Branch:
- Base commit:
- Head commit:
- Reviewer:
- Review date:
- Proposed outcome: `learned | falsified | abandoned`

## 1. Artifact Inventory

- Mechanism Unit:
- Mechanism Map entry:
- Related Coverage Map:
- Experiments:
- Raw evidence:
- Source locators:
- Validation command and output:

## 2. Scope Review

- [ ] 分支只有一个 Mechanism Unit
- [ ] Problem、scope 和 non-goals 明确
- [ ] dependencies 已记录
- [ ] 没有无关重构、整章摘录或临时文件

Findings:

## 3. Claim-Evidence Audit

| Claim ID | Claim status | Source IDs | Runtime Evidence IDs | Boundary | Reviewer decision |
| --- | --- | --- | --- | --- | --- |
| | | | | | accept / revise / reject |

检查：

- [ ] Conclusion 中没有 matrix 外的新 claim
- [ ] 每个关键 claim 有 evidence 或明确 unresolved
- [ ] Source ID 有版本和稳定 locator
- [ ] Runtime Evidence 能回到 experiment / raw evidence
- [ ] AI 回答未被登记为 evidence
- [ ] falsified claim 没有被静默删除

Findings:

## 4. Model Review

- [ ] objects、states、transitions、rules 足以解释行为
- [ ] causal chain 引用 Claim IDs
- [ ] invariants 和 trade-offs 已记录（适用时）
- [ ] conclusion 的确定性没有超过 evidence

Findings:

## 5. Falsifiability and Reproducibility

- [ ] competing hypotheses 在结果前记录
- [ ] falsification criteria 明确
- [ ] observation 与 inference 分离
- [ ] environment、version、commands 和 inputs 完整
- [ ] raw evidence 存在或有稳定 locator
- [ ] alternative explanations 保留
- [ ] 复现结果与差异已记录

Findings:

## 6. Boundary Review

- [ ] 至少一个 boundary、exceptional path 或 counterexample
- [ ] version / implementation applicability 明确
- [ ] concurrency / failure / resource limits 已考虑
- [ ] observation tool 的 blind spots 已记录
- [ ] 没有把实现细节无条件泛化成 invariant

Findings:

## 7. State and Repository Review

- [ ] Coverage status 只使用 navigation enum
- [ ] Unit status 当前为 `review-ready`
- [ ] Claim status 使用 epistemic enum
- [ ] Mechanism Map 已更新（如需）
- [ ] coverage 变更使用独立 commit（如有）
- [ ] branch 基于足够新的 `main`
- [ ] commit history 能重建认知变化
- [ ] `python3 scripts/validate_framework.py` exits `0`

Findings:

## 8. Blocking Issues

| Severity | Issue | Required fix | Evidence needed |
| --- | --- | --- | --- |
| Critical / High / Medium / Low | | | |

## 9. Decision

- [ ] **Accept as learned**：所有 blocking issues 已解决，可以进入 `main`
- [ ] **Accept falsification knowledge**：核心假设被推翻，但反例和修正值得进入 `main`
- [ ] **Request changes**：继续留在 `learn/*`
- [ ] **Abandon**：范围或价值不足，不合并

Decision rationale:

## 10. Post-merge Actions

- [ ] Unit status 改为 `learned` 或保留 `falsified`
- [ ] Merge commit / PR 已记录
- [ ] learning branch 已删除
- [ ] follow-up unresolved questions 已创建新的独立 scope（如需）
