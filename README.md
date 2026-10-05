# Knowledge Work Plugins

Plugins that turn Claude into a specialist for your role, team, and company. Built for [Claude Cowork](https://claude.com/product/cowork), also compatible with [Claude Code](https://claude.com/product/claude-code).

## Why Plugins

Cowork lets you set the goal and Claude delivers finished, professional work. Plugins let you go further: tell Claude how you like work done, which tools and data to pull from, how to handle critical workflows, and what slash commands to expose — so your team gets better and more consistent outcomes.

Each plugin bundles the skills, connectors, slash commands, and sub-agents for a specific job function. Out of the box, they give Claude a strong starting point for helping anyone in that role. The real power comes when you customize them for your company — your tools, your terminology, your processes — so Claude works like it was built for your team.

## Plugin Marketplace

We're open-sourcing 11 plugins built and inspired by our own work:

| Plugin | How it helps | Connectors |
|--------|-------------|------------|
| **[productivity](./productivity)** | Manage tasks, calendars, daily workflows, and personal context so you spend less time repeating yourself. | Slack, Notion, Asana, Linear, Jira, Monday, ClickUp, Microsoft 365 |
| **[sales](./sales)** | Research prospects, prep for calls, review your pipeline, draft outreach, and build competitive battlecards. | Slack, HubSpot, Close, Clay, ZoomInfo, Notion, Jira, Fireflies, Microsoft 365 |
| **[customer-support](./customer-support)** | Triage tickets, draft responses, package escalations, research customer context, and turn resolved issues into knowledge base articles. | Slack, Intercom, HubSpot, Guru, Jira, Notion, Microsoft 365 |
| **[product-management](./product-management)** | Write specs, plan roadmaps, synthesize user research, keep stakeholders updated, and track the competitive landscape. | Slack, Linear, Asana, Monday, ClickUp, Jira, Notion, Figma, Amplitude, Pendo, Intercom, Fireflies |
| **[marketing](./marketing)** | Draft content, plan campaigns, enforce brand voice, brief on competitors, and report on performance across channels. | Slack, Canva, Figma, HubSpot, Amplitude, Notion, Ahrefs, SimilarWeb, Klaviyo |
| **[legal](./legal)** | Review contracts, triage NDAs, navigate compliance, assess risk, prep for meetings, and draft templated responses. | Slack, Box, Egnyte, Jira, Microsoft 365 |
| **[finance](./finance)** | Prep journal entries, reconcile accounts, generate financial statements, analyze variances, manage close, and support audits. | Snowflake, Databricks, BigQuery, Slack, Microsoft 365 |
| **[data](./data)** | Query, visualize, and interpret datasets — write SQL, run statistical analysis, build dashboards, and validate your work before sharing. | Snowflake, Databricks, BigQuery, Definite, Hex, Amplitude, Jira |
| **[enterprise-search](./enterprise-search)** | Find anything across email, chat, docs, and wikis — one query across all your company's tools. | Slack, Notion, Guru, Jira, Asana, Microsoft 365 |
| **[bio-research](./bio-research)** | Connect to preclinical research tools and databases (literature search, genomics analysis, target prioritization) to accelerate early-stage life sciences R&D. | PubMed, BioRender, bioRxiv, ClinicalTrials.gov, ChEMBL, Synapse, Wiley, Owkin, Open Targets, Benchling |
| **[cowork-plugin-management](./cowork-plugin-management)** | Create new plugins or customize existing ones for your organization's specific tools and workflows. | — |

Install these directly from Cowork, browse the full collection here on GitHub, or build your own.

## Getting Started

### Cowork

Install plugins from [claude.com/plugins](https://claude.com/plugins/).

### Claude Code

```bash
# Add the marketplace first
claude plugin marketplace add anthropics/knowledge-work-plugins

# Then install a specific plugin
claude plugin install sales@knowledge-work-plugins
```

Once installed, plugins activate automatically. Skills fire when relevant, and slash commands are available in your session (e.g., `/sales:call-prep`, `/data:write-query`).

## How Plugins Work

Every plugin follows the same structure:

```
plugin-name/
├── .claude-plugin/plugin.json   # Manifest
├── .mcp.json                    # Tool connections
├── commands/                    # Slash commands you invoke explicitly
└── skills/                      # Domain knowledge Claude draws on automatically
```

- **Skills** encode the domain expertise, best practices, and step-by-step workflows Claude needs to give you useful help. Claude draws on them automatically when relevant.
- **Commands** are explicit actions you trigger (e.g., `/finance:reconciliation`, `/product-management:write-spec`).
- **Connectors** wire Claude to the external tools your role depends on — CRMs, project trackers, data warehouses, design tools, and more — via [MCP servers](https://modelcontextprotocol.io/).

Every component is file-based — markdown and JSON, no code, no infrastructure, no build steps.

## Making Them Yours

These plugins are generic starting points. They become much more useful when you customize them for how your company actually works:

- **Swap connectors** — Edit `.mcp.json` to point at your specific tool stack.
- **Add company context** — Drop your terminology, org structure, and processes into skill files so Claude understands your world.
- **Adjust workflows** — Modify skill instructions to match how your team actually does things, not how a textbook says to.
- **Build new plugins** — Use the `cowork-plugin-management` plugin or follow the structure above to create plugins for roles and workflows we haven't covered yet.

As your team builds and shares plugins, Claude becomes a cross-functional expert. The context you define gets baked into every relevant interaction, so leaders and admins can spend less time enforcing processes and more time improving them.

## Contributing

Plugins are just markdown files. Fork the repo, make your changes, and submit a PR.

---

> **以下為繁體中文翻譯 · Traditional Chinese translation below**

# 知識工作外掛程式

這些外掛程式能將 Claude 打造成您職位、團隊與公司的專屬專家。專為 [Claude Cowork](https://claude.com/product/cowork) 打造，也相容於 [Claude Code](https://claude.com/product/claude-code)。

## 為什麼需要外掛程式

Cowork 讓您設定目標，由 Claude 交付專業完成的工作。外掛程式更進一步：告訴 Claude 您偏好的工作方式、應使用的工具與資料來源、如何處理關鍵工作流程，以及要提供哪些斜線指令——讓團隊獲得更好且更一致的工作成果。

每個外掛程式都為特定職能整合了技能（skills）、連接器（connectors）、斜線指令（slash commands）與子代理（sub-agents）。開箱即用時，它們為 Claude 提供協助該職位人員的堅實起點。真正的威力來自於您針對公司進行客製化——您的工具、您的術語、您的流程——讓 Claude 彷彿是為您的團隊量身打造。

## 外掛程式市集

我們將 11 個由我們自身工作啟發並打造的實作開源：

| 外掛程式 | 協助方式 | 連接器 |
|--------|-------------|------------|
| **[生產力](./productivity)** | 管理任務、行事曆、日常工作流程與個人脈絡，減少重複說明所花費的時間。 | Slack、Notion、Asana、Linear、Jira、Monday、ClickUp、Microsoft 365 |
| **[業務](./sales)** | 研究潛在客戶、準備通話、檢視銷售管道、草擬外聯訊息，並建立競爭者戰情卡。 | Slack、HubSpot、Close、Clay、ZoomInfo、Notion、Jira、Fireflies、Microsoft 365 |
| **[客戶支援](./customer-support)** | 分類工單、草擬回覆、整理升級案件、研究客戶脈絡，並將已解決問題轉化為知識庫文章。 | Slack、Intercom、HubSpot、Guru、Jira、Notion、Microsoft 365 |
| **[產品管理](./product-management)** | 撰寫規格、規劃產品藍圖、彙整使用者研究、讓利害關係人掌握進度，並追蹤競爭態勢。 | Slack、Linear、Asana、Monday、ClickUp、Jira、Notion、Figma、Amplitude、Pendo、Intercom、Fireflies |
| **[行銷](./marketing)** | 草擬內容、規劃活動、貫徹品牌語調、提供競爭者簡報，並回報跨渠道成效。 | Slack、Canva、Figma、HubSpot、Amplitude、Notion、Ahrefs、SimilarWeb、Klaviyo |
| **[法務](./legal)** | 審閱合約、分類保密協議、處理合規事宜、評估風險、準備會議，並草擬範本回覆。 | Slack、Box、Egnyte、Jira、Microsoft 365 |
| **[財務](./finance)** | 準備分錄、核對帳戶、產生財務報表、分析差異、管理結帳流程，並支援稽核。 | Snowflake、Databricks、BigQuery、Slack、Microsoft 365 |
| **[資料](./data)** | 查詢、視覺化並解讀資料集——撰寫 SQL、執行統計分析、建置儀表板，並在分享前驗證工作成果。 | Snowflake、Databricks、BigQuery、Definite、Hex、Amplitude、Jira |
| **[企業搜尋](./enterprise-search)** | 在電子郵件、聊天、文件與 Wiki 中尋找任何內容——一個查詢橫跨公司所有工具。 | Slack、Notion、Guru、Jira、Asana、Microsoft 365 |
| **[生醫研究](./bio-research)** | 連接臨床前研究工具與資料庫（文獻搜尋、基因體分析、標靶優先排序），加速早期生命科學研發。 | PubMed、BioRender、bioRxiv、ClinicalTrials.gov、ChEMBL、Synapse、Wiley、Owkin、Open Targets、Benchling |
| **[Cowork 外掛程式管理](./cowork-plugin-management)** | 建立新外掛程式或針對組織的特定工具與工作流程客製化現有外掛程式。 | — |

可直接從 Cowork 安裝這些外掛程式、在 GitHub 瀏覽完整收藏，或自行建立。

## 開始使用

### Cowork

從 [claude.com/plugins](https://claude.com/plugins/) 安裝外掛程式。

### Claude Code

```bash
# 先新增市集（此為繁體中文分叉版本）
claude plugin marketplace add tboydar/anthropics-knowledge-work-plugins

# 然後安裝特定外掛程式
claude plugin install sales@knowledge-work-plugins
```

安裝完成後，外掛程式會自動啟用。技能會在相關情境下自動觸發，斜線指令則可在工作階段中使用（例如 `/sales:call-prep`、`/data:write-query`）。

## 外掛程式的運作方式

每個外掛程式都遵循相同的結構：

```
plugin-name/
├── .claude-plugin/plugin.json   # 資訊清單
├── .mcp.json                    # 工具連線
├── commands/                    # 您明確呼叫的斜線指令
└── skills/                      # Claude 自動參考的領域知識
```

- **技能**編碼了 Claude 提供實用協助所需的領域專業、最佳實務與逐步工作流程。Claude 會在相關情境下自動參考。
- **指令**是您明確觸發的動作（例如 `/finance:reconciliation`、`/product-management:write-spec`）。
- **連接器**透過 [MCP 伺服器](https://modelcontextprotocol.io/) 將 Claude 連接到您職位依賴的外部工具——CRM、專案追蹤器、資料倉儲、設計工具等。

每個元件都以檔案為基礎——Markdown 與 JSON，不需要程式碼、基礎設施或建置步驟。

## 打造屬於您的外掛程式

這些外掛程式是通用的起點。當您針對公司實際運作方式進行客製化後，它們會變得更加實用：

- **更換連接器**——編輯 `.mcp.json` 指向您的特定工具組合。
- **加入公司脈絡**——將您的術語、組織結構與流程放入技能檔案，讓 Claude 理解您的世界。
- **調整工作流程**——修改技能指示以符合團隊實際做法，而非教科書所述。
- **建立新外掛程式**——使用 `cowork-plugin-management` 外掛程式，或依照上述結構為我們尚未涵蓋的職位與工作流程建立新外掛程式。

當您的團隊建立並分享外掛程式時，Claude 便會成為跨職能專家。您定義的脈絡會融入每一次相關互動，讓主管和管理者能花更少時間執行流程，更多時間改善流程。

## 貢獻

外掛程式只是 Markdown 檔案。Fork 此儲存庫、進行變更並提交 Pull Request 即可。

<!-- translated-zh-TW -->
