# 📈 Layer 2 Macro-Economics: Base Network Growth & Revenue Dashboard

**Tech Stack:** `SQL (Dune Analytics)` | `Python (Pandas, Matplotlib)` | `API Integration`

## 📝 Project Overview
As the Web3 ecosystem scales, Layer 2 (L2) rollups have become the primary infrastructure for high-throughput, low-cost transactions. This project evaluates the fundamental business health and macro-economic metrics of the **Base L2 Network** (incubated by Coinbase) over a 30-day period.

Instead of tracking token prices, this analysis focuses on actual network utility and revenue generation, treating the blockchain as a digital economy. The data is extracted directly from raw on-chain transaction tables (`base.transactions`) using Dune Analytics to ensure 100% accuracy and immutable historical records.

## 🎯 Business Value & Impact
* **Adoptability Tracking:** Measured daily active usage to separate organic network growth from bot-driven activity.
* **Revenue Generation:** Calculated the daily network revenue (Gas Fees converted to ETH) to evaluate the protocol's financial sustainability and profitability.
* **Automated Reporting:** Built a Python pipeline via Dune API to extract, clean, and visualize the macro-economic data into a dual-axis dashboard ready for executive presentation.

## 📊 Key Metrics Tracked
1. **Daily Active Users (DAU):** Count of unique wallet addresses executing successful transactions daily.
2. **Transaction Volume:** Total count of successful daily transactions indicating network congestion and usage.
3. **Network Revenue (ETH):** Total gas fees paid by users, representing the gross revenue collected by the network.

## 📂 Repository Structure
* `layer2_macro_economics.sql`: Advanced SQL query to extract and aggregate raw block data from Dune Analytics.
* `layer2_dashboard.py`: Python script utilizing `dune-client` and `pandas` for data wrangling, and `matplotlib` for generating a dual-axis visualization.
* `base_l2_macro_dashboard.png`: The output visualization correlating User Growth (DAU) with Network Revenue.

## 🚀 How to Reproduce
1. Clone this repository.
2. Install the required Python packages:
   ```bash
   pip install pandas matplotlib dune-client
