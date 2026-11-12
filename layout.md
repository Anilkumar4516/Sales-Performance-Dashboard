# Dashboard Layout & Design Guide: Sales Performance Dashboard

This guide walks you through placing, configuring, and formatting your visuals in Power BI Desktop to create a clean, modern, and intuitive executive dashboard.

---

## 1. Canvas Wireframe (Layout Blueprint)

Set your canvas size to standard 16:9 widescreen (**Format page** > **Canvas settings** > **16:9**).

```
+---------------------------------------------------------------------------------------------+
|  HEADER: Sales Performance Dashboard              [Year: All v] [Category: All v] [Region v]|
+---------------------------------------------------------------------------------------------+
|  [ KPI CARD 1 ]      |  [ KPI CARD 2 ]      |  [ KPI CARD 3 ]      |  [ KPI CARD 4 ]        |
|  Total Sales         |  Total Profit        |  Profit Margin %     |  Total Orders          |
|  $184,250            |  $52,410             |  28.4%               |  1,000                 |
+---------------------------------------------------------------------------------------------+
|  LINE CHART: Sales Trend by Month                   |  BAR CHART: Top 10 Products by Sales  |
|                                                     |                                       |
|  Shows monthly revenue over time                    |  Horizontal bars ranked 1 to 10       |
|  (Reveals seasonality and peaks)                    |  (Identifies highest revenue drivers) |
+-----------------------------------------------------+---------------------------------------+
|  COLUMN / BAR CHART: Sales by Region                |  DATA TABLE / BREAKDOWN SUMMARY       |
|                                                     |                                       |
|  Sales and Profit distribution across               |  Category performance table with      |
|  North, South, East, West                           |  Sales, Profit, and Profit Margin %   |
+---------------------------------------------------------------------------------------------+
```

---

## 2. Visual Configurations (Which Fields Go Where)

### Visual 1: Top 4 KPI Cards
In the Visualizations pane, select the **Card (new)** or standard **Card** icon.

- **Card 1 (Total Sales)**:
  - Field: `_Measures[Total Sales]`
  - Format: Currency (`$#,##0`)
- **Card 2 (Total Profit)**:
  - Field: `_Measures[Total Profit]`
  - Format: Currency (`$#,##0`)
- **Card 3 (Profit Margin %)**:
  - Field: `_Measures[Profit Margin %]`
  - Format: Percentage (`0.0%`)
- **Card 4 (Total Orders)**:
  - Field: `_Measures[Total Orders]`
  - Format: Whole Number (`#,##0`)

> **Layout Tip**: Place these 4 cards in a single row across the top of the report. Keep identical widths and align their tops.

---

### Visual 2: Line Chart (Monthly Sales Trend)
In the Visualizations pane, click the **Line chart** icon.

- **X-axis**: Drag `'DateTable'[Month Year]` (or `'DateTable'[Month]`)
- **Y-axis**: Drag `_Measures[Total Sales]`
- **Secondary Y-axis** (Optional) or **Tooltips**: Drag `_Measures[Total Profit]` and `_Measures[Sales YoY %]`
- **Sort Order**: Click the **...** (More options) on the visual > **Sort axis** > select **Month Year** (Ascending).

---

### Visual 3: Horizontal Bar Chart (Top 10 Products by Sales)
In the Visualizations pane, click the **Clustered bar chart** icon (horizontal bars).

- **Y-axis**: Drag `products[ProductName]`
- **X-axis**: Drag `_Measures[Total Sales]`
- **Tooltips**: Drag `_Measures[Total Profit]`
- **How to Filter for Top 10 Only**:
  1. With this chart selected, look at the **Filters** pane on the right side of the canvas.
  2. Under **Filters on this visual**, click on **ProductName**.
  3. Change **Filter type** from *Basic filtering* to **Top N**.
  4. Next to **Show items**, leave it as **Top** and enter `10`.
  5. In the **By value** box, drag and drop `_Measures[Total Sales]`.
  6. Click the yellow **Apply filter** button.

---

### Visual 4: Bar Chart or Map (Sales by Region)
In the Visualizations pane, click the **Clustered column chart** (vertical) or **Clustered bar chart** (horizontal).

- **X-axis (or Y-axis)**: Drag `customers[Region]`
- **Y-axis (or X-axis)**: Drag `_Measures[Total Sales]`
- **Tooltips**: Drag `_Measures[Total Profit]`, `_Measures[Profit Margin %]`

*(Alternative: If you have map permissions enabled in Power BI Desktop options, you can use the **Filled Map** visual: Location: `customers[Region]`, Tooltips: `[Total Sales]`, `[Total Profit]`)*.

---

### Visual 5: Interactive Slicers (Filters)
Add 3 **Slicer** visuals at the top right of your canvas or in a compact left sidebar:

1. **Year Slicer**:
   - Field: `'DateTable'[Year]`
   - Style: In the Visualizations pane under **Format visual** > **Slicer settings** > **Style**, choose **Tile** (creates easy clickable buttons for `2025`, `2026`, and `2027`).
2. **Category Slicer**:
   - Field: `products[Category]`
   - Style: **Dropdown** or **Tile**.
3. **Region Slicer**:
   - Field: `customers[Region]`
   - Style: **Dropdown** (allows selecting East, West, North, South).

---

## 3. Formatting & Design Best Practices (Make It Look Professional)

1. **Consistent Color Palette**:
   - Stick to 2-3 primary colors. For example:
     - Primary Dark Blue / Navy for titles and main bars.
     - Emerald Green for Profit and positive metrics.
     - Slate Grey for axis lines and borders.
   - Avoid using 10 different bright colors; color should highlight insights, not distract.
2. **Clean Up Axis Titles (Reduce Visual Clutter)**:
   - When a chart title already clearly says *"Sales by Month"*, the label *"Month Year"* on the bottom axis is redundant.
   - Go to **Format visual** > **X-axis** > toggle **Title** to **Off**.
3. **Card Callout Values**:
   - Keep card numbers easily readable at a glance: set font size to **24 pt - 28 pt Bold**.
   - Set the label below the number to **10 pt Regular** in a muted dark grey.
4. **Grid Alignment and Padding**:
   - Use Power BI's alignment tools (**Format** tab in ribbon > **Align** > **Distribute Horizontally**).
   - Leave a clean 10-15 pixel gap (gutter) between visual cards so the dashboard breathes.
5. **Background & Cards**:
   - Give the page background a very subtle light grey tint (`#F4F6F9`).
   - Give each visual card a clean white background with rounded corners (set **Border radius** to `6px - 8px`) and a subtle drop shadow.

---

## 4. 5 Practice Exercises to Extend Your Report

Once your core dashboard is running, challenge yourself with these five real-world extensions:

### Exercise 1: Customer Leaderboard (Top 5 Customers)
- **Goal**: Add a table or bar chart showing your highest-spending customers.
- **How to do it**: Add a Table visual with `customers[CustomerName]`, `[Total Sales]`, and `[Total Orders]`. Use the Filters pane on the visual to show the **Top 5** by `[Total Sales]`.

### Exercise 2: Discount Impact Analysis (Scatter Plot)
- **Goal**: Find out whether higher discounts actually lead to larger order quantities.
- **How to do it**: Add a **Scatter chart**. Place `sales[Discount]` on the X-axis, `sales[Quantity]` on the Y-axis, and `products[Category]` in Legend. Look for patterns or clusters.

### Exercise 3: Dynamic KPI Color Alerts (Conditional Formatting)
- **Goal**: Make your `Profit Margin %` card dynamically turn green when healthy (>25%) and red when low (<20%).
- **How to do it**: Select the Profit Margin card > go to **Format visual** > **Callout value** > click the **fx** (Conditional formatting) button next to Color > choose **Rules** > set rule: if value >= 0.25 then Green, if value < 0.20 then Red.

### Exercise 4: Month-over-Month (MoM) Growth DAX Measure
- **Goal**: Compare each month's sales directly against the previous month.
- **How to do it**: Write a new DAX measure:
  ```dax
  Sales MoM % = 
  VAR CurrentMonthSales = [Total Sales]
  VAR PrevMonthSales = [Sales Last Month]
  RETURN
      DIVIDE(CurrentMonthSales - PrevMonthSales, PrevMonthSales, 0)
  ```
  Add this measure to your monthly trend tooltip or data label.

### Exercise 5: Customer Profile Drill-Through Page
- **Goal**: Allow an executive to right-click any customer name and jump to a detailed customer dossier page.
- **How to do it**: Add a new page named `Customer Details`. Drag `customers[CustomerName]` into the **Drill-through** field bucket. On this page, build a detailed purchase history table and KPI cards for that specific customer. Return to Page 1, right-click any customer, and select **Drill through**!

