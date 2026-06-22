# 📊 Global Superstore Sales Performance Dashboard

An interactive **Business Intelligence dashboard** for analyzing sales, profit, and
segment-wise performance of the Global Superstore dataset. The project includes a fully
documented Jupyter Notebook (data cleaning, EDA, and visualizations) and an interactive
**Streamlit** web application with filters and live KPIs.

---

## 📝 Project Description

This project explores 51,290 retail transactions from a global superstore to surface
actionable business insights. The raw data is cleaned and analyzed in a Jupyter Notebook,
where eight visualizations are produced and saved automatically into a `charts/` folder.
A companion Streamlit app (`app.py`) turns these insights into an interactive dashboard
where users filter by **Region, Category, and Sub-Category** and instantly view key
performance indicators.

---

## 🎯 Objectives

- Clean and prepare the Global Superstore dataset.
- Build an interactive Streamlit dashboard with filters (Region, Category, Sub-Category).
- Display key performance indicators (KPIs) using charts:
  - **Total Sales**
  - **Total Profit**
  - **Top 5 Customers by Sales**
- Practice BI dashboarding, data storytelling, Streamlit interactivity, and visual KPI analysis.

---

## 📁 Folder Structure

```
Global_Superstore_Sales_Dashboard/
│
├── Global_Superstore_Sales_Dashboard.ipynb   # Main analysis notebook
├── app.py                                     # Interactive Streamlit dashboard
├── README.md                                  # This file
├── requirements.txt                           # Python dependencies
│
├── charts/                                    # Auto-saved figures from the notebook
│   ├── chart_01_sales_profit_by_category.png
│   ├── chart_02_sales_by_region.png
│   ├── chart_03_sales_profit_by_segment.png
│   ├── chart_04_profit_by_subcategory.png
│   ├── chart_05_monthly_sales_trend.png
│   ├── chart_06_top5_customers.png
│   ├── chart_07_discount_vs_profit.png
│   └── chart_08_correlation_heatmap.png
│
└── data/
    └── Global_Superstore2.csv                 # Dataset
```

---

## ⚙️ Installation Instructions

1. (Recommended) Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate        # On Windows: venv\Scripts\activate
   ```

2. Install the required libraries:

   ```bash
   pip install -r requirements.txt
   ```

---

## 📦 Required Libraries

- pandas
- numpy
- matplotlib
- seaborn
- streamlit
- plotly
- jupyter / notebook

---

## ▶️ How to Run

### Run the analysis notebook

```bash
jupyter notebook Global_Superstore_Sales_Dashboard.ipynb
```

Run all cells (`Kernel → Restart & Run All`). All figures are saved automatically into the
`charts/` folder.

### Run the interactive dashboard

```bash
streamlit run app.py
```

Then open the local URL shown in the terminal (usually http://localhost:8501).

---

## 📈 Results Summary

- **Technology** is the top-performing category in both sales and profit; **Furniture** has the
  thinnest margins.
- Several **sub-categories are loss-making** (notably *Tables*) — clear candidates for pricing review.
- **Higher discounts correlate strongly with negative profit**, confirming that aggressive
  discounting erodes profitability.
- The **Consumer segment** drives the largest share of sales and profit.
- Sales show a **steady upward trend** with year-end seasonal peaks.
- The **Top 5 customers** contribute a disproportionately large share of total sales.

---

## 👤 Author

**[Your Name]**
Business Intelligence / Data Analytics Project
*Submitted as part of a data science assignment.*
