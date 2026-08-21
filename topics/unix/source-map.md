# TLPI Source Map

> Scope: source identity, book structure, stable locators, and parser notes only. This file contains no Mechanism Unit, Claim-Evidence Matrix, experiment, or mechanism conclusion.

- Coverage Map: [`coverage.md`](./coverage.md)
- Unix/Linux Mechanism Map: [`README.md`](./README.md)
- Repository framework: [`../../docs/WHITEBOX_LEARNING_FRAMEWORK.md`](../../docs/WHITEBOX_LEARNING_FRAMEWORK.md)

## 1. Source identity

| Field | Value |
| --- | --- |
| Source alias | `TLPI` |
| Chinese title | 《Linux/UNIX系统编程手册（上、下册）》 |
| Original title | *The Linux Programming Interface* |
| Author | Michael Kerrisk |
| Edition | `unknown / not confirmed` |
| Primary document format | EPUB; exact MCP media-type string is `unknown / not confirmed` |
| Primary reading-mcp document ID | `doc:sha256:286e0104a40d05c3cb76f08e2d6a06391ce9d1bc603351aefc2340aca3349b2f` |
| Primary source path | Local EPUB opened by reading-mcp; exact filename/path is `unknown / not confirmed` |
| Body scale | 64 chapters; 585 numbered sections (`X.Y`); 229 numbered subsections (`X.Y.Z`) |
| Appendix scale | 6 appendices, A–F |
| Current source boundary | Preface states the book is current through Linux 2.6.35 and glibc 2.12; later interface changes require separate sources |

## 2. Reading sources and identifiers

| Source ID | Role | reading-mcp document ID | Format | Stable read unit / locator | Parse result |
| --- | --- | --- | --- | --- | --- |
| `TLPI-PRIMARY-EPUB` | Primary body source for later section reading | `doc:sha256:286e0104a40d05c3cb76f08e2d6a06391ce9d1bc603351aefc2340aca3349b2f` | EPUB | Semantic locator `tlpi:<section-number>` plus exact title; resolve against this document with `search_document`, then read the returned `section_id` | Exact per-section EPUB `section_id` values are `unknown / not confirmed` in this mapping run |
| `TLPI-PREFACE-PDF` | Book purpose, audience, and organization | `doc:sha256:7e4de58ed72799de035497b7702666f5e375c88dfc8e3c6ea2f0977645c91889` | PDF | `section://page-1` … `section://page-11`; native `pdf:page:N` | 11 page sections; structure and reads were not truncated |
| `TLPI-TOC-HTML` | Canonical detailed hierarchy and exact headings | `doc:sha256:fe522b2d5b05b1c76658bad4d6351367dbfed239b85fe33a45d81d42acffe9f9` | HTML | owner `section://detailed-table-of-contents-for-the-linux-programming-interface`; paragraph/native locator `html:heading:1#search-unit:N` | Parser returns the complete detailed TOC under one owner section; no response truncation |
| `TLPI-TOC-PDF` | Page-number cross-check for the detailed TOC | `doc:sha256:f766e1f40b765781b321a5014bd9cef507d9d64624c26ca109490585fb45e62f` | PDF | `section://page-1` … `section://page-19`; native `pdf:page:N` | 19 page sections; Chapter 64 and appendices are present on page 19 |

### Locator contract

Canonical semantic locator:

```text
tlpi:<chapter>.<section>
tlpi:<chapter>.<section>.<subsection>
tlpi:appendix:<letter>
```

Example for “read TLPI 2.1”:

```text
1. Source alias: TLPI-PRIMARY-EPUB
2. document_id: doc:sha256:286e0104a40d05c3cb76f08e2d6a06391ce9d1bc603351aefc2340aca3349b2f
3. semantic locator: tlpi:2.1
4. exact heading: The Core Operating System: The Kernel
5. search_document(document_id, exact heading)
6. select the exact 2.1 hit and call read_document with its returned section_id
```

The semantic number and exact heading are format-independent. The detailed-TOC locator recorded below provides an independently repeatable check even if EPUB-generated node IDs change after reparsing.

## 3. Book structure purpose from the Preface

- **Goal:** describe the Linux programming interface—system calls, library functions, and other low-level interfaces—while separating Linux-specific behavior from portable UNIX/POSIX behavior. Locator: `TLPI-PREFACE-PDF`, `pdf:page:1`.
- **Target readers:** Linux/UNIX/POSIX application programmers and designers; porting engineers; instructors and advanced students; system managers and power users. Prior programming and C/shell familiarity are assumed, but prior system-programming experience is not required. Locator: `pdf:page:2`.
- **Why this organization:** the book supports both linear tutorial reading and random-access reference use. Later chapters build on earlier material and forward references are minimized; the index and cross-references support non-linear use. Locator: `pdf:page:3`.
- **Foundation:** Chapters 1–3 provide history, standards, fundamental Linux/UNIX concepts, and system-programming concepts. Chapters 4–12 cover the fundamental system-programming interface. Locator: `pdf:page:3`.
- **Build-up:** Chapters 13–23 add advanced interface features; 24–33 cover processes/programs/threads; 34–42 advanced process/program topics; 43–55 IPC; 56–61 sockets/networking; 62–64 advanced I/O. Locators: `pdf:page:3` and `pdf:page:4`.

## 4. Hierarchy summary

| Level | Count | Stable mapping level |
| --- | ---: | --- |
| Logical Part | 8 | Preface grouping, page 3–4 |
| Chapter | 64 | `tlpi:<chapter>` and exact title |
| Section (`X.Y`) | 585 | `tlpi:X.Y`, exact title, and detailed-TOC search-unit locator |
| Subsection (`X.Y.Z`) | 229 | `tlpi:X.Y.Z`, exact title, and detailed-TOC search-unit locator |
| Appendix | 6 | `tlpi:appendix:A` … `F` |

Numbering checks:

- Chapters are continuous from 1 through 64.
- Within every chapter, `X.Y` section numbers begin at 1 and are continuous.
- Within every parent section that has children, `X.Y.Z` subsection numbers begin at 1 and are continuous.
- No duplicate numbered locator was found.
- The complete hierarchy was returned without response truncation.

## 5. Complete Source Map

Each entry records the semantic locator and its stable locator in `TLPI-TOC-HTML`. `search-unit:N` is the reading-mcp paragraph/native-location index returned by exact-title search.

## Part 1 — Background and concepts

Preface grouping locator: `TLPI-PREFACE-PDF`, `pdf:page:3`.

### Chapter 1 — HISTORY AND STANDARDS

- Chapter locator: `tlpi:1`; `toc-html#search-unit:3`
- **`1.1` A Brief History of UNIX and C** — `tlpi:1.1`; `toc-html#search-unit:4`
- **`1.2` A Brief History of Linux** — `tlpi:1.2`; `toc-html#search-unit:5`
  - `1.2.1` The GNU Project — `tlpi:1.2.1`; `toc-html#search-unit:6`
  - `1.2.2` The Linux Kernel — `tlpi:1.2.2`; `toc-html#search-unit:7`
- **`1.3` Standardization** — `tlpi:1.3`; `toc-html#search-unit:8`
  - `1.3.1` The C Programming Language — `tlpi:1.3.1`; `toc-html#search-unit:9`
  - `1.3.2` The First POSIX Standards — `tlpi:1.3.2`; `toc-html#search-unit:10`
  - `1.3.3` X/Open Company and The Open Group — `tlpi:1.3.3`; `toc-html#search-unit:11`
  - `1.3.4` SUSv3 and POSIX.1-2001 — `tlpi:1.3.4`; `toc-html#search-unit:12`
  - `1.3.5` SUSv4 and POSIX.1-2008 — `tlpi:1.3.5`; `toc-html#search-unit:13`
  - `1.3.6` UNIX Standards Timeline — `tlpi:1.3.6`; `toc-html#search-unit:14`
  - `1.3.7` Implementation Standards — `tlpi:1.3.7`; `toc-html#search-unit:15`
  - `1.3.8` Linux, Standards, and the Linux Standard Base — `tlpi:1.3.8`; `toc-html#search-unit:16`
- **`1.4` Summary** — `tlpi:1.4`; `toc-html#search-unit:17`

### Chapter 2 — FUNDAMENTAL CONCEPTS

- Chapter locator: `tlpi:2`; `toc-html#search-unit:18`
- **`2.1` The Core Operating System: The Kernel** — `tlpi:2.1`; `toc-html#search-unit:19`
- **`2.2` The Shell** — `tlpi:2.2`; `toc-html#search-unit:20`
- **`2.3` Users and Groups** — `tlpi:2.3`; `toc-html#search-unit:21`
- **`2.4` Single Directory Hierarchy, Directories, Links, and Files** — `tlpi:2.4`; `toc-html#search-unit:22`
- **`2.5` File I/O Model** — `tlpi:2.5`; `toc-html#search-unit:23`
- **`2.6` Programs** — `tlpi:2.6`; `toc-html#search-unit:24`
- **`2.7` Processes** — `tlpi:2.7`; `toc-html#search-unit:25`
- **`2.8` Memory Mappings** — `tlpi:2.8`; `toc-html#search-unit:26`
- **`2.9` Static and Shared Libraries** — `tlpi:2.9`; `toc-html#search-unit:27`
- **`2.10` Interprocess Communication and Synchronization** — `tlpi:2.10`; `toc-html#search-unit:28`
- **`2.11` Signals** — `tlpi:2.11`; `toc-html#search-unit:29`
- **`2.12` Threads** — `tlpi:2.12`; `toc-html#search-unit:30`
- **`2.13` Process Groups and Shell Job Control** — `tlpi:2.13`; `toc-html#search-unit:31`
- **`2.14` Sessions, Controlling Terminals, and Controlling Processes** — `tlpi:2.14`; `toc-html#search-unit:32`
- **`2.15` Pseudoterminals** — `tlpi:2.15`; `toc-html#search-unit:33`
- **`2.16` Date and Time** — `tlpi:2.16`; `toc-html#search-unit:34`
- **`2.17` Client-Server Architecture** — `tlpi:2.17`; `toc-html#search-unit:35`
- **`2.18` Realtime** — `tlpi:2.18`; `toc-html#search-unit:36`
- **`2.19` The /proc File System** — `tlpi:2.19`; `toc-html#search-unit:37`
- **`2.20` Summary** — `tlpi:2.20`; `toc-html#search-unit:38`

### Chapter 3 — SYSTEM PROGRAMMING CONCEPTS

- Chapter locator: `tlpi:3`; `toc-html#search-unit:39`
- **`3.1` System Calls** — `tlpi:3.1`; `toc-html#search-unit:40`
- **`3.2` Library Functions** — `tlpi:3.2`; `toc-html#search-unit:41`
- **`3.3` The Standard C Library; The GNU C Library ( glibc )** — `tlpi:3.3`; `toc-html#search-unit:42`
- **`3.4` Handling Errors from System Calls and Library Functions** — `tlpi:3.4`; `toc-html#search-unit:43`
- **`3.5` Notes on the Example Programs in This Book** — `tlpi:3.5`; `toc-html#search-unit:44`
  - `3.5.1` Command-Line Options and Arguments — `tlpi:3.5.1`; `toc-html#search-unit:45`
  - `3.5.2` Common Functions and Header Files — `tlpi:3.5.2`; `toc-html#search-unit:46`
- **`3.6` Portability Issues** — `tlpi:3.6`; `toc-html#search-unit:47`
  - `3.6.1` Feature Test Macros — `tlpi:3.6.1`; `toc-html#search-unit:48`
  - `3.6.2` System Data Types — `tlpi:3.6.2`; `toc-html#search-unit:49`
  - `3.6.3` Miscellaneous Portability Issues — `tlpi:3.6.3`; `toc-html#search-unit:50`
- **`3.7` Summary** — `tlpi:3.7`; `toc-html#search-unit:51`
- **`3.8` Exercise** — `tlpi:3.8`; `toc-html#search-unit:52`

## Part 2 — Fundamental features of the system programming interface

Preface grouping locator: `TLPI-PREFACE-PDF`, `pdf:page:3`.

### Chapter 4 — FILE I/O: THE UNIVERSAL I/O MODEL

- Chapter locator: `tlpi:4`; `toc-html#search-unit:53`
- **`4.1` Overview** — `tlpi:4.1`; `toc-html#search-unit:54`
- **`4.2` Universality of I/O** — `tlpi:4.2`; `toc-html#search-unit:55`
- **`4.3` Opening a File: open()** — `tlpi:4.3`; `toc-html#search-unit:56`
  - `4.3.1` The open() flags Argument — `tlpi:4.3.1`; `toc-html#search-unit:57`
  - `4.3.2` Errors from open() — `tlpi:4.3.2`; `toc-html#search-unit:58`
  - `4.3.3` The creat() System Call — `tlpi:4.3.3`; `toc-html#search-unit:59`
- **`4.4` Reading from a File: read()** — `tlpi:4.4`; `toc-html#search-unit:60`
- **`4.5` Writing to a File: write()** — `tlpi:4.5`; `toc-html#search-unit:61`
- **`4.6` Closing a File: close()** — `tlpi:4.6`; `toc-html#search-unit:62`
- **`4.7` Changing the File Offset: lseek()** — `tlpi:4.7`; `toc-html#search-unit:63`
- **`4.8` Operations Outside the Universal I/O Model: ioctl()** — `tlpi:4.8`; `toc-html#search-unit:64`
- **`4.9` Summary** — `tlpi:4.9`; `toc-html#search-unit:65`
- **`4.10` Exercises** — `tlpi:4.10`; `toc-html#search-unit:66`

### Chapter 5 — FILE I/O: FURTHER DETAILS

- Chapter locator: `tlpi:5`; `toc-html#search-unit:67`
- **`5.1` Atomicity and Race Conditions** — `tlpi:5.1`; `toc-html#search-unit:68`
- **`5.2` File Control Operations: fcntl()** — `tlpi:5.2`; `toc-html#search-unit:69`
- **`5.3` Open File Status Flags** — `tlpi:5.3`; `toc-html#search-unit:70`
- **`5.4` Relationship Between File Descriptors and Open Files** — `tlpi:5.4`; `toc-html#search-unit:71`
- **`5.5` Duplicating File Descriptors** — `tlpi:5.5`; `toc-html#search-unit:72`
- **`5.6` File I/O at a Specified Offset: pread() and pwrite()** — `tlpi:5.6`; `toc-html#search-unit:73`
- **`5.7` Scatter-Gather I/O: readv() and writev()** — `tlpi:5.7`; `toc-html#search-unit:74`
- **`5.8` Truncating a File: truncate() and ftruncate()** — `tlpi:5.8`; `toc-html#search-unit:75`
- **`5.9` Nonblocking I/O** — `tlpi:5.9`; `toc-html#search-unit:76`
- **`5.10` I/O on Large Files** — `tlpi:5.10`; `toc-html#search-unit:77`
- **`5.11` The /dev/fd Directory** — `tlpi:5.11`; `toc-html#search-unit:78`
- **`5.12` Creating Temporary Files** — `tlpi:5.12`; `toc-html#search-unit:79`
- **`5.13` Summary** — `tlpi:5.13`; `toc-html#search-unit:80`
- **`5.14` Exercises** — `tlpi:5.14`; `toc-html#search-unit:81`

### Chapter 6 — PROCESSES

- Chapter locator: `tlpi:6`; `toc-html#search-unit:82`
- **`6.1` Processes and Programs** — `tlpi:6.1`; `toc-html#search-unit:83`
- **`6.2` Process ID and Parent Process ID** — `tlpi:6.2`; `toc-html#search-unit:84`
- **`6.3` Memory Layout of a Process** — `tlpi:6.3`; `toc-html#search-unit:85`
- **`6.4` Virtual Memory Management** — `tlpi:6.4`; `toc-html#search-unit:86`
- **`6.5` The Stack and Stack Frames** — `tlpi:6.5`; `toc-html#search-unit:87`
- **`6.6` Command-Line Arguments ( argc , argv )** — `tlpi:6.6`; `toc-html#search-unit:88`
- **`6.7` Environment List** — `tlpi:6.7`; `toc-html#search-unit:89`
- **`6.8` Performing a Nonlocal Goto: setjmp() and longjmp()** — `tlpi:6.8`; `toc-html#search-unit:90`
- **`6.9` Summary** — `tlpi:6.9`; `toc-html#search-unit:91`
- **`6.10` Exercises** — `tlpi:6.10`; `toc-html#search-unit:92`

### Chapter 7 — MEMORY ALLOCATION

- Chapter locator: `tlpi:7`; `toc-html#search-unit:93`
- **`7.1` Allocating Memory on the Heap** — `tlpi:7.1`; `toc-html#search-unit:94`
  - `7.1.1` Adjusting the Program Break: brk() and sbrk() — `tlpi:7.1.1`; `toc-html#search-unit:95`
  - `7.1.2` Allocating Memory on the Heap: malloc() and free() — `tlpi:7.1.2`; `toc-html#search-unit:96`
  - `7.1.3` Implementation of malloc() and free() — `tlpi:7.1.3`; `toc-html#search-unit:97`
  - `7.1.4` Other Methods of Allocating Memory on the Heap — `tlpi:7.1.4`; `toc-html#search-unit:98`
- **`7.2` Allocating Memory on the Stack: alloca()** — `tlpi:7.2`; `toc-html#search-unit:99`
- **`7.3` Summary** — `tlpi:7.3`; `toc-html#search-unit:100`
- **`7.4` Exercises** — `tlpi:7.4`; `toc-html#search-unit:101`

### Chapter 8 — USERS AND GROUPS

- Chapter locator: `tlpi:8`; `toc-html#search-unit:102`
- **`8.1` The Password File: /etc/passwd** — `tlpi:8.1`; `toc-html#search-unit:103`
- **`8.2` The Shadow Password File: /etc/shadow** — `tlpi:8.2`; `toc-html#search-unit:104`
- **`8.3` The Group File: /etc/group** — `tlpi:8.3`; `toc-html#search-unit:105`
- **`8.4` Retrieving User and Group Information** — `tlpi:8.4`; `toc-html#search-unit:106`
- **`8.5` Password Encryption and User Authentication** — `tlpi:8.5`; `toc-html#search-unit:107`
- **`8.6` Summary** — `tlpi:8.6`; `toc-html#search-unit:108`
- **`8.7` Exercises** — `tlpi:8.7`; `toc-html#search-unit:109`

### Chapter 9 — PROCESS CREDENTIALS

- Chapter locator: `tlpi:9`; `toc-html#search-unit:110`
- **`9.1` Real User ID and Real Group ID** — `tlpi:9.1`; `toc-html#search-unit:111`
- **`9.2` Effective User ID and Effective Group ID** — `tlpi:9.2`; `toc-html#search-unit:112`
- **`9.3` Set-User-ID and Set-Group-ID Programs** — `tlpi:9.3`; `toc-html#search-unit:113`
- **`9.4` Saved Set-User-ID and Saved Set-Group-ID** — `tlpi:9.4`; `toc-html#search-unit:114`
- **`9.5` File-System User ID and File-System Group ID** — `tlpi:9.5`; `toc-html#search-unit:115`
- **`9.6` Supplementary Group IDs** — `tlpi:9.6`; `toc-html#search-unit:116`
- **`9.7` Retrieving and Modifying Process Credentials** — `tlpi:9.7`; `toc-html#search-unit:117`
  - `9.7.1` Retrieving and Modifying Real, Effective, and Saved Set IDs — `tlpi:9.7.1`; `toc-html#search-unit:118`
  - `9.7.2` Retrieving and Modifying File-System IDs — `tlpi:9.7.2`; `toc-html#search-unit:119`
  - `9.7.3` Retrieving and Modifying Supplementary Group IDs — `tlpi:9.7.3`; `toc-html#search-unit:120`
  - `9.7.4` Summary of Calls for Modifying Process Credentials — `tlpi:9.7.4`; `toc-html#search-unit:121`
  - `9.7.5` Example: Displaying Process Credentials — `tlpi:9.7.5`; `toc-html#search-unit:122`
- **`9.8` Summary** — `tlpi:9.8`; `toc-html#search-unit:123`
- **`9.9` Exercises** — `tlpi:9.9`; `toc-html#search-unit:124`

### Chapter 10 — TIME

- Chapter locator: `tlpi:10`; `toc-html#search-unit:125`
- **`10.1` Calendar Time** — `tlpi:10.1`; `toc-html#search-unit:126`
- **`10.2` Time-Conversion Functions** — `tlpi:10.2`; `toc-html#search-unit:127`
  - `10.2.1` Converting time_t to Printable Form — `tlpi:10.2.1`; `toc-html#search-unit:128`
  - `10.2.2` Converting Between time_t and Broken-Down Time — `tlpi:10.2.2`; `toc-html#search-unit:129`
  - `10.2.3` Converting Between Broken-Down Time and Printable Form — `tlpi:10.2.3`; `toc-html#search-unit:130`
- **`10.3` Timezones** — `tlpi:10.3`; `toc-html#search-unit:131`
- **`10.4` Locales** — `tlpi:10.4`; `toc-html#search-unit:132`
- **`10.5` Updating the System Clock** — `tlpi:10.5`; `toc-html#search-unit:133`
- **`10.6` The Software Clock (Jiffies)** — `tlpi:10.6`; `toc-html#search-unit:134`
- **`10.7` Process Time** — `tlpi:10.7`; `toc-html#search-unit:135`
- **`10.8` Summary** — `tlpi:10.8`; `toc-html#search-unit:136`
- **`10.9` Exercise** — `tlpi:10.9`; `toc-html#search-unit:137`

### Chapter 11 — SYSTEM LIMITS AND OPTIONS

- Chapter locator: `tlpi:11`; `toc-html#search-unit:138`
- **`11.1` System Limits** — `tlpi:11.1`; `toc-html#search-unit:139`
- **`11.2` Retrieving System Limits (and Options) at Run Time** — `tlpi:11.2`; `toc-html#search-unit:140`
- **`11.3` Retrieving File-Related Limits (and Options) at Run Time** — `tlpi:11.3`; `toc-html#search-unit:141`
- **`11.4` Indeterminate Limits** — `tlpi:11.4`; `toc-html#search-unit:142`
- **`11.5` System Options** — `tlpi:11.5`; `toc-html#search-unit:143`
- **`11.6` Summary** — `tlpi:11.6`; `toc-html#search-unit:144`
- **`11.7` Exercises** — `tlpi:11.7`; `toc-html#search-unit:145`

### Chapter 12 — SYSTEM AND PROCESS INFORMATION

- Chapter locator: `tlpi:12`; `toc-html#search-unit:146`
- **`12.1` The /proc File System** — `tlpi:12.1`; `toc-html#search-unit:147`
  - `12.1.1` Obtaining Information About a Process: /proc/ PID — `tlpi:12.1.1`; `toc-html#search-unit:148`
  - `12.1.2` System Information Under /proc — `tlpi:12.1.2`; `toc-html#search-unit:149`
  - `12.1.3` Accessing /proc Files — `tlpi:12.1.3`; `toc-html#search-unit:150`
- **`12.2` System Identification: uname()** — `tlpi:12.2`; `toc-html#search-unit:151`
- **`12.3` Summary** — `tlpi:12.3`; `toc-html#search-unit:152`
- **`12.4` Exercises** — `tlpi:12.4`; `toc-html#search-unit:153`

## Part 3 — More advanced features of the system programming interface

Preface grouping locator: `TLPI-PREFACE-PDF`, `pdf:page:3`.

### Chapter 13 — FILE I/O BUFFERING

- Chapter locator: `tlpi:13`; `toc-html#search-unit:154`
- **`13.1` Kernel Buffering of File I/O: The Buffer Cache** — `tlpi:13.1`; `toc-html#search-unit:155`
- **`13.2` Buffering in the stdio Library** — `tlpi:13.2`; `toc-html#search-unit:156`
- **`13.3` Controlling Kernel Buffering of File I/O** — `tlpi:13.3`; `toc-html#search-unit:157`
- **`13.4` Summary of I/O Buffering** — `tlpi:13.4`; `toc-html#search-unit:158`
- **`13.5` Giving the Kernel Hints About I/O Patterns: posix_fadvise()** — `tlpi:13.5`; `toc-html#search-unit:159`
- **`13.6` Bypassing the Buffer Cache: Direct I/O** — `tlpi:13.6`; `toc-html#search-unit:160`
- **`13.7` Mixing Library Functions and System Calls for File I/O** — `tlpi:13.7`; `toc-html#search-unit:161`
- **`13.8` Summary** — `tlpi:13.8`; `toc-html#search-unit:162`
- **`13.9` Exercises** — `tlpi:13.9`; `toc-html#search-unit:163`

### Chapter 14 — FILE SYSTEMS

- Chapter locator: `tlpi:14`; `toc-html#search-unit:164`
- **`14.1` Device Special Files (Devices)** — `tlpi:14.1`; `toc-html#search-unit:165`
- **`14.2` Disks and Partitions** — `tlpi:14.2`; `toc-html#search-unit:166`
- **`14.3` File Systems** — `tlpi:14.3`; `toc-html#search-unit:167`
- **`14.4` I-nodes** — `tlpi:14.4`; `toc-html#search-unit:168`
- **`14.5` The Virtual File System (VFS)** — `tlpi:14.5`; `toc-html#search-unit:169`
- **`14.6` Journaling File Systems** — `tlpi:14.6`; `toc-html#search-unit:170`
- **`14.7` Single Directory Hierarchy and Mount Points** — `tlpi:14.7`; `toc-html#search-unit:171`
- **`14.8` Mounting and Unmounting File Systems** — `tlpi:14.8`; `toc-html#search-unit:172`
  - `14.8.1` Mounting a File System: mount() — `tlpi:14.8.1`; `toc-html#search-unit:173`
  - `14.8.2` Unmounting a File System: umount() and umount2() — `tlpi:14.8.2`; `toc-html#search-unit:174`
- **`14.9` Advanced Mount Features** — `tlpi:14.9`; `toc-html#search-unit:175`
  - `14.9.1` Mounting a File System at Multiple Mount Points — `tlpi:14.9.1`; `toc-html#search-unit:176`
  - `14.9.2` Stacking Multiple Mounts on the Same Mount Point — `tlpi:14.9.2`; `toc-html#search-unit:177`
  - `14.9.3` Mount Flags That Are Per-Mount Options — `tlpi:14.9.3`; `toc-html#search-unit:178`
  - `14.9.4` Bind Mounts — `tlpi:14.9.4`; `toc-html#search-unit:179`
  - `14.9.5` Recursive Bind Mounts — `tlpi:14.9.5`; `toc-html#search-unit:180`
- **`14.10` A Virtual Memory File System: tmpfs** — `tlpi:14.10`; `toc-html#search-unit:181`
- **`14.11` Obtaining Information About a File System: statvfs()** — `tlpi:14.11`; `toc-html#search-unit:182`
- **`14.12` Summary** — `tlpi:14.12`; `toc-html#search-unit:183`
- **`14.13` Exercise** — `tlpi:14.13`; `toc-html#search-unit:184`

### Chapter 15 — FILE ATTRIBUTES

- Chapter locator: `tlpi:15`; `toc-html#search-unit:185`
- **`15.1` Retrieving File Information: stat()** — `tlpi:15.1`; `toc-html#search-unit:186`
- **`15.2` File Timestamps** — `tlpi:15.2`; `toc-html#search-unit:187`
  - `15.2.1` Changing File Timestamps with utime() and utimes() — `tlpi:15.2.1`; `toc-html#search-unit:188`
  - `15.2.2` Changing File Timestamps with utimensat() and futimens() — `tlpi:15.2.2`; `toc-html#search-unit:189`
- **`15.3` File Ownership** — `tlpi:15.3`; `toc-html#search-unit:190`
  - `15.3.1` Ownership of New Files — `tlpi:15.3.1`; `toc-html#search-unit:191`
  - `15.3.2` Changing File Ownership: chown() , fchown() , and lchown() — `tlpi:15.3.2`; `toc-html#search-unit:192`
- **`15.4` File Permissions** — `tlpi:15.4`; `toc-html#search-unit:193`
  - `15.4.1` Permissions on Regular Files — `tlpi:15.4.1`; `toc-html#search-unit:194`
  - `15.4.2` Permissions on Directories — `tlpi:15.4.2`; `toc-html#search-unit:195`
  - `15.4.3` Permission-Checking Algorithm — `tlpi:15.4.3`; `toc-html#search-unit:196`
  - `15.4.4` Checking File Accessibility: access() — `tlpi:15.4.4`; `toc-html#search-unit:197`
  - `15.4.5` Set-User-ID, Set-Group-ID, and Sticky Bits — `tlpi:15.4.5`; `toc-html#search-unit:198`
  - `15.4.6` The Process File Mode Creation Mask: umask() — `tlpi:15.4.6`; `toc-html#search-unit:199`
  - `15.4.7` Changing File Permissions: chmod() and fchmod() — `tlpi:15.4.7`; `toc-html#search-unit:200`
- **`15.5` I-node Flags ( ext2 Extended File Attributes)** — `tlpi:15.5`; `toc-html#search-unit:201`
- **`15.6` Summary** — `tlpi:15.6`; `toc-html#search-unit:202`
- **`15.7` Exercises** — `tlpi:15.7`; `toc-html#search-unit:203`

### Chapter 16 — EXTENDED ATTRIBUTES

- Chapter locator: `tlpi:16`; `toc-html#search-unit:204`
- **`16.1` Overview** — `tlpi:16.1`; `toc-html#search-unit:205`
- **`16.2` Extended Attribute Implementation Details** — `tlpi:16.2`; `toc-html#search-unit:206`
- **`16.3` System Calls for Manipulating Extended Attributes** — `tlpi:16.3`; `toc-html#search-unit:207`
- **`16.4` Summary** — `tlpi:16.4`; `toc-html#search-unit:208`
- **`16.5` Exercise** — `tlpi:16.5`; `toc-html#search-unit:209`

### Chapter 17 — ACCESS CONTROL LISTS

- Chapter locator: `tlpi:17`; `toc-html#search-unit:210`
- **`17.1` Overview** — `tlpi:17.1`; `toc-html#search-unit:211`
- **`17.2` ACL Permission-Checking Algorithm** — `tlpi:17.2`; `toc-html#search-unit:212`
- **`17.3` Long and Short Text Forms for ACLs** — `tlpi:17.3`; `toc-html#search-unit:213`
- **`17.4` The ACL_MASK Entry and the ACL Group Class** — `tlpi:17.4`; `toc-html#search-unit:214`
- **`17.5` The getfacl and setfacl Commands** — `tlpi:17.5`; `toc-html#search-unit:215`
- **`17.6` Default ACLs and File Creation** — `tlpi:17.6`; `toc-html#search-unit:216`
- **`17.7` ACL Implementation Limits** — `tlpi:17.7`; `toc-html#search-unit:217`
- **`17.8` The ACL API** — `tlpi:17.8`; `toc-html#search-unit:218`
- **`17.9` Summary** — `tlpi:17.9`; `toc-html#search-unit:219`
- **`17.10` Exercise** — `tlpi:17.10`; `toc-html#search-unit:220`

### Chapter 18 — DIRECTORIES AND LINKS

- Chapter locator: `tlpi:18`; `toc-html#search-unit:221`
- **`18.1` Directories and (Hard) Links** — `tlpi:18.1`; `toc-html#search-unit:222`
- **`18.2` Symbolic (Soft) Links** — `tlpi:18.2`; `toc-html#search-unit:223`
- **`18.3` Creating and Removing (Hard) Links: link() and unlink()** — `tlpi:18.3`; `toc-html#search-unit:224`
- **`18.4` Changing the Name of a File: rename()** — `tlpi:18.4`; `toc-html#search-unit:225`
- **`18.5` Working with Symbolic Links: symlink() and readlink()** — `tlpi:18.5`; `toc-html#search-unit:226`
- **`18.6` Creating and Removing Directories: mkdir() and rmdir()** — `tlpi:18.6`; `toc-html#search-unit:227`
- **`18.7` Removing a File or Directory: remove()** — `tlpi:18.7`; `toc-html#search-unit:228`
- **`18.8` Reading Directories: opendir() and readdir()** — `tlpi:18.8`; `toc-html#search-unit:229`
- **`18.9` File Tree Walking: nftw()** — `tlpi:18.9`; `toc-html#search-unit:230`
- **`18.10` The Current Working Directory of a Process** — `tlpi:18.10`; `toc-html#search-unit:231`
- **`18.11` Operating Relative to a Directory File Descriptor** — `tlpi:18.11`; `toc-html#search-unit:232`
- **`18.12` Changing the Root Directory of a Process: chroot()** — `tlpi:18.12`; `toc-html#search-unit:233`
- **`18.13` Resolving a Pathname: realpath()** — `tlpi:18.13`; `toc-html#search-unit:234`
- **`18.14` Parsing Pathname Strings: dirname() and basename()** — `tlpi:18.14`; `toc-html#search-unit:235`
- **`18.15` Summary** — `tlpi:18.15`; `toc-html#search-unit:236`
- **`18.16` Exercises** — `tlpi:18.16`; `toc-html#search-unit:237`

### Chapter 19 — MONITORING FILE EVENTS

- Chapter locator: `tlpi:19`; `toc-html#search-unit:238`
- **`19.1` Overview** — `tlpi:19.1`; `toc-html#search-unit:239`
- **`19.2` The inotify API** — `tlpi:19.2`; `toc-html#search-unit:240`
- **`19.3` inotify Events** — `tlpi:19.3`; `toc-html#search-unit:241`
- **`19.4` Reading inotify Events** — `tlpi:19.4`; `toc-html#search-unit:242`
- **`19.5` Queue Limits and /proc Files** — `tlpi:19.5`; `toc-html#search-unit:243`
- **`19.6` An Older System for Monitoring File Events: dnotify** — `tlpi:19.6`; `toc-html#search-unit:244`
- **`19.7` Summary** — `tlpi:19.7`; `toc-html#search-unit:245`
- **`19.8` Exercise** — `tlpi:19.8`; `toc-html#search-unit:246`

### Chapter 20 — SIGNALS: FUNDAMENTAL CONCEPTS

- Chapter locator: `tlpi:20`; `toc-html#search-unit:247`
- **`20.1` Concepts and Overview** — `tlpi:20.1`; `toc-html#search-unit:248`
- **`20.2` Signal Types and Default Actions** — `tlpi:20.2`; `toc-html#search-unit:249`
- **`20.3` Changing Signal Dispositions: signal()** — `tlpi:20.3`; `toc-html#search-unit:250`
- **`20.4` Introduction to Signal Handlers** — `tlpi:20.4`; `toc-html#search-unit:251`
- **`20.5` Sending Signals: kill()** — `tlpi:20.5`; `toc-html#search-unit:252`
- **`20.6` Checking for the Existence of a Process** — `tlpi:20.6`; `toc-html#search-unit:253`
- **`20.7` Other Ways of Sending Signals: raise() and killpg()** — `tlpi:20.7`; `toc-html#search-unit:254`
- **`20.8` Displaying Signal Descriptions** — `tlpi:20.8`; `toc-html#search-unit:255`
- **`20.9` Signal Sets** — `tlpi:20.9`; `toc-html#search-unit:256`
- **`20.10` The Signal Mask (Blocking Signal Delivery)** — `tlpi:20.10`; `toc-html#search-unit:257`
- **`20.11` Pending Signals** — `tlpi:20.11`; `toc-html#search-unit:258`
- **`20.12` Signals Are Not Queued** — `tlpi:20.12`; `toc-html#search-unit:259`
- **`20.13` Changing Signal Dispositions: sigaction()** — `tlpi:20.13`; `toc-html#search-unit:260`
- **`20.14` Waiting for a Signal: pause()** — `tlpi:20.14`; `toc-html#search-unit:261`
- **`20.15` Summary** — `tlpi:20.15`; `toc-html#search-unit:262`
- **`20.16` Exercises** — `tlpi:20.16`; `toc-html#search-unit:263`

### Chapter 21 — SIGNALS: SIGNAL HANDLERS

- Chapter locator: `tlpi:21`; `toc-html#search-unit:264`
- **`21.1` Designing Signal Handlers** — `tlpi:21.1`; `toc-html#search-unit:265`
  - `21.1.1` Signals Are Not Queued (Revisited) — `tlpi:21.1.1`; `toc-html#search-unit:266`
  - `21.1.2` Reentrant and Async-Signal-Safe Functions — `tlpi:21.1.2`; `toc-html#search-unit:267`
  - `21.1.3` Global Variables and the sig_atomic_t Data Type — `tlpi:21.1.3`; `toc-html#search-unit:268`
- **`21.2` Other Methods of Terminating a Signal Handler** — `tlpi:21.2`; `toc-html#search-unit:269`
  - `21.2.1` Performing a Nonlocal Goto from a Signal Handler — `tlpi:21.2.1`; `toc-html#search-unit:270`
  - `21.2.2` Terminating a Process Abnormally: abort() — `tlpi:21.2.2`; `toc-html#search-unit:271`
- **`21.3` Handling a Signal on an Alternate Stack: sigaltstack()** — `tlpi:21.3`; `toc-html#search-unit:272`
- **`21.4` The SA_SIGINFO Flag** — `tlpi:21.4`; `toc-html#search-unit:273`
- **`21.5` Interruption and Restarting of System Calls** — `tlpi:21.5`; `toc-html#search-unit:274`
- **`21.6` Summary** — `tlpi:21.6`; `toc-html#search-unit:275`
- **`21.7` Exercise** — `tlpi:21.7`; `toc-html#search-unit:276`

### Chapter 22 — SIGNALS: ADVANCED FEATURES

- Chapter locator: `tlpi:22`; `toc-html#search-unit:277`
- **`22.1` Core Dump Files** — `tlpi:22.1`; `toc-html#search-unit:278`
- **`22.2` Special Cases for Signal Delivery, Disposition, and Handling** — `tlpi:22.2`; `toc-html#search-unit:279`
- **`22.3` Interruptible and Uninterruptible Process Sleep States** — `tlpi:22.3`; `toc-html#search-unit:280`
- **`22.4` Hardware-Generated Signals** — `tlpi:22.4`; `toc-html#search-unit:281`
- **`22.5` Synchronous and Asynchronous Signal Generation** — `tlpi:22.5`; `toc-html#search-unit:282`
- **`22.6` Timing and Order of Signal Delivery** — `tlpi:22.6`; `toc-html#search-unit:283`
- **`22.7` Implementation and Portability of signal()** — `tlpi:22.7`; `toc-html#search-unit:284`
- **`22.8` Realtime Signals** — `tlpi:22.8`; `toc-html#search-unit:285`
  - `22.8.1` Sending Realtime Signals — `tlpi:22.8.1`; `toc-html#search-unit:286`
  - `22.8.2` Handling Realtime Signals — `tlpi:22.8.2`; `toc-html#search-unit:287`
- **`22.9` Waiting for a Signal Using a Mask: sigsuspend()** — `tlpi:22.9`; `toc-html#search-unit:288`
- **`22.10` Synchronously Waiting for a Signal** — `tlpi:22.10`; `toc-html#search-unit:289`
- **`22.11` Fetching Signals via a File Descriptor** — `tlpi:22.11`; `toc-html#search-unit:290`
- **`22.12` Interprocess Communication with Signals** — `tlpi:22.12`; `toc-html#search-unit:291`
- **`22.13` Earlier Signal APIs (System V and BSD)** — `tlpi:22.13`; `toc-html#search-unit:292`
- **`22.14` Summary** — `tlpi:22.14`; `toc-html#search-unit:293`
- **`22.15` Exercises** — `tlpi:22.15`; `toc-html#search-unit:294`

### Chapter 23 — TIMERS AND SLEEPING

- Chapter locator: `tlpi:23`; `toc-html#search-unit:295`
- **`23.1` Interval Timers** — `tlpi:23.1`; `toc-html#search-unit:296`
- **`23.2` Scheduling and Accuracy of Timers** — `tlpi:23.2`; `toc-html#search-unit:297`
- **`23.3` Setting Timeouts on Blocking Operations** — `tlpi:23.3`; `toc-html#search-unit:298`
- **`23.4` Suspending Execution for a Fixed Interval (Sleeping)** — `tlpi:23.4`; `toc-html#search-unit:299`
  - `23.4.1` Low-Resolution Sleeping: sleep() — `tlpi:23.4.1`; `toc-html#search-unit:300`
  - `23.4.2` High-Resolution Sleeping: nanosleep() — `tlpi:23.4.2`; `toc-html#search-unit:301`
- **`23.5` POSIX Clocks** — `tlpi:23.5`; `toc-html#search-unit:302`
  - `23.5.1` Retrieving the Value of a Clock: clock_gettime() — `tlpi:23.5.1`; `toc-html#search-unit:303`
  - `23.5.2` Setting the Value of a Clock: clock_settime() — `tlpi:23.5.2`; `toc-html#search-unit:304`
  - `23.5.3` Obtaining the Clock ID of a Specific Process or Thread — `tlpi:23.5.3`; `toc-html#search-unit:305`
  - `23.5.4` Improved High-Resolution Sleeping: clock_nanosleep() — `tlpi:23.5.4`; `toc-html#search-unit:306`
- **`23.6` POSIX Interval Timers** — `tlpi:23.6`; `toc-html#search-unit:307`
  - `23.6.1` Creating a Timer: timer_create() — `tlpi:23.6.1`; `toc-html#search-unit:308`
  - `23.6.2` Arming and Disarming a Timer: timer_settime() — `tlpi:23.6.2`; `toc-html#search-unit:309`
  - `23.6.3` Retrieving the Current Value of a Timer: timer_gettime() — `tlpi:23.6.3`; `toc-html#search-unit:310`
  - `23.6.4` Deleting a Timer: timer_delete() — `tlpi:23.6.4`; `toc-html#search-unit:311`
  - `23.6.5` Notification via a Signal — `tlpi:23.6.5`; `toc-html#search-unit:312`
  - `23.6.6` Timer Overruns — `tlpi:23.6.6`; `toc-html#search-unit:313`
  - `23.6.7` Notification via a Thread — `tlpi:23.6.7`; `toc-html#search-unit:314`
- **`23.7` Timers That Notify via File Descriptors: the timerfd API** — `tlpi:23.7`; `toc-html#search-unit:315`
- **`23.8` Summary** — `tlpi:23.8`; `toc-html#search-unit:316`
- **`23.9` Exercises** — `tlpi:23.9`; `toc-html#search-unit:317`

## Part 4 — Processes, programs, and threads

Preface grouping locator: `TLPI-PREFACE-PDF`, `pdf:page:3`.

### Chapter 24 — PROCESS CREATION

- Chapter locator: `tlpi:24`; `toc-html#search-unit:318`
- **`24.1` Overview of fork() , exit() , wait() , and execve()** — `tlpi:24.1`; `toc-html#search-unit:319`
- **`24.2` Creating a New Process: fork()** — `tlpi:24.2`; `toc-html#search-unit:320`
  - `24.2.1` File Sharing Between Parent and Child — `tlpi:24.2.1`; `toc-html#search-unit:321`
  - `24.2.2` Memory Semantics of fork() — `tlpi:24.2.2`; `toc-html#search-unit:322`
- **`24.3` The vfork() System Call** — `tlpi:24.3`; `toc-html#search-unit:323`
- **`24.4` Race Conditions After fork()** — `tlpi:24.4`; `toc-html#search-unit:324`
- **`24.5` Avoiding Race Conditions by Synchronizing with Signals** — `tlpi:24.5`; `toc-html#search-unit:325`
- **`24.6` Summary** — `tlpi:24.6`; `toc-html#search-unit:326`

### Chapter 25 — PROCESS TERMINATION

- Chapter locator: `tlpi:25`; `toc-html#search-unit:327`
- **`25.1` Terminating a Process: _exit() and exit()** — `tlpi:25.1`; `toc-html#search-unit:328`
- **`25.2` Details of Process Termination** — `tlpi:25.2`; `toc-html#search-unit:329`
- **`25.3` Exit Handlers** — `tlpi:25.3`; `toc-html#search-unit:330`
- **`25.4` Interactions Between fork() , stdio Buffers, and _exit()** — `tlpi:25.4`; `toc-html#search-unit:331`
- **`25.5` Summary** — `tlpi:25.5`; `toc-html#search-unit:332`
- **`25.6` Exercise** — `tlpi:25.6`; `toc-html#search-unit:333`

### Chapter 26 — MONITORING CHILD PROCESSES

- Chapter locator: `tlpi:26`; `toc-html#search-unit:334`
- **`26.1` Waiting on a Child Process** — `tlpi:26.1`; `toc-html#search-unit:335`
  - `26.1.1` The wait() System Call — `tlpi:26.1.1`; `toc-html#search-unit:336`
  - `26.1.2` The waitpid() System Call — `tlpi:26.1.2`; `toc-html#search-unit:337`
  - `26.1.3` The Wait Status Value — `tlpi:26.1.3`; `toc-html#search-unit:338`
  - `26.1.4` Process Termination from a Signal Handler — `tlpi:26.1.4`; `toc-html#search-unit:339`
  - `26.1.5` The waitid() System Call — `tlpi:26.1.5`; `toc-html#search-unit:340`
  - `26.1.6` The wait3() and wait4() System Calls — `tlpi:26.1.6`; `toc-html#search-unit:341`
- **`26.2` Orphans and Zombies** — `tlpi:26.2`; `toc-html#search-unit:342`
- **`26.3` The SIGCHLD Signal** — `tlpi:26.3`; `toc-html#search-unit:343`
  - `26.3.1` Establishing a Handler for SIGCHLD — `tlpi:26.3.1`; `toc-html#search-unit:344`
  - `26.3.2` Delivery of SIGCHLD for Stopped Children — `tlpi:26.3.2`; `toc-html#search-unit:345`
  - `26.3.3` Ignoring Dead Child Processes — `tlpi:26.3.3`; `toc-html#search-unit:346`
- **`26.4` Summary** — `tlpi:26.4`; `toc-html#search-unit:347`
- **`26.5` Exercises** — `tlpi:26.5`; `toc-html#search-unit:348`

### Chapter 27 — PROGRAM EXECUTION

- Chapter locator: `tlpi:27`; `toc-html#search-unit:349`
- **`27.1` Executing a New Program: execve()** — `tlpi:27.1`; `toc-html#search-unit:350`
- **`27.2` The exec() Library Functions** — `tlpi:27.2`; `toc-html#search-unit:351`
  - `27.2.1` The PATH Environment Variable — `tlpi:27.2.1`; `toc-html#search-unit:352`
  - `27.2.2` Specifying Program Arguments As a List — `tlpi:27.2.2`; `toc-html#search-unit:353`
  - `27.2.3` Passing the Caller's Environment to the New Program — `tlpi:27.2.3`; `toc-html#search-unit:354`
  - `27.2.4` Executing a File Referred to by a Descriptor: fexecve() — `tlpi:27.2.4`; `toc-html#search-unit:355`
- **`27.3` Interpreter Scripts** — `tlpi:27.3`; `toc-html#search-unit:356`
- **`27.4` File Descriptors and exec()** — `tlpi:27.4`; `toc-html#search-unit:357`
- **`27.5` Signals and exec()** — `tlpi:27.5`; `toc-html#search-unit:358`
- **`27.6` Executing a Shell Command: system()** — `tlpi:27.6`; `toc-html#search-unit:359`
- **`27.7` Implementing system()** — `tlpi:27.7`; `toc-html#search-unit:360`
- **`27.8` Summary** — `tlpi:27.8`; `toc-html#search-unit:361`
- **`27.9` Exercises** — `tlpi:27.9`; `toc-html#search-unit:362`

### Chapter 28 — PROCESS CREATION AND PROGRAM EXECUTION IN MORE DETAIL

- Chapter locator: `tlpi:28`; `toc-html#search-unit:363`
- **`28.1` Process Accounting** — `tlpi:28.1`; `toc-html#search-unit:364`
- **`28.2` The clone() System Call** — `tlpi:28.2`; `toc-html#search-unit:365`
  - `28.2.1` The clone() flags Argument — `tlpi:28.2.1`; `toc-html#search-unit:366`
  - `28.2.2` Extensions to waitpid() for Cloned Children — `tlpi:28.2.2`; `toc-html#search-unit:367`
- **`28.3` Speed of Process Creation** — `tlpi:28.3`; `toc-html#search-unit:368`
- **`28.4` Effect of exec() and fork() on Process Attributes** — `tlpi:28.4`; `toc-html#search-unit:369`
- **`28.5` Summary** — `tlpi:28.5`; `toc-html#search-unit:370`
- **`28.6` Exercise** — `tlpi:28.6`; `toc-html#search-unit:371`

### Chapter 29 — THREADS: INTRODUCTION

- Chapter locator: `tlpi:29`; `toc-html#search-unit:372`
- **`29.1` Overview** — `tlpi:29.1`; `toc-html#search-unit:373`
- **`29.2` Background Details of the Pthreads API** — `tlpi:29.2`; `toc-html#search-unit:374`
- **`29.3` Thread Creation** — `tlpi:29.3`; `toc-html#search-unit:375`
- **`29.4` Thread Termination** — `tlpi:29.4`; `toc-html#search-unit:376`
- **`29.5` Thread IDs** — `tlpi:29.5`; `toc-html#search-unit:377`
- **`29.6` Joining with a Terminated Thread: pthread_join()** — `tlpi:29.6`; `toc-html#search-unit:378`
- **`29.7` Detaching a Thread: pthread_detach()** — `tlpi:29.7`; `toc-html#search-unit:379`
- **`29.8` Thread Attributes** — `tlpi:29.8`; `toc-html#search-unit:380`
- **`29.9` Threads Versus Processes** — `tlpi:29.9`; `toc-html#search-unit:381`
- **`29.10` Summary** — `tlpi:29.10`; `toc-html#search-unit:382`
- **`29.11` Exercises** — `tlpi:29.11`; `toc-html#search-unit:383`

### Chapter 30 — THREADS: THREAD SYNCHRONIZATION

- Chapter locator: `tlpi:30`; `toc-html#search-unit:384`
- **`30.1` Protecting Accesses to Shared Variables: Mutexes** — `tlpi:30.1`; `toc-html#search-unit:385`
  - `30.1.1` Statically Allocated Mutexes — `tlpi:30.1.1`; `toc-html#search-unit:386`
  - `30.1.2` Locking and Unlocking a Mutex — `tlpi:30.1.2`; `toc-html#search-unit:387`
  - `30.1.3` Performance of Mutexes — `tlpi:30.1.3`; `toc-html#search-unit:388`
  - `30.1.4` Mutex Deadlocks — `tlpi:30.1.4`; `toc-html#search-unit:389`
  - `30.1.5` Dynamically Initializing a Mutex — `tlpi:30.1.5`; `toc-html#search-unit:390`
  - `30.1.6` Mutex Attributes — `tlpi:30.1.6`; `toc-html#search-unit:391`
  - `30.1.7` Mutex Types — `tlpi:30.1.7`; `toc-html#search-unit:392`
- **`30.2` Signaling Changes of State: Condition Variables** — `tlpi:30.2`; `toc-html#search-unit:393`
  - `30.2.1` Statically Allocated Condition Variables — `tlpi:30.2.1`; `toc-html#search-unit:394`
  - `30.2.2` Signaling and Waiting on Condition Variables — `tlpi:30.2.2`; `toc-html#search-unit:395`
  - `30.2.3` Testing a Condition Variable's Predicate — `tlpi:30.2.3`; `toc-html#search-unit:396`
  - `30.2.4` Example Program: Joining Any Terminated Thread — `tlpi:30.2.4`; `toc-html#search-unit:397`
  - `30.2.5` Dynamically Allocated Condition Variables — `tlpi:30.2.5`; `toc-html#search-unit:398`
- **`30.3` Summary** — `tlpi:30.3`; `toc-html#search-unit:399`
- **`30.4` Exercises** — `tlpi:30.4`; `toc-html#search-unit:400`

### Chapter 31 — THREADS: THREAD SAFETY AND PER-THREAD STORAGE

- Chapter locator: `tlpi:31`; `toc-html#search-unit:401`
- **`31.1` Thread Safety (and Reentrancy Revisited)** — `tlpi:31.1`; `toc-html#search-unit:402`
- **`31.2` One-Time Initialization** — `tlpi:31.2`; `toc-html#search-unit:403`
- **`31.3` Thread-Specific Data** — `tlpi:31.3`; `toc-html#search-unit:404`
  - `31.3.1` Thread-Specific Data from the Library Function's Perspective — `tlpi:31.3.1`; `toc-html#search-unit:405`
  - `31.3.2` Overview of the Thread-Specific Data API — `tlpi:31.3.2`; `toc-html#search-unit:406`
  - `31.3.3` Details of the Thread-Specific Data API — `tlpi:31.3.3`; `toc-html#search-unit:407`
  - `31.3.4` Employing the Thread-Specific Data API — `tlpi:31.3.4`; `toc-html#search-unit:408`
  - `31.3.5` Thread-Specific Data Implementation Limits — `tlpi:31.3.5`; `toc-html#search-unit:409`
- **`31.4` Thread-Local Storage** — `tlpi:31.4`; `toc-html#search-unit:410`
- **`31.5` Summary** — `tlpi:31.5`; `toc-html#search-unit:411`
- **`31.6` Exercises** — `tlpi:31.6`; `toc-html#search-unit:412`

### Chapter 32 — THREADS: THREAD CANCELLATION

- Chapter locator: `tlpi:32`; `toc-html#search-unit:413`
- **`32.1` Canceling a Thread** — `tlpi:32.1`; `toc-html#search-unit:414`
- **`32.2` Cancellation State and Type** — `tlpi:32.2`; `toc-html#search-unit:415`
- **`32.3` Cancellation Points** — `tlpi:32.3`; `toc-html#search-unit:416`
- **`32.4` Testing for Thread Cancellation** — `tlpi:32.4`; `toc-html#search-unit:417`
- **`32.5` Cleanup Handlers** — `tlpi:32.5`; `toc-html#search-unit:418`
- **`32.6` Asynchronous Cancelability** — `tlpi:32.6`; `toc-html#search-unit:419`
- **`32.7` Summary** — `tlpi:32.7`; `toc-html#search-unit:420`
- **`32.8` Exercises** — `tlpi:32.8`; `toc-html#search-unit:421`

### Chapter 33 — THREADS: FURTHER DETAILS

- Chapter locator: `tlpi:33`; `toc-html#search-unit:422`
- **`33.1` Thread Stacks** — `tlpi:33.1`; `toc-html#search-unit:423`
- **`33.2` Threads and Signals** — `tlpi:33.2`; `toc-html#search-unit:424`
  - `33.2.1` How the UNIX Signal Model Maps to Threads — `tlpi:33.2.1`; `toc-html#search-unit:425`
  - `33.2.2` Manipulating the Thread Signal Mask — `tlpi:33.2.2`; `toc-html#search-unit:426`
  - `33.2.3` Sending a Signal to a Thread — `tlpi:33.2.3`; `toc-html#search-unit:427`
  - `33.2.4` Dealing with Asynchronous Signals Sanely — `tlpi:33.2.4`; `toc-html#search-unit:428`
- **`33.3` Threads and Process Control** — `tlpi:33.3`; `toc-html#search-unit:429`
- **`33.4` Thread Implementation Models** — `tlpi:33.4`; `toc-html#search-unit:430`
- **`33.5` Linux Implementations of POSIX Threads** — `tlpi:33.5`; `toc-html#search-unit:431`
  - `33.5.1` LinuxThreads — `tlpi:33.5.1`; `toc-html#search-unit:432`
  - `33.5.2` NPTL — `tlpi:33.5.2`; `toc-html#search-unit:433`
  - `33.5.3` Which Threading Implementation? — `tlpi:33.5.3`; `toc-html#search-unit:434`
- **`33.6` Advanced Features of the Pthreads API** — `tlpi:33.6`; `toc-html#search-unit:435`
- **`33.7` Summary** — `tlpi:33.7`; `toc-html#search-unit:436`
- **`33.8` Exercises** — `tlpi:33.8`; `toc-html#search-unit:437`

## Part 5 — Advanced process and program topics

Preface grouping locator: `TLPI-PREFACE-PDF`, `pdf:page:3`.

### Chapter 34 — PROCESS GROUPS, SESSIONS, AND JOB CONTROL

- Chapter locator: `tlpi:34`; `toc-html#search-unit:438`
- **`34.1` Overview** — `tlpi:34.1`; `toc-html#search-unit:439`
- **`34.2` Process Groups** — `tlpi:34.2`; `toc-html#search-unit:440`
- **`34.3` Sessions** — `tlpi:34.3`; `toc-html#search-unit:441`
- **`34.4` Controlling Terminals and Controlling Processes** — `tlpi:34.4`; `toc-html#search-unit:442`
- **`34.5` Foreground and Background Process Groups** — `tlpi:34.5`; `toc-html#search-unit:443`
- **`34.6` The SIGHUP Signal** — `tlpi:34.6`; `toc-html#search-unit:444`
  - `34.6.1` Handling of SIGHUP by the Shell — `tlpi:34.6.1`; `toc-html#search-unit:445`
  - `34.6.2` SIGHUP and Termination of the Controlling Process — `tlpi:34.6.2`; `toc-html#search-unit:446`
- **`34.7` Job Control** — `tlpi:34.7`; `toc-html#search-unit:447`
  - `34.7.1` Using Job Control Within the Shell — `tlpi:34.7.1`; `toc-html#search-unit:448`
  - `34.7.2` Implementing Job Control — `tlpi:34.7.2`; `toc-html#search-unit:449`
  - `34.7.3` Handling Job-Control Signals — `tlpi:34.7.3`; `toc-html#search-unit:450`
  - `34.7.4` Orphaned Process Groups (and SIGHUP Revisited) — `tlpi:34.7.4`; `toc-html#search-unit:451`
- **`34.8` Summary** — `tlpi:34.8`; `toc-html#search-unit:452`
- **`34.9` Exercises** — `tlpi:34.9`; `toc-html#search-unit:453`

### Chapter 35 — PROCESS PRIORITIES AND SCHEDULING

- Chapter locator: `tlpi:35`; `toc-html#search-unit:454`
- **`35.1` Process Priorities (Nice Values)** — `tlpi:35.1`; `toc-html#search-unit:455`
- **`35.2` Overview of Realtime Process Scheduling** — `tlpi:35.2`; `toc-html#search-unit:456`
  - `35.2.1` The SCHED_RR Policy — `tlpi:35.2.1`; `toc-html#search-unit:457`
  - `35.2.2` The SCHED_FIFO Policy — `tlpi:35.2.2`; `toc-html#search-unit:458`
  - `35.2.3` The SCHED_BATCH and SCHED_IDLE Policies — `tlpi:35.2.3`; `toc-html#search-unit:459`
- **`35.3` Realtime Process Scheduling API** — `tlpi:35.3`; `toc-html#search-unit:460`
  - `35.3.1` Realtime Priority Ranges — `tlpi:35.3.1`; `toc-html#search-unit:461`
  - `35.3.2` Modifying and Retrieving Policies and Priorities — `tlpi:35.3.2`; `toc-html#search-unit:462`
  - `35.3.3` Relinquishing the CPU — `tlpi:35.3.3`; `toc-html#search-unit:463`
  - `35.3.4` The SCHED_RR Time Slice — `tlpi:35.3.4`; `toc-html#search-unit:464`
- **`35.4` CPU Affinity** — `tlpi:35.4`; `toc-html#search-unit:465`
- **`35.5` Summary** — `tlpi:35.5`; `toc-html#search-unit:466`
- **`35.6` Exercises** — `tlpi:35.6`; `toc-html#search-unit:467`

### Chapter 36 — PROCESS RESOURCES

- Chapter locator: `tlpi:36`; `toc-html#search-unit:468`
- **`36.1` Process Resource Usage: getrusage()** — `tlpi:36.1`; `toc-html#search-unit:469`
- **`36.2` Process Resource Limits: getrlimit() and setrlimit()** — `tlpi:36.2`; `toc-html#search-unit:470`
- **`36.3` Details of Specific Resource Limits** — `tlpi:36.3`; `toc-html#search-unit:471`
- **`36.4` Summary** — `tlpi:36.4`; `toc-html#search-unit:472`
- **`36.5` Exercises** — `tlpi:36.5`; `toc-html#search-unit:473`

### Chapter 37 — DAEMONS

- Chapter locator: `tlpi:37`; `toc-html#search-unit:474`
- **`37.1` Overview** — `tlpi:37.1`; `toc-html#search-unit:475`
- **`37.2` Creating a Daemon** — `tlpi:37.2`; `toc-html#search-unit:476`
- **`37.3` Guidelines for Writing Daemons** — `tlpi:37.3`; `toc-html#search-unit:477`
- **`37.4` Using SIGHUP to Reinitialize a Daemon** — `tlpi:37.4`; `toc-html#search-unit:478`
- **`37.5` Logging Messages and Errors Using syslog** — `tlpi:37.5`; `toc-html#search-unit:479`
  - `37.5.1` Overview — `tlpi:37.5.1`; `toc-html#search-unit:480`
  - `37.5.2` The syslog API — `tlpi:37.5.2`; `toc-html#search-unit:481`
  - `37.5.3` The /etc/syslog.conf File — `tlpi:37.5.3`; `toc-html#search-unit:482`
- **`37.6` Summary** — `tlpi:37.6`; `toc-html#search-unit:483`
- **`37.7` Exercise** — `tlpi:37.7`; `toc-html#search-unit:484`

### Chapter 38 — WRITING SECURE PRIVILEGED PROGRAMS

- Chapter locator: `tlpi:38`; `toc-html#search-unit:485`
- **`38.1` Is a Set-User-ID or Set-Group-ID Program Required?** — `tlpi:38.1`; `toc-html#search-unit:486`
- **`38.2` Operate with Least Privilege** — `tlpi:38.2`; `toc-html#search-unit:487`
- **`38.3` Be Careful when Executing a Program** — `tlpi:38.3`; `toc-html#search-unit:488`
- **`38.4` Avoid Exposing Sensitive Information** — `tlpi:38.4`; `toc-html#search-unit:489`
- **`38.5` Confine the Process** — `tlpi:38.5`; `toc-html#search-unit:490`
- **`38.6` Beware of Signals and Race Conditions** — `tlpi:38.6`; `toc-html#search-unit:491`
- **`38.7` Pitfalls when Performing File Operations and File I/O** — `tlpi:38.7`; `toc-html#search-unit:492`
- **`38.8` Don't Trust Inputs or the Environment** — `tlpi:38.8`; `toc-html#search-unit:493`
- **`38.9` Beware of Buffer Overruns** — `tlpi:38.9`; `toc-html#search-unit:494`
- **`38.10` Beware of Denial-of-Service Attacks** — `tlpi:38.10`; `toc-html#search-unit:495`
- **`38.11` Check for Failures; Fail Safely** — `tlpi:38.11`; `toc-html#search-unit:496`
- **`38.12` Summary** — `tlpi:38.12`; `toc-html#search-unit:497`
- **`38.13` Exercises** — `tlpi:38.13`; `toc-html#search-unit:498`

### Chapter 39 — CAPABILITIES

- Chapter locator: `tlpi:39`; `toc-html#search-unit:499`
- **`39.1` Rationale for Capabilities** — `tlpi:39.1`; `toc-html#search-unit:500`
- **`39.2` The Linux Capabilities** — `tlpi:39.2`; `toc-html#search-unit:501`
- **`39.3` Process and File Capabilities** — `tlpi:39.3`; `toc-html#search-unit:502`
  - `39.3.1` Process Capabilities — `tlpi:39.3.1`; `toc-html#search-unit:503`
  - `39.3.2` File Capabilities — `tlpi:39.3.2`; `toc-html#search-unit:504`
  - `39.3.3` Purpose of the Process Permitted and Effective Capability Sets — `tlpi:39.3.3`; `toc-html#search-unit:505`
  - `39.3.4` Purpose of the File Permitted and Effective Capability Sets — `tlpi:39.3.4`; `toc-html#search-unit:506`
  - `39.3.5` Purpose of the Process and File Inheritable Sets — `tlpi:39.3.5`; `toc-html#search-unit:507`
  - `39.3.6` Assigning and Viewing File Capabilities from the Shell — `tlpi:39.3.6`; `toc-html#search-unit:508`
- **`39.4` The Modern Capabilities Implementation** — `tlpi:39.4`; `toc-html#search-unit:509`
- **`39.5` Transformation of Process Capabilities During exec()** — `tlpi:39.5`; `toc-html#search-unit:510`
  - `39.5.1` Capability Bounding Set — `tlpi:39.5.1`; `toc-html#search-unit:511`
  - `39.5.2` Preserving root Semantics — `tlpi:39.5.2`; `toc-html#search-unit:512`
- **`39.6` Effect on Process Capabilities of Changing User IDs** — `tlpi:39.6`; `toc-html#search-unit:513`
- **`39.7` Changing Process Capabilities Programmatically** — `tlpi:39.7`; `toc-html#search-unit:514`
- **`39.8` Creating Capabilities-Only Environments** — `tlpi:39.8`; `toc-html#search-unit:515`
- **`39.9` Discovering the Capabilities Required by a Program** — `tlpi:39.9`; `toc-html#search-unit:516`
- **`39.10` Older Kernels and Systems Without File Capabilities** — `tlpi:39.10`; `toc-html#search-unit:517`
- **`39.11` Summary** — `tlpi:39.11`; `toc-html#search-unit:518`
- **`39.12` Exercise** — `tlpi:39.12`; `toc-html#search-unit:519`

### Chapter 40 — LOGIN ACCOUNTING

- Chapter locator: `tlpi:40`; `toc-html#search-unit:520`
- **`40.1` Overview of the utmp and wtmp Files** — `tlpi:40.1`; `toc-html#search-unit:521`
- **`40.2` The utmpx API** — `tlpi:40.2`; `toc-html#search-unit:522`
- **`40.3` The utmpx Structure** — `tlpi:40.3`; `toc-html#search-unit:523`
- **`40.4` Retrieving Information from the utmp and wtmp Files** — `tlpi:40.4`; `toc-html#search-unit:524`
- **`40.5` Retrieving the Login Name: getlogin()** — `tlpi:40.5`; `toc-html#search-unit:525`
- **`40.6` Updating the utmp and wtmp Files for a Login Session** — `tlpi:40.6`; `toc-html#search-unit:526`
- **`40.7` The lastlog File** — `tlpi:40.7`; `toc-html#search-unit:527`
- **`40.8` Summary** — `tlpi:40.8`; `toc-html#search-unit:528`
- **`40.9` Exercises** — `tlpi:40.9`; `toc-html#search-unit:529`

### Chapter 41 — FUNDAMENTALS OF SHARED LIBRARIES

- Chapter locator: `tlpi:41`; `toc-html#search-unit:530`
- **`41.1` Object Libraries** — `tlpi:41.1`; `toc-html#search-unit:531`
- **`41.2` Static Libraries** — `tlpi:41.2`; `toc-html#search-unit:532`
- **`41.3` Overview of Shared Libraries** — `tlpi:41.3`; `toc-html#search-unit:533`
- **`41.4` Creating and Using Shared Libraries—A First Pass** — `tlpi:41.4`; `toc-html#search-unit:534`
  - `41.4.1` Creating a Shared Library — `tlpi:41.4.1`; `toc-html#search-unit:535`
  - `41.4.2` Position-Independent Code — `tlpi:41.4.2`; `toc-html#search-unit:536`
  - `41.4.3` Using a Shared Library — `tlpi:41.4.3`; `toc-html#search-unit:537`
  - `41.4.4` The Shared Library Soname — `tlpi:41.4.4`; `toc-html#search-unit:538`
- **`41.5` Useful Tools for Working with Shared Libraries** — `tlpi:41.5`; `toc-html#search-unit:539`
- **`41.6` Shared Library Versions and Naming Conventions** — `tlpi:41.6`; `toc-html#search-unit:540`
- **`41.7` Installing Shared Libraries** — `tlpi:41.7`; `toc-html#search-unit:541`
- **`41.8` Compatible Versus Incompatible Libraries** — `tlpi:41.8`; `toc-html#search-unit:542`
- **`41.9` Upgrading Shared Libraries** — `tlpi:41.9`; `toc-html#search-unit:543`
- **`41.10` Specifying Library Search Directories in an Object File** — `tlpi:41.10`; `toc-html#search-unit:544`
- **`41.11` Finding Shared Libraries at Run Time** — `tlpi:41.11`; `toc-html#search-unit:545`
- **`41.12` Run-Time Symbol Resolution** — `tlpi:41.12`; `toc-html#search-unit:546`
- **`41.13` Using a Static Library Instead of a Shared Library** — `tlpi:41.13`; `toc-html#search-unit:547`
- **`41.14` Summary** — `tlpi:41.14`; `toc-html#search-unit:548`
- **`41.15` Exercise** — `tlpi:41.15`; `toc-html#search-unit:549`

### Chapter 42 — ADVANCED FEATURES OF SHARED LIBRARIES

- Chapter locator: `tlpi:42`; `toc-html#search-unit:550`
- **`42.1` Dynamically Loaded Libraries** — `tlpi:42.1`; `toc-html#search-unit:551`
  - `42.1.1` Opening a Shared Library — `tlpi:42.1.1`; `toc-html#search-unit:552`
  - `42.1.2` Diagnosing Errors from the dlopen API — `tlpi:42.1.2`; `toc-html#search-unit:553`
  - `42.1.3` Obtaining the Address of a Symbol: dlsym() — `tlpi:42.1.3`; `toc-html#search-unit:554`
  - `42.1.4` Closing a Shared Library: dlclose() — `tlpi:42.1.4`; `toc-html#search-unit:555`
  - `42.1.5` Obtaining Information About Loaded Symbols: dladdr() — `tlpi:42.1.5`; `toc-html#search-unit:556`
  - `42.1.6` Accessing Symbols in the Main Program — `tlpi:42.1.6`; `toc-html#search-unit:557`
- **`42.2` Controlling Symbol Visibility** — `tlpi:42.2`; `toc-html#search-unit:558`
- **`42.3` Linker Version Scripts** — `tlpi:42.3`; `toc-html#search-unit:559`
  - `42.3.1` Controlling Symbol Visibility with Version Scripts — `tlpi:42.3.1`; `toc-html#search-unit:560`
  - `42.3.2` Symbol Versioning — `tlpi:42.3.2`; `toc-html#search-unit:561`
- **`42.4` Initialization and Finalization Functions** — `tlpi:42.4`; `toc-html#search-unit:562`
- **`42.5` Preloading Shared Libraries** — `tlpi:42.5`; `toc-html#search-unit:563`
- **`42.6` Monitoring the Dynamic Linker: LD_DEBUG** — `tlpi:42.6`; `toc-html#search-unit:564`
- **`42.7` Summary** — `tlpi:42.7`; `toc-html#search-unit:565`
- **`42.8` Exercises** — `tlpi:42.8`; `toc-html#search-unit:566`

## Part 6 — Interprocess communication (IPC)

Preface grouping locator: `TLPI-PREFACE-PDF`, `pdf:page:3`.

### Chapter 43 — INTERPROCESS COMMUNICATION OVERVIEW

- Chapter locator: `tlpi:43`; `toc-html#search-unit:567`
- **`43.1` A Taxonomy of IPC Facilities** — `tlpi:43.1`; `toc-html#search-unit:568`
- **`43.2` Communication Facilities** — `tlpi:43.2`; `toc-html#search-unit:569`
- **`43.3` Synchronization Facilities** — `tlpi:43.3`; `toc-html#search-unit:570`
- **`43.4` Comparing IPC Facilities** — `tlpi:43.4`; `toc-html#search-unit:571`
- **`43.5` Summary** — `tlpi:43.5`; `toc-html#search-unit:572`
- **`43.6` Exercises** — `tlpi:43.6`; `toc-html#search-unit:573`

### Chapter 44 — PIPES AND FIFOS

- Chapter locator: `tlpi:44`; `toc-html#search-unit:574`
- **`44.1` Overview** — `tlpi:44.1`; `toc-html#search-unit:575`
- **`44.2` Creating and Using Pipes** — `tlpi:44.2`; `toc-html#search-unit:576`
- **`44.3` Pipes As a Method of Process Synchronization** — `tlpi:44.3`; `toc-html#search-unit:577`
- **`44.4` Using Pipes to Connect Filters** — `tlpi:44.4`; `toc-html#search-unit:578`
- **`44.5` Talking to a Shell Command via a Pipe: popen() and pclose()** — `tlpi:44.5`; `toc-html#search-unit:579`
- **`44.6` Pipes and stdio Buffering** — `tlpi:44.6`; `toc-html#search-unit:580`
- **`44.7` FIFOs** — `tlpi:44.7`; `toc-html#search-unit:581`
- **`44.8` A Client-Server Application Using FIFOs** — `tlpi:44.8`; `toc-html#search-unit:582`
- **`44.9` Nonblocking I/O** — `tlpi:44.9`; `toc-html#search-unit:583`
- **`44.10` Semantics of read() and write() on Pipes and FIFOs** — `tlpi:44.10`; `toc-html#search-unit:584`
- **`44.11` Summary** — `tlpi:44.11`; `toc-html#search-unit:585`
- **`44.12` Exercises** — `tlpi:44.12`; `toc-html#search-unit:586`

### Chapter 45 — INTRODUCTION TO SYSTEM V IPC

- Chapter locator: `tlpi:45`; `toc-html#search-unit:587`
- **`45.1` API Overview** — `tlpi:45.1`; `toc-html#search-unit:588`
- **`45.2` IPC Keys** — `tlpi:45.2`; `toc-html#search-unit:589`
- **`45.3` Associated Data Structure and Object Permissions** — `tlpi:45.3`; `toc-html#search-unit:590`
- **`45.4` IPC Identifiers and Client-Server Applications** — `tlpi:45.4`; `toc-html#search-unit:591`
- **`45.5` Algorithm Employed by System V IPC get Calls** — `tlpi:45.5`; `toc-html#search-unit:592`
- **`45.6` The ipcs and ipcrm Commands** — `tlpi:45.6`; `toc-html#search-unit:593`
- **`45.7` Obtaining a List of All IPC Objects** — `tlpi:45.7`; `toc-html#search-unit:594`
- **`45.8` IPC Limits** — `tlpi:45.8`; `toc-html#search-unit:595`
- **`45.9` Summary** — `tlpi:45.9`; `toc-html#search-unit:596`
- **`45.10` Exercises** — `tlpi:45.10`; `toc-html#search-unit:597`

### Chapter 46 — SYSTEM V MESSAGE QUEUES

- Chapter locator: `tlpi:46`; `toc-html#search-unit:598`
- **`46.1` Creating or Opening a Message Queue: msgget()** — `tlpi:46.1`; `toc-html#search-unit:599`
- **`46.2` Exchanging Messages** — `tlpi:46.2`; `toc-html#search-unit:600`
  - `46.2.1` Sending Messages: msgsnd() — `tlpi:46.2.1`; `toc-html#search-unit:601`
  - `46.2.2` Receiving Messages: msgrcv() — `tlpi:46.2.2`; `toc-html#search-unit:602`
- **`46.3` Message Queue Control Operations: msgctl()** — `tlpi:46.3`; `toc-html#search-unit:603`
- **`46.4` Message Queue Associated Data Structure** — `tlpi:46.4`; `toc-html#search-unit:604`
- **`46.5` Message Queue Limits** — `tlpi:46.5`; `toc-html#search-unit:605`
- **`46.6` Displaying All Message Queues on the System** — `tlpi:46.6`; `toc-html#search-unit:606`
- **`46.7` Client-Server Programming with Message Queues** — `tlpi:46.7`; `toc-html#search-unit:607`
- **`46.8` A File-Server Application Using Message Queues** — `tlpi:46.8`; `toc-html#search-unit:608`
- **`46.9` Disadvantages of System V Message Queues** — `tlpi:46.9`; `toc-html#search-unit:609`
- **`46.10` Summary** — `tlpi:46.10`; `toc-html#search-unit:610`
- **`46.11` Exercises** — `tlpi:46.11`; `toc-html#search-unit:611`

### Chapter 47 — SYSTEM V SEMAPHORES

- Chapter locator: `tlpi:47`; `toc-html#search-unit:612`
- **`47.1` Overview** — `tlpi:47.1`; `toc-html#search-unit:613`
- **`47.2` Creating or Opening a Semaphore Set: semget()** — `tlpi:47.2`; `toc-html#search-unit:614`
- **`47.3` Semaphore Control Operations: semctl()** — `tlpi:47.3`; `toc-html#search-unit:615`
- **`47.4` Semaphore Associated Data Structure** — `tlpi:47.4`; `toc-html#search-unit:616`
- **`47.5` Semaphore Initialization** — `tlpi:47.5`; `toc-html#search-unit:617`
- **`47.6` Semaphore Operations: semop()** — `tlpi:47.6`; `toc-html#search-unit:618`
- **`47.7` Handling of Multiple Blocked Semaphore Operations** — `tlpi:47.7`; `toc-html#search-unit:619`
- **`47.8` Semaphore Undo Values** — `tlpi:47.8`; `toc-html#search-unit:620`
- **`47.9` Implementing a Binary Semaphores Protocol** — `tlpi:47.9`; `toc-html#search-unit:621`
- **`47.10` Semaphore Limits** — `tlpi:47.10`; `toc-html#search-unit:622`
- **`47.11` Disadvantages of System V Semaphores** — `tlpi:47.11`; `toc-html#search-unit:623`
- **`47.12` Summary** — `tlpi:47.12`; `toc-html#search-unit:624`
- **`47.13` Exercises** — `tlpi:47.13`; `toc-html#search-unit:625`

### Chapter 48 — SYSTEM V SHARED MEMORY

- Chapter locator: `tlpi:48`; `toc-html#search-unit:626`
- **`48.1` Overview** — `tlpi:48.1`; `toc-html#search-unit:627`
- **`48.2` Creating or Opening a Shared Memory Segment: shmget()** — `tlpi:48.2`; `toc-html#search-unit:628`
- **`48.3` Using Shared Memory: shmat() and shmdt()** — `tlpi:48.3`; `toc-html#search-unit:629`
- **`48.4` Example: Transferring Data Via Shared Memory** — `tlpi:48.4`; `toc-html#search-unit:630`
- **`48.5` Location of Shared Memory Segments in Virtual Memory** — `tlpi:48.5`; `toc-html#search-unit:631`
- **`48.6` Storing Pointers in Shared Memory** — `tlpi:48.6`; `toc-html#search-unit:632`
- **`48.7` Shared Memory Control Operations: shmctl()** — `tlpi:48.7`; `toc-html#search-unit:633`
- **`48.8` Shared Memory Associated Data Structure** — `tlpi:48.8`; `toc-html#search-unit:634`
- **`48.9` Shared Memory Limits** — `tlpi:48.9`; `toc-html#search-unit:635`
- **`48.10` Summary** — `tlpi:48.10`; `toc-html#search-unit:636`
- **`48.11` Exercises** — `tlpi:48.11`; `toc-html#search-unit:637`

### Chapter 49 — MEMORY MAPPINGS

- Chapter locator: `tlpi:49`; `toc-html#search-unit:638`
- **`49.1` Overview** — `tlpi:49.1`; `toc-html#search-unit:639`
- **`49.2` Creating a Mapping: mmap()** — `tlpi:49.2`; `toc-html#search-unit:640`
- **`49.3` Unmapping a Mapped Region: munmap()** — `tlpi:49.3`; `toc-html#search-unit:641`
- **`49.4` File Mappings** — `tlpi:49.4`; `toc-html#search-unit:642`
  - `49.4.1` Private File Mappings — `tlpi:49.4.1`; `toc-html#search-unit:643`
  - `49.4.2` Shared File Mappings — `tlpi:49.4.2`; `toc-html#search-unit:644`
  - `49.4.3` Boundary Cases — `tlpi:49.4.3`; `toc-html#search-unit:645`
  - `49.4.4` Memory Protection and File Access Mode Interactions — `tlpi:49.4.4`; `toc-html#search-unit:646`
- **`49.5` Synchronizing a Mapped Region: msync()** — `tlpi:49.5`; `toc-html#search-unit:647`
- **`49.6` Additional mmap() Flags** — `tlpi:49.6`; `toc-html#search-unit:648`
- **`49.7` Anonymous Mappings** — `tlpi:49.7`; `toc-html#search-unit:649`
- **`49.8` Remapping a Mapped Region: mremap()** — `tlpi:49.8`; `toc-html#search-unit:650`
- **`49.9` The MAP_NORESERVE Flag and Swap Space Overcommitting** — `tlpi:49.9`; `toc-html#search-unit:651`
- **`49.10` The MAP_FIXED Flag** — `tlpi:49.10`; `toc-html#search-unit:652`
- **`49.11` Nonlinear Mappings: remap_file_pages()** — `tlpi:49.11`; `toc-html#search-unit:653`
- **`49.12` Summary** — `tlpi:49.12`; `toc-html#search-unit:654`
- **`49.13` Exercises** — `tlpi:49.13`; `toc-html#search-unit:655`

### Chapter 50 — VIRTUAL MEMORY OPERATIONS

- Chapter locator: `tlpi:50`; `toc-html#search-unit:656`
- **`50.1` Changing Memory Protection: mprotect()** — `tlpi:50.1`; `toc-html#search-unit:657`
- **`50.2` Memory Locking: mlock() and mlockall()** — `tlpi:50.2`; `toc-html#search-unit:658`
- **`50.3` Determining Memory Residence: mincore()** — `tlpi:50.3`; `toc-html#search-unit:659`
- **`50.4` Advising Future Memory Usage Patterns: madvise()** — `tlpi:50.4`; `toc-html#search-unit:660`
- **`50.5` Summary** — `tlpi:50.5`; `toc-html#search-unit:661`
- **`50.6` Exercises** — `tlpi:50.6`; `toc-html#search-unit:662`

### Chapter 51 — INTRODUCTION TO POSIX IPC

- Chapter locator: `tlpi:51`; `toc-html#search-unit:663`
- **`51.1` API Overview** — `tlpi:51.1`; `toc-html#search-unit:664`
- **`51.2` Comparison of System V IPC and POSIX IPC** — `tlpi:51.2`; `toc-html#search-unit:665`
- **`51.3` Summary** — `tlpi:51.3`; `toc-html#search-unit:666`

### Chapter 52 — POSIX MESSAGE QUEUES

- Chapter locator: `tlpi:52`; `toc-html#search-unit:667`
- **`52.1` Overview** — `tlpi:52.1`; `toc-html#search-unit:668`
- **`52.2` Opening, Closing, and Unlinking a Message Queue** — `tlpi:52.2`; `toc-html#search-unit:669`
- **`52.3` Relationship Between Descriptors and Message Queues** — `tlpi:52.3`; `toc-html#search-unit:670`
- **`52.4` Message Queue Attributes** — `tlpi:52.4`; `toc-html#search-unit:671`
- **`52.5` Exchanging Messages** — `tlpi:52.5`; `toc-html#search-unit:672`
  - `52.5.1` Sending Messages: mq_send() — `tlpi:52.5.1`; `toc-html#search-unit:673`
  - `52.5.2` Receiving Messages: mq_receive() — `tlpi:52.5.2`; `toc-html#search-unit:674`
  - `52.5.3` Sending and Receiving Messages with a Timeout — `tlpi:52.5.3`; `toc-html#search-unit:675`
- **`52.6` Message Notification** — `tlpi:52.6`; `toc-html#search-unit:676`
  - `52.6.1` Receiving Notification via a Signal — `tlpi:52.6.1`; `toc-html#search-unit:677`
  - `52.6.2` Receiving Notification via a Thread — `tlpi:52.6.2`; `toc-html#search-unit:678`
- **`52.7` Linux-Specific Features** — `tlpi:52.7`; `toc-html#search-unit:679`
- **`52.8` Message Queue Limits** — `tlpi:52.8`; `toc-html#search-unit:680`
- **`52.9` Comparison of POSIX and System V Message Queues** — `tlpi:52.9`; `toc-html#search-unit:681`
- **`52.10` Summary** — `tlpi:52.10`; `toc-html#search-unit:682`
- **`52.11` Exercises** — `tlpi:52.11`; `toc-html#search-unit:683`

### Chapter 53 — POSIX SEMAPHORES

- Chapter locator: `tlpi:53`; `toc-html#search-unit:684`
- **`53.1` Overview** — `tlpi:53.1`; `toc-html#search-unit:685`
- **`53.2` Named Semaphores** — `tlpi:53.2`; `toc-html#search-unit:686`
  - `53.2.1` Opening a Named Semaphore — `tlpi:53.2.1`; `toc-html#search-unit:687`
  - `53.2.2` Closing a Semaphore — `tlpi:53.2.2`; `toc-html#search-unit:688`
  - `53.2.3` Removing a Named Semaphore — `tlpi:53.2.3`; `toc-html#search-unit:689`
- **`53.3` Semaphore Operations** — `tlpi:53.3`; `toc-html#search-unit:690`
  - `53.3.1` Waiting on a Semaphore — `tlpi:53.3.1`; `toc-html#search-unit:691`
  - `53.3.2` Posting a Semaphore — `tlpi:53.3.2`; `toc-html#search-unit:692`
  - `53.3.3` Retrieving the Current Value of a Semaphore — `tlpi:53.3.3`; `toc-html#search-unit:693`
- **`53.4` Unnamed Semaphores** — `tlpi:53.4`; `toc-html#search-unit:694`
  - `53.4.1` Initializing an Unnamed Semaphore — `tlpi:53.4.1`; `toc-html#search-unit:695`
  - `53.4.2` Destroying an Unnamed Semaphore — `tlpi:53.4.2`; `toc-html#search-unit:696`
- **`53.5` Comparisons with Other Synchronization Techniques** — `tlpi:53.5`; `toc-html#search-unit:697`
- **`53.6` Semaphore Limits** — `tlpi:53.6`; `toc-html#search-unit:698`
- **`53.7` Summary** — `tlpi:53.7`; `toc-html#search-unit:699`
- **`53.8` Exercises** — `tlpi:53.8`; `toc-html#search-unit:700`

### Chapter 54 — POSIX SHARED MEMORY

- Chapter locator: `tlpi:54`; `toc-html#search-unit:701`
- **`54.1` Overview** — `tlpi:54.1`; `toc-html#search-unit:702`
- **`54.2` Creating Shared Memory Objects: shm_open()** — `tlpi:54.2`; `toc-html#search-unit:703`
- **`54.3` Using Shared Memory Objects** — `tlpi:54.3`; `toc-html#search-unit:704`
- **`54.4` Removing Shared Memory Objects: shm_unlink()** — `tlpi:54.4`; `toc-html#search-unit:705`
- **`54.5` Comparisons Between Shared Memory APIs** — `tlpi:54.5`; `toc-html#search-unit:706`
- **`54.6` Summary** — `tlpi:54.6`; `toc-html#search-unit:707`
- **`54.7` Exercise** — `tlpi:54.7`; `toc-html#search-unit:708`

### Chapter 55 — FILE LOCKING

- Chapter locator: `tlpi:55`; `toc-html#search-unit:709`
- **`55.1` Overview** — `tlpi:55.1`; `toc-html#search-unit:710`
- **`55.2` File Locking with flock()** — `tlpi:55.2`; `toc-html#search-unit:711`
  - `55.2.1` Semantics of Lock Inheritance and Release — `tlpi:55.2.1`; `toc-html#search-unit:712`
  - `55.2.2` Limitations of flock() — `tlpi:55.2.2`; `toc-html#search-unit:713`
- **`55.3` Record Locking with fcntl()** — `tlpi:55.3`; `toc-html#search-unit:714`
  - `55.3.1` Deadlock — `tlpi:55.3.1`; `toc-html#search-unit:715`
  - `55.3.2` Example: An Interactive Locking Program — `tlpi:55.3.2`; `toc-html#search-unit:716`
  - `55.3.3` Example: A Library of Locking Functions — `tlpi:55.3.3`; `toc-html#search-unit:717`
  - `55.3.4` Lock Limits and Performance — `tlpi:55.3.4`; `toc-html#search-unit:718`
  - `55.3.5` Semantics of Lock Inheritance and Release — `tlpi:55.3.5`; `toc-html#search-unit:719`
  - `55.3.6` Lock Starvation and Priority of Queued Lock Requests — `tlpi:55.3.6`; `toc-html#search-unit:720`
- **`55.4` Mandatory Locking** — `tlpi:55.4`; `toc-html#search-unit:721`
- **`55.5` The /proc/locks File** — `tlpi:55.5`; `toc-html#search-unit:722`
- **`55.6` Running Just One Instance of a Program** — `tlpi:55.6`; `toc-html#search-unit:723`
- **`55.7` Older Locking Techniques** — `tlpi:55.7`; `toc-html#search-unit:724`
- **`55.8` Summary** — `tlpi:55.8`; `toc-html#search-unit:725`
- **`55.9` Exercises** — `tlpi:55.9`; `toc-html#search-unit:726`

## Part 7 — Sockets and network programming

Preface grouping locator: `TLPI-PREFACE-PDF`, `pdf:page:4`.

### Chapter 56 — SOCKETS: INTRODUCTION

- Chapter locator: `tlpi:56`; `toc-html#search-unit:727`
- **`56.1` Overview** — `tlpi:56.1`; `toc-html#search-unit:728`
- **`56.2` Creating a Socket: socket()** — `tlpi:56.2`; `toc-html#search-unit:729`
- **`56.3` Binding a Socket to an Address: bind()** — `tlpi:56.3`; `toc-html#search-unit:730`
- **`56.4` Generic Socket Address Structures: struct sockaddr** — `tlpi:56.4`; `toc-html#search-unit:731`
- **`56.5` Stream Sockets** — `tlpi:56.5`; `toc-html#search-unit:732`
  - `56.5.1` Listening for Incoming Connections: listen() — `tlpi:56.5.1`; `toc-html#search-unit:733`
  - `56.5.2` Accepting a Connection: accept() — `tlpi:56.5.2`; `toc-html#search-unit:734`
  - `56.5.3` Connecting to a Peer Socket: connect() — `tlpi:56.5.3`; `toc-html#search-unit:735`
  - `56.5.4` I/O on Stream Sockets — `tlpi:56.5.4`; `toc-html#search-unit:736`
  - `56.5.5` Connection Termination: close() — `tlpi:56.5.5`; `toc-html#search-unit:737`
- **`56.6` Datagram Sockets** — `tlpi:56.6`; `toc-html#search-unit:738`
  - `56.6.1` Exchanging Datagrams: recvfrom() and sendto() — `tlpi:56.6.1`; `toc-html#search-unit:739`
  - `56.6.2` Using connect() with Datagram Sockets — `tlpi:56.6.2`; `toc-html#search-unit:740`
- **`56.7` Summary** — `tlpi:56.7`; `toc-html#search-unit:741`

### Chapter 57 — SOCKETS: UNIX DOMAIN

- Chapter locator: `tlpi:57`; `toc-html#search-unit:742`
- **`57.1` UNIX Domain Socket Addresses: struct sockaddr_un** — `tlpi:57.1`; `toc-html#search-unit:743`
- **`57.2` Stream Sockets in the UNIX Domain** — `tlpi:57.2`; `toc-html#search-unit:744`
- **`57.3` Datagram Sockets in the UNIX Domain** — `tlpi:57.3`; `toc-html#search-unit:745`
- **`57.4` UNIX Domain Socket Permissions** — `tlpi:57.4`; `toc-html#search-unit:746`
- **`57.5` Creating a Connected Socket Pair: socketpair()** — `tlpi:57.5`; `toc-html#search-unit:747`
- **`57.6` The Linux Abstract Socket Namespace** — `tlpi:57.6`; `toc-html#search-unit:748`
- **`57.7` Summary** — `tlpi:57.7`; `toc-html#search-unit:749`
- **`57.8` Exercises** — `tlpi:57.8`; `toc-html#search-unit:750`

### Chapter 58 — SOCKETS: FUNDAMENTALS OF TCP/IP NETWORKS

- Chapter locator: `tlpi:58`; `toc-html#search-unit:751`
- **`58.1` Internets** — `tlpi:58.1`; `toc-html#search-unit:752`
- **`58.2` Networking Protocols and Layers** — `tlpi:58.2`; `toc-html#search-unit:753`
- **`58.3` The Data-Link Layer** — `tlpi:58.3`; `toc-html#search-unit:754`
- **`58.4` The Network Layer: IP** — `tlpi:58.4`; `toc-html#search-unit:755`
- **`58.5` IP Addresses** — `tlpi:58.5`; `toc-html#search-unit:756`
- **`58.6` The Transport Layer** — `tlpi:58.6`; `toc-html#search-unit:757`
  - `58.6.1` Port Numbers — `tlpi:58.6.1`; `toc-html#search-unit:758`
  - `58.6.2` User Datagram Protocol (UDP) — `tlpi:58.6.2`; `toc-html#search-unit:759`
  - `58.6.3` Transmission Control Protocol (TCP) — `tlpi:58.6.3`; `toc-html#search-unit:760`
- **`58.7` Requests for Comments (RFCs)** — `tlpi:58.7`; `toc-html#search-unit:761`
- **`58.8` Summary** — `tlpi:58.8`; `toc-html#search-unit:762`

### Chapter 59 — SOCKETS: INTERNET DOMAINS

- Chapter locator: `tlpi:59`; `toc-html#search-unit:763`
- **`59.1` Internet Domain Sockets** — `tlpi:59.1`; `toc-html#search-unit:764`
- **`59.2` Network Byte Order** — `tlpi:59.2`; `toc-html#search-unit:765`
- **`59.3` Data Representation** — `tlpi:59.3`; `toc-html#search-unit:766`
- **`59.4` Internet Socket Addresses** — `tlpi:59.4`; `toc-html#search-unit:767`
- **`59.5` Overview of Host and Service Conversion Functions** — `tlpi:59.5`; `toc-html#search-unit:768`
- **`59.6` IPv6 and IPv4 Address Conversion: inet_pton() and inet_ntop()** — `tlpi:59.6`; `toc-html#search-unit:769`
- **`59.7` Client-Server Example (Datagram Sockets)** — `tlpi:59.7`; `toc-html#search-unit:770`
- **`59.8` Domain Name System (DNS)** — `tlpi:59.8`; `toc-html#search-unit:771`
- **`59.9` The /etc/services File** — `tlpi:59.9`; `toc-html#search-unit:772`
- **`59.10` Protocol-Independent Host and Service Conversion** — `tlpi:59.10`; `toc-html#search-unit:773`
  - `59.10.1` The getaddrinfo() Function — `tlpi:59.10.1`; `toc-html#search-unit:774`
  - `59.10.2` Freeing addrinfo Lists: freeaddrinfo() — `tlpi:59.10.2`; `toc-html#search-unit:775`
  - `59.10.3` Diagnosing Errors: gai_strerror() — `tlpi:59.10.3`; `toc-html#search-unit:776`
  - `59.10.4` The getnameinfo() Function — `tlpi:59.10.4`; `toc-html#search-unit:777`
- **`59.11` Client-Server Example (Stream Sockets)** — `tlpi:59.11`; `toc-html#search-unit:778`
- **`59.12` An Internet Domain Sockets Library** — `tlpi:59.12`; `toc-html#search-unit:779`
- **`59.13` Obsolete APIs for Host, Service, and Address Conversion** — `tlpi:59.13`; `toc-html#search-unit:780`
  - `59.13.1` The inet_ aton() and inet_ ntoa() Functions — `tlpi:59.13.1`; `toc-html#search-unit:781`
  - `59.13.2` The gethostbyname() and gethostbyaddr() Functions — `tlpi:59.13.2`; `toc-html#search-unit:782`
  - `59.13.3` The getservbyname() and getservbyport() Functions — `tlpi:59.13.3`; `toc-html#search-unit:783`
- **`59.14` UNIX Versus Internet Domain Sockets** — `tlpi:59.14`; `toc-html#search-unit:784`
- **`59.15` Further Information** — `tlpi:59.15`; `toc-html#search-unit:785`
- **`59.16` Summary** — `tlpi:59.16`; `toc-html#search-unit:786`
- **`59.17` Exercises** — `tlpi:59.17`; `toc-html#search-unit:787`

### Chapter 60 — SOCKETS: SERVER DESIGN

- Chapter locator: `tlpi:60`; `toc-html#search-unit:788`
- **`60.1` Iterative and Concurrent Servers** — `tlpi:60.1`; `toc-html#search-unit:789`
- **`60.2` An Iterative UDP echo Server** — `tlpi:60.2`; `toc-html#search-unit:790`
- **`60.3` A Concurrent TCP echo Server** — `tlpi:60.3`; `toc-html#search-unit:791`
- **`60.4` Other Concurrent Server Designs** — `tlpi:60.4`; `toc-html#search-unit:792`
- **`60.5` The inetd (Internet Superserver) Daemon** — `tlpi:60.5`; `toc-html#search-unit:793`
- **`60.6` Summary** — `tlpi:60.6`; `toc-html#search-unit:794`
- **`60.7` Exercises** — `tlpi:60.7`; `toc-html#search-unit:795`

### Chapter 61 — SOCKETS: ADVANCED TOPICS

- Chapter locator: `tlpi:61`; `toc-html#search-unit:796`
- **`61.1` Partial Reads and Writes on Stream Sockets** — `tlpi:61.1`; `toc-html#search-unit:797`
- **`61.2` The shutdown() system call** — `tlpi:61.2`; `toc-html#search-unit:798`
- **`61.3` Socket-Specific I/O System Calls: recv() and send()** — `tlpi:61.3`; `toc-html#search-unit:799`
- **`61.4` The sendfile() System Call** — `tlpi:61.4`; `toc-html#search-unit:800`
- **`61.5` Retrieving Socket Addresses: getsockname() and getpeername()** — `tlpi:61.5`; `toc-html#search-unit:801`
- **`61.6` A Closer Look at TCP** — `tlpi:61.6`; `toc-html#search-unit:802`
  - `61.6.1` Format of a TCP Segment — `tlpi:61.6.1`; `toc-html#search-unit:803`
  - `61.6.2` TCP Sequence Numbers and Acknowledgements — `tlpi:61.6.2`; `toc-html#search-unit:804`
  - `61.6.3` TCP State Machine and State Transition Diagram — `tlpi:61.6.3`; `toc-html#search-unit:805`
  - `61.6.4` TCP Connection Establishment — `tlpi:61.6.4`; `toc-html#search-unit:806`
  - `61.6.5` TCP Connection Termination — `tlpi:61.6.5`; `toc-html#search-unit:807`
  - `61.6.6` Calling shutdown() on a TCP Socket — `tlpi:61.6.6`; `toc-html#search-unit:808`
  - `61.6.7` The TIME_WAIT State — `tlpi:61.6.7`; `toc-html#search-unit:809`
- **`61.7` Monitoring Sockets: netstat** — `tlpi:61.7`; `toc-html#search-unit:810`
- **`61.8` Using tcpdump to Monitor TCP Traffic** — `tlpi:61.8`; `toc-html#search-unit:811`
- **`61.9` Socket Options: setsockopt() and getsockopt()** — `tlpi:61.9`; `toc-html#search-unit:812`
- **`61.10` The SO_REUSEADDR Socket Option** — `tlpi:61.10`; `toc-html#search-unit:813`
- **`61.11` Inheritance of File Flags and Socket Options across accept()** — `tlpi:61.11`; `toc-html#search-unit:814`
- **`61.12` TCP Versus UDP** — `tlpi:61.12`; `toc-html#search-unit:815`
- **`61.13` Advanced Features** — `tlpi:61.13`; `toc-html#search-unit:816`
  - `61.13.1` Out-of-Band Data — `tlpi:61.13.1`; `toc-html#search-unit:817`
  - `61.13.2` The sendmsg() and recvmsg() System Calls — `tlpi:61.13.2`; `toc-html#search-unit:818`
  - `61.13.3` Passing File Descriptors — `tlpi:61.13.3`; `toc-html#search-unit:819`
  - `61.13.4` Receiving Sender Credentials — `tlpi:61.13.4`; `toc-html#search-unit:820`
  - `61.13.5` Sequenced-Packet Sockets — `tlpi:61.13.5`; `toc-html#search-unit:821`
  - `61.13.6` SCTP and DCCP Transport-Layer Protocols — `tlpi:61.13.6`; `toc-html#search-unit:822`
- **`61.14` Summary** — `tlpi:61.14`; `toc-html#search-unit:823`
- **`61.15` Exercises** — `tlpi:61.15`; `toc-html#search-unit:824`

## Part 8 — Advanced I/O topics

Preface grouping locator: `TLPI-PREFACE-PDF`, `pdf:page:4`.

### Chapter 62 — TERMINALS

- Chapter locator: `tlpi:62`; `toc-html#search-unit:825`
- **`62.1` Overview** — `tlpi:62.1`; `toc-html#search-unit:826`
- **`62.2` Retrieving and Modifying Terminal Attributes** — `tlpi:62.2`; `toc-html#search-unit:827`
- **`62.3` The stty Command** — `tlpi:62.3`; `toc-html#search-unit:828`
- **`62.4` Terminal Special Characters** — `tlpi:62.4`; `toc-html#search-unit:829`
- **`62.5` Terminal Flags** — `tlpi:62.5`; `toc-html#search-unit:830`
- **`62.6` Terminal I/O Modes** — `tlpi:62.6`; `toc-html#search-unit:831`
  - `62.6.1` Canonical Mode — `tlpi:62.6.1`; `toc-html#search-unit:832`
  - `62.6.2` Noncanonical Mode — `tlpi:62.6.2`; `toc-html#search-unit:833`
  - `62.6.3` Cooked, Cbreak, and Raw Modes — `tlpi:62.6.3`; `toc-html#search-unit:834`
- **`62.7` Terminal Line Speed (Bit Rate)** — `tlpi:62.7`; `toc-html#search-unit:835`
- **`62.8` Terminal Line Control** — `tlpi:62.8`; `toc-html#search-unit:836`
- **`62.9` Terminal Window Size** — `tlpi:62.9`; `toc-html#search-unit:837`
- **`62.10` Terminal Identification** — `tlpi:62.10`; `toc-html#search-unit:838`
- **`62.11` Summary** — `tlpi:62.11`; `toc-html#search-unit:839`
- **`62.12` Exercises** — `tlpi:62.12`; `toc-html#search-unit:840`

### Chapter 63 — ALTERNATIVE I/O MODELS

- Chapter locator: `tlpi:63`; `toc-html#search-unit:841`
- **`63.1` Overview** — `tlpi:63.1`; `toc-html#search-unit:842`
  - `63.1.1` Level-Triggered and Edge-Triggered Notification — `tlpi:63.1.1`; `toc-html#search-unit:843`
  - `63.1.2` Employing Nonblocking I/O with Alternative I/O Models — `tlpi:63.1.2`; `toc-html#search-unit:844`
- **`63.2` I/O Multiplexing** — `tlpi:63.2`; `toc-html#search-unit:845`
  - `63.2.1` The select() System Call — `tlpi:63.2.1`; `toc-html#search-unit:846`
  - `63.2.2` The poll() System Call — `tlpi:63.2.2`; `toc-html#search-unit:847`
  - `63.2.3` When Is a File Descriptor Ready? — `tlpi:63.2.3`; `toc-html#search-unit:848`
  - `63.2.4` Comparison of select() and poll() — `tlpi:63.2.4`; `toc-html#search-unit:849`
  - `63.2.5` Problems with select() and poll() — `tlpi:63.2.5`; `toc-html#search-unit:850`
- **`63.3` Signal-Driven I/O** — `tlpi:63.3`; `toc-html#search-unit:851`
  - `63.3.1` When Is "I/O Possible" Signaled? — `tlpi:63.3.1`; `toc-html#search-unit:852`
  - `63.3.2` Refining the Use of Signal-Driven I/O — `tlpi:63.3.2`; `toc-html#search-unit:853`
- **`63.4` The epoll API** — `tlpi:63.4`; `toc-html#search-unit:854`
  - `63.4.1` Creating an epoll Instance: epoll_create() — `tlpi:63.4.1`; `toc-html#search-unit:855`
  - `63.4.2` Modifying the epoll Interest List: epoll_ctl() — `tlpi:63.4.2`; `toc-html#search-unit:856`
  - `63.4.3` Waiting for Events: epoll_wait() — `tlpi:63.4.3`; `toc-html#search-unit:857`
  - `63.4.4` A Closer Look at epoll Semantics — `tlpi:63.4.4`; `toc-html#search-unit:858`
  - `63.4.5` Performance of epoll Versus I/O Multiplexing — `tlpi:63.4.5`; `toc-html#search-unit:859`
  - `63.4.6` Edge-Triggered Notification — `tlpi:63.4.6`; `toc-html#search-unit:860`
- **`63.5` Waiting on Signals and File Descriptors** — `tlpi:63.5`; `toc-html#search-unit:861`
  - `63.5.1` The pselect() System Call — `tlpi:63.5.1`; `toc-html#search-unit:862`
  - `63.5.2` The Self-Pipe Trick — `tlpi:63.5.2`; `toc-html#search-unit:863`
- **`63.6` Summary** — `tlpi:63.6`; `toc-html#search-unit:864`
- **`63.7` Exercises** — `tlpi:63.7`; `toc-html#search-unit:865`

### Chapter 64 — PSEUDOTERMINALS

- Chapter locator: `tlpi:64`; `toc-html#search-unit:866`
- **`64.1` Overview** — `tlpi:64.1`; `toc-html#search-unit:867`
- **`64.2` UNIX 98 Pseudoterminals** — `tlpi:64.2`; `toc-html#search-unit:868`
  - `64.2.1` Opening an Unused Master: posix_openpt() — `tlpi:64.2.1`; `toc-html#search-unit:869`
  - `64.2.2` Changing Slave Ownership and Permissions: grantpt() — `tlpi:64.2.2`; `toc-html#search-unit:870`
  - `64.2.3` Unlocking the Slave: unlockpt() — `tlpi:64.2.3`; `toc-html#search-unit:871`
  - `64.2.4` Obtaining the Name of the Slave: ptsname() — `tlpi:64.2.4`; `toc-html#search-unit:872`
- **`64.3` Opening a Pseudoterminal Master: ptyMasterOpen()** — `tlpi:64.3`; `toc-html#search-unit:873`
- **`64.4` Connecting Two Processes with a Pseudoterminal: ptyFork()** — `tlpi:64.4`; `toc-html#search-unit:874`
- **`64.5` Pseudoterminal I/O** — `tlpi:64.5`; `toc-html#search-unit:875`
- **`64.6` Implementing script(1)** — `tlpi:64.6`; `toc-html#search-unit:876`
- **`64.7` Terminal Attributes and Window Size** — `tlpi:64.7`; `toc-html#search-unit:877`
- **`64.8` BSD Pseudoterminals** — `tlpi:64.8`; `toc-html#search-unit:878`
- **`64.9` Summary** — `tlpi:64.9`; `toc-html#search-unit:879`
- **`64.10` Exercises** — `tlpi:64.10`; `toc-html#search-unit:880`

## Appendices

- **Appendix A — TRACING SYSTEM CALLS** — `tlpi:appendix:A`; `toc-html#search-unit:881`
- **Appendix B — PARSING COMMAND-LINE OPTIONS** — `tlpi:appendix:B`; `toc-html#search-unit:882`
- **Appendix C — CASTING THE NULL POINTER** — `tlpi:appendix:C`; `toc-html#search-unit:883`
- **Appendix D — KERNEL CONFIGURATION** — `tlpi:appendix:D`; `toc-html#search-unit:884`
- **Appendix E — FURTHER SOURCES OF INFORMATION** — `tlpi:appendix:E`; `toc-html#search-unit:885`
- **Appendix F — SOLUTIONS TO SELECTED EXERCISES** — `tlpi:appendix:F`; `toc-html#search-unit:886`

## 6. Known parsing anomalies and limits

1. **Primary EPUB Chapter 14 title mismatch:** the EPUB structure previously exposed Chapter 14 as “系统编程概念”; the Preface grouping and both detailed TOC sources identify Chapter 14 as **FILE SYSTEMS / 文件系统**. The Source Map uses the canonical Chapter 14 title and retains this mismatch as an explicit parser anomaly.
2. **HTML hierarchy flattening:** `TLPI-TOC-HTML` is complete, but the HTML parser represents the entire detailed TOC as one owner section plus paragraph/search units rather than nested Chapter/Section nodes. The `search-unit:N` locators preserve repeatable navigation.
3. **PDF page granularity:** the Preface and detailed-TOC PDFs are parsed as page sections. They are reliable structural/page cross-checks, not substitutes for the primary EPUB body.
4. **Primary EPUB node IDs:** the existing primary document ID is stable, but individual EPUB-generated `section_id` values were not available in this mapping run. They must be captured when the first body section is opened. Until then, the canonical semantic locator + exact heading is the stable resolver.
5. **Edition metadata:** the available reading sources do not explicitly confirm an edition statement; it remains `unknown / not confirmed` rather than inferred from publication-era details.

## 7. Mapping boundary

This Source Map establishes source identity, book structure, and navigation only. It does not assert that any body section has been read, mapped to a mechanism, experimentally observed, or learned.
