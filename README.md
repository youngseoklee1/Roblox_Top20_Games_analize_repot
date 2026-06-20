# Roblox_Top20_Games_analize_repot
This is the first step of my success story.

# Project Genesis: AI-Powered Roblox Startup

This repository serves as the core data-driven research architecture, business planning, and development logs for a 7-year Roblox entrepreneurial masterplan. 

---

## 🌐 Language Options
* [한국어 버전 (Korean Version)](./README.ko.md)

---

## 📜 The Roblox Constitution (Core Principles)
*Derived and verified from the official Roblox Developer Forum handbook: [How to actually make a popular game](https://devforum.roblox.com/t/how-to-actually-make-a-popular-game/3115791).*

To pass the Roblox recommendation algorithm and scale to the top charts, every experience built under this project must strictly satisfy the following three pillars:

### 1. Target Engagement & Playtime
* **Metric**: Average playtime must hit **9 to 15 minutes** (Excellent tier) or 15+ minutes (Crazy good tier).
* **Strategy**: Implement tight core loops that prevent early bounces within the first 5 minutes.

### 2. Retention-Driven Core Loop
* **Principle**: Create a flexible, infinitely replayable system (e.g., trading economies, prestiges, incremental rewards).
* **Strategy**: Ensure players always have a clear macro-goal and micro-rewards every 3 minutes.

### 3. Data-Driven Pivot Evaluation
* **Principle**: The fate of a Roblox game is entirely decided within the first **10 to 25 days** of its data tracking window.
* **Strategy**: Run precision targeted test ads to gather baseline analytics. If core metrics fail to hit the algorithmic threshold within this window, abandon/pivot without emotional attachment.

---

## 📊 Phase 1: Top 20 Experiences Reverse-Engineering List
*The detailed architectural breakdown of top-charting games is documented chronologically below:*

| # | Experience Name | Universe ID | Category & Core Focus | Analysis Link | Status |
| :---: | :--- | :---: | :--- | :---: | :---: |
| 01 | **Grow a Garden 2** | `10200395747` | Incremental Tycoon / Viral Social Stealing Loop | [View Report](./market_analysis/auto_Grow_a_Garden_2_10200395747.md) | 🟢 Complete |
| 02 | **RIVALS** | `6035872082` | 1v1 Arena Shooter / Social Flexing Vanity BM | [View Report](./market_analysis/auto_RIVALS_6035872082.md) | 🟢 Complete |
| 03 | **Blox Fruits** | `994732206` | Open World Anime RPG / Macro Funnel Progression Retention | [View Report](./market_analysis/auto_Blox_Fruits_994732206.md) | 🟢 Complete |
| 04 | **Jujutsu Shenanigans** | `3508322461` | Sandbox Battlegrounds / Short Viral CTR Optimization | [View Report](./market_analysis/auto_[BLACK_DEATH]_Jujutsu_Shenanigans_3508322461.md) | 🟢 Complete |

---

## 🚀 Roblox Top 20 Games Market Analysis Pipeline
A professional data-mining pipeline designed to target the backend microservice endpoints of top-tier Roblox experiences to extract quantitative traffic metrics and retention architectures.

### 🛠️ Automated Analytics Engine Tools
* **Source Code**: [`roblox_analyst_bot.py`](./roblox_analyst_bot.py)
* **Technical Documentation**: [English Specification](./roblox_analyst_bot.md) | [한국어 명세서](./roblox_analyst_bot.ko.md)

---

## 📅 Development Log & Milestones

### 📌 [Day 1] Core Engine Deployment & Data Churn Barriers (2026-06-20)
* **Key Achievements**:
    * Successfully deployed `RobloxAnalystBot (V2)` Python infrastructure and linked multi-language technical specifications (`roblox_analyst_bot.md`, `roblox_analyst_bot.ko.md`).
    * Mapped out the platform's multi-tiered architecture (Place ID vs. Universe ID) and programmatically mined the exact Universe IDs for 4 core marketplace monsters listed in Phase 1.
    * Perfected the data ingestion pipeline for real-time CCU, total visit counts, and macroeconomic macro-progression via player badge win rates (Win Rate %).
* **Identified Technical Limitations (Future Backlog)**:
    * **The Issue**: Section 2 (Monetization: Game Passes / Developer Products) outputs empty matrices (`0 items found`) for top earning games like `Grow a Garden 2`.
    * **Root-Cause Analysis**: Major studios have locked down standard endpoints or enforced strict session-cookie header validation to prevent external scrapers. Additionally, their marketplace monetization layer is hard-linked inside internal Developer Products arrays rather than public game-pass endpoints.
    * **Conclusion**: Day 1 baseline is frozen with comprehensive traffic and retention distribution models. This data harvesting mismatch will be documented as a structural API constraint for the executive report. Upgrading to proxy-cookie injection remains a backlog item.