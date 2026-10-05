---
name: ticket-triage
description: Triage and prioritize a support ticket or customer issue. Use when a new ticket comes in and needs categorization, assigning P1-P4 priority, deciding which team should handle it, or checking whether it's a duplicate or known issue before routing.
argument-hint: "<ticket or issue description>"
---

# /ticket-triage

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Categorize, prioritize, and route an incoming support ticket or customer issue. Produces a structured triage assessment with a suggested initial response.

## Usage

```
/ticket-triage <ticket text, customer message, or issue description>
```

Examples:
- `/ticket-triage Customer says their dashboard has been showing a blank page since this morning`
- `/ticket-triage "I was charged twice for my subscription this month"`
- `/ticket-triage User can't connect their SSO — getting a 403 error on the callback URL`
- `/ticket-triage Feature request: they want to export reports as PDF`

## Workflow

### 1. Parse the Issue

Read the input and extract:

- **Core problem**: What is the customer actually experiencing?
- **Symptoms**: What specific behavior or error are they seeing?
- **Customer context**: Who is this? Any account details, plan level, or history available?
- **Urgency signals**: Are they blocked? Is this production? How many users affected?
- **Emotional state**: Frustrated, confused, matter-of-fact, escalating?

### 2. Categorize and Prioritize

Using the category taxonomy and priority framework below:

- Assign a **primary category** (bug, how-to, feature request, billing, account, integration, security, data, performance) and an optional secondary category
- Assign a **priority** (P1–P4) based on impact and urgency
- Identify the **product area** the issue maps to

### 3. Check for Duplicates and Known Issues

Before routing, check available sources:

- **~~support platform**: Search for similar open or recently resolved tickets
- **~~knowledge base**: Check for known issues or existing documentation
- **~~project tracker**: Check if there's an existing bug report or feature request

Apply the duplicate detection process below.

### 4. Determine Routing

Using the routing rules below, recommend which team or queue should handle this based on category and complexity.

### 5. Generate Triage Output

```
## Triage: [One-line issue summary]

**Category:** [Primary] / [Secondary if applicable]
**Priority:** [P1-P4] — [Brief justification]
**Product area:** [Area/team]

### Issue Summary
[2-3 sentence summary of what the customer is experiencing]

### Key Details
- **Customer:** [Name/account if known]
- **Impact:** [Who and what is affected]
- **Workaround:** [Available / Not available / Unknown]
- **Related tickets:** [Links to similar issues if found]
- **Known issue:** [Yes — link / No / Checking]

### Routing Recommendation
**Route to:** [Team or queue]
**Why:** [Brief reasoning]

### Suggested Initial Response
[Draft first response to the customer — acknowledge the issue,
set expectations, provide workaround if available.
Use the auto-response templates below as a starting point.]

### Internal Notes
- [Any additional context for the agent picking this up]
- [Reproduction hints if it's a bug]
- [Escalation triggers to watch for]
```

### 6. Offer Next Steps

After presenting the triage:
- "Want me to draft a full response to the customer?"
- "Should I search for more context on this issue?"
- "Want me to check if this is a known bug in the tracker?"
- "Should I escalate this? I can package it with /customer-escalation."

---

## Category Taxonomy

Assign every ticket a **primary category** and optionally a **secondary category**:

| Category | Description | Signal Words |
|----------|-------------|-------------|
| **Bug** | Product is behaving incorrectly or unexpectedly | Error, broken, crash, not working, unexpected, wrong, failing |
| **How-to** | Customer needs guidance on using the product | How do I, can I, where is, setting up, configure, help with |
| **Feature request** | Customer wants a capability that doesn't exist | Would be great if, wish I could, any plans to, requesting |
| **Billing** | Payment, subscription, invoice, or pricing issues | Charge, invoice, payment, subscription, refund, upgrade, downgrade |
| **Account** | Account access, permissions, settings, or user management | Login, password, access, permission, SSO, locked out, can't sign in |
| **Integration** | Issues connecting to third-party tools or APIs | API, webhook, integration, connect, OAuth, sync, third-party |
| **Security** | Security concerns, data access, or compliance questions | Data breach, unauthorized, compliance, GDPR, SOC 2, vulnerability |
| **Data** | Data quality, migration, import/export issues | Missing data, export, import, migration, incorrect data, duplicates |
| **Performance** | Speed, reliability, or availability issues | Slow, timeout, latency, down, unavailable, degraded |

### Category Determination Tips

- If the customer reports **both** a bug and a feature request, the bug is primary
- If they can't log in due to a bug, category is **Bug** (not Account) — root cause drives the category
- "It used to work and now it doesn't" = **Bug**
- "I want it to work differently" = **Feature request**
- "How do I make it work?" = **How-to**
- When in doubt, lean toward **Bug** — it's better to investigate than dismiss

## Priority Framework

### P1 — Critical
**Criteria:** Production system down, data loss or corruption, security breach, all or most users affected.

- The customer cannot use the product at all
- Data is being lost, corrupted, or exposed
- A security incident is in progress
- The issue is worsening or expanding in scope

**SLA expectation:** Respond within 1 hour. Continuous work until resolved or mitigated. Updates every 1-2 hours.

### P2 — High
**Criteria:** Major feature broken, significant workflow blocked, many users affected, no workaround.

- A core workflow is broken but the product is partially usable
- Multiple users are affected or a key account is impacted
- The issue is blocking time-sensitive work
- No reasonable workaround exists

**SLA expectation:** Respond within 4 hours. Active investigation same day. Updates every 4 hours.

### P3 — Medium
**Criteria:** Feature partially broken, workaround available, single user or small team affected.

- A feature isn't working correctly but a workaround exists
- The issue is inconvenient but not blocking critical work
- A single user or small team is affected
- The customer is not escalating urgently

**SLA expectation:** Respond within 1 business day. Resolution or update within 3 business days.

### P4 — Low
**Criteria:** Minor inconvenience, cosmetic issue, general question, feature request.

- Cosmetic or UI issues that don't affect functionality
- Feature requests and enhancement ideas
- General questions or how-to inquiries
- Issues with simple, documented solutions

**SLA expectation:** Respond within 2 business days. Resolution at normal pace.

### Priority Escalation Triggers

Automatically bump priority up when:
- Customer has been waiting longer than the SLA allows
- Multiple customers report the same issue (pattern detected)
- The customer explicitly escalates or mentions executive involvement
- A workaround that was in place stops working
- The issue expands in scope (more users, more data, new symptoms)

## Routing Rules

Route tickets based on category and complexity:

| Route to | When |
|----------|------|
| **Tier 1 (frontline support)** | How-to questions, known issues with documented solutions, billing inquiries, password resets |
| **Tier 2 (senior support)** | Bugs requiring investigation, complex configuration, integration troubleshooting, account issues |
| **Engineering** | Confirmed bugs needing code fixes, infrastructure issues, performance degradation |
| **Product** | Feature requests with significant demand, design decisions, workflow gaps |
| **Security** | Data access concerns, vulnerability reports, compliance questions |
| **Billing/Finance** | Refund requests, contract disputes, complex billing adjustments |

## Duplicate Detection

Before creating a new ticket or routing, check for duplicates:

1. **Search by symptom**: Look for tickets with similar error messages or descriptions
2. **Search by customer**: Check if this customer has an open ticket for the same issue
3. **Search by product area**: Look for recent tickets in the same feature area
4. **Check known issues**: Compare against documented known issues

**If a duplicate is found:**
- Link the new ticket to the existing one
- Notify the customer that this is a known issue being tracked
- Add any new information from the new report to the existing ticket
- Bump priority if the new report adds urgency (more customers affected, etc.)

## Auto-Response Templates by Category

### Bug — Initial Response
```
Thank you for reporting this. I can see how [specific impact]
would be disruptive for your work.

I've logged this as a [priority] issue and our team is
investigating. [If workaround exists: "In the meantime, you
can [workaround]."]

I'll update you within [SLA timeframe] with what we find.
```

### How-to — Initial Response
```
Great question! [Direct answer or link to documentation]

[If more complex: "Let me walk you through the steps:"]
[Steps or guidance]

Let me know if that helps, or if you have any follow-up
questions.
```

### Feature Request — Initial Response
```
Thank you for this suggestion — I can see why [capability]
would be valuable for your workflow.

I've documented this and shared it with our product team.
While I can't commit to a specific timeline, your feedback
directly informs our roadmap priorities.

[If alternative exists: "In the meantime, you might find
[alternative] helpful for achieving something similar."]
```

### Billing — Initial Response
```
I understand billing issues need prompt attention. Let me
look into this for you.

[If straightforward: resolution details]
[If complex: "I'm reviewing your account now and will have
an answer for you within [timeframe]."]
```

### Security — Initial Response
```
Thank you for flagging this — we take security concerns
seriously and are reviewing this immediately.

I've escalated this to our security team for investigation.
We'll follow up with you within [timeframe] with our findings.

[If action is needed: "In the meantime, we recommend
[protective action]."]
```

## Triage Best Practices

1. Read the full ticket before categorizing — context in later messages often changes the assessment
2. Categorize by **root cause**, not just the symptom described
3. When in doubt on priority, err on the side of higher — it's easier to de-escalate than to recover from a missed SLA
4. Always check for duplicates and known issues before routing
5. Write internal notes that help the next person pick up context quickly
6. Include what you've already checked or ruled out to avoid duplicate investigation
7. Flag patterns — if you're seeing the same issue repeatedly, escalate the pattern even if individual tickets are low priority

---

> **以下為繁體中文翻譯 · Traditional Chinese translation below**

# /ticket-triage

> 如果您看到不熟悉的佔位符號，或需要確認已連接哪些工具，請參閱 [CONNECTORS.md](../../CONNECTORS.md)。

分類、排序並分派收到的支援單或客戶問題。產出結構化的分流評估，並附上建議的初步回覆。

## 使用方式

```
/ticket-triage <票單內容、客戶訊息或問題描述>
```

範例：
- `/ticket-triage 客戶表示他們的儀表板從今天早上開始就一直顯示空白頁面`
- `/ticket-triage「我這個月被重複扣款了兩次訂閱費用」`
- `/ticket-triage 使用者無法連接他們的 SSO——在回呼 URL 上收到 403 錯誤`
- `/ticket-triage 功能請求：他們想要將報表匯出為 PDF`

## 工作流程

### 1. 解析問題

閱讀輸入內容並擷取：

- **核心問題**：客戶實際上遇到了什麼情況？
- **症狀**：他們看到哪些具體的行為或錯誤？
- **客戶背景**：這是誰？是否有可用的帳戶詳細資料、方案等級或歷史記錄？
- **緊急訊號**：他們是否受阻？這是否影響生產環境？有多少使用者受到影響？
- **情緒狀態**：沮喪、困惑、就事論事、情緒升高中？

### 2. 分類與排序

使用下方分類架構與優先級框架：

- 指定一個**主要類別**（錯誤、操作指引、功能請求、帳單、帳戶、整合、安全性、資料、效能），並可選擇性地指定次要類別
- 根據影響程度與緊急性指定**優先級**（P1–P4）
- 確認問題對應的**產品領域**

### 3. 檢查重複項目與已知問題

在分派前，檢查可用的來源：

- **~~支援平台**：搜尋類似且開啟中或近期已解決的票單
- **~~知識庫**：檢查是否有已知問題或既有文件
- **~~專案追蹤系統**：檢查是否已有既有的錯誤回報或功能請求

套用下方重複項目偵測流程。

### 4. 決定分派對象

根據下方分派規則，根據類別與複雜度，建議應由哪個團隊或佇列處理。

### 5. 產生分流輸出

```
## 分流：[一句話的議題摘要]

**類別：** [主要類別] / [次要類別（如適用）]
**優先級：** [P1-P4] — [簡短理由]
**產品領域：** [領域/團隊]

### 議題摘要
[2-3 句描述客戶遇到的情況]

### 關鍵細節
- **客戶：** [姓名/帳戶（如已知）]
- **影響範圍：** [受影響的對象與內容]
- **替代方案：** [可用 / 不可用 / 未知]
- **相關票單：** [如找到類似議題的連結]
- **已知問題：** [是 — 連結 / 否 / 確認中]

### 分派建議
**分派至：** [團隊或佇列]
**原因：** [簡短說明]

### 建議的初步回覆
[草擬給客戶的第一則回覆 —— 確認問題、
設定期望、如可行提供替代方案。
以下方的自動回覆範本作為起點。]

### 內部備註
- [提供接手處理的專員任何額外背景資訊]
- [如果是錯誤，提供重現提示]
- [需留意的升級觸發條件]
```

### 6. 提供後續步驟

呈現分流結果後：
- 「需要我草擬一封完整的回覆給客戶嗎？」
- 「需要我搜尋更多關於此議題的相關資訊嗎？」
- 「需要我檢查追蹤系統中是否已有已知錯誤嗎？」
- 「需要我升級處理嗎？我可以搭配 /customer-escalation 一起打包。」

---

## 分類架構

為每張票單指定一個**主要類別**，並可選擇性地指定**次要類別**：

| 類別 | 描述 | 訊號詞 |
|----------|-------------|-------------|
| **錯誤** | 產品行為不正確或出乎意料 | 錯誤、壞掉、當機、無法運作、異常、錯誤的、失敗中 |
| **操作指引** | 客戶需要產品使用上的引導 | 該怎麼做、能不能、在哪裡、設定中、組態、需要協助 |
| **功能請求** | 客戶想要目前不存在的功能 | 如果有……就好了、希望可以、是否有計畫、請求 |
| **帳單** | 付款、訂閱、發票或定價問題 | 扣款、發票、付款、訂閱、退款、升級、降級 |
| **帳戶** | 帳戶存取、權限、設定或使用者管理 | 登入、密碼、存取、權限、SSO、被鎖定、無法登入 |
| **整合** | 連接第三方工具或 API 的問題 | API、Webhook、整合、連接、OAuth、同步、第三方 |
| **安全性** | 安全疑慮、資料存取或合規問題 | 資料外洩、未經授權、合規、GDPR、SOC 2、漏洞 |
| **資料** | 資料品質、遷移、匯入/匯出問題 | 資料遺失、匯出、匯入、遷移、資料不正確、重複 |
| **效能** | 速度、可靠性或可用性問題 | 緩慢、逾時、延遲、當機、無法使用、效能下降 |

### 分類判定技巧

- 如果客戶同時回報**錯誤**和**功能請求**，則以錯誤為主要類別
- 如果他們因為錯誤而無法登入，類別應為**錯誤**（而非帳戶）——根本原因決定類別
- 「以前可以用，現在不行」= **錯誤**
- 「我希望它能有不同的運作方式」= **功能請求**
- 「要怎麼讓它運作？」= **操作指引**
- 不確定時，傾向歸類為**錯誤**——先調查總比直接排除好

## 優先級框架

### P1 — 重大
**條件：** 生產系統停機、資料遺失或毀損、安全漏洞、全部或大部分使用者受到影響。

- 客戶完全無法使用產品
- 資料正在遺失、毀損或外洩
- 安全事件正在發生中
- 問題正在惡化或影響範圍持續擴大

**SLA 期望：** 1 小時內回覆。持續處理直到解決或緩解。每 1-2 小時更新一次。

### P2 — 高
**條件：** 主要功能損壞、重要工作流程受阻、許多使用者受到影響、無替代方案。

- 核心工作流程損壞，但產品仍可部分使用
- 多位使用者受到影響，或關鍵帳戶受到衝擊
- 問題阻礙了有時效性的工作
- 沒有合理的替代方案

**SLA 期望：** 4 小時內回覆。當天進行主動調查。每 4 小時更新一次。

### P3 — 中
**條件：** 功能部分損壞、有替代方案、單一使用者或少數團隊受到影響。

- 功能運作不正常，但存在替代方案
- 問題造成不便，但未阻礙關鍵工作
- 單一使用者或少數團隊受到影響
- 客戶未緊急要求升級

**SLA 期望：** 1 個工作天內回覆。3 個工作天內解決或更新。

### P4 — 低
**條件：** 輕微不便、外觀問題、一般性問題、功能請求。

- 不影響功能的外觀或 UI 問題
- 功能請求與改進建議
- 一般性問題或操作指引詢問
- 有簡單且有文件記載解決方案的問題

**SLA 期望：** 2 個工作天內回覆。以正常速度解決。

### 優先級升級觸發條件

在以下情況自動調升優先級：
- 客戶等待時間已超過 SLA 允許範圍
- 多位客戶回報相同問題（偵測到模式）
- 客戶明確要求升級或提及高層介入
- 原本生效的替代方案失效
- 問題影響範圍擴大（更多使用者、更多資料、新的症狀）

## 分派規則

根據類別與複雜度分派票單：

| 分派對象 | 時機 |
|----------|------|
| **第一線支援** | 操作指引問題、有文件化解決方案的已知問題、帳單詢問、密碼重設 |
| **第二線支援** | 需要調查的錯誤、複雜組態、整合故障排除、帳戶問題 |
| **工程部門** | 需要程式碼修正的已確認錯誤、基礎設施問題、效能下降 |
| **產品部門** | 有顯著需求的功能請求、設計決策、工作流程缺口 |
| **安全部門** | 資料存取疑慮、漏洞回報、合規問題 |
| **帳務/財務部門** | 退款請求、合約糾紛、複雜的帳務調整 |

## 重複項目偵測

在建立新票單或分派前，檢查是否有重複：

1. **依症狀搜尋**：尋找具有類似錯誤訊息或描述的票單
2. **依客戶搜尋**：檢查此客戶是否已有針對相同問題的開啟中票單
3. **依產品領域搜尋**：尋找相同功能領域的近期待處理票單
4. **檢查已知問題**：與有文件記載的已知問題進行比對

**如果找到重複項目：**
- 將新票單連結至既有的票單
- 通知客戶這是正在追蹤中的已知問題
- 將新回報中的任何新資訊新增至既有票單
- 如果新回報增加了緊急性（更多客戶受影響等），則調升優先級

## 依類別的自動回覆範本

### 錯誤 — 初步回覆
```
感謝您回報此問題。我能理解 [具體影響]
會對您的工作造成多大的干擾。

我已將此記錄為 [優先級] 問題，我們的團隊正在
調查中。[如果存在替代方案：「在此期間，您可以
[替代方案]。」]

我會在 [SLA 時限] 內向您更新我們的發現。
```

### 操作指引 — 初步回覆
```
好問題！[直接回答或提供文件連結]

[如果較複雜：「讓我逐步引導您：」]
[步驟或指引]

請讓我知道這是否有幫助，或您是否還有其他
問題。
```

### 功能請求 — 初步回覆
```
感謝您的建議 —— 我能理解 [功能]
為何會對您的工作流程有價值。

我已記錄此建議並分享給我們的產品團隊。
雖然我無法承諾具體時程，但您的回饋會直接
影響我們的路線圖優先順序。

[如果存在替代方案：「在此期間，您可能會發現
[替代方案] 有助於達成類似目標。」]
```

### 帳單 — 初步回覆
```
我了解帳單問題需要立即處理。讓我為您
調查此事。

[如果單純：解決方案細節]
[如果複雜：「我正在檢視您的帳戶，並會在
[時限] 內給您答覆。」]
```

### 安全性 — 初步回覆
```
感謝您提出此問題 —— 我們非常重視安全疑慮，
並正在立即審查此事。

我已將此升級至我們的安全團隊進行調查。
我們會在 [時限] 內與您聯繫並告知調查結果。

[如果需要採取行動：「在此期間，我們建議
[防護措施]。」]
```

## 分流最佳實務

1. 在分類前完整閱讀票單——後續訊息中的背景資訊常會改變評估結果
2. 依**根本原因**分類，而非僅依描述的症狀
3. 優先級不確定時，寧可從高——降級比錯過 SLA 之後再彌補容易
4. 分派前務必檢查重複項目與已知問題
5. 撰寫能幫助下一位接手者快速掌握背景的內部備註
6. 包含您已檢查或已排除的項目，以避免重複調查
7. 標記模式——如果您反覆看到相同問題，即使個別票單優先級低，也應升級處理該模式

<!-- translated-zh-TW -->
