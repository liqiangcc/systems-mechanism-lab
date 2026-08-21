# Unix/Linux Mechanism Map

本文件只负责索引 Unix/Linux Mechanism Units、依赖关系和生命周期状态，不承担章节覆盖，也不复制机制正文。

- Source Coverage Map: [`coverage.md`](./coverage.md)
- Repository learning protocol: [`../../docs/LEARNING_MECHANISM.md`](../../docs/LEARNING_MECHANISM.md)
- Unit template: [`../../templates/MECHANISM_UNIT.md`](../../templates/MECHANISM_UNIT.md)

## Status model

Mechanism Unit status：

```text
draft | investigating | review-ready | learned | falsified | abandoned
```

Claim evidence status 不写入本表；它属于各 Mechanism Unit 的 Claim-Evidence Matrix。

## Mechanism Units

| Unit ID | Problem summary | Dependencies | Unit status | Evidence summary | Unit |
| --- | --- | --- | --- | --- | --- |
| — | 尚无通过 merge gate 的 Unix/Linux Mechanism Unit | — | — | — | — |

## Rules

1. 每个 unit 由一个 `learn/unix/<mechanism>` branch 建立；
2. 一个 unit 可以引用多个章节，但只保留一份机制正文；
3. dependencies 使用 Unit ID 或明确标记 `external / unresolved`；
4. 只有 merge review 通过后才把 status 标记为 `learned`；
5. coverage 的 `mapped` 只表示来源已映射，不表示 unit 已验证；
6. 本表只做索引，结论和 evidence 必须留在 unit 目录。
