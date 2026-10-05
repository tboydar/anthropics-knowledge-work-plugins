# Connectors

## How tool references work

Plugin files use `~~category` as a placeholder for whatever tool the user connects in that category. For example, `~~design tool` might mean Figma, Sketch, or any other design tool with an MCP server.

Plugins are **tool-agnostic** — they describe workflows in terms of categories (design tool, project tracker, user feedback, etc.) rather than specific products. The `.mcp.json` pre-configures specific MCP servers, but any MCP server in that category works.

## Connectors for this plugin

| Category | Placeholder | Included servers | Other options |
|----------|-------------|-----------------|---------------|
| Chat | `~~chat` | Slack | Microsoft Teams |
| Design tool | `~~design tool` | Figma | Sketch, Adobe XD, Framer |
| Knowledge base | `~~knowledge base` | Notion | Confluence, Guru, Coda |
| Project tracker | `~~project tracker` | Linear, Asana, Atlassian (Jira/Confluence) | Shortcut, ClickUp |
| User feedback | `~~user feedback` | Intercom | Productboard, Canny, UserVoice, Dovetail |
| Product analytics | `~~product analytics` | — | Amplitude, Mixpanel, Heap, FullStory |

---

> **以下為繁體中文翻譯 · Traditional Chinese translation below**

# 連接器

## 工具參考的運作方式

外掛檔案使用 `~~category` 作為佔位符，代表使用者在该類別中連接的任何工具。例如，`~~design tool` 可能代表 Figma、Sketch，或任何其他具備 MCP 伺服器的設計工具。

外掛是**與工具無關**的——它們以類別（設計工具、專案追蹤器、使用者回饋等）而非特定產品來描述工作流程。`.mcp.json` 預先設定了特定的 MCP 伺服器，但該類別中的任何 MCP 伺服器皆可使用。

## 此外掛的連接器

| 類別 | 佔位符 | 內建伺服器 | 其他選項 |
|----------|-------------|-----------------|---------------|
| 聊天 | `~~chat` | Slack | Microsoft Teams |
| 設計工具 | `~~design tool` | Figma | Sketch、Adobe XD、Framer |
| 知識庫 | `~~knowledge base` | Notion | Confluence、Guru、Coda |
| 專案追蹤器 | `~~project tracker` | Linear、Asana、Atlassian（Jira/Confluence） | Shortcut、ClickUp |
| 使用者回饋 | `~~user feedback` | Intercom | Productboard、Canny、UserVoice、Dovetail |
| 產品分析 | `~~product analytics` | — | Amplitude、Mixpanel、Heap、FullStory |

<!-- translated-zh-TW -->
