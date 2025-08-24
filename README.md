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
## 📂 Dataset
The full dataset is too large to be uploaded to GitHub.  

- 🔗 [Download Full Dataset (Google Drive)](https://drive.google.com/drive/folders/18OpOv5mRQyL4tS-3Z0Uf3RNEL7YjdeIr?usp=sharing)
- Check out Cleaned_Data.csv, which contains the processed dataset merged from all source files.
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

## 📊 Exploratory Data Analysis (EDA)

### 🔎 Negative or Zero Values Detected
- **Gross Profit:** Min = -52,002.78 (loss-making sales)  
- **Profit Margin:** Min = -∞ (sales at zero or below cost)  
- **Unsold Inventory:** Indicates slow-moving stock  

### 📈 Outliers Identified
- High Freight Costs (up to 257K)  
- Large Purchase/Actual Prices  

### 🔗 Correlation Analysis
- Weak between **Purchase Price & Profit**  
- Strong between **Purchase Qty & Sales Qty** (0.999)  
- Negative between **Profit Margin & Sales Price** (-0.179)
  
---

### ❓ Research Questions & Key Findings
- **Brands for Promotions:** 198 brands with low sales but high profit margins  
- **Top Vendors:** Top 10 vendors = 65.69% of purchases → risk of over-reliance  
- **Bulk Purchasing Impact:** 72% cost savings per unit in large orders  
- **Inventory Turnover:** $2.71M worth of unsold inventory  

### 💰 Vendor Profitability
- **High Vendors:** Mean Margin = 31.17%  
- **Low Vendors:** Mean Margin = 41.55%  

### 🧪 Hypothesis Testing
- Statistically significant difference in profit margins → distinct vendor strategies

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
   Then open notebooks/vendor_performance_analysis.ipynb & Exploratory Data Analysis.ipynb then execute the cells.

## 📂 Folder Structure

```text
vendor-performance-etl/
│
├── Cleaned_Data/                        # processed data files
│   ├── vendor_sales_summary.xls
|
├── data/                                # Raw  data files
│   ├── end_inventory.csv
│   ├── purchase_prices.csv
│   ├── begin_inventory.csv
│   ├── purchases.csv
│   ├── sales.csv
│   ├── vendor_invoice.csv
│
├── notebooks/                           # Jupyter Notebooks
│   ├── vendor_performance_analysis.ipynb
|   ├── Exploratory Data Analysis.ipynb
│
├── scripts/                             # Python scripts for ETL
│   ├── et_vendor_summary.log
│   ├── ingestion_db.py
│
├── logs/                                # Logs of Ingestion and summary table
│   ├── get_vendor_summary.log
│   ├── injestion_db.log
| 
└── README.md                            # Project documentation

```

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

