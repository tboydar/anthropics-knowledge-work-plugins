---
name: update
description: Sync tasks and refresh memory from your current activity. Use when pulling new assignments from your project tracker into TASKS.md, triaging stale or overdue tasks, filling memory gaps for unknown people or projects, or running a comprehensive scan to catch todos buried in chat and email.
argument-hint: "[--comprehensive]"
---

# Update Command

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Keep your task list and memory current. Two modes:

- **Default:** Sync tasks from external tools, triage stale items, check memory for gaps
- **`--comprehensive`:** Deep scan chat, email, calendar, docs — flag missed todos and suggest new memories

## Usage

```bash
/productivity:update
/productivity:update --comprehensive
```

## Default Mode

### 1. Load Current State

Read `TASKS.md` and `memory/` directory. If they don't exist, suggest `/productivity:start` first.

### 2. Sync Tasks from External Sources

Check for available task sources:
- **Project tracker** (e.g. Asana, Linear, Jira) (if MCP available)
- **GitHub Issues** (if in a repo): `gh issue list --assignee=@me`

If no sources are available, skip to Step 3.

**Fetch tasks assigned to the user** (open/in-progress). Compare against TASKS.md:

| External task | TASKS.md match? | Action |
|---------------|-----------------|--------|
| Found, not in TASKS.md | No match | Offer to add |
| Found, already in TASKS.md | Match by title (fuzzy) | Skip |
| In TASKS.md, not in external | No match | Flag as potentially stale |
| Completed externally | In Active section | Offer to mark done |

Present diff and let user decide what to add/complete.

### 3. Triage Stale Items

Review Active tasks in TASKS.md and flag:
- Tasks with due dates in the past
- Tasks in Active for 30+ days
- Tasks with no context (no person, no project)

Present each for triage: Mark done? Reschedule? Move to Someday?

### 4. Decode Tasks for Memory Gaps

For each task, attempt to decode all entities (people, projects, acronyms, tools, links):

```
Task: "Send PSR to Todd re: Phoenix blockers"

Decode:
- PSR → ✓ Pipeline Status Report (in glossary)
- Todd → ✓ Todd Martinez (in people/)
- Phoenix → ? Not in memory
```

Track what's fully decoded vs. what has gaps.

### 5. Fill Gaps

Present unknown terms grouped:
```
I found terms in your tasks I don't have context for:

1. "Phoenix" (from: "Send PSR to Todd re: Phoenix blockers")
   → What's Phoenix?

2. "Maya" (from: "sync with Maya on API design")
   → Who is Maya?
```

Add answers to the appropriate memory files (people/, projects/, glossary.md).

### 6. Capture Enrichment

Tasks often contain richer context than memory. Extract and update:
- **Links** from tasks → add to project/people files
- **Status changes** ("launch done") → update project status, demote from CLAUDE.md
- **Relationships** ("Todd's sign-off on Maya's proposal") → cross-reference people
- **Deadlines** → add to project files

### 7. Report

```
Update complete:
- Tasks: +3 from project tracker (e.g. Asana), 1 completed, 2 triaged
- Memory: 2 gaps filled, 1 project enriched
- All tasks decoded ✓
```

## Comprehensive Mode (`--comprehensive`)

Everything in Default Mode, plus a deep scan of recent activity.

### Extra Step: Scan Activity Sources

Gather data from available MCP sources:
- **Chat:** Search recent messages, read active channels
- **Email:** Search sent messages
- **Documents:** List recently touched docs
- **Calendar:** List recent + upcoming events

### Extra Step: Flag Missed Todos

Compare activity against TASKS.md. Surface action items that aren't tracked:

```
## Possible Missing Tasks

From your activity, these look like todos you haven't captured:

1. From chat (Jan 18):
   "I'll send the updated mockups by Friday"
   → Add to TASKS.md?

2. From meeting "Phoenix Standup" (Jan 17):
   You have a recurring meeting but no Phoenix tasks active
   → Anything needed here?

3. From email (Jan 16):
   "I'll review the API spec this week"
   → Add to TASKS.md?
```

Let user pick which to add.

### Extra Step: Suggest New Memories

Surface new entities not in memory:

```
## New People (not in memory)
| Name | Frequency | Context |
|------|-----------|---------|
| Maya Rodriguez | 12 mentions | design, UI reviews |
| Alex K | 8 mentions | DMs about API |

## New Projects/Topics
| Name | Frequency | Context |
|------|-----------|---------|
| Starlight | 15 mentions | planning docs, product |

## Suggested Cleanup
- **Horizon project** — No mentions in 30 days. Mark completed?
```

Present grouped by confidence. High-confidence items offered to add directly; low-confidence items asked about.

## Notes

- Never auto-add tasks or memories without user confirmation
- External source links are preserved when available
- Fuzzy matching on task titles handles minor wording differences
- Safe to run frequently — only updates when there's new info
- `--comprehensive` always runs interactively

---

> **以下為繁體中文翻譯 · Traditional Chinese translation below**

# 更新指令

> 若您看到不熟悉的佔位符號，或需要確認已連接哪些工具，請參閱 [CONNECTORS.md](../../CONNECTORS.md)。

保持您的任務清單與記憶為最新狀態。共有兩種模式：

- **預設模式：** 從外部工具同步任務、整理過期項目、檢查記憶是否有遺漏
- **`--comprehensive`（全面模式）：** 深度掃描聊天、電子郵件、行事曆、文件 — 標記遺漏的待辦事項並建議新的記憶

## 使用方式

```bash
/productivity:update
/productivity:update --comprehensive
```

## 預設模式

### 1. 載入目前狀態

讀取 `TASKS.md` 與 `memory/` 目錄。若這些檔案不存在，請建議先執行 `/productivity:start`。

### 2. 從外部來源同步任務

檢查可用的任務來源：
- **專案追蹤工具**（例如 Asana、Linear、Jira）（若 MCP 可用）
- **GitHub Issues**（若在儲存庫中）：`gh issue list --assignee=@me`

若無任何可用來源，請跳至步驟 3。

**擷取指派給使用者的任務**（開啟／進行中）。與 TASKS.md 比對：

| 外部任務 | TASKS.md 中是否有相符項目？ | 動作 |
|---------|-----------------------------|------|
| 找到，但不在 TASKS.md 中 | 無相符項目 | 建議新增 |
| 找到，且已在 TASKS.md 中 | 依標題比對（模糊比對） | 略過 |
| 在 TASKS.md 中，但不存在於外部來源 | 無相符項目 | 標記為可能過時 |
| 已在外部完成 | 位於「進行中」區段 | 建議標記為完成 |

呈現差異清單，讓使用者決定要新增或完成哪些項目。

### 3. 整理過期項目

檢視 TASKS.md 中「進行中」的任務並標記：
- 截止日期已過的任務
- 在「進行中」超過 30 天的任務
- 缺乏上下文（無人員、無專案）的任務

逐一呈現供整理：標記完成？重新排程？移至「日後再做」？

### 4. 解碼任務以找出記憶缺口

針對每項任務，嘗試解碼所有實體（人員、專案、縮寫、工具、連結）：

```
任務：「將 PSR 寄給 Todd，內容與 Phoenix 阻礙事項有關」

解碼：
- PSR → ✓ 管道狀態報告（位於 glossary）
- Todd → ✓ Todd Martinez（位於 people/）
- Phoenix → ？ 記憶中無此項目
```

追蹤哪些已完整解碼、哪些仍有缺口。

### 5. 填補缺口

將未知詞彙分組呈現：
```
我在您的任務中發現一些沒有上下文的詞彙：

1. 「Phoenix」（來源：「將 PSR 寄給 Todd，內容與 Phoenix 阻礙事項有關」）
   → 什麼是 Phoenix？

2. 「Maya」（來源：「與 Maya 討論 API 設計」）
   → Maya 是誰？
```

將答案新增至適當的記憶檔案（people/、projects/、glossary.md）。

### 6. 捕捉強化資訊

任務通常包含比記憶更豐富的上下文。擷取並更新：
- **任務中的連結** → 新增至專案／人員檔案
- **狀態變更**（「已上線」）→ 更新專案狀態，從 CLAUDE.md 中降級
- **關聯性**（「Todd 已簽核 Maya 的提案」）→ 建立人員交叉參照
- **截止日期** → 新增至專案檔案

### 7. 回報

```
更新完成：
- 任務：從專案追蹤工具（例如 Asana）新增 3 項，1 項完成，2 項已整理
- 記憶：填補 2 個缺口，1 個專案已強化
- 所有任務皆已解碼 ✓
```

## 全面模式（`--comprehensive`）

包含預設模式的所有功能，加上對近期活動的深度掃描。

### 額外步驟：掃描活動來源

從可用的 MCP 來源收集資料：
- **聊天：** 搜尋最近的訊息，讀取活躍頻道
- **電子郵件：** 搜尋已寄出的訊息
- **文件：** 列出近期觸碰過的文件
- **行事曆：** 列出近期與即將到來的事件

### 額外步驟：標記遺漏的待辦事項

將活動內容與 TASKS.md 比對。找出未追蹤的待辦事項：

```
## 可能遺漏的任務

從您的活動中，以下項目看起來像是尚未捕捉的待辦事項：

1. 來自聊天（1 月 18 日）：
   「我會在星期五前寄出更新的模型稿」
   → 新增至 TASKS.md？

2. 來自會議「Phoenix 站立會議」（1 月 17 日）：
   您有例行會議，但目前沒有進行中的 Phoenix 任務
   → 這裡需要處理什麼嗎？

3. 來自電子郵件（1 月 16 日）：
   「我會在本週檢視 API 規格」
   → 新增至 TASKS.md？
```

讓使用者選擇要新增哪些項目。

### 額外步驟：建議新記憶

找出記憶中不存在的新實體：

```
## 新人員（記憶中無此項目）
| 姓名 | 出現頻率 | 上下文 |
|------|---------|--------|
| Maya Rodriguez | 12 次提及 | 設計、UI 審查 |
| Alex K | 8 次提及 | 關於 API 的私訊 |

## 新專案／主題
| 名稱 | 出現頻率 | 上下文 |
|------|---------|--------|
| Starlight | 15 次提及 | 規劃文件、產品 |

## 建議清理
- **Horizon 專案** — 30 天內無任何提及。標記為已完成？
```

依信心程度分組呈現。高信心項目可直接建議新增；低信心項目則需詢問使用者。

## 注意事項

- 未經使用者確認，絕不自動新增任務或記憶
- 外部來源的連結在可用時會予以保留
- 任務標題的模糊比對可處理細微的文字差異
- 可頻繁執行 — 僅在有新資訊時才會更新
- `--comprehensive` 一律以互動模式執行

<!-- translated-zh-TW -->
