---
name: start
description: Initialize the productivity system and open the dashboard. Use when setting up the plugin for the first time, bootstrapping working memory from your existing task list, or decoding the shorthand (nicknames, acronyms, project codenames) you use in your todos.
---

# Start Command

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Initialize the task and memory systems, then open the unified dashboard.

## Instructions

### 1. Check What Exists

Check the working directory for:
- `TASKS.md` — task list
- `CLAUDE.md` — working memory
- `memory/` — deep memory directory
- `dashboard.html` — the visual UI

### 2. Create What's Missing

**If `TASKS.md` doesn't exist:** Create it with the standard template (see task-management skill). Place it in the current working directory.

**If `dashboard.html` doesn't exist:** Copy it from `${CLAUDE_PLUGIN_ROOT}/skills/dashboard.html` to the current working directory.

**If `CLAUDE.md` and `memory/` don't exist:** This is a fresh setup — after opening the dashboard, begin the memory bootstrap workflow (see below). Place these in the current working directory.

### 3. Open the Dashboard

Do NOT use `open` or `xdg-open` — in Cowork, the agent runs in a VM and shell open commands won't reach the user's browser. Instead, tell the user: "Dashboard is ready at `dashboard.html`. Open it from your file browser to get started."

### 4. Orient the User

If everything was already initialized:
```
Dashboard open. Your tasks and memory are both loaded.
- /productivity:update to sync tasks and check memory
- /productivity:update --comprehensive for a deep scan of all activity
```

If memory hasn't been bootstrapped yet, continue to step 5.

### 5. Bootstrap Memory (First Run Only)

Only do this if `CLAUDE.md` and `memory/` don't exist yet.

The best source of workplace language is the user's actual task list. Real tasks = real shorthand.

**Ask the user:**
```
Where do you keep your todos or task list? This could be:
- A local file (e.g., TASKS.md, todo.txt)
- An app (e.g. Asana, Linear, Jira, Notion, Todoist)
- A notes file

I'll use your tasks to learn your workplace shorthand.
```

**Once you have access to the task list:**

For each task item, analyze it for potential shorthand:
- Names that might be nicknames
- Acronyms or abbreviations
- Project references or codenames
- Internal terms or jargon

**For each item, decode it interactively:**

```
Task: "Send PSR to Todd re: Phoenix blockers"

I see some terms I want to make sure I understand:

1. **PSR** - What does this stand for?
2. **Todd** - Who is Todd? (full name, role)
3. **Phoenix** - Is this a project codename? What's it about?
```

Continue through each task, asking only about terms you haven't already decoded.

### 6. Optional Comprehensive Scan

After task list decoding, offer:
```
Do you want me to do a comprehensive scan of your messages, emails, and documents?
This takes longer but builds much richer context about the people, projects, and terms in your work.

Or we can stick with what we have and add context later.
```

**If they choose comprehensive scan:**

Gather data from available MCP sources:
- **Chat:** Recent messages, channels, DMs
- **Email:** Sent messages, recipients
- **Documents:** Recent docs, collaborators
- **Calendar:** Meetings, attendees

Build a braindump of people, projects, and terms found. Present findings grouped by confidence:
- **Ready to add** (high confidence) — offer to add directly
- **Needs clarification** — ask the user
- **Low frequency / unclear** — note for later

### 7. Write Memory Files

From everything gathered, create:

**CLAUDE.md** (working memory, ~50-80 lines):
```markdown
# Memory

## Me
[Name], [Role] on [Team].

## People
| Who | Role |
|-----|------|
| **[Nickname]** | [Full Name], [role] |

## Terms
| Term | Meaning |
|------|---------|
| [acronym] | [expansion] |

## Projects
| Name | What |
|------|------|
| **[Codename]** | [description] |

## Preferences
- [preferences discovered]
```

**memory/** directory:
- `memory/glossary.md` — full decoder ring (acronyms, terms, nicknames, codenames)
- `memory/people/{name}.md` — individual profiles
- `memory/projects/{name}.md` — project details
- `memory/context/company.md` — teams, tools, processes

### 8. Report Results

```
Productivity system ready:
- Tasks: TASKS.md (X items)
- Memory: X people, X terms, X projects
- Dashboard: open in browser

Use /productivity:update to keep things current (add --comprehensive for a deep scan).
```

## Notes

- If memory is already initialized, this just opens the dashboard
- Nicknames are critical — always capture how people are actually referred to
- If a source isn't available, skip it and note the gap
- Memory grows organically through natural conversation after bootstrap

---

> **以下為繁體中文翻譯 · Traditional Chinese translation below**

# 開始指令

> 如果您看到不熟悉的佔位符，或需要確認哪些工具已連接，請參閱 [CONNECTORS.md](../../CONNECTORS.md)。

初始化任務與記憶系統，然後開啟統一的儀表板。

## 操作說明

### 1. 檢查現有內容

檢查工作目錄中是否有：
- `TASKS.md` — 任務清單
- `CLAUDE.md` — 工作記憶
- `memory/` — 深度記憶目錄
- `dashboard.html` — 視覺化介面

### 2. 建立缺失的內容

**如果 `TASKS.md` 不存在：** 使用標準範本建立（請參閱任務管理技能），並放置於目前的工作目錄。

**如果 `dashboard.html` 不存在：** 從 `${CLAUDE_PLUGIN_ROOT}/skills/dashboard.html` 複製到目前的工作目錄。

**如果 `CLAUDE.md` 和 `memory/` 不存在：** 這代表全新安裝 — 開啟儀表板後，開始執行記憶啟動流程（請參閱下方說明）。將這些檔案放置於目前的工作目錄。

### 3. 開啟儀表板

請勿使用 `open` 或 `xdg-open` 指令 — 在 Cowork 環境中，代理程式執行於虛擬機器內，Shell 的開啟指令無法觸及使用者的瀏覽器。請改為告知使用者：「儀表板已就緒，位於 `dashboard.html`。請從您的檔案瀏覽器開啟以開始使用。」

### 4. 引導使用者

如果所有項目皆已完成初始化：
```
儀表板已開啟。您的任務與記憶皆已載入。
- /productivity:update 用於同步任務並檢查記憶
- /productivity:update --comprehensive 用於深度掃描所有活動
```

如果記憶尚未啟動，請繼續執行步驟 5。

### 5. 啟動記憶（僅限首次執行）

僅在 `CLAUDE.md` 和 `memory/` 尚不存在時執行此步驟。

了解職場語言的最佳來源是使用者的實際任務清單。真實的任務 = 真實的簡稱。

**詢問使用者：**
```
您把待辦事項或任務清單存放在哪裡？可能的位置包括：
- 本機檔案（例如 TASKS.md、todo.txt）
- 應用程式（例如 Asana、Linear、Jira、Notion、Todoist）
- 筆記檔案

我會利用您的任務來學習您的職場簡稱用法。
```

**取得任務清單後：**

針對每個任務項目，分析其中可能的簡稱：
- 可能是暱稱的名字
- 縮寫或簡稱
- 專案代稱或代號
- 內部術語或行話

**針對每個項目，以互動方式解碼：**

```
任務：「將 PSR 寄給 Todd，主旨：Phoenix 阻礙項目」

我看到幾個想確認的詞彙：

1. **PSR** — 這是什麼的縮寫？
2. **Todd** — Todd 是誰？（全名、職稱）
3. **Phoenix** — 這是專案代號嗎？內容是什麼？
```

逐一瀏覽每個任務，只需要詢問尚未解碼過的詞彙。

### 6. 選擇性的全面掃描

完成任務清單解碼後，提供選項：
```
您是否希望我對您的訊息、電子郵件和文件進行全面掃描？
這會花費較長時間，但能建立更豐富的脈絡，涵蓋您工作中的人物、專案與術語。

或者我們可以先使用現有資訊，之後再補充脈絡。
```

**若對方選擇全面掃描：**

從可用的 MCP 來源收集資料：
- **聊天紀錄：** 最近的訊息、頻道、私訊
- **電子郵件：** 寄出的信件、收件人
- **文件：** 最近的文件、協作者
- **行事曆：** 會議、與會者

建立人物、專案與術語的腦力激盪整理。依可信度分組呈現發現結果：
- **可直接新增**（高可信度）— 提議直接加入
- **需要釐清** — 詢問使用者
- **低頻率／不明確** — 記錄備查

### 7. 撰寫記憶檔案

根據收集到的所有資訊，建立：

**CLAUDE.md**（工作記憶，約 50-80 行）：
```markdown
# 記憶

## 關於我
[姓名]，[團隊] 的 [職稱]。

## 人物
| 誰 | 角色 |
|-----|------|
| **[暱稱]** | [全名]，[職稱] |

## 術語
| 詞彙 | 含義 |
|------|---------|
| [縮寫] | [完整內容] |

## 專案
| 名稱 | 內容 |
|------|------|
| **[代號]** | [描述] |

## 偏好
- [發現的偏好設定]
```

**memory/ 目錄：**
- `memory/glossary.md` — 完整解碼手冊（縮寫、術語、暱稱、代號）
- `memory/people/{name}.md` — 個人檔案
- `memory/projects/{name}.md` — 專案詳細資訊
- `memory/context/company.md` — 團隊、工具、流程

### 8. 回報結果

```
生產力系統已就緒：
- 任務：TASKS.md（X 個項目）
- 記憶：X 位人物、X 個術語、X 個專案
- 儀表板：已於瀏覽器中開啟

使用 /productivity:update 保持資訊更新（加上 --comprehensive 進行深度掃描）。
```

## 備註

- 如果記憶已初始化，此指令僅會開啟儀表板
- 暱稱至關重要 — 務必記錄人們實際被稱呼的方式
- 如果某個來源無法取得，請跳過並記錄此缺口
- 啟動完成後，記憶會透過日常對話自然地持續成長

<!-- translated-zh-TW -->
