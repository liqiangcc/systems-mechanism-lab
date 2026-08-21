# Unix/Linux Coverage Map

本文件只回答 **“来源处理到哪里、是否已映射到机制”**。机制模型、实验、evidence 和 learned 状态必须写入 [`README.md`](./README.md) 与 `mechanisms/`。

## Primary source

- 书籍：Michael Kerrisk，《Linux/UNIX系统编程手册（上、下册）》
- 原书：*The Linux Programming Interface*
- 当前来源：reading-mcp 已打开的本地 EPUB
- 正文规模：64 章 + 附录 A–F
- 初始化日期：2026-08-20

## Coverage status contract

Coverage status 只能使用：

| Status | 含义 |
| --- | --- |
| `not-started` | 尚未开始阅读该来源单元 |
| `in-progress` | 已开始阅读，但 source review 尚未完成 |
| `source-reviewed` | 已审阅来源，记录了 locator、关键问题和候选 claims |
| `mapped` | 已把候选机制链接到 Mechanism Map 或对应 unit；不表示机制已验证 |

禁止在本文件使用 `observed`、`cross-validated`、`learned` 等 Claim 或 Unit 状态。

## Current checkpoint

当前进度：**已定位并打开教材；已抽取并核对全书目录；正文尚未标记为 source-reviewed。**

已完成：

- [x] 找到 Unix/Linux 系统编程主教材
- [x] 打开教材并建立可读取文档
- [x] 提取 64 章与附录 A–F 的目录结构
- [x] 核对第 14 章主题：EPUB 结构节点误标为“系统编程概念”，前言和正文均表明实际主题是“文件系统”

待完成：

- [ ] 开始逐 section source-first 阅读
- [ ] 记录稳定 reading locator
- [ ] 提取机制问题和候选 Claim IDs
- [ ] 把候选机制映射到 [`README.md`](./README.md)
- [ ] 在独立 `learn/unix/<mechanism>` branch 中验证机制

## Chapter coverage

| # | 章节 | 状态 |
| ---: | --- | --- |
| 1 | 历史和标准 | not-started |
| 2 | 基本概念 | not-started |
| 3 | 系统编程概念 | not-started |
| 4 | 文件I/O：通用的I/O模型 | not-started |
| 5 | 深入探究文件I/O | not-started |
| 6 | 进程 | not-started |
| 7 | 内存分配 | not-started |
| 8 | 用户和组 | not-started |
| 9 | 进程凭证 | not-started |
| 10 | 时间 | not-started |
| 11 | 系统限制和选项 | not-started |
| 12 | 系统和进程信息 | not-started |
| 13 | 文件I/O缓冲 | not-started |
| 14 | 文件系统 | not-started |
| 15 | 文件属性 | not-started |
| 16 | 扩展属性 | not-started |
| 17 | 访问控制列表 | not-started |
| 18 | 目录与链接 | not-started |
| 19 | 监控文件事件 | not-started |
| 20 | 信号：基本概念 | not-started |
| 21 | 信号：信号处理器函数 | not-started |
| 22 | 信号：高级特性 | not-started |
| 23 | 定时器与休眠 | not-started |
| 24 | 进程的创建 | not-started |
| 25 | 进程的终止 | not-started |
| 26 | 监控子进程 | not-started |
| 27 | 程序的执行 | not-started |
| 28 | 详述进程创建和程序执行 | not-started |
| 29 | 线程：介绍 | not-started |
| 30 | 线程：线程同步 | not-started |
| 31 | 线程：线程安全和每线程存储 | not-started |
| 32 | 线程：线程取消 | not-started |
| 33 | 线程：更多细节 | not-started |
| 34 | 进程组、会话和作业控制 | not-started |
| 35 | 进程优先级和调度 | not-started |
| 36 | 进程资源 | not-started |
| 37 | DAEMON | not-started |
| 38 | 编写安全的特权程序 | not-started |
| 39 | 能力 | not-started |
| 40 | 登录记账 | not-started |
| 41 | 共享库基础 | not-started |
| 42 | 共享库高级特性 | not-started |
| 43 | 进程间通信简介 | not-started |
| 44 | 管道和FIFO | not-started |
| 45 | System V IPC介绍 | not-started |
| 46 | System V消息队列 | not-started |
| 47 | System V信号量 | not-started |
| 48 | System V共享内存 | not-started |
| 49 | 内存映射 | not-started |
| 50 | 虚拟内存操作 | not-started |
| 51 | POSIX IPC介绍 | not-started |
| 52 | POSIX消息队列 | not-started |
| 53 | POSIX信号量 | not-started |
| 54 | POSIX共享内存 | not-started |
| 55 | 文件加锁 | not-started |
| 56 | SOCKET：介绍 | not-started |
| 57 | SOCKET：UNIX DOMAIN | not-started |
| 58 | SOCKET：TCP/IP网络基础 | not-started |
| 59 | SOCKET：Internet Domain | not-started |
| 60 | SOCKET：服务器设计 | not-started |
| 61 | SOCKET：高级主题 | not-started |
| 62 | 终端 | not-started |
| 63 | 其他备选的I/O模型 | not-started |
| 64 | 伪终端 | not-started |

## Appendices

| 附录 | 主题 | 状态 |
| --- | --- | --- |
| A | 跟踪系统调用 | not-started |
| B | 解析命令行选项 | not-started |
| C | 对NULL指针做转型 | not-started |
| D | 内核配置 | not-started |
| E | 更多信息源 | not-started |
| F | 部分习题解答 | not-started |

## Update rule

完成来源处理时按事实更新：

```text
not-started
→ in-progress
→ source-reviewed
→ mapped
```

`mapped` 只说明 chapter / section 已关联到候选 Mechanism Unit。真正的 Claim status 和 Unit status 由对应 unit 与 merge review 决定。

Coverage 更新使用独立 `coverage(unix): ...` commit，不与 mechanism/evidence 变更混合。

## Next checkpoint

下一次学习从一个明确 section 和问题开始：

```text
section reading
→ source locator
→ candidate claims
→ candidate mechanism
→ update coverage
```

需要实验和证据时，创建独立 Mechanism Unit，不把结论塞回本文件。
