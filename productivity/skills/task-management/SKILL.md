---
name: task-management
description: Simple task management using a shared TASKS.md file. Reference this when the user asks about their tasks, wants to add/complete tasks, or needs help tracking commitments.
user-invocable: false
---

# Task Management

Tasks are tracked in a simple `TASKS.md` file that both you and the user can edit.

## File Location

**Always use `TASKS.md` in the current working directory.**

- If it exists, read/write to it
- If it doesn't exist, create it with the template below

## Dashboard Setup (First Run)

A visual dashboard is available for managing tasks and memory. **On first interaction with tasks:**

1. Check if `dashboard.html` exists in the current working directory
2. If not, copy it from `${CLAUDE_PLUGIN_ROOT}/skills/dashboard.html` to the current working directory
3. Inform the user: "I've added the dashboard. Run `/productivity:start` to set up the full system."

The task board:
- Reads and writes to the same `TASKS.md` file
- Auto-saves changes
- Watches for external changes (syncs when you edit via CLI)
- Supports drag-and-drop reordering of tasks and sections

## Format & Template

When creating a new TASKS.md, use this exact template (without example tasks):

```markdown
# Tasks

## Active

## Waiting On

## Someday

## Done
```

Task format:
- `- [ ] **Task title** - context, for whom, due date`
- Sub-bullets for additional details
- Completed: `- [x] ~~Task~~ (date)`

## How to Interact

**When user asks "what's on my plate" / "my tasks":**
- Read TASKS.md
- Summarize Active and Waiting On sections
- Highlight anything overdue or urgent

**When user says "add a task" / "remind me to":**
- Add to Active section with `- [ ] **Task**` format
- Include context if provided (who it's for, due date)

**When user says "done with X" / "finished X":**
- Find the task
- Change `[ ]` to `[x]`
- Add strikethrough: `~~task~~`
- Add completion date
- Move to Done section

**When user asks "what am I waiting on":**
- Read the Waiting On section
- Note how long each item has been waiting

## Conventions

- **Bold** the task title for scannability
- Include "for [person]" when it's a commitment to someone
- Include "due [date]" for deadlines
- Include "since [date]" for waiting items
- Sub-bullets for additional context
- Keep Done section for ~1 week, then clear old items

## Extracting Tasks

When summarizing meetings or conversations, offer to add extracted tasks:
- Commitments the user made ("I'll send that over")
- Action items assigned to them
- Follow-ups mentioned

Ask before adding - don't auto-add without confirmation.

---

> **以下為繁體中文翻譯 · Traditional Chinese translation below**

# 任務管理

任務透過一個簡單的 `TASKS.md` 檔案來追蹤，您和使用者都可以編輯此檔案。

## 檔案位置

**一律使用目前工作目錄中的 `TASKS.md`。**

- 如果檔案存在，請讀取/寫入
- 如果檔案不存在，請使用下方範本建立

## 儀表板設定（首次執行）

提供視覺化儀表板來管理任務和記憶。**在首次與任務互動時：**

1. 檢查目前工作目錄中是否有 `dashboard.html`
2. 如果沒有，請從 `${CLAUDE_PLUGIN_ROOT}/skills/dashboard.html` 複製到目前工作目錄
3. 告知使用者：「我已新增儀表板。執行 `/productivity:start` 來設定完整系統。」

任務看板：
- 讀取和寫入同一個 `TASKS.md` 檔案
- 自動儲存變更
- 監看外部變更（當您透過 CLI 編輯時會同步）
- 支援拖放重新排序任務和區段

## 格式與範本

建立新的 TASKS.md 時，請使用這個確切範本（不含範例任務）：

```markdown
# Tasks

## Active

## Waiting On

## Someday

## Done
```

任務格式：
- `- [ ] **任務標題** - 背景、對象、截止日期`
- 子項目用於補充細節
- 已完成：`- [x] ~~任務~~ (日期)`

## 互動方式

**當使用者詢問「我有哪些待辦事項」/「我的任務」時：**
- 讀取 TASKS.md
- 摘要 Active 和 Waiting On 區段
- 標示任何逾期或緊急事項

**當使用者說「新增任務」/「提醒我」時：**
- 使用 `- [ ] **任務**` 格式新增至 Active 區段
- 如果有提供背景資訊（對象、截止日期），請一併納入

**當使用者說「完成 X」/「搞定 X」時：**
- 找到該任務
- 將 `[ ]` 改為 `[x]`
- 加上刪除線：`~~任務~~`
- 加上完成日期
- 移至 Done 區段

**當使用者詢問「我在等什麼」時：**
- 讀取 Waiting On 區段
- 記錄每個項目已等待多久

## 慣例

- 將任務標題以**粗體**呈現，方便快速瀏覽
- 若是對某人的承諾，請加上「for [人名]」
- 對於截止日期，請加上「due [日期]」
- 對於等待中的項目，請加上「since [日期]」
- 使用子項目補充額外背景
- Done 區段保留約 1 週，之後清除舊項目

## 擷取任務

在總結會議或對話時，主動提供擷取任務的選項：
- 使用者做出的承諾（「我會把那個寄過去」）
- 指派給他們的待辦事項
- 提到的後續追蹤事項

新增前請先詢問——未經確認請勿自動新增。

<!-- translated-zh-TW -->
