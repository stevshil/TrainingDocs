#!/usr/bin/env python3

import sqlite3

def create_and_populate_database(db_name="mobile_store.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # ---------------------------
    # Create Tables
    # ---------------------------

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Products (
        product_id INTEGER PRIMARY KEY AUTOINCREMENT,
        model TEXT NOT NULL,
        manufacturer TEXT NOT NULL,
        name TEXT NOT NULL,
        price_net REAL NOT NULL,
        tax_rate REAL NOT NULL,
        product_code TEXT UNIQUE NOT NULL,
        release_date TEXT NOT NULL,
        stock_quantity INTEGER DEFAULT 0
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Customers (
        customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        phone TEXT,
        address TEXT
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Orders (
        order_id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER NOT NULL,
        order_date TEXT NOT NULL,
        FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS OrderItems (
        order_item_id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_id INTEGER NOT NULL,
        product_id INTEGER NOT NULL,
        quantity INTEGER NOT NULL,
        price_net_at_purchase REAL NOT NULL,
        tax_rate_at_purchase REAL NOT NULL,
        FOREIGN KEY (order_id) REFERENCES Orders(order_id),
        FOREIGN KEY (product_id) REFERENCES Products(product_id)
    );
    """)

    # ---------------------------
    # Insert Product Data
    # ---------------------------

    products = [
        ('Galaxy S24', 'Samsung', 'Samsung Galaxy S24 128GB', 620.00, 0.20, 'SAM-S24-128', '2024-01-15', 120),
        ('Galaxy S24 Ultra', 'Samsung', 'Samsung Galaxy S24 Ultra 256GB', 980.00, 0.20, 'SAM-S24U-256', '2024-01-15', 80),
        ('iPhone 15', 'Apple', 'Apple iPhone 15 128GB', 650.00, 0.20, 'APP-IP15-128', '2023-09-22', 150),
        ('iPhone 15 Pro', 'Apple', 'Apple iPhone 15 Pro 256GB', 1020.00, 0.20, 'APP-IP15P-256', '2023-09-22', 90),
        ('Pixel 8', 'Google', 'Google Pixel 8 128GB', 520.00, 0.20, 'GOO-PX8-128', '2023-10-12', 110),
        ('Pixel 8 Pro', 'Google', 'Google Pixel 8 Pro 256GB', 780.00, 0.20, 'GOO-PX8P-256', '2023-10-12', 70),
        ('Xperia 1 V', 'Sony', 'Sony Xperia 1 V 256GB', 900.00, 0.20, 'SON-XP1V-256', '2023-06-01', 40),
        ('Xperia 10 V', 'Sony', 'Sony Xperia 10 V 128GB', 340.00, 0.20, 'SON-XP10V-128', '2023-06-01', 60),
        ('OnePlus 12', 'OnePlus', 'OnePlus 12 256GB', 680.00, 0.20, 'ONE-12-256', '2024-01-23', 100),
        ('OnePlus 12R', 'OnePlus', 'OnePlus 12R 128GB', 420.00, 0.20, 'ONE-12R-128', '2024-01-23', 140),
        ('Moto Edge 40', 'Motorola', 'Motorola Edge 40 256GB', 360.00, 0.20, 'MOT-E40-256', '2023-05-04', 75),
        ('Moto G84', 'Motorola', 'Motorola G84 256GB', 220.00, 0.20, 'MOT-G84-256', '2023-09-01', 200),
        ('Nokia XR21', 'Nokia', 'Nokia XR21 128GB', 380.00, 0.20, 'NOK-XR21-128', '2023-05-10', 50),
        ('Nokia G42', 'Nokia', 'Nokia G42 128GB', 180.00, 0.20, 'NOK-G42-128', '2023-06-28', 180),
        ('Asus ROG 8', 'Asus', 'Asus ROG Phone 8 256GB', 950.00, 0.20, 'ASU-ROG8-256', '2024-01-08', 30),
        ('Asus Zenfone 10', 'Asus', 'Asus Zenfone 10 128GB', 520.00, 0.20, 'ASU-ZF10-128', '2023-07-01', 55),
        ('Honor Magic 6', 'Honor', 'Honor Magic 6 256GB', 620.00, 0.20, 'HON-MG6-256', '2024-01-10', 65),
        ('Honor 90', 'Honor', 'Honor 90 256GB', 330.00, 0.20, 'HON-90-256', '2023-07-06', 95),
        ('Xiaomi 14', 'Xiaomi', 'Xiaomi 14 256GB', 680.00, 0.20, 'XIA-14-256', '2024-02-25', 85),
        ('Xiaomi Redmi Note 13', 'Xiaomi', 'Redmi Note 13 128GB', 190.00, 0.20, 'XIA-RN13-128', '2024-01-05', 210)
    ]

    cursor.executemany("""
        INSERT INTO Products (model, manufacturer, name, price_net, tax_rate, product_code, release_date, stock_quantity)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?);
    """, products)

    # ---------------------------
    # Insert Customer Data
    # ---------------------------

    customers = [
        ('Alice', 'Turner', 'alice.turner@example.com', '07111 234567', '12 Marine Parade, Folkestone'),
        ('Ben', 'Hughes', 'ben.hughes@example.com', '07222 345678', '44 Sandgate Road, Folkestone'),
        ('Chloe', 'Martin', 'chloe.martin@example.com', '07333 456789', '8 Dover Road, Folkestone'),
        ('Daniel', 'Reed', 'daniel.reed@example.com', '07444 567890', '19 Castle Hill, Dover'),
        ('Ella', 'Shaw', 'ella.shaw@example.com', '07555 678901', '3 Harbour Way, Hythe'),
        ('Frank', 'Bennett', 'frank.bennett@example.com', '07666 789012', '22 Canterbury Lane, Canterbury'),
        ('Grace', 'Foster', 'grace.foster@example.com', '07777 890123', '5 Station Road, Ashford'),
        ('Harry', 'Cole', 'harry.cole@example.com', '07888 901234', '17 Tontine Street, Folkestone'),
        ('Isla', 'Wright', 'isla.wright@example.com', '07999 012345', '9 Millfield, Dover'),
        ('Jack', 'Stevens', 'jack.stevens@example.com', '07000 123456', '14 High Street, Hythe'),
        ('Katie', 'Morgan', 'katie.morgan@example.com', '07123 987654', '6 The Leas, Folkestone'),
        ('Leo', 'Parker', 'leo.parker@example.com', '07234 876543', '2 West Terrace, Folkestone')
    ]

    cursor.executemany("""
        INSERT INTO Customers (first_name, last_name, email, phone, address)
        VALUES (?, ?, ?, ?, ?);
    """, customers)

    # ---------------------------
    # Insert Orders
    # ---------------------------

    orders = [
        (1, '2024-02-01'),
        (2, '2024-02-03'),
        (3, '2024-02-05'),
        (4, '2024-02-06'),
        (5, '2024-02-10'),
        (6, '2024-02-12'),
        (7, '2024-02-14'),
        (8, '2024-02-15'),
        (9, '2024-02-18'),
        (10, '2024-02-20'),
        (11, '2024-02-22'),
        (12, '2024-02-25'),
        (1, '2024-03-01'),
        (3, '2024-03-02'),
        (5, '2024-03-05'),
        (7, '2024-03-06'),
        (9, '2024-03-08'),
        (11, '2024-03-10'),
        (2, '2024-03-12'),
        (4, '2024-03-15')
    ]

    cursor.executemany("""
        INSERT INTO Orders (customer_id, order_date)
        VALUES (?, ?);
    """, orders)

    # ---------------------------
    # Insert Order Items
    # ---------------------------

    order_items = [
        (1, 3, 1, 650.00, 0.20),
        (2, 1, 1, 620.00, 0.20),
        (3, 5, 1, 520.00, 0.20),
        (4, 10, 2, 420.00, 0.20),
        (5, 2, 1, 980.00, 0.20),
        (6, 4, 1, 1020.00, 0.20),
        (7, 12, 3, 220.00, 0.20),
        (8, 9, 1, 680.00, 0.20),
        (9, 14, 2, 180.00, 0.20),
        (10, 7, 1, 900.00, 0.20),
        (11, 8, 1, 340.00, 0.20),
        (12, 6, 1, 780.00, 0.20),
        (13, 3, 1, 650.00, 0.20),
        (14, 5, 1, 520.00, 0.20),
        (15, 18, 2, 330.00, 0.20),
        (16, 11, 1, 360.00, 0.20),
        (17, 19, 1, 680.00, 0.20),
        (18, 20, 2, 190.00, 0.20),
        (19, 1, 1, 620.00, 0.20),
        (20, 4, 1, 1020.00, 0.20),
        (20, 3, 1, 650.00, 0.20),
        (15, 9, 1, 680.00, 0.20),
        (7, 13, 1, 380.00, 0.20),
        (8, 16, 1, 520.00, 0.20),
        (12, 17, 1, 620.00, 0.20),
        (10, 15, 1, 950.00, 0.20),
        (11, 2, 1, 980.00, 0.20),
        (14, 6, 1, 780.00, 0.20),
        (18, 10, 1, 420.00, 0.20),
        (19, 7, 1, 900.00, 0.20)
    ]

    cursor.executemany("""
        INSERT INTO OrderItems (order_id, product_id, quantity, price_net_at_purchase, tax_rate_at_purchase)
        VALUES (?, ?, ?, ?, ?);
    """, order_items)

    conn.commit()
    conn.close()
    print("Database created and populated successfully.")

if __name__ == "__main__":
    create_and_populate_database()
