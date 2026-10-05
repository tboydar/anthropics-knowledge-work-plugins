# Productivity Plugin

A productivity plugin primarily designed for [Cowork](https://claude.com/product/cowork), Anthropic's agentic desktop application — though it also works in Claude Code. Task management, workplace memory, and a visual dashboard — Claude learns your people, projects, and terminology so it can act like a colleague, not a chatbot.

## Installation

```
claude plugin marketplace add anthropics/knowledge-work-plugins
claude plugin install productivity@knowledge-work-plugins
```

## What It Does

This plugin gives Claude a persistent understanding of your work:

- **Task management** — A markdown task list (`TASKS.md`) that Claude reads, writes, and executes against. Add tasks naturally, and Claude tracks status, triages stale items, and syncs with external tools.
- **Workplace memory** — A two-tier memory system that teaches Claude your shorthand, people, projects, and terminology. Say "ask todd to do the PSR for oracle" and Claude knows exactly who, what, and which deal.
- **Visual dashboard** — A local HTML file that gives you a board view of your tasks and a live view of what Claude knows about your workplace. Edit from the board or the file — they stay in sync.

## Commands

| Command | What it does |
|---------|--------------|
| `/start` | Initialize tasks + memory, open the dashboard |
| `/update` | Triage stale items, check memory for gaps, sync from external tools if applicable |
| `/update --comprehensive` | Deep scan email, calendar, chat — flag missed todos and suggest new memories |

## Skills

| Skill | Description |
|-------|-------------|
| `memory-management` | Two-tier memory system — CLAUDE.md for working memory, memory/ directory for deep storage |
| `task-management` | Markdown-based task tracking using a shared TASKS.md file |

## Example Workflows

### Getting Started

```
You: /start

Claude: [Creates TASKS.md, CLAUDE.md, memory/ directory, and dashboard.html]
        [Opens the dashboard in your browser]
        [Asks about your role, team, and current priorities to seed memory]
```

### Adding Tasks Naturally

```
You: I need to review the budget proposal for Sarah by Friday,
     draft the Q2 roadmap after syncing with Greg, and follow up
     on the API spec from the Platform team

Claude: [Adds all three tasks to TASKS.md with context]
        [Dashboard updates automatically]
```

### Morning Sync

```
You: /update --comprehensive

Claude: [Scans email, calendar, and chat for new action items]
        [Flags: "Budget proposal review is due tomorrow — still open"]
        [Suggests: "New person mentioned in 3 threads: Jamie Park,
         Design Lead — add to memory?"]
        [Updates stale tasks and fills memory gaps]
```

### Workplace Shorthand

Once memory is populated, Claude decodes your shorthand instantly:

```
You: ask todd to do the PSR for oracle

Claude: "Ask Todd Martinez (Finance lead) to prepare the Pipeline
         Status Report for the Oracle Systems deal ($2.3M, closing Q2)"
```

No clarifying questions. No round trips.

## Data Sources

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](CONNECTORS.md).

Connect your communication and project management tools for the best experience. Without them, manage tasks and memory manually.

**Included MCP connections:**
- Chat (Slack) for team context and message scanning
- Email and calendar (Microsoft 365) for action item discovery
- Knowledge base (Notion) for reference documents
- Project tracker (Asana, Linear, Atlassian, monday.com, ClickUp) for task syncing
- Office suite (Microsoft 365) for documents

**Additional options:**
- See [CONNECTORS.md](CONNECTORS.md) for alternative tools in each category

---

> **以下為繁體中文翻譯 · Traditional Chinese translation below**

# 生產力外掛程式

一個主要為 [Cowork](https://claude.com/product/cowork)（Anthropic 的代理式桌面應用程式）設計的生產力外掛程式——不過它也適用於 Claude Code。任務管理、職場記憶，以及視覺化儀表板——Claude 會學習你的人员、專案和術語，讓它表現得像同事，而不是聊天機器人。

## 安裝方式

```
claude plugin marketplace add anthropics/knowledge-work-plugins
claude plugin install productivity@knowledge-work-plugins
```

## 功能說明

此外掛程式讓 Claude 能持續理解你的工作內容：

- **任務管理** — 一份 Markdown 任務清單（`TASKS.md`），Claude 會讀取、寫入並據以執行。自然地在其中加入任務，Claude 會追蹤狀態、分類處理過期項目，並與外部工具同步。
- **職場記憶** — 雙層記憶系統，教導 Claude 你的簡稱、人员、專案和術語。說「叫 Todd 處理 Oracle 的 PSR」，Claude 就知道確切該找誰、做什麼事，以及是哪筆交易。
- **視覺化儀表板** — 一個本機 HTML 檔案，提供你任務的看板檢視，以及 Claude 對你職場認知的即時檢視。可從看板或檔案編輯——兩者會保持同步。

## 指令

| 指令 | 功能 |
|---------|--------------|
| `/start` | 初始化任務 + 記憶，開啟儀表板 |
| `/update` | 分類處理過期項目、檢查記憶缺口、如適用則從外部工具同步 |
| `/update --comprehensive` | 深度掃描電子郵件、行事曆、聊天記錄——標記遺漏的待辦事項並建議新的記憶 |

## 技能

| 技能 | 說明 |
|-------|-------------|
| `memory-management` | 雙層記憶系統——CLAUDE.md 用於工作記憶，memory/ 目錄用於深度儲存 |
| `task-management` | 使用共享 TASKS.md 檔案進行基於 Markdown 的任務追蹤 |

## 範例工作流程

### 開始使用

```
You: /start

Claude: [建立 TASKS.md、CLAUDE.md、memory/ 目錄和 dashboard.html]
        [在瀏覽器中開啟儀表板]
        [詢問你的角色、團隊和當前優先事項以建立初始記憶]
```

### 自然地加入任務

```
You: 我需要在週五前審閱 Sarah 的預算提案、
     與 Greg 同步後起草 Q2 路線圖、並追蹤
     Platform 團隊的 API 規格

Claude: [將這三個任務連同背景資訊加入 TASKS.md]
        [儀表板自動更新]
```

### 早晨同步

```
You: /update --comprehensive

Claude: [掃描電子郵件、行事曆和聊天記錄以找出新的行動項目]
        [標記：「預算提案審閱明天到期——仍待處理」]
        [建議：「有 3 個討論串提到新人：Jamie Park、
         Design Lead——要加入記憶嗎？」]
        [更新過期任務並填補記憶缺口]
```

### 職場簡稱

記憶建立後，Claude 能立即解讀你的簡稱：

```
You: 叫 todd 處理 oracle 的 PSR

Claude: 「請 Todd Martinez（財務主管）準備
         Oracle Systems 交易的 Pipeline
         Status Report（230 萬美元，Q2 結案）」
```

無需額外提問。無需往返確認。

## 資料來源

> 如果你看到不熟悉的佔位符，或需要確認已連線哪些工具，請參閱 [CONNECTORS.md](CONNECTORS.md)。

連線你的通訊與專案管理工具以獲得最佳體驗。若無這些工具，則可手動管理任務和記憶。

**內建的 MCP 連線：**
- 聊天（Slack）— 用於團隊背景資訊和訊息掃描
- 電子郵件和行事曆（Microsoft 365）— 用於發掘行動項目
- 知識庫（Notion）— 用於參考文件
- 專案追蹤器（Asana、Linear、Atlassian、monday.com、ClickUp）— 用於任務同步
- 辦公室套件（Microsoft 365）— 用於文件

**其他選項：**
- 各類別的替代工具請參閱 [CONNECTORS.md](CONNECTORS.md)

<!-- translated-zh-TW -->
