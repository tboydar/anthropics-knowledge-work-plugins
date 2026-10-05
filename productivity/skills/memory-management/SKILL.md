---
name: memory-management
description: Two-tier memory system that makes Claude a true workplace collaborator. Decodes shorthand, acronyms, nicknames, and internal language so Claude understands requests like a colleague would. CLAUDE.md for working memory, memory/ directory for the full knowledge base.
user-invocable: false
---

# Memory Management

Memory makes Claude your workplace collaborator - someone who speaks your internal language.

## The Goal

Transform shorthand into understanding:

```
User: "ask todd to do the PSR for oracle"
              ↓ Claude decodes
"Ask Todd Martinez (Finance lead) to prepare the Pipeline Status Report
 for the Oracle Systems deal ($2.3M, closing Q2)"
```

Without memory, that request is meaningless. With memory, Claude knows:
- **todd** → Todd Martinez, Finance lead, prefers Slack
- **PSR** → Pipeline Status Report (weekly sales doc)
- **oracle** → Oracle Systems deal, not the company

## Architecture

```
CLAUDE.md          ← Hot cache (~30 people, common terms)
memory/
  glossary.md      ← Full decoder ring (everything)
  people/          ← Complete profiles
  projects/        ← Project details
  context/         ← Company, teams, tools
```

**CLAUDE.md (Hot Cache):**
- Top ~30 people you interact with most
- ~30 most common acronyms/terms
- Active projects (5-15)
- Your preferences
- **Goal: Cover 90% of daily decoding needs**

**memory/glossary.md (Full Glossary):**
- Complete decoder ring - everyone, every term
- Searched when something isn't in CLAUDE.md
- Can grow indefinitely

**memory/people/, projects/, context/:**
- Rich detail when needed for execution
- Full profiles, history, context

## Lookup Flow

```
User: "ask todd about the PSR for phoenix"

1. Check CLAUDE.md (hot cache)
   → Todd? ✓ Todd Martinez, Finance
   → PSR? ✓ Pipeline Status Report
   → Phoenix? ✓ DB migration project

2. If not found → search memory/glossary.md
   → Full glossary has everyone/everything

3. If still not found → ask user
   → "What does X mean? I'll remember it."
```

This tiered approach keeps CLAUDE.md lean (~100 lines) while supporting unlimited scale in memory/.

## File Locations

- **Working memory:** `CLAUDE.md` in current working directory
- **Deep memory:** `memory/` subdirectory

## Working Memory Format (CLAUDE.md)

Use tables for compactness. Target ~50-80 lines total.

```markdown
# Memory

## Me
[Name], [Role] on [Team]. [One sentence about what I do.]

## People
| Who | Role |
|-----|------|
| **Todd** | Todd Martinez, Finance lead |
| **Sarah** | Sarah Chen, Engineering (Platform) |
| **Greg** | Greg Wilson, Sales |
→ Full list: memory/glossary.md, profiles: memory/people/

## Terms
| Term | Meaning |
|------|---------|
| PSR | Pipeline Status Report |
| P0 | Drop everything priority |
| standup | Daily 9am sync |
→ Full glossary: memory/glossary.md

## Projects
| Name | What |
|------|------|
| **Phoenix** | DB migration, Q2 launch |
| **Horizon** | Mobile app redesign |
→ Details: memory/projects/

## Preferences
- 25-min meetings with buffers
- Async-first, Slack over email
- No meetings Friday afternoons
```

## Deep Memory Format (memory/)

**memory/glossary.md** - The decoder ring:
```markdown
# Glossary

Workplace shorthand, acronyms, and internal language.

## Acronyms
| Term | Meaning | Context |
|------|---------|---------|
| PSR | Pipeline Status Report | Weekly sales doc |
| OKR | Objectives & Key Results | Quarterly planning |
| P0/P1/P2 | Priority levels | P0 = drop everything |

## Internal Terms
| Term | Meaning |
|------|---------|
| standup | Daily 9am sync in #engineering |
| the migration | Project Phoenix database work |
| ship it | Deploy to production |
| escalate | Loop in leadership |

## Nicknames → Full Names
| Nickname | Person |
|----------|--------|
| Todd | Todd Martinez (Finance) |
| T | Also Todd Martinez |

## Project Codenames
| Codename | Project |
|----------|---------|
| Phoenix | Database migration |
| Horizon | New mobile app |
```

**memory/people/{name}.md:**
```markdown
# Todd Martinez

**Also known as:** Todd, T
**Role:** Finance Lead
**Team:** Finance
**Reports to:** CFO (Michael Chen)

## Communication
- Prefers Slack DM
- Quick responses, very direct
- Best time: mornings

## Context
- Handles all PSRs and financial reporting
- Key contact for deal approvals over $500k
- Works closely with Sales on forecasting

## Notes
- Cubs fan, likes talking baseball
```

**memory/projects/{name}.md:**
```markdown
# Project Phoenix

**Codename:** Phoenix
**Also called:** "the migration"
**Status:** Active, launching Q2

## What It Is
Database migration from legacy Oracle to PostgreSQL.

## Key People
- Sarah - tech lead
- Todd - budget owner
- Greg - stakeholder (sales impact)

## Context
$1.2M budget, 6-month timeline. Critical path for Horizon project.
```

**memory/context/company.md:**
```markdown
# Company Context

## Tools & Systems
| Tool | Used for | Internal name |
|------|----------|---------------|
| Slack | Communication | - |
| Asana | Engineering tasks | - |
| Salesforce | CRM | "SF" or "the CRM" |
| Notion | Docs/wiki | - |

## Teams
| Team | What they do | Key people |
|------|--------------|------------|
| Platform | Infrastructure | Sarah (lead) |
| Finance | Money stuff | Todd (lead) |
| Sales | Revenue | Greg |

## Processes
| Process | What it means |
|---------|---------------|
| Weekly sync | Monday 10am all-hands |
| Ship review | Thursday deploy approval |
```

## How to Interact

### Decoding User Input (Tiered Lookup)

**Always** decode shorthand before acting on requests:

```
1. CLAUDE.md (hot cache)     → Check first, covers 90% of cases
2. memory/glossary.md        → Full glossary if not in hot cache
3. memory/people/, projects/ → Rich detail when needed
4. Ask user                  → Unknown term? Learn it.
```

Example:
```
User: "ask todd to do the PSR for oracle"

CLAUDE.md lookup:
  "todd" → Todd Martinez, Finance ✓
  "PSR" → Pipeline Status Report ✓
  "oracle" → (not in hot cache)

memory/glossary.md lookup:
  "oracle" → Oracle Systems deal ($2.3M) ✓

Now Claude can act with full context.
```

### Adding Memory

When user says "remember this" or "X means Y":

1. **Glossary items** (acronyms, terms, shorthand):
   - Add to memory/glossary.md
   - If frequently used, add to CLAUDE.md Quick Glossary

2. **People:**
   - Create/update memory/people/{name}.md
   - Add to CLAUDE.md Key People if important
   - **Capture nicknames** - critical for decoding

3. **Projects:**
   - Create/update memory/projects/{name}.md
   - Add to CLAUDE.md Active Projects if current
   - **Capture codenames** - "Phoenix", "the migration", etc.

4. **Preferences:** Add to CLAUDE.md Preferences section

### Recalling Memory

When user asks "who is X" or "what does X mean":

1. Check CLAUDE.md first
2. Check memory/ for full detail
3. If not found: "I don't know what X means yet. Can you tell me?"

### Progressive Disclosure

1. Load CLAUDE.md for quick parsing of any request
2. Dive into memory/ when you need full context for execution
3. Example: drafting an email to todd about the PSR
   - CLAUDE.md tells you Todd = Todd Martinez, PSR = Pipeline Status Report
   - memory/people/todd-martinez.md tells you he prefers Slack, is direct

## Bootstrapping

Use `/productivity:start` to initialize by scanning your chat, calendar, email, and documents. Extracts people, projects, and starts building the glossary.

## Conventions

- **Bold** terms in CLAUDE.md for scannability
- Keep CLAUDE.md under ~100 lines (the "hot 30" rule)
- Filenames: lowercase, hyphens (`todd-martinez.md`, `project-phoenix.md`)
- Always capture nicknames and alternate names
- Glossary tables for easy lookup
- When something's used frequently, promote it to CLAUDE.md
- When something goes stale, demote it to memory/ only

## What Goes Where

| Type | CLAUDE.md (Hot Cache) | memory/ (Full Storage) |
|------|----------------------|------------------------|
| Person | Top ~30 frequent contacts | glossary.md + people/{name}.md |
| Acronym/term | ~30 most common | glossary.md (complete list) |
| Project | Active projects only | glossary.md + projects/{name}.md |
| Nickname | In Key People if top 30 | glossary.md (all nicknames) |
| Company context | Quick reference only | context/company.md |
| Preferences | All preferences | - |
| Historical/stale | ✗ Remove | ✓ Keep in memory/ |

## Promotion / Demotion

**Promote to CLAUDE.md when:**
- You use a term/person frequently
- It's part of active work

**Demote to memory/ only when:**
- Project completed
- Person no longer frequent contact
- Term rarely used

This keeps CLAUDE.md fresh and relevant.

---

> **以下為繁體中文翻譯 · Traditional Chinese translation below**

# 記憶管理

記憶讓 Claude 成為你的職場協作者——一個能理解你內部語言的工作夥伴。

## 目標

將簡稱轉化為理解：

```
使用者：「請 Todd 為 oracle 做 PSR」
              ↓ Claude 解碼
「請 Todd Martinez（財務主管）為 Oracle Systems 交易（230 萬美元，Q2 結案）準備管線狀態報告」
```

沒有記憶，這個請求毫無意義。有了記憶，Claude 知道：
- **todd** → Todd Martinez，財務主管，偏好 Slack
- **PSR** → 管線狀態報告（每週銷售文件）
- **oracle** → Oracle Systems 交易，而非該公司

## 架構

```
CLAUDE.md          ← 熱快取（約 30 位人員、常用術語）
memory/
  glossary.md      ← 完整解碼環（所有內容）
  people/          ← 完整個人檔案
  projects/        ← 專案細節
  context/         ← 公司、團隊、工具
```

**CLAUDE.md（熱快取）：**
- 你最常互動的前 30 位人員
- 約 30 個最常見的縮寫／術語
- 進行中的專案（5-15 個）
- 你的偏好
- **目標：涵蓋 90% 的日常解碼需求**

**memory/glossary.md（完整詞彙表）：**
- 完整的解碼環——每個人、每個術語
- 當 CLAUDE.md 未涵蓋時搜尋此處
- 可無限期擴充

**memory/people/、projects/、context/：**
- 需要執行時提供豐富細節
- 完整的個人檔案、歷史記錄、背景脈絡

## 查詢流程

```
使用者：「請 Todd 為 phoenix 了解 PSR」

1. 檢查 CLAUDE.md（熱快取）
   → Todd？✓ Todd Martinez，財務
   → PSR？✓ 管線狀態報告
   → Phoenix？✓ 資料庫遷移專案

2. 若未找到 → 搜尋 memory/glossary.md
   → 完整詞彙表涵蓋所有人／所有事物

3. 若仍未找到 → 詢問使用者
   → 「X 是什麼意思？我會記住它。」
```

這種分層方式讓 CLAUDE.md 保持精簡（約 100 行），同時支援 memory/ 中的無限擴充。

## 檔案位置

- **工作記憶：** 當前工作目錄中的 `CLAUDE.md`
- **深度記憶：** `memory/` 子目錄

## 工作記憶格式（CLAUDE.md）

使用表格以保持精簡。目標總長度約 50-80 行。

```markdown
# 記憶

## 關於我
[姓名]，[團隊]的[職稱]。[一句話描述我的工作。]

## 人員
| 誰 | 角色 |
|-----|------|
| **Todd** | Todd Martinez，財務主管 |
| **Sarah** | Sarah Chen，工程（平台） |
| **Greg** | Greg Wilson，業務 |
→ 完整清單：memory/glossary.md，個人檔案：memory/people/

## 術語
| 術語 | 意義 |
|------|---------|
| PSR | 管線狀態報告 |
| P0 | 最高優先級，放下一切 |
| standup | 每日上午 9 點同步會議 |
→ 完整詞彙表：memory/glossary.md

## 專案
| 名稱 | 內容 |
|------|------|
| **Phoenix** | 資料庫遷移，Q2 上線 |
| **Horizon** | 行動應用程式重新設計 |
→ 詳細資訊：memory/projects/

## 偏好
- 25 分鐘會議，預留緩衝時間
- 非同步優先，用 Slack 而非 Email
- 週五下午不安排會議
```

## 深度記憶格式（memory/）

**memory/glossary.md** - 解碼環：
```markdown
# 詞彙表

職場簡稱、縮寫及內部語言。

## 縮寫
| 術語 | 意義 | 情境 |
|------|---------|---------|
| PSR | 管線狀態報告 | 每週銷售文件 |
| OKR | 目標與關鍵結果 | 季度規劃 |
| P0/P1/P2 | 優先級別 | P0 = 放下一切 |

## 內部術語
| 術語 | 意義 |
|------|---------|
| standup | 每日上午 9 點 #engineering 頻道同步 |
| the migration | Phoenix 專案資料庫工作 |
| ship it | 部署至正式環境 |
| escalate | 讓高層介入 |

## 暱稱 → 全名
| 暱稱 | 人員 |
|----------|--------|
| Todd | Todd Martinez（財務） |
| T | 也是 Todd Martinez |

## 專案代號
| 代號 | 專案 |
|----------|---------|
| Phoenix | 資料庫遷移 |
| Horizon | 新行動應用程式 |
```

**memory/people/{name}.md：**
```markdown
# Todd Martinez

**別名：** Todd、T
**角色：** 財務主管
**團隊：** 財務
**匯報對象：** 財務長（Michael Chen）

## 溝通方式
- 偏好 Slack 私訊
- 回覆迅速，非常直接
- 最佳時段：上午

## 背景脈絡
- 負責所有 PSR 及財務報告
- 超過 50 萬美元交易審批的關鍵聯絡人
- 與業務部門密切合作進行預測

## 備註
- 小熊隊球迷，喜歡聊棒球
```

**memory/projects/{name}.md：**
```markdown
# Phoenix 專案

**代號：** Phoenix
**別稱：**「the migration」
**狀態：** 進行中，Q2 上線

## 專案內容
從舊版 Oracle 資料庫遷移至 PostgreSQL。

## 關鍵人員
- Sarah - 技術負責人
- Todd - 預算負責人
- Greg - 利害關係人（業務影響）

## 背景脈絡
120 萬美元預算，6 個月時程。Horizon 專案的關鍵路徑。
```

**memory/context/company.md：**
```markdown
# 公司背景脈絡

## 工具與系統
| 工具 | 用途 | 內部名稱 |
|------|----------|---------------|
| Slack | 通訊 | - |
| Asana | 工程任務 | - |
| Salesforce | CRM |「SF」或「the CRM」 |
| Notion | 文件／知識庫 | - |

## 團隊
| 團隊 | 工作內容 | 關鍵人員 |
|------|--------------|------------|
| 平台 | 基礎設施 | Sarah（負責人） |
| 財務 | 財務相關 | Todd（負責人） |
| 業務 | 營收 | Greg |

## 流程
| 流程 | 意義 |
|---------|---------------|
| 每週同步 | 週一上午 10 點全員會議 |
| 發布審查 | 週四部署審批 |
```

## 如何互動

### 解碼使用者輸入（分層查詢）

**務必**在執行請求前先解碼簡稱：

```
1. CLAUDE.md（熱快取）     → 優先檢查，涵蓋 90% 的情況
2. memory/glossary.md      → 若不在熱快取中，查詢完整詞彙表
3. memory/people/、projects/ → 需要時查詢豐富細節
4. 詢問使用者              → 遇到未知術語？學習它。
```

範例：
```
使用者：「請 Todd 為 oracle 做 PSR」

CLAUDE.md 查詢：
  "todd" → Todd Martinez，財務 ✓
  "PSR" → 管線狀態報告 ✓
  "oracle" →（不在熱快取中）

memory/glossary.md 查詢：
  "oracle" → Oracle Systems 交易（230 萬美元）✓

現在 Claude 可以在完整脈絡下行動。
```

### 新增記憶

當使用者說「記住這個」或「X 的意思是 Y」時：

1. **詞彙表項目**（縮寫、術語、簡稱）：
   - 新增至 memory/glossary.md
   - 若經常使用，新增至 CLAUDE.md 快速詞彙表

2. **人員：**
   - 建立／更新 memory/people/{name}.md
   - 若重要則新增至 CLAUDE.md 關鍵人員
   - **記錄暱稱**——對解碼至關重要

3. **專案：**
   - 建立／更新 memory/projects/{name}.md
   - 若為當前專案則新增至 CLAUDE.md 進行中專案
   - **記錄代號**——「Phoenix」、「the migration」等

4. **偏好：** 新增至 CLAUDE.md 的偏好區段

### 回憶記憶

當使用者問「X 是誰」或「X 是什麼意思」時：

1. 先檢查 CLAUDE.md
2. 檢查 memory/ 獲取完整細節
3. 若未找到：「我目前不知道 X 是什麼意思。可以請你告訴我嗎？」

### 漸進式揭露

1. 載入 CLAUDE.md 以快速解析任何請求
2. 需要完整脈絡執行時深入 memory/
3. 範例：撰寫寄給 todd 關於 PSR 的電子郵件
   - CLAUDE.md 告訴你 Todd = Todd Martinez，PSR = 管線狀態報告
   - memory/people/todd-martinez.md 告訴你他偏好 Slack、說話直接

## 初始化

使用 `/productivity:start` 透過掃描你的聊天紀錄、行事曆、電子郵件及文件來初始化。擷取人員、專案，並開始建立詞彙表。

## 慣例

- CLAUDE.md 中對術語使用**粗體**以利快速瀏覽
- 將 CLAUDE.md 保持在約 100 行以內（「熱 30」規則）
- 檔名：小寫、使用連字號（`todd-martinez.md`、`project-phoenix.md`）
- 務必記錄暱稱及替代名稱
- 詞彙表使用表格以利快速查詢
- 當某項目頻繁使用時，提升至 CLAUDE.md
- 當某項目過時時，降級至 memory/ 即可

## 內容歸屬

| 類型 | CLAUDE.md（熱快取） | memory/（完整儲存） |
|------|----------------------|------------------------|
| 人員 | 前 30 位頻繁聯絡人 | glossary.md + people/{name}.md |
| 縮寫／術語 | 約 30 個最常見 | glossary.md（完整清單） |
| 專案 | 僅進行中專案 | glossary.md + projects/{name}.md |
| 暱稱 | 若為前 30 位則列入關鍵人員 | glossary.md（所有暱稱） |
| 公司脈絡 | 僅快速參考 | context/company.md |
| 偏好 | 所有偏好 | - |
| 歷史／過時 | ✗ 移除 | ✓ 保留於 memory/ |

## 提升／降級

**以下情況提升至 CLAUDE.md：**
- 你頻繁使用某術語／某人員
- 屬於進行中工作的一部分

**以下情況僅降級至 memory/：**
- 專案已完成
- 該人員不再是頻繁聯絡人
- 該術語很少使用

這能讓 CLAUDE.md 保持最新且相關。

<!-- translated-zh-TW -->
