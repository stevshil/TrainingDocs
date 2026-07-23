#!/usr/bin/env python

import sqlite3
import csv
import io

# -----------------------------
# CSV DATA FOR NEW SCHEMA
# -----------------------------

products_csv = """product_id,product_name,release_date,product_type,manufacturer_price
1,Nova One,2023-01-01,Phone,120
2,Nova Air,2023-01-01,Phone,180
3,Nova Pro,2023-01-01,Phone,260
4,Nova Max,2023-01-01,Phone,400
5,Nova Ultra,2023-01-01,Phone,520
6,Charger,2023-01-01,Accessory,10
7,Cable,2023-01-01,Accessory,4
8,Headphones,2023-01-01,Accessory,35
9,Case,2023-01-01,Accessory,6
10,Screen Protector,2023-01-01,Accessory,2
"""

pricing_csv = """price_id,product_id,retail_price,date_price_set
1,1,199,2023-01-01
2,2,299,2023-01-01
3,3,449,2023-01-01
4,4,699,2023-01-01
5,5,899,2023-01-01
6,6,25,2023-01-01
7,7,12,2023-01-01
8,8,79,2023-01-01
9,9,20,2023-01-01
10,10,10,2023-01-01
"""

orders_csv = """order_id,product_id,price_id,quantity
1,1,1,12500
2,2,2,9800
3,3,3,7200
4,4,4,4500
5,5,5,2100
6,6,6,18000
7,7,7,22000
8,8,8,8500
9,9,9,15000
10,10,10,20000
"""

# -----------------------------
# DATABASE CREATION
# -----------------------------

conn = sqlite3.connect("data2.db")
cur = conn.cursor()

# Drop old tables
cur.execute("DROP TABLE IF EXISTS products")
cur.execute("DROP TABLE IF EXISTS pricing")
cur.execute("DROP TABLE IF EXISTS orders")

# Create new schema
cur.execute("""
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT,
    release_date TEXT,
    product_type TEXT,
    manufacturer_price REAL
)
""")

cur.execute("""
CREATE TABLE pricing (
    price_id INTEGER PRIMARY KEY,
    product_id INTEGER,
    retail_price REAL,
    date_price_set TEXT,
    FOREIGN KEY(product_id) REFERENCES products(product_id)
)
""")

cur.execute("""
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    product_id INTEGER,
    price_id INTEGER,
    quantity INTEGER,
    FOREIGN KEY(product_id) REFERENCES products(product_id),
    FOREIGN KEY(price_id) REFERENCES pricing(price_id)
)
""")

# -----------------------------
# INSERT CSV DATA
# -----------------------------

def insert_csv(csv_string, table_name):
    reader = csv.reader(io.StringIO(csv_string.strip()))
    headers = next(reader)
    placeholders = ",".join(["?"] * len(headers))
    insert_sql = f"INSERT INTO {table_name} VALUES ({placeholders})"
    for row in reader:
        cur.execute(insert_sql, row)

insert_csv(products_csv, "products")
insert_csv(pricing_csv, "pricing")
insert_csv(orders_csv, "orders")

conn.commit()
conn.close()

print("Database created and populated successfully!")
