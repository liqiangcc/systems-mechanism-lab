# Unix/Linux Coverage Map

本文件只回答 **“来源在哪里、来源结构是什么、读到哪里、是否已完成 source review、是否已映射到机制”**。机制模型、实验、evidence 和 Unit/Claim 状态不写入本文件。

- Complete Source Map: [`source-map.md`](./source-map.md)
- Mechanism Map: [`README.md`](./README.md)
- Coverage/Mechanism separation: [`../../docs/WHITEBOX_LEARNING_FRAMEWORK.md`](../../docs/WHITEBOX_LEARNING_FRAMEWORK.md)

## Primary source

- 书籍：Michael Kerrisk，《Linux/UNIX系统编程手册（上、下册）》
- 原书：*The Linux Programming Interface*
- edition / 版本：`unknown / not confirmed`
- 当前正文来源：reading-mcp 已打开的本地 EPUB
- primary reading-mcp identifier：`doc:sha256:286e0104a40d05c3cb76f08e2d6a06391ce9d1bc603351aefc2340aca3349b2f`
- 正文规模：64 Chapters / 585 Sections / 229 Subsections
- 附录规模：A–F，共 6 个
- 当前粒度：**Section (`X.Y`)**；Subsection 保留在 Source Map 中，不单独承担 Coverage status

## Coverage status contract

Coverage status 只能使用：

| Status | 含义 |
| --- | --- |
| `not-started` | 尚未开始阅读该来源单元 |
| `in-progress` | 已开始阅读，但 source review 尚未完成 |
| `source-reviewed` | 已完成该来源单元的 source-first 审阅并记录 locator |
| `mapped` | 已把该来源单元链接到候选 Mechanism Unit；不表示机制已验证 |

正文目录已映射不等于正文已阅读。任何 Chapter/Section 都不会仅因出现在目录中而升级状态。

## Structural source coverage

| Unit | Locator | Purpose | Status |
| --- | --- | --- | --- |
| Preface | `doc:sha256:7e4de58ed72799de035497b7702666f5e375c88dfc8e3c6ea2f0977645c91889`; `pdf:page:1`–`11` | 只提取书的目标、读者和组织结构 | source-reviewed |
| Detailed TOC (HTML) | `doc:sha256:fe522b2d5b05b1c76658bad4d6351367dbfed239b85fe33a45d81d42acffe9f9`; `section://detailed-table-of-contents-for-the-linux-programming-interface` | 完整编号、标题和 search-unit locators | source-reviewed |
| Detailed TOC (PDF) | `doc:sha256:f766e1f40b765781b321a5014bd9cef507d9d64624c26ca109490585fb45e62f`; `pdf:page:1`–`19` | 页码与后半本/附录交叉核对 | source-reviewed |

## Current checkpoint

Source Map / Coverage Map 建设已经完成；本次进一步完成了 **TLPI 1.1 正文的 source-first review**。当前 `1.1 = source-reviewed`，其余 584 个编号 Section 仍为 `not-started`；Mechanism Map 仍为空。

已验证：

- 64 个 Chapter 连续，无 1–64 断层；
- 585 个 `X.Y` Section，章内编号连续；
- 229 个 `X.Y.Z` Subsection，父级内编号连续；
- 6 个 Appendix，A–F 完整；
- Chapter 64 和 Appendix A–F 均存在，未因响应大小遗漏；
- TLPI 1.1 使用 primary EPUB 的精确 `section_id` 完整读取，`truncated=false`；
- Chapter 14 EPUB 标题异常已记录在 Source Map，不据异常节点猜测正文主题。

## Chapter summary

Chapter status 是本章 Section 状态的汇总；Chapter 1 已开始但未完成全部 Section，因此为 `in-progress`，其余 Chapter 仍为 `not-started`。

| Chapter | Canonical title | Section range | Section count | Status |
| ---: | --- | --- | ---: | --- |
| 1 | HISTORY AND STANDARDS | `1.1`–`1.4` | 4 | in-progress |
| 2 | FUNDAMENTAL CONCEPTS | `2.1`–`2.20` | 20 | not-started |
| 3 | SYSTEM PROGRAMMING CONCEPTS | `3.1`–`3.8` | 8 | not-started |
| 4 | FILE I/O: THE UNIVERSAL I/O MODEL | `4.1`–`4.10` | 10 | not-started |
| 5 | FILE I/O: FURTHER DETAILS | `5.1`–`5.14` | 14 | not-started |
| 6 | PROCESSES | `6.1`–`6.10` | 10 | not-started |
| 7 | MEMORY ALLOCATION | `7.1`–`7.4` | 4 | not-started |
| 8 | USERS AND GROUPS | `8.1`–`8.7` | 7 | not-started |
| 9 | PROCESS CREDENTIALS | `9.1`–`9.9` | 9 | not-started |
| 10 | TIME | `10.1`–`10.9` | 9 | not-started |
| 11 | SYSTEM LIMITS AND OPTIONS | `11.1`–`11.7` | 7 | not-started |
| 12 | SYSTEM AND PROCESS INFORMATION | `12.1`–`12.4` | 4 | not-started |
| 13 | FILE I/O BUFFERING | `13.1`–`13.9` | 9 | not-started |
| 14 | FILE SYSTEMS | `14.1`–`14.13` | 13 | not-started |
| 15 | FILE ATTRIBUTES | `15.1`–`15.7` | 7 | not-started |
| 16 | EXTENDED ATTRIBUTES | `16.1`–`16.5` | 5 | not-started |
| 17 | ACCESS CONTROL LISTS | `17.1`–`17.10` | 10 | not-started |
| 18 | DIRECTORIES AND LINKS | `18.1`–`18.16` | 16 | not-started |
| 19 | MONITORING FILE EVENTS | `19.1`–`19.8` | 8 | not-started |
| 20 | SIGNALS: FUNDAMENTAL CONCEPTS | `20.1`–`20.16` | 16 | not-started |
| 21 | SIGNALS: SIGNAL HANDLERS | `21.1`–`21.7` | 7 | not-started |
| 22 | SIGNALS: ADVANCED FEATURES | `22.1`–`22.15` | 15 | not-started |
| 23 | TIMERS AND SLEEPING | `23.1`–`23.9` | 9 | not-started |
| 24 | PROCESS CREATION | `24.1`–`24.6` | 6 | not-started |
| 25 | PROCESS TERMINATION | `25.1`–`25.6` | 6 | not-started |
| 26 | MONITORING CHILD PROCESSES | `26.1`–`26.5` | 5 | not-started |
| 27 | PROGRAM EXECUTION | `27.1`–`27.9` | 9 | not-started |
| 28 | PROCESS CREATION AND PROGRAM EXECUTION IN MORE DETAIL | `28.1`–`28.6` | 6 | not-started |
| 29 | THREADS: INTRODUCTION | `29.1`–`29.11` | 11 | not-started |
| 30 | THREADS: THREAD SYNCHRONIZATION | `30.1`–`30.4` | 4 | not-started |
| 31 | THREADS: THREAD SAFETY AND PER-THREAD STORAGE | `31.1`–`31.6` | 6 | not-started |
| 32 | THREADS: THREAD CANCELLATION | `32.1`–`32.8` | 8 | not-started |
| 33 | THREADS: FURTHER DETAILS | `33.1`–`33.8` | 8 | not-started |
| 34 | PROCESS GROUPS, SESSIONS, AND JOB CONTROL | `34.1`–`34.9` | 9 | not-started |
| 35 | PROCESS PRIORITIES AND SCHEDULING | `35.1`–`35.6` | 6 | not-started |
| 36 | PROCESS RESOURCES | `36.1`–`36.5` | 5 | not-started |
| 37 | DAEMONS | `37.1`–`37.7` | 7 | not-started |
| 38 | WRITING SECURE PRIVILEGED PROGRAMS | `38.1`–`38.13` | 13 | not-started |
| 39 | CAPABILITIES | `39.1`–`39.12` | 12 | not-started |
| 40 | LOGIN ACCOUNTING | `40.1`–`40.9` | 9 | not-started |
| 41 | FUNDAMENTALS OF SHARED LIBRARIES | `41.1`–`41.15` | 15 | not-started |
| 42 | ADVANCED FEATURES OF SHARED LIBRARIES | `42.1`–`42.8` | 8 | not-started |
| 43 | INTERPROCESS COMMUNICATION OVERVIEW | `43.1`–`43.6` | 6 | not-started |
| 44 | PIPES AND FIFOS | `44.1`–`44.12` | 12 | not-started |
| 45 | INTRODUCTION TO SYSTEM V IPC | `45.1`–`45.10` | 10 | not-started |
| 46 | SYSTEM V MESSAGE QUEUES | `46.1`–`46.11` | 11 | not-started |
| 47 | SYSTEM V SEMAPHORES | `47.1`–`47.13` | 13 | not-started |
| 48 | SYSTEM V SHARED MEMORY | `48.1`–`48.11` | 11 | not-started |
| 49 | MEMORY MAPPINGS | `49.1`–`49.13` | 13 | not-started |
| 50 | VIRTUAL MEMORY OPERATIONS | `50.1`–`50.6` | 6 | not-started |
| 51 | INTRODUCTION TO POSIX IPC | `51.1`–`51.3` | 3 | not-started |
| 52 | POSIX MESSAGE QUEUES | `52.1`–`52.11` | 11 | not-started |
| 53 | POSIX SEMAPHORES | `53.1`–`53.8` | 8 | not-started |
| 54 | POSIX SHARED MEMORY | `54.1`–`54.7` | 7 | not-started |
| 55 | FILE LOCKING | `55.1`–`55.9` | 9 | not-started |
| 56 | SOCKETS: INTRODUCTION | `56.1`–`56.7` | 7 | not-started |
| 57 | SOCKETS: UNIX DOMAIN | `57.1`–`57.8` | 8 | not-started |
| 58 | SOCKETS: FUNDAMENTALS OF TCP/IP NETWORKS | `58.1`–`58.8` | 8 | not-started |
| 59 | SOCKETS: INTERNET DOMAINS | `59.1`–`59.17` | 17 | not-started |
| 60 | SOCKETS: SERVER DESIGN | `60.1`–`60.7` | 7 | not-started |
| 61 | SOCKETS: ADVANCED TOPICS | `61.1`–`61.15` | 15 | not-started |
| 62 | TERMINALS | `62.1`–`62.12` | 12 | not-started |
| 63 | ALTERNATIVE I/O MODELS | `63.1`–`63.7` | 7 | not-started |
| 64 | PSEUDOTERMINALS | `64.1`–`64.10` | 10 | not-started |

## Section coverage

每个 Section 使用格式无关的 `tlpi:X.Y` 语义 locator；精确标题和 reading-mcp TOC locator 见 [`source-map.md`](./source-map.md)。

### Part 1 — Background and concepts

#### Chapter 1 — HISTORY AND STANDARDS

| Chapter | Section | Exact source title | Locator | Status |
| ---: | --- | --- | --- | --- |
| 1 | `1.1` | A Brief History of UNIX and C | `tlpi:1.1` | source-reviewed |
| 1 | `1.2` | A Brief History of Linux | `tlpi:1.2` | not-started |
| 1 | `1.3` | Standardization | `tlpi:1.3` | not-started |
| 1 | `1.4` | Summary | `tlpi:1.4` | not-started |

##### TLPI 1.1 source review

- Primary EPUB exact title：`1.1 UNIX和C语言简史`
- reading-mcp document_id：`doc:sha256:286e0104a40d05c3cb76f08e2d6a06391ce9d1bc603351aefc2340aca3349b2f`
- source：`file:///root/doc/LinuxUNIX系统编程手册（上、下册）（异步图书） (Michael Kerrisk) (z-library.sk, 1lib.sk, z-lib.sk) (2).epub`
- section_id：`section://epub-10/第1章-历史和标准/1-1-unix和c语言简史`
- stable semantic locator：`tlpi:1.1`
- native locator：`epub:OEBPS/text00009.html#nav_point_21`
- section_path：`第1章 历史和标准` → `1.1 UNIX和C语言简史`
- truncated：`false`
- Locator 核对：Source Map 的 `tlpi:1.1` 与英文 canonical TOC 标题仍可用于格式无关导航；本次 primary EPUB 实测标题为中文，并首次确认可直接恢复到正文的 `section_id` 与 native locator。
- 最小结构摘要：本节先交代 UNIX 的早期来源以及 C 与 UNIX 的共同发展，再概述 UNIX 第一版至第六版及高校传播，最后进入第七版后的 BSD/System V 分支、早期跨硬件移植、4.2BSD 的 TCP/IP/套接字 API 与商业 UNIX 扩展。
- Candidate questions：C 重写 UNIX 为什么促进跨硬件移植；早期管道如何演化为后续 IPC 接口；BSD/System V 分支分别怎样影响后来的 UNIX/Linux 编程接口；4.2BSD 套接字 API 为什么成为后续网络编程的重要接口来源。
- Mechanism Unit mapping：`none`。**本 Section 完成 source review，但暂不产生 Mechanism Unit。** 本节以历史背景和接口来路为主，尚未形成一个在本节内部就足够独立解释、实验和审查的机制问题。

#### Chapter 2 — FUNDAMENTAL CONCEPTS

| Chapter | Section | Exact source title | Locator | Status |
| ---: | --- | --- | --- | --- |
| 2 | `2.1` | The Core Operating System: The Kernel | `tlpi:2.1` | not-started |
| 2 | `2.2` | The Shell | `tlpi:2.2` | not-started |
| 2 | `2.3` | Users and Groups | `tlpi:2.3` | not-started |
| 2 | `2.4` | Single Directory Hierarchy, Directories, Links, and Files | `tlpi:2.4` | not-started |
| 2 | `2.5` | File I/O Model | `tlpi:2.5` | not-started |
| 2 | `2.6` | Programs | `tlpi:2.6` | not-started |
| 2 | `2.7` | Processes | `tlpi:2.7` | not-started |
| 2 | `2.8` | Memory Mappings | `tlpi:2.8` | not-started |
| 2 | `2.9` | Static and Shared Libraries | `tlpi:2.9` | not-started |
| 2 | `2.10` | Interprocess Communication and Synchronization | `tlpi:2.10` | not-started |
| 2 | `2.11` | Signals | `tlpi:2.11` | not-started |
| 2 | `2.12` | Threads | `tlpi:2.12` | not-started |
| 2 | `2.13` | Process Groups and Shell Job Control | `tlpi:2.13` | not-started |
| 2 | `2.14` | Sessions, Controlling Terminals, and Controlling Processes | `tlpi:2.14` | not-started |
| 2 | `2.15` | Pseudoterminals | `tlpi:2.15` | not-started |
| 2 | `2.16` | Date and Time | `tlpi:2.16` | not-started |
| 2 | `2.17` | Client-Server Architecture | `tlpi:2.17` | not-started |
| 2 | `2.18` | Realtime | `tlpi:2.18` | not-started |
| 2 | `2.19` | The /proc File System | `tlpi:2.19` | not-started |
| 2 | `2.20` | Summary | `tlpi:2.20` | not-started |

#### Chapter 3 — SYSTEM PROGRAMMING CONCEPTS

| Chapter | Section | Exact source title | Locator | Status |
| ---: | --- | --- | --- | --- |
| 3 | `3.1` | System Calls | `tlpi:3.1` | not-started |
| 3 | `3.2` | Library Functions | `tlpi:3.2` | not-started |
| 3 | `3.3` | The Standard C Library; The GNU C Library ( glibc ) | `tlpi:3.3` | not-started |
| 3 | `3.4` | Handling Errors from System Calls and Library Functions | `tlpi:3.4` | not-started |
| 3 | `3.5` | Notes on the Example Programs in This Book | `tlpi:3.5` | not-started |
| 3 | `3.6` | Portability Issues | `tlpi:3.6` | not-started |
| 3 | `3.7` | Summary | `tlpi:3.7` | not-started |
| 3 | `3.8` | Exercise | `tlpi:3.8` | not-started |

### Part 2 — Fundamental features of the system programming interface

#### Chapter 4 — FILE I/O: THE UNIVERSAL I/O MODEL

| Chapter | Section | Exact source title | Locator | Status |
| ---: | --- | --- | --- | --- |
| 4 | `4.1` | Overview | `tlpi:4.1` | not-started |
| 4 | `4.2` | Universality of I/O | `tlpi:4.2` | not-started |
| 4 | `4.3` | Opening a File: open() | `tlpi:4.3` | not-started |
| 4 | `4.4` | Reading from a File: read() | `tlpi:4.4` | not-started |
| 4 | `4.5` | Writing to a File: write() | `tlpi:4.5` | not-started |
| 4 | `4.6` | Closing a File: close() | `tlpi:4.6` | not-started |
| 4 | `4.7` | Changing the File Offset: lseek() | `tlpi:4.7` | not-started |
| 4 | `4.8` | Operations Outside the Universal I/O Model: ioctl() | `tlpi:4.8` | not-started |
| 4 | `4.9` | Summary | `tlpi:4.9` | not-started |
| 4 | `4.10` | Exercises | `tlpi:4.10` | not-started |

#### Chapter 5 — FILE I/O: FURTHER DETAILS

| Chapter | Section | Exact source title | Locator | Status |
| ---: | --- | --- | --- | --- |
| 5 | `5.1` | Atomicity and Race Conditions | `tlpi:5.1` | not-started |
| 5 | `5.2` | File Control Operations: fcntl() | `tlpi:5.2` | not-started |
| 5 | `5.3` | Open File Status Flags | `tlpi:5.3` | not-started |
| 5 | `5.4` | Relationship Between File Descriptors and Open Files | `tlpi:5.4` | not-started |
| 5 | `5.5` | Duplicating File Descriptors | `tlpi:5.5` | not-started |
| 5 | `5.6` | File I/O at a Specified Offset: pread() and pwrite() | `tlpi:5.6` | not-started |
| 5 | `5.7` | Scatter-Gather I/O: readv() and writev() | `tlpi:5.7` | not-started |
| 5 | `5.8` | Truncating a File: truncate() and ftruncate() | `tlpi:5.8` | not-started |
| 5 | `5.9` | Nonblocking I/O | `tlpi:5.9` | not-started |
| 5 | `5.10` | I/O on Large Files | `tlpi:5.10` | not-started |
| 5 | `5.11` | The /dev/fd Directory | `tlpi:5.11` | not-started |
| 5 | `5.12` | Creating Temporary Files | `tlpi:5.12` | not-started |
| 5 | `5.13` | Summary | `tlpi:5.13` | not-started |
| 5 | `5.14` | Exercises | `tlpi:5.14` | not-started |

#### Chapter 6 — PROCESSES

| Chapter | Section | Exact source title | Locator | Status |
| ---: | --- | --- | --- | --- |
| 6 | `6.1` | Processes and Programs | `tlpi:6.1` | not-started |
| 6 | `6.2` | Process ID and Parent Process ID | `tlpi:6.2` | not-started |
| 6 | `6.3` | Memory Layout of a Process | `tlpi:6.3` | not-started |
| 6 | `6.4` | Virtual Memory Management | `tlpi:6.4` | not-started |
| 6 | `6.5` | The Stack and Stack Frames | `tlpi:6.5` | not-started |
| 6 | `6.6` | Command-Line Arguments ( argc , argv ) | `tlpi:6.6` | not-started |
| 6 | `6.7` | Environment List | `tlpi:6.7` | not-started |
| 6 | `6.8` | Performing a Nonlocal Goto: setjmp() and longjmp() | `tlpi:6.8` | not-started |
| 6 | `6.9` | Summary | `tlpi:6.9` | not-started |
| 6 | `6.10` | Exercises | `tlpi:6.10` | not-started |

#### Chapter 7 — MEMORY ALLOCATION

| Chapter | Section | Exact source title | Locator | Status |
| ---: | --- | --- | --- | --- |
| 7 | `7.1` | Allocating Memory on the Heap | `tlpi:7.1` | not-started |
| 7 | `7.2` | Allocating Memory on the Stack: alloca() | `tlpi:7.2` | not-started |
| 7 | `7.3` | Summary | `tlpi:7.3` | not-started |
| 7 | `7.4` | Exercises | `tlpi:7.4` | not-started |

#### Chapter 8 — USERS AND GROUPS

| Chapter | Section | Exact source title | Locator | Status |
| ---: | --- | --- | --- | --- |
| 8 | `8.1` | The Password File: /etc/passwd | `tlpi:8.1` | not-started |
| 8 | `8.2` | The Shadow Password File: /etc/shadow | `tlpi:8.2` | not-started |
| 8 | `8.3` | The Group File: /etc/group | `tlpi:8.3` | not-started |
| 8 | `8.4` | Retrieving User and Group Information | `tlpi:8.4` | not-started |
| 8 | `8.5` | Password Encryption and User Authentication | `tlpi:8.5` | not-started |
| 8 | `8.6` | Summary | `tlpi:8.6` | not-started |
| 8 | `8.7` | Exercises | `tlpi:8.7` | not-started |

#### Chapter 9 — PROCESS CREDENTIALS

| Chapter | Section | Exact source title | Locator | Status |
| ---: | --- | --- | --- | --- |
| 9 | `9.1` | Real User ID and Real Group ID | `tlpi:9.1` | not-started |
| 9 | `9.2` | Effective User ID and Effective Group ID | `tlpi:9.2` | not-started |
| 9 | `9.3` | Set-User-ID and Set-Group-ID Programs | `tlpi:9.3` | not-started |
| 9 | `9.4` | Saved Set-User-ID and Saved Set-Group-ID | `tlpi:9.4` | not-started |
| 9 | `9.5` | File-System User ID and File-System Group ID | `tlpi:9.5` | not-started |
| 9 | `9.6` | Supplementary Group IDs | `tlpi:9.6` | not-started |
| 9 | `9.7` | Retrieving and Modifying Process Credentials | `tlpi:9.7` | not-started |
| 9 | `9.8` | Summary | `tlpi:9.8` | not-started |
| 9 | `9.9` | Exercises | `tlpi:9.9` | not-started |

#### Chapter 10 — TIME

| Chapter | Section | Exact source title | Locator | Status |
| ---: | --- | --- | --- | --- |
| 10 | `10.1` | Calendar Time | `tlpi:10.1` | not-started |
| 10 | `10.2` | Time-Conversion Functions | `tlpi:10.2` | not-started |
| 10 | `10.3` | Timezones | `tlpi:10.3` | not-started |
| 10 | `10.4` | Locales | `tlpi:10.4` | not-started |
| 10 | `10.5` | Updating the System Clock | `tlpi:10.5` | not-started |
| 10 | `10.6` | The Software Clock (Jiffies) | `tlpi:10.6` | not-started |
| 10 | `10.7` | Process Time | `tlpi:10.7` | not-started |
| 10 | `10.8` | Summary | `tlpi:10.8` | not-started |
| 10 | `10.9` | Exercise | `tlpi:10.9` | not-started |

#### Chapter 11 — SYSTEM LIMITS AND OPTIONS

| Chapter | Section | Exact source title | Locator | Status |
| ---: | --- | --- | --- | --- |
| 11 | `11.1` | System Limits | `tlpi:11.1` | not-started |
| 11 | `11.2` | Retrieving System Limits (and Options) at Run Time | `tlpi:11.2` | not-started |
| 11 | `11.3` | Retrieving File-Related Limits (and Options) at Run Time | `tlpi:11.3` | not-started |
| 11 | `11.4` | Indeterminate Limits | `tlpi:11.4` | not-started |
| 11 | `11.5` | System Options | `tlpi:11.5` | not-started |
| 11 | `11.6` | Summary | `tlpi:11.6` | not-started |
| 11 | `11.7` | Exercises | `tlpi:11.7` | not-started |

#### Chapter 12 — SYSTEM AND PROCESS INFORMATION

| Chapter | Section | Exact source title | Locator | Status |
| ---: | --- | --- | --- | --- |
| 12 | `12.1` | The /proc File System | `tlpi:12.1` | not-started |
| 12 | `12.2` | System Identification: uname() | `tlpi:12.2` | not-started |
| 12 | `12.3` | Summary | `tlpi:12.3` | not-started |
| 12 | `12.4` | Exercises | `tlpi:12.4` | not-started |

### Part 3 — More advanced features of the system programming interface

#### Chapter 13 — FILE I/O BUFFERING

| Chapter | Section | Exact source title | Locator | Status |
| ---: | --- | --- | --- | --- |
| 13 | `13.1` | Kernel Buffering of File I/O: The Buffer Cache | `tlpi:13.1` | not-started |
| 13 | `13.2` | Buffering in the stdio Library | `tlpi:13.2` | not-started |
| 13 | `13.3` | Controlling Kernel Buffering of File I/O | `tlpi:13.3` | not-started |
| 13 | `13.4` | Summary of I/O Buffering | `tlpi:13.4` | not-started |
| 13 | `13.5` | Giving the Kernel Hints About I/O Patterns: posix_fadvise() | `tlpi:13.5` | not-started |
| 13 | `13.6` | Bypassing the Buffer Cache: Direct I/O | `tlpi:13.6` | not-started |
| 13 | `13.7` | Mixing Library Functions and System Calls for File I/O | `tlpi:13.7` | not-started |
| 13 | `13.8` | Summary | `tlpi:13.8` | not-started |
| 13 | `13.9` | Exercises | `tlpi:13.9` | not-started |

#### Chapter 14 — FILE SYSTEMS

| Chapter | Section | Exact source title | Locator | Status |
| ---: | --- | --- | --- | --- |
| 14 | `14.1` | Device Special Files (Devices) | `tlpi:14.1` | not-started |
| 14 | `14.2` | Disks and Partitions | `tlpi:14.2` | not-started |
| 14 | `14.3` | File Systems | `tlpi:14.3` | not-started |
| 14 | `14.4` | I-nodes | `tlpi:14.4` | not-started |
| 14 | `14.5` | The Virtual File System (VFS) | `tlpi:14.5` | not-started |
| 14 | `14.6` | Journaling File Systems | `tlpi:14.6` | not-started |
| 14 | `14.7` | Single Directory Hierarchy and Mount Points | `tlpi:14.7` | not-started |
| 14 | `14.8` | Mounting and Unmounting File Systems | `tlpi:14.8` | not-started |
| 14 | `14.9` | Advanced Mount Features | `tlpi:14.9` | not-started |
| 14 | `14.10` | A Virtual Memory File System: tmpfs | `tlpi:14.10` | not-started |
| 14 | `14.11` | Obtaining Information About a File System: statvfs() | `tlpi:14.11` | not-started |
| 14 | `14.12` | Summary | `tlpi:14.12` | not-started |
| 14 | `14.13` | Exercise | `tlpi:14.13` | not-started |

#### Chapter 15 — FILE ATTRIBUTES

| Chapter | Section | Exact source title | Locator | Status |
| ---: | --- | --- | --- | --- |
| 15 | `15.1` | Retrieving File Information: stat() | `tlpi:15.1` | not-started |
| 15 | `15.2` | File Timestamps | `tlpi:15.2` | not-started |
| 15 | `15.3` | File Ownership | `tlpi:15.3` | not-started |
| 15 | `15.4` | File Permissions | `tlpi:15.4` | not-started |
| 15 | `15.5` | I-node Flags ( ext2 Extended File Attributes) | `tlpi:15.5` | not-started |
| 15 | `15.6` | Summary | `tlpi:15.6` | not-started |
| 15 | `15.7` | Exercises | `tlpi:15.7` | not-started |

#### Chapter 16 — EXTENDED ATTRIBUTES

| Chapter | Section | Exact source title | Locator | Status |
| ---: | --- | --- | --- | --- |
| 16 | `16.1` | Overview | `tlpi:16.1` | not-started |
| 16 | `16.2` | Extended Attribute Implementation Details | `tlpi:16.2` | not-started |
| 16 | `16.3` | System Calls for Manipulating Extended Attributes | `tlpi:16.3` | not-started |
| 16 | `16.4` | Summary | `tlpi:16.4` | not-started |
| 16 | `16.5` | Exercise | `tlpi:16.5` | not-started |

#### Chapter 17 — ACCESS CONTROL LISTS

| Chapter | Section | Exact source title | Locator | Status |
| ---: | --- | --- | --- | --- |
| 17 | `17.1` | Overview | `tlpi:17.1` | not-started |
| 17 | `17.2` | ACL Permission-Checking Algorithm | `tlpi:17.2` | not-started |
| 17 | `17.3` | Long and Short Text Forms for ACLs | `tlpi:17.3` | not-started |
| 17 | `17.4` | The ACL_MASK Entry and the ACL Group Class | `tlpi:17.4` | not-started |
| 17 | `17.5` | The getfacl and setfacl Commands | `tlpi:17.5` | not-started |
| 17 | `17.6` | Default ACLs and File Creation | `tlpi:17.6` | not-started |
| 17 | `17.7` | ACL Implementation Limits | `tlpi:17.7` | not-started |
| 17 | `17.8` | The ACL API | `tlpi:17.8` | not-started |
| 17 | `17.9` | Summary | `tlpi:17.9` | not-started |
| 17 | `17.10` | Exercise | `tlpi:17.10` | not-started |

#### Chapter 18 — DIRECTORIES AND LINKS

| Chapter | Section | Exact source title | Locator | Status |
| ---: | --- | --- | --- | --- |
| 18 | `18.1` | Directories and (Hard) Links | `tlpi:18.1` | not-started |
| 18 | `18.2` | Symbolic (Soft) Links | `tlpi:18.2` | not-started |
| 18 | `18.3` | Creating and Removing (Hard) Links: link() and unlink() | `tlpi:18.3` | not-started |
| 18 | `18.4` | Changing the Name of a File: rename() | `tlpi:18.4` | not-started |
| 18 | `18.5` | Working with Symbolic Links: symlink() and readlink() | `tlpi:18.5` | not-started |
| 18 | `18.6` | Creating and Removing Directories: mkdir() and rmdir() | `tlpi:18.6` | not-started |
| 18 | `18.7` | Removing a File or Directory: remove() | `tlpi:18.7` | not-started |
| 18 | `18.8` | Reading Directories: opendir() and readdir() | `tlpi:18.8` | not-started |
| 18 | `18.9` | File Tree Walking: nftw() | `tlpi:18.9` | not-started |
| 18 | `18.10` | The Current Working Directory of a Process | `tlpi:18.10` | not-started |
| 18 | `18.11` | Operating Relative to a Directory File Descriptor | `tlpi:18.11` | not-started |
| 18 | `18.12` | Changing the Root Directory of a Process: chroot() | `tlpi:18.12` | not-started |
| 18 | `18.13` | Resolving a Pathname: realpath() | `tlpi:18.13` | not-started |
| 18 | `18.14` | Parsing Pathname Strings: dirname() and basename() | `tlpi:18.14` | not-started |
| 18 | `18.15` | Summary | `tlpi:18.15` | not-started |
| 18 | `18.16` | Exercises | `tlpi:18.16` | not-started |

#### Chapter 19 — MONITORING FILE EVENTS

| Chapter | Section | Exact source title | Locator | Status |
| ---: | --- | --- | --- | --- |
| 19 | `19.1` | Overview | `tlpi:19.1` | not-started |
| 19 | `19.2` | The inotify API | `tlpi:19.2` | not-started |
| 19 | `19.3` | inotify Events | `tlpi:19.3` | not-started |
| 19 | `19.4` | Reading inotify Events | `tlpi:19.4` | not-started |
| 19 | `19.5` | Queue Limits and /proc Files | `tlpi:19.5` | not-started |
| 19 | `19.6` | An Older System for Monitoring File Events: dnotify | `tlpi:19.6` | not-started |
| 19 | `19.7` | Summary | `tlpi:19.7` | not-started |
| 19 | `19.8` | Exercise | `tlpi:19.8` | not-started |

#### Chapter 20 — SIGNALS: FUNDAMENTAL CONCEPTS

| Chapter | Section | Exact source title | Locator | Status |
| ---: | --- | --- | --- | --- |
| 20 | `20.1` | Concepts and Overview | `tlpi:20.1` | not-started |
| 20 | `20.2` | Signal Types and Default Actions | `tlpi:20.2` | not-started |
| 20 | `20.3` | Changing Signal Dispositions: signal() | `tlpi:20.3` | not-started |
| 20 | `20.4` | Introduction to Signal Handlers | `tlpi:20.4` | not-started |
| 20 | `20.5` | Sending Signals: kill() | `tlpi:20.5` | not-started |
| 20 | `20.6` | Checking for the Existence of a Process | `tlpi:20.6` | not-started |
| 20 | `20.7` | Other Ways of Sending Signals: raise() and killpg() | `tlpi:20.7` | not-started |
| 20 | `20.8` | Displaying Signal Descriptions | `tlpi:20.8` | not-started |
| 20 | `20.9` | Signal Sets | `tlpi:20.9` | not-started |
| 20 | `20.10` | The Signal Mask (Blocking Signal Delivery) | `tlpi:20.10` | not-started |
| 20 | `20.11` | Pending Signals | `tlpi:20.11` | not-started |
| 20 | `20.12` | Signals Are Not Queued | `tlpi:20.12` | not-started |
| 20 | `20.13` | Changing Signal Dispositions: sigaction() | `tlpi:20.13` | not-started |
| 20 | `20.14` | Waiting for a Signal: pause() | `tlpi:20.14` | not-started |
| 20 | `20.15` | Summary | `tlpi:20.15` | not-started |
| 20 | `20.16` | Exercises | `tlpi:20.16` | not-started |

#### Chapter 21 — SIGNALS: SIGNAL HANDLERS

| Chapter | Section | Exact source title | Locator | Status |
| ---: | --- | --- | --- | --- |
| 21 | `21.1` | Designing Signal Handlers | `tlpi:21.1` | not-started |
| 21 | `21.2` | Other Methods of Terminating a Signal Handler | `tlpi:21.2` | not-started |
| 21 | `21.3` | Handling a Signal on an Alternate Stack: sigaltstack() | `tlpi:21.3` | not-started |
| 21 | `21.4` | The SA_SIGINFO Flag | `tlpi:21.4` | not-started |
| 21 | `21.5` | Interruption and Restarting of System Calls | `tlpi:21.5` | not-started |
| 21 | `21.6` | Summary | `tlpi:21.6` | not-started |
| 21 | `21.7` | Exercise | `tlpi:21.7` | not-started |

#### Chapter 22 — SIGNALS: ADVANCED FEATURES

| Chapter | Section | Exact source title | Locator | Status |
| ---: | --- | --- | --- | --- |
| 22 | `22.1` | Core Dump Files | `tlpi:22.1` | not-started |
| 22 | `22.2` | Special Cases for Signal Delivery, Disposition, and Handling | `tlpi:22.2` | not-started |
| 22 | `22.3` | Interruptible and Uninterruptible Process Sleep States | `tlpi:22.3` | not-started |
| 22 | `22.4` | Hardware-Generated Signals | `tlpi:22.4` | not-started |
| 22 | `22.5` | Synchronous and Asynchronous Signal Generation | `tlpi:22.5` | not-started |
| 22 | `22.6` | Timing and Order of Signal Delivery | `tlpi:22.6` | not-started |
| 22 | `22.7` | Implementation and Portability of signal() | `tlpi:22.7` | not-started |
| 22 | `22.8` | Realtime Signals | `tlpi:22.8` | not-started |
| 22 | `22.9` | Waiting for a Signal Using a Mask: sigsuspend() | `tlpi:22.9` | not-started |
| 22 | `22.10` | Synchronously Waiting for a Signal | `tlpi:22.10` | not-started |
| 22 | `22.11` | Fetching Signals via a File Descriptor | `tlpi:22.11` | not-started |
| 22 | `22.12` | Interprocess Communication with Signals | `tlpi:22.12` | not-started |
| 22 | `22.13` | Earlier Signal APIs (System V and BSD) | `tlpi:22.13` | not-started |
| 22 | `22.14` | Summary | `tlpi:22.14` | not-started |
| 22 | `22.15` | Exercises | `tlpi:22.15` | not-started |

#### Chapter 23 — TIMERS AND SLEEPING

| Chapter | Section | Exact source title | Locator | Status |
| ---: | --- | --- | --- | --- |
| 23 | `23.1` | Interval Timers | `tlpi:23.1` | not-started |
| 23 | `23.2` | Scheduling and Accuracy of Timers | `tlpi:23.2` | not-started |
| 23 | `23.3` | Setting Timeouts on Blocking Operations | `tlpi:23.3` | not-started |
| 23 | `23.4` | Suspending Execution for a Fixed Interval (Sleeping) | `tlpi:23.4` | not-started |
| 23 | `23.5` | POSIX Clocks | `tlpi:23.5` | not-started |
| 23 | `23.6` | POSIX Interval Timers | `tlpi:23.6` | not-started |
| 23 | `23.7` | Timers That Notify via File Descriptors: the timerfd API | `tlpi:23.7` | not-started |
| 23 | `23.8` | Summary | `tlpi:23.8` | not-started |
| 23 | `23.9` | Exercises | `tlpi:23.9` | not-started |

### Part 4 — Processes, programs, and threads

#### Chapter 24 — PROCESS CREATION

| Chapter | Section | Exact source title | Locator | Status |
| ---: | --- | --- | --- | --- |
| 24 | `24.1` | Overview of fork() , exit() , wait() , and execve() | `tlpi:24.1` | not-started |
| 24 | `24.2` | Creating a New Process: fork() | `tlpi:24.2` | not-started |
| 24 | `24.3` | The vfork() System Call | `tlpi:24.3` | not-started |
| 24 | `24.4` | Race Conditions After fork() | `tlpi:24.4` | not-started |
| 24 | `24.5` | Avoiding Race Conditions by Synchronizing with Signals | `tlpi:24.5` | not-started |
| 24 | `24.6` | Summary | `tlpi:24.6` | not-started |

#### Chapter 25 — PROCESS TERMINATION

| Chapter | Section | Exact source title | Locator | Status |
| ---: | --- | --- | --- | --- |
| 25 | `25.1` | Terminating a Process: _exit() and exit() | `tlpi:25.1` | not-started |
| 25 | `25.2` | Details of Process Termination | `tlpi:25.2` | not-started |
| 25 | `25.3` | Exit Handlers | `tlpi:25.3` | not-started |
| 25 | `25.4` | Interactions Between fork() , stdio Buffers, and _exit() | `tlpi:25.4` | not-started |
| 25 | `25.5` | Summary | `tlpi:25.5` | not-started |
| 25 | `25.6` | Exercise | `tlpi:25.6` | not-started |

#### Chapter 26 — MONITORING CHILD PROCESSES

| Chapter | Section | Exact source title | Locator | Status |
| ---: | --- | --- | --- | --- |
| 26 | `26.1` | Waiting on a Child Process | `tlpi:26.1` | not-started |
| 26 | `26.2` | Orphans and Zombies | `tlpi:26.2` | not-started |
| 26 | `26.3` | The SIGCHLD Signal | `tlpi:26.3` | not-started |
| 26 | `26.4` | Summary | `tlpi:26.4` | not-started |
| 26 | `26.5` | Exercises | `tlpi:26.5` | not-started |

#### Chapter 27 — PROGRAM EXECUTION

| Chapter | Section | Exact source title | Locator | Status |
| ---: | --- | --- | --- | --- |
| 27 | `27.1` | Executing a New Program: execve() | `tlpi:27.1` | not-started |
| 27 | `27.2` | The exec() Library Functions | `tlpi:27.2` | not-started |
| 27 | `27.3` | Interpreter Scripts | `tlpi:27.3` | not-started |
| 27 | `27.4` | File Descriptors and exec() | `tlpi:27.4` | not-started |
| 27 | `27.5` | Signals and exec() | `tlpi:27.5` | not-started |
| 27 | `27.6` | Executing a Shell Command: system() | `tlpi:27.6` | not-started |
| 27 | `27.7` | Implementing system() | `tlpi:27.7` | not-started |
| 27 | `27.8` | Summary | `tlpi:27.8` | not-started |
| 27 | `27.9` | Exercises | `tlpi:27.9` | not-started |

#### Chapter 28 — PROCESS CREATION AND PROGRAM EXECUTION IN MORE DETAIL

| Chapter | Section | Exact source title | Locator | Status |
| ---: | --- | --- | --- | --- |
| 28 | `28.1` | Process Accounting | `tlpi:28.1` | not-started |
| 28 | `28.2` | The clone() System Call | `tlpi:28.2` | not-started |
| 28 | `28.3` | Speed of Process Creation | `tlpi:28.3` | not-started |
| 28 | `28.4` | Effect of exec() and fork() on Process Attributes | `tlpi:28.4` | not-started |
| 28 | `28.5` | Summary | `tlpi:28.5` | not-started |
| 28 | `28.6` | Exercise | `tlpi:28.6` | not-started |

#### Chapter 29 — THREADS: INTRODUCTION

| Chapter | Section | Exact source title | Locator | Status |
| ---: | --- | --- | --- | --- |
| 29 | `29.1` | Overview | `tlpi:29.1` | not-started |
| 29 | `29.2` | Background Details of the Pthreads API | `tlpi:29.2` | not-started |
| 29 | `29.3` | Thread Creation | `tlpi:29.3` | not-started |
| 29 | `29.4` | Thread Termination | `tlpi:29.4` | not-started |
| 29 | `29.5` | Thread IDs | `tlpi:29.5` | not-started |
| 29 | `29.6` | Joining with a Terminated Thread: pthread_join() | `tlpi:29.6` | not-started |
| 29 | `29.7` | Detaching a Thread: pthread_detach() | `tlpi:29.7` | not-started |
| 29 | `29.8` | Thread Attributes | `tlpi:29.8` | not-started |
| 29 | `29.9` | Threads Versus Processes | `tlpi:29.9` | not-started |
| 29 | `29.10` | Summary | `tlpi:29.10` | not-started |
| 29 | `29.11` | Exercises | `tlpi:29.11` | not-started |

#### Chapter 30 — THREADS: THREAD SYNCHRONIZATION

| Chapter | Section | Exact source title | Locator | Status |
| ---: | --- | --- | --- | --- |
| 30 | `30.1` | Protecting Accesses to Shared Variables: Mutexes | `tlpi:30.1` | not-started |
| 30 | `30.2` | Signaling Changes of State: Condition Variables | `tlpi:30.2` | not-started |
| 30 | `30.3` | Summary | `tlpi:30.3` | not-started |
| 30 | `30.4` | Exercises | `tlpi:30.4` | not-started |

#### Chapter 31 — THREADS: THREAD SAFETY AND PER-THREAD STORAGE

| Chapter | Section | Exact source title | Locator | Status |
| ---: | --- | --- | --- | --- |
| 31 | `31.1` | Thread Safety (and Reentrancy Revisited) | `tlpi:31.1` | not-started |
| 31 | `31.2` | One-Time Initialization | `tlpi:31.2` | not-started |
| 31 | `31.3` | Thread-Specific Data | `tlpi:31.3` | not-started |
| 31 | `31.4` | Thread-Local Storage | `tlpi:31.4` | not-started |
| 31 | `31.5` | Summary | `tlpi:31.5` | not-started |
| 31 | `31.6` | Exercises | `tlpi:31.6` | not-started |

#### Chapter 32 — THREADS: THREAD CANCELLATION

| Chapter | Section | Exact source title | Locator | Status |
| ---: | --- | --- | --- | --- |
| 32 | `32.1` | Canceling a Thread | `tlpi:32.1` | not-started |
| 32 | `32.2` | Cancellation State and Type | `tlpi:32.2` | not-started |
| 32 | `32.3` | Cancellation Points | `tlpi:32.3` | not-started |
| 32 | `32.4` | Testing for Thread Cancellation | `tlpi:32.4` | not-started |
| 32 | `32.5` | Cleanup Handlers | `tlpi:32.5` | not-started |
| 32 | `32.6` | Asynchronous Cancelability | `tlpi:32.6` | not-started |
| 32 | `32.7` | Summary | `tlpi:32.7` | not-started |
| 32 | `32.8` | Exercises | `tlpi:32.8` | not-started |

#### Chapter 33 — THREADS: FURTHER DETAILS

| Chapter | Section | Exact source title | Locator | Status |
| ---: | --- | --- | --- | --- |
| 33 | `33.1` | Thread Stacks | `tlpi:33.1` | not-started |
| 33 | `33.2` | Threads and Signals | `tlpi:33.2` | not-started |
| 33 | `33.3` | Threads and Process Control | `tlpi:33.3` | not-started |
| 33 | `33.4` | Thread Implementation Models | `tlpi:33.4` | not-started |
| 33 | `33.5` | Linux Implementations of POSIX Threads | `tlpi:33.5` | not-started |
| 33 | `33.6` | Advanced Features of the Pthreads API | `tlpi:33.6` | not-started |
| 33 | `33.7` | Summary | `tlpi:33.7` | not-started |
| 33 | `33.8` | Exercises | `tlpi:33.8` | not-started |

### Part 5 — Advanced process and program topics

#### Chapter 34 — PROCESS GROUPS, SESSIONS, AND JOB CONTROL

| Chapter | Section | Exact source title | Locator | Status |
| ---: | --- | --- | --- | --- |
| 34 | `34.1` | Overview | `tlpi:34.1` | not-started |
| 34 | `34.2` | Process Groups | `tlpi:34.2` | not-started |
| 34 | `34.3` | Sessions | `tlpi:34.3` | not-started |
| 34 | `34.4` | Controlling Terminals and Controlling Processes | `tlpi:34.4` | not-started |
| 34 | `34.5` | Foreground and Background Process Groups | `tlpi:34.5` | not-started |
| 34 | `34.6` | The SIGHUP Signal | `tlpi:34.6` | not-started |
| 34 | `34.7` | Job Control | `tlpi:34.7` | not-started |
| 34 | `34.8` | Summary | `tlpi:34.8` | not-started |
| 34 | `34.9` | Exercises | `tlpi:34.9` | not-started |

#### Chapter 35 — PROCESS PRIORITIES AND SCHEDULING

| Chapter | Section | Exact source title | Locator | Status |
| ---: | --- | --- | --- | --- |
| 35 | `35.1` | Process Priorities (Nice Values) | `tlpi:35.1` | not-started |
| 35 | `35.2` | Overview of Realtime Process Scheduling | `tlpi:35.2` | not-started |
| 35 | `35.3` | Realtime Process Scheduling API | `tlpi:35.3` | not-started |
| 35 | `35.4` | CPU Affinity | `tlpi:35.4` | not-started |
| 35 | `35.5` | Summary | `tlpi:35.5` | not-started |
| 35 | `35.6` | Exercises | `tlpi:35.6` | not-started |

#### Chapter 36 — PROCESS RESOURCES

| Chapter | Section | Exact source title | Locator | Status |
| ---: | --- | --- | --- | --- |
| 36 | `36.1` | Process Resource Usage: getrusage() | `tlpi:36.1` | not-started |
| 36 | `36.2` | Process Resource Limits: getrlimit() and setrlimit() | `tlpi:36.2` | not-started |
| 36 | `36.3` | Details of Specific Resource Limits | `tlpi:36.3` | not-started |
| 36 | `36.4` | Summary | `tlpi:36.4` | not-started |
| 36 | `36.5` | Exercises | `tlpi:36.5` | not-started |

#### Chapter 37 — DAEMONS

| Chapter | Section | Exact source title | Locator | Status |
| ---: | --- | --- | --- | --- |
| 37 | `37.1` | Overview | `tlpi:37.1` | not-started |
| 37 | `37.2` | Creating a Daemon | `tlpi:37.2` | not-started |
| 37 | `37.3` | Guidelines for Writing Daemons | `tlpi:37.3` | not-started |
| 37 | `37.4` | Using SIGHUP to Reinitialize a Daemon | `tlpi:37.4` | not-started |
| 37 | `37.5` | Logging Messages and Errors Using syslog | `tlpi:37.5` | not-started |
| 37 | `37.6` | Summary | `tlpi:37.6` | not-started |
| 37 | `37.7` | Exercise | `tlpi:37.7` | not-started |

#### Chapter 38 — WRITING SECURE PRIVILEGED PROGRAMS

| Chapter | Section | Exact source title | Locator | Status |
| ---: | --- | --- | --- | --- |
| 38 | `38.1` | Is a Set-User-ID or Set-Group-ID Program Required? | `tlpi:38.1` | not-started |
| 38 | `38.2` | Operate with Least Privilege | `tlpi:38.2` | not-started |
| 38 | `38.3` | Be Careful when Executing a Program | `tlpi:38.3` | not-started |
| 38 | `38.4` | Avoid Exposing Sensitive Information | `tlpi:38.4` | not-started |
| 38 | `38.5` | Confine the Process | `tlpi:38.5` | not-started |
| 38 | `38.6` | Beware of Signals and Race Conditions | `tlpi:38.6` | not-started |
| 38 | `38.7` | Pitfalls when Performing File Operations and File I/O | `tlpi:38.7` | not-started |
| 38 | `38.8` | Don't Trust Inputs or the Environment | `tlpi:38.8` | not-started |
| 38 | `38.9` | Beware of Buffer Overruns | `tlpi:38.9` | not-started |
| 38 | `38.10` | Beware of Denial-of-Service Attacks | `tlpi:38.10` | not-started |
| 38 | `38.11` | Check for Failures; Fail Safely | `tlpi:38.11` | not-started |
| 38 | `38.12` | Summary | `tlpi:38.12` | not-started |
| 38 | `38.13` | Exercises | `tlpi:38.13` | not-started |

#### Chapter 39 — CAPABILITIES

| Chapter | Section | Exact source title | Locator | Status |
| ---: | --- | --- | --- | --- |
| 39 | `39.1` | Rationale for Capabilities | `tlpi:39.1` | not-started |
| 39 | `39.2` | The Linux Capabilities | `tlpi:39.2` | not-started |
| 39 | `39.3` | Process and File Capabilities | `tlpi:39.3` | not-started |
| 39 | `39.4` | The Modern Capabilities Implementation | `tlpi:39.4` | not-started |
| 39 | `39.5` | Transformation of Process Capabilities During exec() | `tlpi:39.5` | not-started |
| 39 | `39.6` | Effect on Process Capabilities of Changing User IDs | `tlpi:39.6` | not-started |
| 39 | `39.7` | Changing Process Capabilities Programmatically | `tlpi:39.7` | not-started |
| 39 | `39.8` | Creating Capabilities-Only Environments | `tlpi:39.8` | not-started |
| 39 | `39.9` | Discovering the Capabilities Required by a Program | `tlpi:39.9` | not-started |
| 39 | `39.10` | Older Kernels and Systems Without File Capabilities | `tlpi:39.10` | not-started |
| 39 | `39.11` | Summary | `tlpi:39.11` | not-started |
| 39 | `39.12` | Exercise | `tlpi:39.12` | not-started |

#### Chapter 40 — LOGIN ACCOUNTING

| Chapter | Section | Exact source title | Locator | Status |
| ---: | --- | --- | --- | --- |
| 40 | `40.1` | Overview of the utmp and wtmp Files | `tlpi:40.1` | not-started |
| 40 | `40.2` | The utmpx API | `tlpi:40.2` | not-started |
| 40 | `40.3` | The utmpx Structure | `tlpi:40.3` | not-started |
| 40 | `40.4` | Retrieving Information from the utmp and wtmp Files | `tlpi:40.4` | not-started |
| 40 | `40.5` | Retrieving the Login Name: getlogin() | `tlpi:40.5` | not-started |
| 40 | `40.6` | Updating the utmp and wtmp Files for a Login Session | `tlpi:40.6` | not-started |
| 40 | `40.7` | The lastlog File | `tlpi:40.7` | not-started |
| 40 | `40.8` | Summary | `tlpi:40.8` | not-started |
| 40 | `40.9` | Exercises | `tlpi:40.9` | not-started |

#### Chapter 41 — FUNDAMENTALS OF SHARED LIBRARIES

| Chapter | Section | Exact source title | Locator | Status |
| ---: | --- | --- | --- | --- |
| 41 | `41.1` | Object Libraries | `tlpi:41.1` | not-started |
| 41 | `41.2` | Static Libraries | `tlpi:41.2` | not-started |
| 41 | `41.3` | Overview of Shared Libraries | `tlpi:41.3` | not-started |
| 41 | `41.4` | Creating and Using Shared Libraries—A First Pass | `tlpi:41.4` | not-started |
| 41 | `41.5` | Useful Tools for Working with Shared Libraries | `tlpi:41.5` | not-started |
| 41 | `41.6` | Shared Library Versions and Naming Conventions | `tlpi:41.6` | not-started |
| 41 | `41.7` | Installing Shared Libraries | `tlpi:41.7` | not-started |
| 41 | `41.8` | Compatible Versus Incompatible Libraries | `tlpi:41.8` | not-started |
| 41 | `41.9` | Upgrading Shared Libraries | `tlpi:41.9` | not-started |
| 41 | `41.10` | Specifying Library Search Directories in an Object File | `tlpi:41.10` | not-started |
| 41 | `41.11` | Finding Shared Libraries at Run Time | `tlpi:41.11` | not-started |
| 41 | `41.12` | Run-Time Symbol Resolution | `tlpi:41.12` | not-started |
| 41 | `41.13` | Using a Static Library Instead of a Shared Library | `tlpi:41.13` | not-started |
| 41 | `41.14` | Summary | `tlpi:41.14` | not-started |
| 41 | `41.15` | Exercise | `tlpi:41.15` | not-started |

#### Chapter 42 — ADVANCED FEATURES OF SHARED LIBRARIES

| Chapter | Section | Exact source title | Locator | Status |
| ---: | --- | --- | --- | --- |
| 42 | `42.1` | Dynamically Loaded Libraries | `tlpi:42.1` | not-started |
| 42 | `42.2` | Controlling Symbol Visibility | `tlpi:42.2` | not-started |
| 42 | `42.3` | Linker Version Scripts | `tlpi:42.3` | not-started |
| 42 | `42.4` | Initialization and Finalization Functions | `tlpi:42.4` | not-started |
| 42 | `42.5` | Preloading Shared Libraries | `tlpi:42.5` | not-started |
| 42 | `42.6` | Monitoring the Dynamic Linker: LD_DEBUG | `tlpi:42.6` | not-started |
| 42 | `42.7` | Summary | `tlpi:42.7` | not-started |
| 42 | `42.8` | Exercises | `tlpi:42.8` | not-started |

### Part 6 — Interprocess communication (IPC)

#### Chapter 43 — INTERPROCESS COMMUNICATION OVERVIEW

| Chapter | Section | Exact source title | Locator | Status |
| ---: | --- | --- | --- | --- |
| 43 | `43.1` | A Taxonomy of IPC Facilities | `tlpi:43.1` | not-started |
| 43 | `43.2` | Communication Facilities | `tlpi:43.2` | not-started |
| 43 | `43.3` | Synchronization Facilities | `tlpi:43.3` | not-started |
| 43 | `43.4` | Comparing IPC Facilities | `tlpi:43.4` | not-started |
| 43 | `43.5` | Summary | `tlpi:43.5` | not-started |
| 43 | `43.6` | Exercises | `tlpi:43.6` | not-started |

#### Chapter 44 — PIPES AND FIFOS

| Chapter | Section | Exact source title | Locator | Status |
| ---: | --- | --- | --- | --- |
| 44 | `44.1` | Overview | `tlpi:44.1` | not-started |
| 44 | `44.2` | Creating and Using Pipes | `tlpi:44.2` | not-started |
| 44 | `44.3` | Pipes As a Method of Process Synchronization | `tlpi:44.3` | not-started |
| 44 | `44.4` | Using Pipes to Connect Filters | `tlpi:44.4` | not-started |
| 44 | `44.5` | Talking to a Shell Command via a Pipe: popen() and pclose() | `tlpi:44.5` | not-started |
| 44 | `44.6` | Pipes and stdio Buffering | `tlpi:44.6` | not-started |
| 44 | `44.7` | FIFOs | `tlpi:44.7` | not-started |
| 44 | `44.8` | A Client-Server Application Using FIFOs | `tlpi:44.8` | not-started |
| 44 | `44.9` | Nonblocking I/O | `tlpi:44.9` | not-started |
| 44 | `44.10` | Semantics of read() and write() on Pipes and FIFOs | `tlpi:44.10` | not-started |
| 44 | `44.11` | Summary | `tlpi:44.11` | not-started |
| 44 | `44.12` | Exercises | `tlpi:44.12` | not-started |

#### Chapter 45 — INTRODUCTION TO SYSTEM V IPC

| Chapter | Section | Exact source title | Locator | Status |
| ---: | --- | --- | --- | --- |
| 45 | `45.1` | API Overview | `tlpi:45.1` | not-started |
| 45 | `45.2` | IPC Keys | `tlpi:45.2` | not-started |
| 45 | `45.3` | Associated Data Structure and Object Permissions | `tlpi:45.3` | not-started |
| 45 | `45.4` | IPC Identifiers and Client-Server Applications | `tlpi:45.4` | not-started |
| 45 | `45.5` | Algorithm Employed by System V IPC get Calls | `tlpi:45.5` | not-started |
| 45 | `45.6` | The ipcs and ipcrm Commands | `tlpi:45.6` | not-started |
| 45 | `45.7` | Obtaining a List of All IPC Objects | `tlpi:45.7` | not-started |
| 45 | `45.8` | IPC Limits | `tlpi:45.8` | not-started |
| 45 | `45.9` | Summary | `tlpi:45.9` | not-started |
| 45 | `45.10` | Exercises | `tlpi:45.10` | not-started |

#### Chapter 46 — SYSTEM V MESSAGE QUEUES

| Chapter | Section | Exact source title | Locator | Status |
| ---: | --- | --- | --- | --- |
| 46 | `46.1` | Creating or Opening a Message Queue: msgget() | `tlpi:46.1` | not-started |
| 46 | `46.2` | Exchanging Messages | `tlpi:46.2` | not-started |
| 46 | `46.3` | Message Queue Control Operations: msgctl() | `tlpi:46.3` | not-started |
| 46 | `46.4` | Message Queue Associated Data Structure | `tlpi:46.4` | not-started |
| 46 | `46.5` | Message Queue Limits | `tlpi:46.5` | not-started |
| 46 | `46.6` | Displaying All Message Queues on the System | `tlpi:46.6` | not-started |
| 46 | `46.7` | Client-Server Programming with Message Queues | `tlpi:46.7` | not-started |
| 46 | `46.8` | A File-Server Application Using Message Queues | `tlpi:46.8` | not-started |
| 46 | `46.9` | Disadvantages of System V Message Queues | `tlpi:46.9` | not-started |
| 46 | `46.10` | Summary | `tlpi:46.10` | not-started |
| 46 | `46.11` | Exercises | `tlpi:46.11` | not-started |

#### Chapter 47 — SYSTEM V SEMAPHORES

| Chapter | Section | Exact source title | Locator | Status |
| ---: | --- | --- | --- | --- |
| 47 | `47.1` | Overview | `tlpi:47.1` | not-started |
| 47 | `47.2` | Creating or Opening a Semaphore Set: semget() | `tlpi:47.2` | not-started |
| 47 | `47.3` | Semaphore Control Operations: semctl() | `tlpi:47.3` | not-started |
| 47 | `47.4` | Semaphore Associated Data Structure | `tlpi:47.4` | not-started |
| 47 | `47.5` | Semaphore Initialization | `tlpi:47.5` | not-started |
| 47 | `47.6` | Semaphore Operations: semop() | `tlpi:47.6` | not-started |
| 47 | `47.7` | Handling of Multiple Blocked Semaphore Operations | `tlpi:47.7` | not-started |
| 47 | `47.8` | Semaphore Undo Values | `tlpi:47.8` | not-started |
| 47 | `47.9` | Implementing a Binary Semaphores Protocol | `tlpi:47.9` | not-started |
| 47 | `47.10` | Semaphore Limits | `tlpi:47.10` | not-started |
| 47 | `47.11` | Disadvantages of System V Semaphores | `tlpi:47.11` | not-started |
| 47 | `47.12` | Summary | `tlpi:47.12` | not-started |
| 47 | `47.13` | Exercises | `tlpi:47.13` | not-started |

#### Chapter 48 — SYSTEM V SHARED MEMORY

| Chapter | Section | Exact source title | Locator | Status |
| ---: | --- | --- | --- | --- |
| 48 | `48.1` | Overview | `tlpi:48.1` | not-started |
| 48 | `48.2` | Creating or Opening a Shared Memory Segment: shmget() | `tlpi:48.2` | not-started |
| 48 | `48.3` | Using Shared Memory: shmat() and shmdt() | `tlpi:48.3` | not-started |
| 48 | `48.4` | Example: Transferring Data Via Shared Memory | `tlpi:48.4` | not-started |
| 48 | `48.5` | Location of Shared Memory Segments in Virtual Memory | `tlpi:48.5` | not-started |
| 48 | `48.6` | Storing Pointers in Shared Memory | `tlpi:48.6` | not-started |
| 48 | `48.7` | Shared Memory Control Operations: shmctl() | `tlpi:48.7` | not-started |
| 48 | `48.8` | Shared Memory Associated Data Structure | `tlpi:48.8` | not-started |
| 48 | `48.9` | Shared Memory Limits | `tlpi:48.9` | not-started |
| 48 | `48.10` | Summary | `tlpi:48.10` | not-started |
| 48 | `48.11` | Exercises | `tlpi:48.11` | not-started |

#### Chapter 49 — MEMORY MAPPINGS

| Chapter | Section | Exact source title | Locator | Status |
| ---: | --- | --- | --- | --- |
| 49 | `49.1` | Overview | `tlpi:49.1` | not-started |
| 49 | `49.2` | Creating a Mapping: mmap() | `tlpi:49.2` | not-started |
| 49 | `49.3` | Unmapping a Mapped Region: munmap() | `tlpi:49.3` | not-started |
| 49 | `49.4` | File Mappings | `tlpi:49.4` | not-started |
| 49 | `49.5` | Synchronizing a Mapped Region: msync() | `tlpi:49.5` | not-started |
| 49 | `49.6` | Additional mmap() Flags | `tlpi:49.6` | not-started |
| 49 | `49.7` | Anonymous Mappings | `tlpi:49.7` | not-started |
| 49 | `49.8` | Remapping a Mapped Region: mremap() | `tlpi:49.8` | not-started |
| 49 | `49.9` | The MAP_NORESERVE Flag and Swap Space Overcommitting | `tlpi:49.9` | not-started |
| 49 | `49.10` | The MAP_FIXED Flag | `tlpi:49.10` | not-started |
| 49 | `49.11` | Nonlinear Mappings: remap_file_pages() | `tlpi:49.11` | not-started |
| 49 | `49.12` | Summary | `tlpi:49.12` | not-started |
| 49 | `49.13` | Exercises | `tlpi:49.13` | not-started |

#### Chapter 50 — VIRTUAL MEMORY OPERATIONS

| Chapter | Section | Exact source title | Locator | Status |
| ---: | --- | --- | --- | --- |
| 50 | `50.1` | Changing Memory Protection: mprotect() | `tlpi:50.1` | not-started |
| 50 | `50.2` | Memory Locking: mlock() and mlockall() | `tlpi:50.2` | not-started |
| 50 | `50.3` | Determining Memory Residence: mincore() | `tlpi:50.3` | not-started |
| 50 | `50.4` | Advising Future Memory Usage Patterns: madvise() | `tlpi:50.4` | not-started |
| 50 | `50.5` | Summary | `tlpi:50.5` | not-started |
| 50 | `50.6` | Exercises | `tlpi:50.6` | not-started |

#### Chapter 51 — INTRODUCTION TO POSIX IPC

| Chapter | Section | Exact source title | Locator | Status |
| ---: | --- | --- | --- | --- |
| 51 | `51.1` | API Overview | `tlpi:51.1` | not-started |
| 51 | `51.2` | Comparison of System V IPC and POSIX IPC | `tlpi:51.2` | not-started |
| 51 | `51.3` | Summary | `tlpi:51.3` | not-started |

#### Chapter 52 — POSIX MESSAGE QUEUES

| Chapter | Section | Exact source title | Locator | Status |
| ---: | --- | --- | --- | --- |
| 52 | `52.1` | Overview | `tlpi:52.1` | not-started |
| 52 | `52.2` | Opening, Closing, and Unlinking a Message Queue | `tlpi:52.2` | not-started |
| 52 | `52.3` | Relationship Between Descriptors and Message Queues | `tlpi:52.3` | not-started |
| 52 | `52.4` | Message Queue Attributes | `tlpi:52.4` | not-started |
| 52 | `52.5` | Exchanging Messages | `tlpi:52.5` | not-started |
| 52 | `52.6` | Message Notification | `tlpi:52.6` | not-started |
| 52 | `52.7` | Linux-Specific Features | `tlpi:52.7` | not-started |
| 52 | `52.8` | Message Queue Limits | `tlpi:52.8` | not-started |
| 52 | `52.9` | Comparison of POSIX and System V Message Queues | `tlpi:52.9` | not-started |
| 52 | `52.10` | Summary | `tlpi:52.10` | not-started |
| 52 | `52.11` | Exercises | `tlpi:52.11` | not-started |

#### Chapter 53 — POSIX SEMAPHORES

| Chapter | Section | Exact source title | Locator | Status |
| ---: | --- | --- | --- | --- |
| 53 | `53.1` | Overview | `tlpi:53.1` | not-started |
| 53 | `53.2` | Named Semaphores | `tlpi:53.2` | not-started |
| 53 | `53.3` | Semaphore Operations | `tlpi:53.3` | not-started |
| 53 | `53.4` | Unnamed Semaphores | `tlpi:53.4` | not-started |
| 53 | `53.5` | Comparisons with Other Synchronization Techniques | `tlpi:53.5` | not-started |
| 53 | `53.6` | Semaphore Limits | `tlpi:53.6` | not-started |
| 53 | `53.7` | Summary | `tlpi:53.7` | not-started |
| 53 | `53.8` | Exercises | `tlpi:53.8` | not-started |

#### Chapter 54 — POSIX SHARED MEMORY

| Chapter | Section | Exact source title | Locator | Status |
| ---: | --- | --- | --- | --- |
| 54 | `54.1` | Overview | `tlpi:54.1` | not-started |
| 54 | `54.2` | Creating Shared Memory Objects: shm_open() | `tlpi:54.2` | not-started |
| 54 | `54.3` | Using Shared Memory Objects | `tlpi:54.3` | not-started |
| 54 | `54.4` | Removing Shared Memory Objects: shm_unlink() | `tlpi:54.4` | not-started |
| 54 | `54.5` | Comparisons Between Shared Memory APIs | `tlpi:54.5` | not-started |
| 54 | `54.6` | Summary | `tlpi:54.6` | not-started |
| 54 | `54.7` | Exercise | `tlpi:54.7` | not-started |

#### Chapter 55 — FILE LOCKING

| Chapter | Section | Exact source title | Locator | Status |
| ---: | --- | --- | --- | --- |
| 55 | `55.1` | Overview | `tlpi:55.1` | not-started |
| 55 | `55.2` | File Locking with flock() | `tlpi:55.2` | not-started |
| 55 | `55.3` | Record Locking with fcntl() | `tlpi:55.3` | not-started |
| 55 | `55.4` | Mandatory Locking | `tlpi:55.4` | not-started |
| 55 | `55.5` | The /proc/locks File | `tlpi:55.5` | not-started |
| 55 | `55.6` | Running Just One Instance of a Program | `tlpi:55.6` | not-started |
| 55 | `55.7` | Older Locking Techniques | `tlpi:55.7` | not-started |
| 55 | `55.8` | Summary | `tlpi:55.8` | not-started |
| 55 | `55.9` | Exercises | `tlpi:55.9` | not-started |

### Part 7 — Sockets and network programming

#### Chapter 56 — SOCKETS: INTRODUCTION

| Chapter | Section | Exact source title | Locator | Status |
| ---: | --- | --- | --- | --- |
| 56 | `56.1` | Overview | `tlpi:56.1` | not-started |
| 56 | `56.2` | Creating a Socket: socket() | `tlpi:56.2` | not-started |
| 56 | `56.3` | Binding a Socket to an Address: bind() | `tlpi:56.3` | not-started |
| 56 | `56.4` | Generic Socket Address Structures: struct sockaddr | `tlpi:56.4` | not-started |
| 56 | `56.5` | Stream Sockets | `tlpi:56.5` | not-started |
| 56 | `56.6` | Datagram Sockets | `tlpi:56.6` | not-started |
| 56 | `56.7` | Summary | `tlpi:56.7` | not-started |

#### Chapter 57 — SOCKETS: UNIX DOMAIN

| Chapter | Section | Exact source title | Locator | Status |
| ---: | --- | --- | --- | --- |
| 57 | `57.1` | UNIX Domain Socket Addresses: struct sockaddr_un | `tlpi:57.1` | not-started |
| 57 | `57.2` | Stream Sockets in the UNIX Domain | `tlpi:57.2` | not-started |
| 57 | `57.3` | Datagram Sockets in the UNIX Domain | `tlpi:57.3` | not-started |
| 57 | `57.4` | UNIX Domain Socket Permissions | `tlpi:57.4` | not-started |
| 57 | `57.5` | Creating a Connected Socket Pair: socketpair() | `tlpi:57.5` | not-started |
| 57 | `57.6` | The Linux Abstract Socket Namespace | `tlpi:57.6` | not-started |
| 57 | `57.7` | Summary | `tlpi:57.7` | not-started |
| 57 | `57.8` | Exercises | `tlpi:57.8` | not-started |

#### Chapter 58 — SOCKETS: FUNDAMENTALS OF TCP/IP NETWORKS

| Chapter | Section | Exact source title | Locator | Status |
| ---: | --- | --- | --- | --- |
| 58 | `58.1` | Internets | `tlpi:58.1` | not-started |
| 58 | `58.2` | Networking Protocols and Layers | `tlpi:58.2` | not-started |
| 58 | `58.3` | The Data-Link Layer | `tlpi:58.3` | not-started |
| 58 | `58.4` | The Network Layer: IP | `tlpi:58.4` | not-started |
| 58 | `58.5` | IP Addresses | `tlpi:58.5` | not-started |
| 58 | `58.6` | The Transport Layer | `tlpi:58.6` | not-started |
| 58 | `58.7` | Requests for Comments (RFCs) | `tlpi:58.7` | not-started |
| 58 | `58.8` | Summary | `tlpi:58.8` | not-started |

#### Chapter 59 — SOCKETS: INTERNET DOMAINS

| Chapter | Section | Exact source title | Locator | Status |
| ---: | --- | --- | --- | --- |
| 59 | `59.1` | Internet Domain Sockets | `tlpi:59.1` | not-started |
| 59 | `59.2` | Network Byte Order | `tlpi:59.2` | not-started |
| 59 | `59.3` | Data Representation | `tlpi:59.3` | not-started |
| 59 | `59.4` | Internet Socket Addresses | `tlpi:59.4` | not-started |
| 59 | `59.5` | Overview of Host and Service Conversion Functions | `tlpi:59.5` | not-started |
| 59 | `59.6` | IPv6 and IPv4 Address Conversion: inet_pton() and inet_ntop() | `tlpi:59.6` | not-started |
| 59 | `59.7` | Client-Server Example (Datagram Sockets) | `tlpi:59.7` | not-started |
| 59 | `59.8` | Domain Name System (DNS) | `tlpi:59.8` | not-started |
| 59 | `59.9` | The /etc/services File | `tlpi:59.9` | not-started |
| 59 | `59.10` | Protocol-Independent Host and Service Conversion | `tlpi:59.10` | not-started |
| 59 | `59.11` | Client-Server Example (Stream Sockets) | `tlpi:59.11` | not-started |
| 59 | `59.12` | An Internet Domain Sockets Library | `tlpi:59.12` | not-started |
| 59 | `59.13` | Obsolete APIs for Host, Service, and Address Conversion | `tlpi:59.13` | not-started |
| 59 | `59.14` | UNIX Versus Internet Domain Sockets | `tlpi:59.14` | not-started |
| 59 | `59.15` | Further Information | `tlpi:59.15` | not-started |
| 59 | `59.16` | Summary | `tlpi:59.16` | not-started |
| 59 | `59.17` | Exercises | `tlpi:59.17` | not-started |

#### Chapter 60 — SOCKETS: SERVER DESIGN

| Chapter | Section | Exact source title | Locator | Status |
| ---: | --- | --- | --- | --- |
| 60 | `60.1` | Iterative and Concurrent Servers | `tlpi:60.1` | not-started |
| 60 | `60.2` | An Iterative UDP echo Server | `tlpi:60.2` | not-started |
| 60 | `60.3` | A Concurrent TCP echo Server | `tlpi:60.3` | not-started |
| 60 | `60.4` | Other Concurrent Server Designs | `tlpi:60.4` | not-started |
| 60 | `60.5` | The inetd (Internet Superserver) Daemon | `tlpi:60.5` | not-started |
| 60 | `60.6` | Summary | `tlpi:60.6` | not-started |
| 60 | `60.7` | Exercises | `tlpi:60.7` | not-started |

#### Chapter 61 — SOCKETS: ADVANCED TOPICS

| Chapter | Section | Exact source title | Locator | Status |
| ---: | --- | --- | --- | --- |
| 61 | `61.1` | Partial Reads and Writes on Stream Sockets | `tlpi:61.1` | not-started |
| 61 | `61.2` | The shutdown() system call | `tlpi:61.2` | not-started |
| 61 | `61.3` | Socket-Specific I/O System Calls: recv() and send() | `tlpi:61.3` | not-started |
| 61 | `61.4` | The sendfile() System Call | `tlpi:61.4` | not-started |
| 61 | `61.5` | Retrieving Socket Addresses: getsockname() and getpeername() | `tlpi:61.5` | not-started |
| 61 | `61.6` | A Closer Look at TCP | `tlpi:61.6` | not-started |
| 61 | `61.7` | Monitoring Sockets: netstat | `tlpi:61.7` | not-started |
| 61 | `61.8` | Using tcpdump to Monitor TCP Traffic | `tlpi:61.8` | not-started |
| 61 | `61.9` | Socket Options: setsockopt() and getsockopt() | `tlpi:61.9` | not-started |
| 61 | `61.10` | The SO_REUSEADDR Socket Option | `tlpi:61.10` | not-started |
| 61 | `61.11` | Inheritance of File Flags and Socket Options across accept() | `tlpi:61.11` | not-started |
| 61 | `61.12` | TCP Versus UDP | `tlpi:61.12` | not-started |
| 61 | `61.13` | Advanced Features | `tlpi:61.13` | not-started |
| 61 | `61.14` | Summary | `tlpi:61.14` | not-started |
| 61 | `61.15` | Exercises | `tlpi:61.15` | not-started |

### Part 8 — Advanced I/O topics

#### Chapter 62 — TERMINALS

| Chapter | Section | Exact source title | Locator | Status |
| ---: | --- | --- | --- | --- |
| 62 | `62.1` | Overview | `tlpi:62.1` | not-started |
| 62 | `62.2` | Retrieving and Modifying Terminal Attributes | `tlpi:62.2` | not-started |
| 62 | `62.3` | The stty Command | `tlpi:62.3` | not-started |
| 62 | `62.4` | Terminal Special Characters | `tlpi:62.4` | not-started |
| 62 | `62.5` | Terminal Flags | `tlpi:62.5` | not-started |
| 62 | `62.6` | Terminal I/O Modes | `tlpi:62.6` | not-started |
| 62 | `62.7` | Terminal Line Speed (Bit Rate) | `tlpi:62.7` | not-started |
| 62 | `62.8` | Terminal Line Control | `tlpi:62.8` | not-started |
| 62 | `62.9` | Terminal Window Size | `tlpi:62.9` | not-started |
| 62 | `62.10` | Terminal Identification | `tlpi:62.10` | not-started |
| 62 | `62.11` | Summary | `tlpi:62.11` | not-started |
| 62 | `62.12` | Exercises | `tlpi:62.12` | not-started |

#### Chapter 63 — ALTERNATIVE I/O MODELS

| Chapter | Section | Exact source title | Locator | Status |
| ---: | --- | --- | --- | --- |
| 63 | `63.1` | Overview | `tlpi:63.1` | not-started |
| 63 | `63.2` | I/O Multiplexing | `tlpi:63.2` | not-started |
| 63 | `63.3` | Signal-Driven I/O | `tlpi:63.3` | not-started |
| 63 | `63.4` | The epoll API | `tlpi:63.4` | not-started |
| 63 | `63.5` | Waiting on Signals and File Descriptors | `tlpi:63.5` | not-started |
| 63 | `63.6` | Summary | `tlpi:63.6` | not-started |
| 63 | `63.7` | Exercises | `tlpi:63.7` | not-started |

#### Chapter 64 — PSEUDOTERMINALS

| Chapter | Section | Exact source title | Locator | Status |
| ---: | --- | --- | --- | --- |
| 64 | `64.1` | Overview | `tlpi:64.1` | not-started |
| 64 | `64.2` | UNIX 98 Pseudoterminals | `tlpi:64.2` | not-started |
| 64 | `64.3` | Opening a Pseudoterminal Master: ptyMasterOpen() | `tlpi:64.3` | not-started |
| 64 | `64.4` | Connecting Two Processes with a Pseudoterminal: ptyFork() | `tlpi:64.4` | not-started |
| 64 | `64.5` | Pseudoterminal I/O | `tlpi:64.5` | not-started |
| 64 | `64.6` | Implementing script(1) | `tlpi:64.6` | not-started |
| 64 | `64.7` | Terminal Attributes and Window Size | `tlpi:64.7` | not-started |
| 64 | `64.8` | BSD Pseudoterminals | `tlpi:64.8` | not-started |
| 64 | `64.9` | Summary | `tlpi:64.9` | not-started |
| 64 | `64.10` | Exercises | `tlpi:64.10` | not-started |

## Appendices

| Appendix | Exact source title | Locator | Status |
| --- | --- | --- | --- |
| A | TRACING SYSTEM CALLS | `tlpi:appendix:A` | not-started |
| B | PARSING COMMAND-LINE OPTIONS | `tlpi:appendix:B` | not-started |
| C | CASTING THE NULL POINTER | `tlpi:appendix:C` | not-started |
| D | KERNEL CONFIGURATION | `tlpi:appendix:D` | not-started |
| E | FURTHER SOURCES OF INFORMATION | `tlpi:appendix:E` | not-started |
| F | SOLUTIONS TO SELECTED EXERCISES | `tlpi:appendix:F` | not-started |

## Update rule

正文来源单元只能按实际完成情况推进：

```text
not-started
→ in-progress
→ source-reviewed
→ mapped
```

Coverage 更新使用独立 `coverage(unix): ...` commit。目录映射、Mechanism Map 和 Mechanism Unit 的状态彼此独立。

## Next checkpoint

下一次只读取 **TLPI 1.2 — Linux简史**。reading-mcp 的结构定位已确认该标题，但本次未读取 1.2 正文；按 Chapter 1 的顺序，它是 1.1 之后唯一的下一 Section，并继续补足进入标准化内容前的 Linux 历史背景。
