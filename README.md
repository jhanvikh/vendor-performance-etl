# Vendor Performance Data Engineering Project

## 📌 Project Overview
This project focuses on analyzing vendor performance using **SQL + Python (Pandas, Matplotlib, Seaborn)**.  
It simulates a **Data Engineering workflow with ETL (Extract, Transform, Load)** followed by **Data Analysis & Visualization** to generate insights on vendor contribution, profitability, and stock turnover.  

The goal is to demonstrate **data pipeline creation, preprocessing, and analytical reporting** for decision-making.

---

## ⚙️ Tech Stack
- **Python** (Pandas, NumPy, Matplotlib, Seaborn)
- **SQL (SQLite)** – for structured querying
- **Jupyter Notebook / VSCode** – development environment
- **ETL Concepts** – Extract, Transform, Load pipeline simulation

---

## 📂 Project Workflow

### 1. Extract
- Load vendor and purchase data into **SQLite database** (`inventory.db`).
- Query tables using `sqlite3` and `pandas.read_sql_query`.

### 2. Transform
- Cleaned missing values and handled outliers.
- Created new features:
  - `ProfitMargin = GrossProfit / TotalSalesDollars * 100`
  - `PurchaseContribution% = VendorPurchase / TotalPurchaseDollars`
  - `StockTurnover = TotalSalesDollars / TotalPurchaseDollars`
- Applied thresholding (quantiles) to filter high/low-performing vendors.

### 3. Load
- Final transformed datasets stored back into SQLite and CSV for reporting.

### 4. Analyze
- Vendor contribution analysis (which vendor contributes most to purchases/sales).
- Brand-level performance analysis.
- Outlier detection and filtering (`TotalSalesDollars < 10000`).
- Identification of vendors with low stock turnover (`StockTurnover < 1`).

### 5. Visualize
- Distribution plots for numerical columns.
- Count plots for categorical columns (Top Vendors, Top Brands).
- Vendor ranking based on contribution % and profitability.
- Stock turnover performance heatmaps.

---

## 📊 Key Insights
- Identified top-performing vendors contributing the majority of purchase dollars.
- Vendors with low stock turnover (<1) were highlighted for inventory optimization.
- Outlier filtering improved the accuracy of performance metrics.
- High-margin vendors (85th percentile) vs. low-sales vendors (15th percentile) comparison.

---
# 📊 Vendor Performance ETL Project

## 🚀 How to Run

1. Clone this repository:
   git clone https://github.com/jhanvikh/vendor-performance-etl.git
   cd vendor-performance-etl

2. Install dependencies:
   pip install pandas numpy matplotlib seaborn

3. Run Jupyter Notebook:
   jupyter notebook

   Then open notebooks/vendor_analysis.ipynb and execute the cells.

## 📂 Folder Structure
vendor-performance-etl/
│
├── data/ # Raw & processed data files
│ ├── inventory.db
│ ├── vendor_data.csv
│
├── notebooks/ # Jupyter Notebooks
│ └── vendor_analysis.ipynb
│
├── scripts/ # Python scripts for ETL
│ ├── extract.py
│ ├── transform.py
│ └── load.py
│
├── visuals/ # Plots & graphs
│
└── README.md # Project documentation


## 📈 Key Insights
- Identified top vendors by Total Purchase Contribution
- Filtered outliers in sales & profitability
- Ranked vendors by stock turnover & efficiency
- Built an ETL pipeline for repeatable analysis

## 🛠️ Tech Stack
- Python (Pandas, NumPy, Matplotlib, Seaborn)
- SQLite (Data storage & queries)
- Jupyter Notebook
- ETL Workflow (Extract → Transform → Load)

