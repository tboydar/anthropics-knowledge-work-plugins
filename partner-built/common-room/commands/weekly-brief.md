---
description: "從您的日曆和 Common Room 產生每週準備簡報 | Generate a weekly prep briefing from your calendar and Common Room"
argument-hint: "日期範圍，預設為未來 7 天 | [date range, defaults to next 7 days]"
---

Generate a weekly prep briefing using Common Room and your calendar.

Follow the weekly-prep-brief skill:
1. Use the ~~calendar connector to retrieve all external customer-facing meetings scheduled for the next 7 days (or the date range specified in "$ARGUMENTS"). Filter out internal meetings — focus on calls with customers, prospects, or partners.
2. If no ~~calendar connector is available, ask the user to list their external calls (company name, date, attendees).
3. For each external meeting, run account research and contact research on attendees in parallel.
4. Compile into a single weekly briefing: week overview + per-meeting sections sorted by date.

Keep each per-meeting section tight and scannable. Total briefing should be readable in under 10 minutes.

---

> **以下為繁體中文翻譯 · Traditional Chinese translation below**

Generate a weekly prep briefing using Common Room and your calendar.

依照 weekly-prep-brief 技能執行：
1. 使用 ~~calendar 連接器擷取未來 7 天（或 "$ARGUMENTS" 中指定的日期範圍）所有外部客戶會議。篩除內部會議 — 專注於與客戶、潛在客戶或合作夥伴的通話。
2. 如果沒有可用的 ~~calendar 連接器，請要求使用者列出他們的外部通話（公司名稱、日期、與會者）。
3. 針對每場外部會議，並行執行帳戶研究與與會者聯絡人研究。
4. 彙整成單一週報：週總覽 + 依日期排序的各會議區段。

每個會議區段應保持精簡且易於掃讀。整份週報應可在 10 分鐘內閱讀完畢。

<!-- translated-zh-TW -->
