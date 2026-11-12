# Beginner's Guide: Building a Sales Performance Dashboard in Power BI

Welcome to Power BI! This guide walks you through building your first complete, professional dashboard from scratch using the files in your `data/` folder.

Every new concept is explained in plain English the first moment it appears.

---

## Key Terms Explained (Jargon Buster)

- **Power BI Desktop**: A free application installed on your PC used to connect to data sources, build calculations, and design interactive visual reports.
- **Power Query**: The built-in data preparation tool inside Power BI (like a data cleaning kitchen) where you clean, reshape, and transform raw files before loading them into your dashboard.
- **Data Type**: The classification of a column's contents (such as `Text`, `Whole Number`, `Decimal Number`, or `Date`).
- **Null / Blank**: An empty cell where no data was recorded.
- **Model View**: The screen in Power BI where you see your tables represented as boxes and draw connections between them like puzzle pieces.
- **Fact Table**: A table recording business activities or transactions that occur over time (in our case, `sales.csv` with Order ID, dates, quantities, and prices).
- **Dimension Table**: A lookup table containing descriptive context about the facts (e.g., `products.csv` describing what items were sold, and `customers.csv` describing who bought them).
- **Star Schema**: A proven, best-practice database layout where one central Fact table is connected outward to multiple Dimension tables, resembling a star.
- **Relationship & Cardinality**: A link connecting two tables using a common column (like `ProductID`). **Cardinality** describes the count relationship: **"One-to-Many" (1:*)** means a product appears once in the products list (the "1" side) but can be purchased multiple times across the sales table (the "*" Many side).
- **Date Table**: A dedicated table containing a continuous list of every calendar day without gaps. Power BI requires this to perform time comparisons like Year-over-Year (YoY) and Month-over-Month (MoM).
- **DAX (Data Analysis Expressions)**: The formula language of Power BI (similar to Excel formulas, but designed to work across relational tables) to calculate custom metrics.

---

## Step 1: Importing the CSV Files

1. Open **Power BI Desktop**.
2. If a welcome splash screen appears, click the **X** in the top-right corner or click **Get Data**.
3. In the top ribbon, on the **Home** tab, click **Get Data** > **Text/CSV**.
4. Browse to your project folder:
   `c:\Users\rajuv\OneDrive\Desktop\POWER BI\report\data\`
5. Select `sales.csv` and click **Open**.
6. A preview window will appear. 
   > **Golden Rule for Beginners:** Do **NOT** click "Load". Always click **Transform Data**. This opens the Power Query Editor so you can inspect and clean the data first.
7. Inside Power Query, to bring in the other two files:
   - On the Home tab of Power Query, click **New Source** > **Text/CSV**.
   - Select `products.csv` and click **OK**.
   - Click **New Source** > **Text/CSV** again, select `customers.csv`, and click **OK**.
8. You will now see all three queries (`sales`, `products`, `customers`) listed in the left-hand **Queries** pane.

---

## Step 2: Cleaning Data in Power Query

Real-world data always has imperfections. Let's fix the duplicates, whitespace, blanks, and data types in each table.

### 2.1 Cleaning `products`
1. Click on the **products** query on the left.
2. **Remove Duplicates**:
   - Right-click the **ProductID** column header.
   - Click **Remove Duplicates**. (This removes the duplicate row for `PROD-002`).
3. **Trim Whitespace**:
   - Accidental spaces at the start or end of text (like `"Office Supplies "`) cause grouping errors.
   - Right-click the **Category** column header > **Transform** > **Trim**.
4. **Verify Data Types**:
   - Look at the icon next to each column header:
     - `ProductID`: **ABC** (Text)
     - `ProductName`: **ABC** (Text)
     - `Category`: **ABC** (Text)
     - `Cost`: **$** or **1.2** (Fixed Decimal Number or Decimal Number). If it shows ABC, click the icon and select **Fixed Decimal Number**.

---

### 2.2 Cleaning `customers`
1. Click on the **customers** query on the left.
2. **Remove Duplicates**:
   - Right-click the **CustomerID** column header > select **Remove Duplicates**. (Removes duplicate customer entries).
3. **Trim Customer Names**:
   - Right-click **CustomerName** > **Transform** > **Trim** (cleans extra spacing around names).
4. **Handle Blank Region**:
   - Right-click the **Region** column header > select **Replace Values**.
   - **Value To Find**: leave completely blank.
   - **Replace With**: type `Unassigned`.
   - Click **OK**.
5. **Verify Data Types**:
   - Confirm all 4 columns (`CustomerID`, `CustomerName`, `City`, `Region`) have the **ABC** (Text) icon.

---

### 2.3 Cleaning `sales`
1. Click on the **sales** query on the left.
2. **Remove Duplicates**:
   - In transaction tables, an exact duplicate across all columns represents an accidental double-entry.
   - Click the top-left table icon (above row 1) or press `Ctrl + A` to select all columns.
   - Right-click any column header > select **Remove Duplicates**.
3. **Handle Blank Discounts**:
   - Some rows have empty discounts where zero discount was applied.
   - Right-click the **Discount** column header > select **Replace Values**.
   - **Value To Find**: leave blank.
   - **Replace With**: type `0`.
   - Click **OK**.
4. **Handle Blank Customer IDs**:
   - Click the dropdown arrow on the **CustomerID** column header.
   - Uncheck `(blank)` / `(null)` to filter them out, or right-click the column > **Replace Values** with `CUST-GUEST`.
5. **Set Proper Data Types**:
   - Click the icon in each header to set:
     - `OrderID`: **ABC** (Text)
     - `OrderDate`: **Calendar** (Date)
     - `CustomerID`: **ABC** (Text)
     - `ProductID`: **ABC** (Text)
     - `Quantity`: **123** (Whole Number)
     - `UnitPrice`: **Fixed Decimal Number** (Currency)
     - `Discount`: **Decimal Number** (or Percentage)

### 2.4 Apply Changes
In the top-left corner of Power Query, click **Close & Apply**.
Power BI will process the cleaned tables and load them into your data model.

---

## Step 3: Creating Relationships (Star Schema) in Model View

1. On the far-left sidebar of Power BI Desktop, click the **Model View** icon (the 3rd icon down, resembling an organizational chart).
2. You will see three rectangular boxes representing your tables: `sales`, `products`, and `customers`.
3. **Arrange Your Canvas (Star Schema Layout)**:
   - Place `sales` in the center (this is your **Fact table**).
   - Place `products` on the upper-left (a **Dimension table**).
   - Place `customers` on the upper-right (a **Dimension table**).
4. **Create the Product Relationship**:
   - Click and hold the `ProductID` field in the `products` table.
   - Drag your mouse and drop it directly onto `ProductID` inside the `sales` table.
   - A line will appear connecting the two tables.
   - Double-click the line: verify **Cardinality** says **One to Many (1:*)** and **Cross filter direction** is **Single**. Click **OK**.
5. **Create the Customer Relationship**:
   - Click and hold `CustomerID` in the `customers` table.
   - Drag and drop it onto `CustomerID` in the `sales` table.
   - Verify the line shows a `1` on `customers` and a `*` on `sales`.

> **Why Single Direction?** Filters naturally flow downward from dimension tables (e.g. filtering a Category in `products`) to calculate corresponding numbers in `sales`. Keeping relationships 1-to-many single-direction prevents ambiguous calculations and ensures fast performance.

---

## Step 4: Creating a Dedicated Date Table

Why do we need a separate Date table when `sales` already has `OrderDate`?
If your store makes no sales on a holiday, that date is missing in `sales.csv`. Time-intelligence calculations (like comparing this year vs last year) require an unbroken calendar sequence with zero missing dates.

### 4.1 Generate the Date Table with DAX
1. In the top ribbon, click the **Modeling** tab (or **Table Tools**).
2. Click **New Table**.
3. In the formula bar that opens above, paste the following DAX code:

```dax
DateTable = 
ADDCOLUMNS(
    CALENDAR(DATE(2025, 1, 1), DATE(2027, 12, 31)),
    "Year", YEAR([Date]),
    "Month Number", MONTH([Date]),
    "Month", FORMAT([Date], "mmm"),
    "Month Year", FORMAT([Date], "mmm yyyy"),
    "Quarter", "Q" & FORMAT([Date], "q"),
    "Year Month Sort", FORMAT([Date], "yyyyMM")
)
```

4. Press **Enter**. You now have a calendar covering every single day from Jan 1, 2025 to Dec 31, 2027.

### 4.2 Fix Month Sorting (The #1 Beginner Trap!)
By default, Power BI sorts text columns alphabetically. This means `Month` will sort: *April, August, December...* instead of *Jan, Feb, Mar*.
1. In the right-hand **Data** pane, click on the **DateTable** to expand it.
2. Click on the **Month** column.
3. In the top ribbon, the **Column tools** tab will activate.
4. Click **Sort by Column** > select **Month Number**.
5. Similarly, click the **Month Year** column > click **Sort by Column** > select **Year Month Sort**.

### 4.3 Mark as Official Date Table
1. Right-click **DateTable** in the Data pane (or click **Mark as date table** on the Table Tools tab).
2. Choose **Mark as date table**.
3. In the popup, choose **Date** from the dropdown. Click **OK**.

### 4.4 Connect DateTable to Sales
1. Switch back to **Model View** (left sidebar).
2. Drag `Date` from `DateTable` and drop it onto `OrderDate` in the `sales` table.
3. You now have a complete, professional Star Schema!

---

## Next Steps
Now that your data is cleaned and modeled:
1. Open [`measures.dax`](file:///c:/Users/rajuv/OneDrive/Desktop/POWER BI/report/measures.dax) to create your core business metrics.
2. Open [`layout.md`](file:///c:/Users/rajuv/OneDrive/Desktop/POWER BI/report/layout.md) to build your visual dashboard step by step.

