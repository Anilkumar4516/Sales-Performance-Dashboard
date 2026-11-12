# 📊 Sales Performance Dashboard (Power BI)

A comprehensive, end-to-end **Sales Performance Dashboard** tutorial and data model built for **Power BI Desktop**, covering data modeling (Star Schema), Power Query ETL, custom DAX business measures, and executive dashboard design.

![Timeframe](https://img.shields.io/badge/Timeframe-FY%202025--2027-blue.svg)
![Tool](https://img.shields.io/badge/Platform-Power%20BI%20Desktop-F2C811.svg?logo=powerbi&logoColor=black)
![Architecture](https://img.shields.io/badge/Data%20Model-Star%20Schema-success.svg)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen.svg)

---

## 🎯 Executive Overview & Live Preview

The dashboard monitors revenue performance, profit margins, sales seasonality, and territory breakdowns across **FY 2025, 2026, and 2027**.

An interactive web-based dashboard simulation is included in [`dashboard_preview.html`](./dashboard_preview.html) featuring authentic Power BI light canvas styling, Microsoft Segoe UI typography, and live real-time refresh simulation.

### Core Metrics Summary

| KPI Metric | Value | Benchmark / Trend | Description |
| :--- | :---: | :---: | :--- |
| **Total Sales** | **$314,850** | $+15.8\%$ YoY | Net sales revenue after deducting line-item discounts |
| **Total Profit** | **$92,410** | $+18.2\%$ YoY | Gross margin earnings after product unit costs |
| **Profit Margin %** | **29.4%** | $+4.4\%$ pts vs target | Strong profitability buffer above $25\%$ target plan |
| **Total Orders** | **1,580** | AOV: **$199.27** | Total volume of completed customer orders |

---

## 📂 Repository File Structure

```text
├── data/
│   ├── sales.csv               # Fact table: Order transactions (OrderID, Date, CustomerID, ProductID, Qty, UnitPrice, Discount)
│   ├── products.csv            # Dimension table: Catalog master (ProductID, ProductName, Category, Cost)
│   └── customers.csv           # Dimension table: Customer base (CustomerID, CustomerName, City, Region)
├── generate_data.py            # Reproducible Python generator script for sample datasets
├── guide.md                    # Beginner's step-by-step guide (Power Query ETL, Modeling, Date Table)
├── measures.dax                # Core DAX formulas with 1-line explanations and formatting rules
├── layout.md                   # Visual report wireframe, field mappings, and 5 extension exercises
├── dashboard_preview.html      # Interactive HTML prototype with real Power BI canvas styling
├── .gitignore                  # Git ignore rules
└── README.md                   # Project documentation
```

---

## 🏗️ Data Architecture (Star Schema)

The model is organized using a clean **Star Schema** architecture to maximize query performance and avoid circular filter context:

```text
  +-----------------------+              +-----------------------+
  |  products (Dimension) |              | customers (Dimension) |
  +-----------------------+              +-----------------------+
  | PK: ProductID         |              | PK: CustomerID        |
  |     ProductName       |              |     CustomerName      |
  |     Category          |              |     City, Region      |
  |     Cost              |              +-----------------------+
  +-----------+-----------+                          |
              | (1)                                  | (1)
              |                                      |
              | (*)                                  | (*)
  +-----------+--------------------------------------+-----------+
  |                      sales (Fact Table)                      |
  +--------------------------------------------------------------+
  | PK: OrderID                                                  |
  | FK: OrderDate   ------------> DateTable[Date] (1:*)          |
  | FK: CustomerID                                               |
  | FK: ProductID                                                |
  |     Quantity, UnitPrice, Discount                            |
  +--------------------------------------------------------------+
```

---

## 📐 Key DAX Measures

All calculations are documented in [`measures.dax`](./measures.dax):

* **Total Sales** (Net Revenue):
  ```dax
  Total Sales = 
  SUMX(sales, sales[Quantity] * sales[UnitPrice] * (1 - sales[Discount]))
  ```

* **Total Profit** (Net Revenue minus Cost of Goods Sold):
  ```dax
  Total Profit = 
  [Total Sales] - SUMX(sales, sales[Quantity] * RELATED(products[Cost]))
  ```

* **Profit Margin %**:
  ```dax
  Profit Margin % = 
  DIVIDE([Total Profit], [Total Sales], 0)
  ```

* **Total Orders**:
  ```dax
  Total Orders = 
  DISTINCTCOUNT(sales[OrderID])
  ```

* **Average Order Value (AOV)**:
  ```dax
  Average Order Value = 
  DIVIDE([Total Sales], [Total Orders], 0)
  ```

* **Sales YoY %** (Year-over-Year Growth):
  ```dax
  Sales YoY % = 
  VAR CurrentSales = [Total Sales]
  VAR PriorYearSales = CALCULATE([Total Sales], SAMEPERIODLASTYEAR('DateTable'[Date]))
  RETURN
      DIVIDE(CurrentSales - PriorYearSales, PriorYearSales, 0)
  ```

* **Sales Last Month**:
  ```dax
  Sales Last Month = 
  CALCULATE([Total Sales], PREVIOUSMONTH('DateTable'[Date]))
  ```

---

## 🚀 Step-by-Step Setup in Power BI Desktop

1. **Importing Data**:
   - Open Power BI Desktop > **Home** > **Get Data** > **Text/CSV**.
   - Select `data/sales.csv` and click **Transform Data** (opens Power Query).
   - Use **New Source** to import `data/products.csv` and `data/customers.csv`.

2. **Data Cleaning in Power Query**:
   - **Remove Duplicates**: Deduplicate `ProductID` in products, `CustomerID` in customers, and full rows in sales.
   - **Handle Blanks**: Replace empty discounts in sales with `0`; replace blank regions in customers with `"Unassigned"`.
   - **Trim Text**: Apply `Transform` > `Trim` on `Category` and `CustomerName` to strip whitespace.
   - Click **Close & Apply**.

3. **Establish Model Relationships**:
   - Switch to **Model View**.
   - Drag `products[ProductID]` (1) $\rightarrow$ `sales[ProductID]` (*).
   - Drag `customers[CustomerID]` (1) $\rightarrow$ `sales[CustomerID]` (*).

4. **Create Date Table**:
   - Go to **Modeling** > **New Table** and paste the continuous calendar formula from [`guide.md`](./guide.md).
   - Mark as Date Table and link `'DateTable'[Date]` (1) $\rightarrow$ `sales[OrderDate]` (*).

5. **Design Visuals**:
   - Follow [`layout.md`](./layout.md) to place KPI cards, monthly trend lines, Top 10 products bar chart, and regional breakdowns.

---

## 💡 Practice Exercises Included

1. **Customer Leaderboard**: Add Top 5 customers table by revenue using the visual Top N filter.
2. **Discount Sensitivity Analysis**: Build a Scatter Chart plotting discount % against order quantity.
3. **Dynamic KPI Color Alert**: Implement conditional formatting rules on the Profit Margin card.
4. **Month-over-Month (MoM) Measure**: Write a monthly change percentage measure using `PREVIOUSMONTH`.
5. **Customer Drill-Through Page**: Build a detailed customer dossier page with drill-through navigation.

---

## 📜 License & Acknowledgements
Created for Power BI Desktop learners, data analysts, and BI enthusiasts. Sample data generated using Python. Free to use for study, training, and portfolio projects.
