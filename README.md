# 🏏 Cricket World Cup Insights Dashboard

## 📊 Overview
This project analyzes historical Cricket World Cup data to identify performance trends, player statistics, and venue insights. The final output is an interactive Google Looker Studio Dashboard.

## 🔗 Live Dashboard
**[👉 Click Here to View the Interactive Dashboard](https://lookerstudio.google.com/reporting/34fb28ba-f78d-4297-ac21-a3d32feff598)**

*(If the link above does not work, please ensure you are logged into a Google account)*

## 📂 Data Engineering
The dataset was generated using Python to simulate historical match data from 1975 to 2023.

* **Script:** `generate_data.py`
* **Output:** `cricket_data.csv`
* **Libraries Used:** Pandas, Random

## 📈 Visualizations Included
1.  **Country-wise Performance:** Analysis of win rates and total runs.
2.  **Player Analytics:** Breakdown of runs, wide balls, and no-balls.
3.  **Venue Analysis:** Geospatial view of best-performing grounds for Team India.
4.  **Trend Lines:** Highest individual scores across different World Cup years.

## ⚙️ How to Reproduce
1.  Run the data generation script:

    python generate_data.py

2.  Upload the resulting `cricket_data.csv` to Google Looker Studio.
3.  Create charts based on the `Runs_Scored` and `Team` metrics.