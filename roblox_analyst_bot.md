# Roblox Market Analyst Bot: Technical Specification

This module is a professional data-mining pipeline designed to target Roblox's distributed microservice backend endpoints. It programmatically extracts monetization frameworks and retention mechanics, generating compliance audit reports based on our Core Development Constitution.

---

## 🌐 Language Options
* [한국어 버전 (Korean Version)](./roblox_analyst_bot.ko.md)

---

## 🏗️ Architectural Blueprint

The pipeline executes a 3-step synchronization pattern: **[Ingestion ➔ Processing ➔ Markdown Automation]**.
[Roblox Core Web APIs]
│
├── games.roblox.com  ──> (CCU, Visits, Raw Up/Down Votes)
├── economy.roblox.com ──> (Pass Names, Price Points in Robux)
└── badges.roblox.com  ──> (Weekly Awarded Count & Funnel Metrics)
│
▼
[RobloxAnalystBot Engine] ──> Calculates Upvote Formula & Constitutional Mapping
│
▼
[market_analysis/*.md]   ──> Formatted Executive Strategic Reports

### 1. Multi-Endpoint Data Harvesting
* **`games.roblox.com`**: Captures baseline traffic matrices (Live Players, Cumulative Visits, Creation Stamps).
* **`economy.roblox.com`**: Extracts monetization metadata (`price`). It turns game-pass itemization into clean JSON matrices, mapping the spending triggers.
* **`badges.roblox.com`**: Tracks `pastWeekAwardedCount`. This acts as a quantitative funnel model to measure macro-progression retention without manual game execution.

### 2. Analytical Calculations & Inference
* **Algorithmic Voting Matrix**: Parses raw `upVotes` and `downVotes` to derive the live satisfaction index using the formula:
  $$\text{Upvote Ratio} = \frac{\text{upVotes}}{\text{upVotes} + \text{downVotes}} \times 100$$
* **Rule-Based Auditing**: Mechanically evaluates whether the experience qualifies under the 9-15 minute engagement rule or flags potential retention churn risks based on rating anomalies.

### 3. Rate-Limiting Mitigation
* Utilizes a non-intrusive scheduling sequence (`time.sleep`) to prevent IP throttling and comply with Roblox's backend infrastructure traffic rules.

---

## 💻 Installation & Execution

```bash
# Install required HTTP communication modules
pip install requests

# Execute the data-mining bot
python roblox_analyst_bot.py