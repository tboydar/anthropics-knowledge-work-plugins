# Connectors

## How tool references work

Plugin files use `~~category` as a placeholder for whatever tool the user connects in that category. For example, `~~project tracker` might mean Asana, Linear, Jira, or any other project tracker with an MCP server.

Plugins are **tool-agnostic** — they describe workflows in terms of categories (chat, project tracker, knowledge base, etc.) rather than specific products. The `.mcp.json` pre-configures specific MCP servers, but any MCP server in that category works.

## Connectors for this plugin

| Category | Placeholder | Included servers | Other options |
|----------|-------------|-----------------|---------------|
| Chat | `~~chat` | Slack | Microsoft Teams, Discord |
| Email | `~~email` | Microsoft 365 | — |
| Calendar | `~~calendar` | Microsoft 365 | — |
| Knowledge base | `~~knowledge base` | Notion | Confluence, Guru, Coda |
| Project tracker | `~~project tracker` | Asana, Linear, Atlassian (Jira/Confluence), monday.com, ClickUp | Shortcut, Basecamp, Wrike |
| Office suite | `~~office suite` | Microsoft 365 | — |

---

> **以下為繁體中文翻譯 · Traditional Chinese translation below**

# 連接器

## 工具參考的運作方式

外掛檔案使用 `~~category` 作為該類別中使用者所連接之工具的佔位符。例如，`~~project tracker` 可能代表 Asana、Linear、Jira，或任何其他具有 MCP 伺服器的專案追蹤工具。

外掛是**與工具無關**的——它們以類別（聊天、專案追蹤、知識庫等）來描述工作流程，而非特定產品。`.mcp.json` 預先設定了特定的 MCP 伺服器，但任何屬於該類別的 MCP 伺服器皆可使用。

## 此外掛的連接器

| 類別 | 佔位符 | 內建伺服器 | 其他選項 |
|----------|-------------|-----------------|---------------|
| 聊天 | `~~chat` | Slack | Microsoft Teams、Discord |
| 電子郵件 | `~~email` | Microsoft 365 | — |
| 行事曆 | `~~calendar` | Microsoft 365 | — |
| 知識庫 | `~~knowledge base` | Notion | Confluence、Guru、Coda |
| 專案追蹤 | `~~project tracker` | Asana、Linear、Atlassian (Jira/Confluence)、monday.com、ClickUp | Shortcut、Basecamp、Wrike |
| 辦公套件 | `~~office suite` | Microsoft 365 | — |

<!-- translated-zh-TW -->
