"""
generate_data.py
----------------
Generates realistic, slightly messy sample sales data for a beginner Power BI tutorial.
Output files created in the 'data/' folder:
  1. products.csv   - Product catalog (ProductID, ProductName, Category, Cost)
  2. customers.csv  - Customer master list (CustomerID, CustomerName, City, Region)
  3. sales.csv      - Transaction log (OrderID, OrderDate, CustomerID, ProductID, Quantity, UnitPrice, Discount)

Includes intentional real-world imperfections for Power Query practice:
  - Exact duplicate rows
  - Missing/blank values (e.g., blank Discount, missing CustomerID, missing Region)
  - Leading/trailing whitespace
"""

import os
import csv
import random
from datetime import datetime, timedelta

# Set fixed seed for reproducibility
random.seed(42)

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
os.makedirs(DATA_DIR, exist_ok=True)

# ---------------------------------------------------------
# 1. GENERATE PRODUCTS
# ---------------------------------------------------------
products_data = [
    ("PROD-001", "Laptop Pro 15", "Technology", 750.00, 1050.00),
    ("PROD-002", "Wireless Mouse", "Technology", 12.00, 24.99),
    ("PROD-003", "Mechanical Keyboard", "Technology", 45.00, 79.99),
    ("PROD-004", "27-inch 4K Monitor", "Technology", 210.00, 319.99),
    ("PROD-005", "USB-C Multiport Hub", "Technology", 18.00, 34.99),
    ("PROD-006", "Noise-Canceling Headphones", "Technology", 95.00, 169.99),
    ("PROD-007", "HD Pro Webcam", "Technology", 35.00, 64.99),
    ("PROD-008", "Ergonomic Office Chair", "Furniture", 140.00, 239.99),
    ("PROD-009", "Electric Standing Desk", "Furniture", 280.00, 479.99),
    ("PROD-010", "LED Desk Lamp", "Furniture", 16.00, 32.99),
    ("PROD-011", "5-Shelf Bookcase", "Furniture", 65.00, 119.99),
    ("PROD-012", "3-Drawer Filing Cabinet", "Furniture", 75.00, 134.99),
    ("PROD-013", "Multipurpose Copy Paper", "Office Supplies", 4.50, 9.49),
    ("PROD-014", "Gel Pen Pack (12-ct)", "Office Supplies", 5.00, 11.99),
    ("PROD-015", "Heavy-Duty Desk Stapler", "Office Supplies", 8.00, 17.99),
    ("PROD-016", "Adhesive Sticky Notes (6-pk)", "Office Supplies", 2.50, 5.99),
    ("PROD-017", "Heavy-Duty 3-Ring Binder", "Office Supplies", 4.00, 8.49),
    ("PROD-018", "Ergonomic Mouse Pad", "Office Supplies", 6.00, 14.99),
]

products_rows = []
product_catalog = {}
for pid, name, cat, cost, price in products_data:
    products_rows.append({"ProductID": pid, "ProductName": name, "Category": cat, "Cost": cost})
    product_catalog[pid] = {"name": name, "category": cat, "cost": cost, "price": price}

# Add intentional messy rows:
# 1. Duplicate row for PROD-002
products_rows.append({"ProductID": "PROD-002", "ProductName": "Wireless Mouse", "Category": "Technology", "Cost": 12.00})
# 2. Category with accidental trailing whitespace
products_rows.append({"ProductID": "PROD-019", "ProductName": "Cable Management Sleeve", "Category": "Office Supplies ", "Cost": 7.50})
product_catalog["PROD-019"] = {"name": "Cable Management Sleeve", "category": "Office Supplies", "cost": 7.50, "price": 15.99}

products_file = os.path.join(DATA_DIR, "products.csv")
with open(products_file, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["ProductID", "ProductName", "Category", "Cost"])
    writer.writeheader()
    writer.writerows(products_rows)
print(f"Created {products_file} with {len(products_rows)} rows (includes 1 duplicate and 1 row with whitespace).")

# ---------------------------------------------------------
# 2. GENERATE CUSTOMERS
# ---------------------------------------------------------
customer_base = [
    ("CUST-1001", "Emma Watson", "New York", "East"),
    ("CUST-1002", "Liam Smith", "Boston", "East"),
    ("CUST-1003", "Olivia Johnson", "Philadelphia", "East"),
    ("CUST-1004", "Noah Williams", "New York", "East"),
    ("CUST-1005", "Sophia Brown", "Boston", "East"),
    ("CUST-1006", "Lucas Jones", "Philadelphia", "East"),
    ("CUST-1007", "Ava Garcia", "Newark", "East"),
    ("CUST-1008", "Mason Miller", "Buffalo", "East"),
    ("CUST-1009", "Isabella Davis", "Pittsburgh", "East"),
    ("CUST-1010", "Ethan Rodriguez", "Hartford", "East"),
    ("CUST-1011", "Mia Martinez", "Los Angeles", "West"),
    ("CUST-1012", "James Hernandez", "San Francisco", "West"),
    ("CUST-1013", "Harper Lopez", "Seattle", "West"),
    ("CUST-1014", "Alexander Gonzalez", "San Diego", "West"),
    ("CUST-1015", "Evelyn Wilson", "Denver", "West"),
    ("CUST-1016", "Benjamin Anderson", "Portland", "West"),
    ("CUST-1017", "Charlotte Thomas", "Phoenix", "West"),
    ("CUST-1018", "Elijah Taylor", "Las Vegas", "West"),
    ("CUST-1019", "Amelia Moore", "San Jose", "West"),
    ("CUST-1020", "Daniel Jackson", "Salt Lake City", "West"),
    ("CUST-1021", "Emily Martin", "Chicago", "North"),
    ("CUST-1022", "Henry Lee", "Minneapolis", "North"),
    ("CUST-1023", "Ella Perez", "Detroit", "North"),
    ("CUST-1024", "Jackson White", "Milwaukee", "North"),
    ("CUST-1025", "Avery Harris", "Cleveland", "North"),
    ("CUST-1026", "Sebastian Clark", "Columbus", "North"),
    ("CUST-1027", "Scarlett Lewis", "Indianapolis", "North"),
    ("CUST-1028", "Matthew Robinson", "Des Moines", "North"),
    ("CUST-1029", "Chloe Walker", "Kansas City", "North"),
    ("CUST-1030", "David Young", "Omaha", "North"),
    ("CUST-1031", "Grace Allen", "Dallas", "South"),
    ("CUST-1032", "Carter King", "Houston", "South"),
    ("CUST-1033", "Zoey Wright", "Atlanta", "South"),
    ("CUST-1034", "Wyatt Scott", "Miami", "South"),
    ("CUST-1035", "Penelope Torres", "Austin", "South"),
    ("CUST-1036", "Julian Nguyen", "Orlando", "South"),
    ("CUST-1037", "Riley Hill", "Nashville", "South"),
    ("CUST-1038", "Leo Flores", "Charlotte", "South"),
    ("CUST-1039", "Layla Green", "Tampa", "South"),
    ("CUST-1040", "Gabriel Adams", "New Orleans", "South"),
]

customer_rows = []
customer_ids = []
for cid, name, city, region in customer_base:
    customer_rows.append({"CustomerID": cid, "CustomerName": name, "City": city, "Region": region})
    customer_ids.append(cid)

# Add intentional messy rows:
# 1. Duplicate row for CUST-1005
customer_rows.append({"CustomerID": "CUST-1005", "CustomerName": "Sophia Brown", "City": "Boston", "Region": "East"})
# 2. Duplicate row for CUST-1031
customer_rows.append({"CustomerID": "CUST-1031", "CustomerName": "Grace Allen", "City": "Dallas", "Region": "South"})
# 3. Missing Region for CUST-1041
customer_rows.append({"CustomerID": "CUST-1041", "CustomerName": "Hannah Baker", "City": "Raleigh", "Region": ""})
customer_ids.append("CUST-1041")
# 4. Leading and trailing spaces in name
customer_rows.append({"CustomerID": "CUST-1042", "CustomerName": "  Victor Vance  ", "City": "Memphis", "Region": "South"})
customer_ids.append("CUST-1042")

customers_file = os.path.join(DATA_DIR, "customers.csv")
with open(customers_file, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["CustomerID", "CustomerName", "City", "Region"])
    writer.writeheader()
    writer.writerows(customer_rows)
print(f"Created {customers_file} with {len(customer_rows)} rows (includes 2 duplicates, 1 blank Region, 1 trimmed name).")

# ---------------------------------------------------------
# 3. GENERATE SALES (Transactions covering 2024-01-01 to 2025-12-31)
# ---------------------------------------------------------
start_date = datetime(2024, 1, 1)
total_days = 730  # 2 years (2024 leap year = 366, 2025 = 365 => 731 days, covering all 24 months)

sales_rows = []
all_pids = list(product_catalog.keys())

# Weights to give realistic product distributions (accessories sell more frequently than standing desks)
prod_weights = [
    5,  # Laptop Pro 15
    18, # Wireless Mouse
    10, # Mechanical Keyboard
    7,  # 27-inch Monitor
    15, # USB-C Hub
    9,  # Noise-Canceling Headphones
    12, # HD Webcam
    6,  # Ergonomic Office Chair
    4,  # Electric Standing Desk
    11, # LED Desk Lamp
    5,  # Bookcase
    6,  # Filing Cabinet
    25, # Copy Paper
    22, # Gel Pen Pack
    14, # Stapler
    20, # Sticky Notes
    16, # 3-Ring Binder
    15, # Mouse Pad
    10, # Cable Sleeve
]

for order_num in range(1, 1001):
    order_id = f"ORD-{order_num:05d}"
    
    # Slight upward sales trend from 2024 to 2025, with holiday boosts in Nov/Dec
    day_offset = int(random.triangular(0, 730, 480))
    order_date = start_date + timedelta(days=day_offset)
    order_date_str = order_date.strftime("%Y-%m-%d")

    cust_id = random.choice(customer_ids)
    prod_id = random.choices(all_pids, weights=prod_weights, k=1)[0]
    
    # Quantities: lower for expensive tech/furniture, higher for office supplies
    cat = product_catalog[prod_id]["category"]
    if cat == "Technology":
        qty = random.choices([1, 2, 3], weights=[80, 16, 4])[0]
    elif cat == "Furniture":
        qty = random.choices([1, 2, 4], weights=[85, 12, 3])[0]
    else:  # Office Supplies
        qty = random.choices([1, 2, 3, 5, 8, 10], weights=[35, 25, 15, 12, 8, 5])[0]

    unit_price = product_catalog[prod_id]["price"]

    # Discounts: mostly 0, occasionally 0.05, 0.10, 0.15, 0.20
    disc = random.choices([0.0, 0.05, 0.10, 0.15, 0.20], weights=[65, 15, 10, 7, 3])[0]
    disc_val = f"{disc:.2f}"

    sales_rows.append({
        "OrderID": order_id,
        "OrderDate": order_date_str,
        "CustomerID": cust_id,
        "ProductID": prod_id,
        "Quantity": qty,
        "UnitPrice": unit_price,
        "Discount": disc_val
    })

# Add intentional messy rows:
# 1. Blank Discounts (simulate missing entry where discount was 0) - in 8 rows
blank_discount_indices = [45, 120, 267, 412, 580, 723, 854, 960]
for idx in blank_discount_indices:
    sales_rows[idx]["Discount"] = ""

# 2. Blank CustomerIDs (missing lookup) - in 3 rows
blank_cust_indices = [88, 340, 777]
for idx in blank_cust_indices:
    sales_rows[idx]["CustomerID"] = ""

# 3. Exact Duplicate rows (duplicate transactions) - 6 duplicates
duplicates = [
    sales_rows[15].copy(),
    sales_rows[150].copy(),
    sales_rows[320].copy(),
    sales_rows[512].copy(),
    sales_rows[699].copy(),
    sales_rows[888].copy(),
]
sales_rows.extend(duplicates)

sales_file = os.path.join(DATA_DIR, "sales.csv")
with open(sales_file, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["OrderID", "OrderDate", "CustomerID", "ProductID", "Quantity", "UnitPrice", "Discount"])
    writer.writeheader()
    writer.writerows(sales_rows)

print(f"Created {sales_file} with {len(sales_rows)} rows (1,000 original + 6 duplicates = 1,006 rows total).")
print("Data generation complete!")

