-- =========================================================
-- Part 2: Database & Schema (DDL)
-- =========================================================

CREATE DATABASE IF NOT EXISTS tps_financial
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

USE tps_financial;

-- ---------------------------------------------------------
-- Lookup tables
-- ---------------------------------------------------------

CREATE TABLE account_type (
    account_type_id TINYINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE transaction_type (
    transaction_type_id TINYINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE product_category (
    product_category_id TINYINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE risk_level (
    risk_level_id TINYINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL UNIQUE
);

-- ---------------------------------------------------------
-- Core entities
-- ---------------------------------------------------------

CREATE TABLE client (
    client_id INT UNSIGNED PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    dob DATE NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    phone VARCHAR(20),
    address VARCHAR(255),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE account (
    account_id INT UNSIGNED PRIMARY KEY,
    client_id INT UNSIGNED NOT NULL,
    account_type_id TINYINT UNSIGNED NOT NULL,
    open_date DATE NOT NULL,
    balance DECIMAL(15,2) NOT NULL DEFAULT 0.00,
    interest_rate DECIMAL(6,4) NOT NULL DEFAULT 0.0000,
    is_active TINYINT(1) NOT NULL DEFAULT 1,
    closed_date DATE NULL,
    CONSTRAINT fk_account_client
        FOREIGN KEY (client_id) REFERENCES client(client_id)
        ON UPDATE CASCADE ON DELETE RESTRICT,
    CONSTRAINT fk_account_type
        FOREIGN KEY (account_type_id) REFERENCES account_type(account_type_id)
        ON UPDATE CASCADE ON DELETE RESTRICT,
    INDEX idx_account_client (client_id),
    INDEX idx_account_type (account_type_id),
    CHECK (interest_rate >= 0.0000)
);

CREATE TABLE transaction (
    txn_id INT UNSIGNED PRIMARY KEY,
    account_id INT UNSIGNED NOT NULL,
    txn_date DATE NOT NULL,
    transaction_type_id TINYINT UNSIGNED NOT NULL,
    amount DECIMAL(15,2) NOT NULL,
    description VARCHAR(255),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_txn_account
        FOREIGN KEY (account_id) REFERENCES account(account_id)
        ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT fk_txn_type
        FOREIGN KEY (transaction_type_id) REFERENCES transaction_type(transaction_type_id)
        ON UPDATE CASCADE ON DELETE RESTRICT,
    INDEX idx_txn_account_date (account_id, txn_date),
    INDEX idx_txn_type (transaction_type_id)
);

CREATE TABLE product (
    product_id INT UNSIGNED PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    product_category_id TINYINT UNSIGNED NOT NULL,
    risk_level_id TINYINT UNSIGNED NOT NULL,
    mgmt_fee DECIMAL(6,4) NOT NULL,
    CONSTRAINT fk_product_category
        FOREIGN KEY (product_category_id) REFERENCES product_category(product_category_id)
        ON UPDATE CASCADE ON DELETE RESTRICT,
    CONSTRAINT fk_product_risk
        FOREIGN KEY (risk_level_id) REFERENCES risk_level(risk_level_id)
        ON UPDATE CASCADE ON DELETE RESTRICT,
    CHECK (mgmt_fee >= 0.0000),
    INDEX idx_product_category (product_category_id),
    INDEX idx_product_risk (risk_level_id)
);

CREATE TABLE holding (
    holding_id INT UNSIGNED PRIMARY KEY,
    client_id INT UNSIGNED NOT NULL,
    product_id INT UNSIGNED NOT NULL,
    units DECIMAL(18,4) NOT NULL,
    purchase_price DECIMAL(15,2) NOT NULL,
    current_value DECIMAL(15,2) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_holding_client
        FOREIGN KEY (client_id) REFERENCES client(client_id)
        ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT fk_holding_product
        FOREIGN KEY (product_id) REFERENCES product(product_id)
        ON UPDATE CASCADE ON DELETE RESTRICT,
    INDEX idx_holding_client (client_id),
    INDEX idx_holding_product (product_id),
    CHECK (units >= 0.0000),
    CHECK (purchase_price >= 0.0000),
    CHECK (current_value >= 0.0000)
);

-- =========================================================
-- Part 3: Sample Data (DML)
-- =========================================================

START TRANSACTION;

-- Lookup data
INSERT INTO account_type (name) VALUES
  ('Current'),
  ('Savings'),
  ('Loan'),
  ('Credit Card');

INSERT INTO transaction_type (name) VALUES
  ('Deposit'),
  ('Withdrawal'),
  ('Transfer'),
  ('Card Payment'),
  ('Loan Payment');

INSERT INTO product_category (name) VALUES
  ('Mutual Fund'),
  ('Bond'),
  ('ETF'),
  ('Retirement Plan');

INSERT INTO risk_level (name) VALUES
  ('Low'),
  ('Medium'),
  ('High');

-- Clients
INSERT INTO client (client_id, full_name, dob, email, phone, address) VALUES
  (1001, 'Sarah Johnson', '1985-04-12', 'sarah.j@nbf.com', '07123456789', '14 West Street, Sheffield'),
  (1002, 'Mark Thompson', '1990-11-02', 'mark.t@nbf.com', '07987654321', '22 Brook Lane, Manchester'),
  (1003, 'Priya Patel', '1978-06-30', 'priya.p@nbf.com', '07711223344', '8 Riverside Walk, Birmingham');

-- Accounts
-- Map types: Current=1, Savings=2, Loan=3, Credit Card=4
INSERT INTO account (account_id, client_id, account_type_id, open_date, balance, interest_rate) VALUES
  (20001, 1001, 1, '2020-01-10', 3500.75, 0.0100),
  (20002, 1001, 2, '2021-03-15', 12000.00, 0.0200),
  (20003, 1002, 3, '2019-07-01', -8000.00, 0.0500),
  (20004, 1003, 1, '2022-09-20', 540.20, 0.0100);

-- Products
-- Categories: Mutual Fund=1, Bond=2, ETF=3
-- Risk: High=3, Low=1, Medium=2
INSERT INTO product (product_id, name, product_category_id, risk_level_id, mgmt_fee) VALUES
  (3001, 'Global Equity Mutual Fund', 1, 3, 0.0150),
  (3002, 'UK Bond Fund', 2, 1, 0.0050),
  (3003, 'Tech Growth ETF', 3, 2, 0.0100);

-- Holdings
INSERT INTO holding (holding_id, client_id, product_id, units, purchase_price, current_value) VALUES
  (4001, 1001, 3001, 50.0000, 1200.00, 1500.00),
  (4002, 1002, 3003, 10.0000, 800.00, 950.00),
  (4003, 1003, 3002, 100.0000, 1000.00, 1100.00);

-- Transactions
-- Types: Deposit=1, Withdrawal=2, Transfer=3, Card Payment=4, Loan Payment=5
INSERT INTO transaction (txn_id, account_id, txn_date, transaction_type_id, amount, description) VALUES
  (50001, 20001, '2023-01-05', 1, 1000.00, 'Salary'),
  (50002, 20001, '2023-01-12', 2, -150.00, 'ATM Withdrawal'),
  (50003, 20002, '2023-02-01', 1, 500.00, 'Transfer from Current'),
  (50004, 20003, '2023-02-10', 5, 300.00, 'Monthly Loan Payment'),
  (50005, 20004, '2023-03-01', 4, -45.20, 'Grocery Store');

COMMIT;

-- =========================================================
-- Part 4: CRUD Operations
-- =========================================================

-- -----------------------
-- CREATE
-- -----------------------

-- Add a new client
INSERT INTO client (client_id, full_name, dob, email, phone, address)
VALUES (1004, 'John Smith', '1988-09-15', 'john.s@nbf.com', '07000000000', '1 High Street, Leeds');

-- Open a new account for an existing client (e.g., Savings for client 1004)
INSERT INTO account (account_id, client_id, account_type_id, open_date, balance, interest_rate)
VALUES (20005, 1004, 2, CURDATE(), 0.00, 0.0200);

-- Add a new investment holding
INSERT INTO holding (holding_id, client_id, product_id, units, purchase_price, current_value)
VALUES (4004, 1004, 3001, 20.0000, 500.00, 520.00);

-- -----------------------
-- READ
-- -----------------------

-- Retrieve a client’s full financial profile (accounts + balances + holdings)
SELECT
    c.client_id,
    c.full_name,
    c.email,
    c.phone,
    a.account_id,
    at.name AS account_type,
    a.balance,
    a.interest_rate,
    h.holding_id,
    p.name AS product_name,
    h.units,
    h.purchase_price,
    h.current_value
FROM client c
LEFT JOIN account a
    ON c.client_id = a.client_id
LEFT JOIN account_type at
    ON a.account_type_id = at.account_type_id
LEFT JOIN holding h
    ON c.client_id = h.client_id
LEFT JOIN product p
    ON h.product_id = p.product_id
WHERE c.client_id = 1001
ORDER BY a.account_id, h.holding_id;

-- Get all transactions for a given account
SELECT
    t.txn_id,
    t.txn_date,
    tt.name AS transaction_type,
    t.amount,
    t.description
FROM transaction t
JOIN transaction_type tt
    ON t.transaction_type_id = tt.transaction_type_id
WHERE t.account_id = 20001
ORDER BY t.txn_date;

-- List all clients with loans above £5,000 (loan balance < -5000)
SELECT
    c.client_id,
    c.full_name,
    a.account_id,
    a.balance
FROM client c
JOIN account a
    ON c.client_id = a.client_id
JOIN account_type at
    ON a.account_type_id = at.account_type_id
WHERE at.name = 'Loan'
  AND a.balance < -5000.00;

-- -----------------------
-- UPDATE
-- -----------------------

-- Update a client’s contact details
UPDATE client
SET email = 'sarah.johnson@nbf.com',
    phone = '07111111111',
    address = '20 New Street, Sheffield'
WHERE client_id = 1001;

-- Apply monthly interest to all savings accounts
-- (simple interest: balance = balance + balance * (interest_rate / 12))
UPDATE account a
JOIN account_type at
    ON a.account_type_id = at.account_type_id
SET a.balance = a.balance + (a.balance * (a.interest_rate / 12))
WHERE at.name = 'Savings'
  AND a.is_active = 1;

-- Update the current value of all holdings (example: +2% adjustment)
UPDATE holding
SET current_value = current_value * 1.02;

-- -----------------------
-- DELETE
-- -----------------------

-- Delete a transaction
DELETE FROM transaction
WHERE txn_id = 50005;

-- Close an account (soft delete: mark inactive and set closed_date)
UPDATE account
SET is_active = 0,
    closed_date = CURDATE()
WHERE account_id = 20004;

-- =========================================================
-- Part 5: Advanced SQL Queries
-- =========================================================

-- 1. Complex Joins
-- a) Show all clients with their total account balances and total investment value
SELECT
    c.client_id,
    c.full_name,
    COALESCE(SUM(DISTINCT a.balance), 0.00) AS total_account_balance,
    COALESCE(SUM(DISTINCT h.current_value), 0.00) AS total_investment_value
FROM client c
LEFT JOIN account a
    ON c.client_id = a.client_id
LEFT JOIN holding h
    ON c.client_id = h.client_id
GROUP BY c.client_id, c.full_name
ORDER BY total_account_balance + total_investment_value DESC;

-- b) List all transactions with client names and account types
SELECT
    t.txn_id,
    t.txn_date,
    c.full_name,
    at.name AS account_type,
    tt.name AS transaction_type,
    t.amount,
    t.description
FROM transaction t
JOIN account a
    ON t.account_id = a.account_id
JOIN client c
    ON a.client_id = c.client_id
JOIN account_type at
    ON a.account_type_id = at.account_type_id
JOIN transaction_type tt
    ON t.transaction_type_id = tt.transaction_type_id
ORDER BY t.txn_date DESC, t.txn_id;

-- 2. Aggregations
-- a) Total deposits per client per month
SELECT
    c.client_id,
    c.full_name,
    DATE_FORMAT(t.txn_date, '%Y-%m') AS year_month,
    SUM(t.amount) AS total_deposits
FROM transaction t
JOIN transaction_type tt
    ON t.transaction_type_id = tt.transaction_type_id
JOIN account a
    ON t.account_id = a.account_id
JOIN client c
    ON a.client_id = c.client_id
WHERE tt.name = 'Deposit'
GROUP BY c.client_id, c.full_name, DATE_FORMAT(t.txn_date, '%Y-%m')
ORDER BY c.client_id, year_month;

-- b) Average balance by account type
SELECT
    at.name AS account_type,
    AVG(a.balance) AS avg_balance
FROM account a
JOIN account_type at
    ON a.account_type_id = at.account_type_id
GROUP BY at.name
ORDER BY avg_balance DESC;

-- c) Total assets under management (AUM: accounts + holdings)
SELECT
    (SELECT COALESCE(SUM(balance), 0.00) FROM account) +
    (SELECT COALESCE(SUM(current_value), 0.00) FROM holding) AS total_aum;

-- 3. Window Functions (MySQL 8+)
-- a) Rank clients by total net worth (accounts + holdings)
WITH client_net_worth AS (
    SELECT
        c.client_id,
        c.full_name,
        COALESCE(SUM(DISTINCT a.balance), 0.00) AS total_account_balance,
        COALESCE(SUM(DISTINCT h.current_value), 0.00) AS total_investment_value,
        COALESCE(SUM(DISTINCT a.balance), 0.00) +
        COALESCE(SUM(DISTINCT h.current_value), 0.00) AS net_worth
    FROM client c
    LEFT JOIN account a
        ON c.client_id = a.client_id
    LEFT JOIN holding h
        ON c.client_id = h.client_id
    GROUP BY c.client_id, c.full_name
)
SELECT
    client_id,
    full_name,
    total_account_balance,
    total_investment_value,
    net_worth,
    RANK() OVER (ORDER BY net_worth DESC) AS net_worth_rank
FROM client_net_worth
ORDER BY net_worth DESC;

-- b) Running balance per account ordered by transaction date
SELECT
    t.account_id,
    t.txn_id,
    t.txn_date,
    tt.name AS transaction_type,
    t.amount,
    SUM(t.amount) OVER (
        PARTITION BY t.account_id
        ORDER BY t.txn_date, t.txn_id
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS running_balance_delta
FROM transaction t
JOIN transaction_type tt
    ON t.transaction_type_id = tt.transaction_type_id
ORDER BY t.account_id, t.txn_date, t.txn_id;

-- 4. Subqueries
-- a) Clients whose investment returns exceed 10%
-- Return = (current_value - purchase_price) / purchase_price
SELECT
    c.client_id,
    c.full_name,
    SUM(h.purchase_price) AS total_invested,
    SUM(h.current_value) AS total_current_value,
    (SUM(h.current_value) - SUM(h.purchase_price)) / SUM(h.purchase_price) AS total_return_ratio
FROM client c
JOIN holding h
    ON c.client_id = h.client_id
GROUP BY c.client_id, c.full_name
HAVING total_return_ratio > 0.10;

-- b) Accounts with more than 5 transactions in the last 30 days
SELECT
    a.account_id,
    c.client_id,
    c.full_name,
    COUNT(t.txn_id) AS txn_count_last_30_days
FROM account a
JOIN client c
    ON a.client_id = c.client_id
JOIN transaction t
    ON a.account_id = t.account_id
WHERE t.txn_date >= (CURDATE() - INTERVAL 30 DAY)
GROUP BY a.account_id, c.client_id, c.full_name
HAVING COUNT(t.txn_id) > 5;

-- 5. Banking-Relevant Analysis
-- a) Identify clients at risk (loan balance > 2× total deposits)
-- Here we approximate "total deposits" as sum of positive Deposit transactions.
WITH client_loans AS (
    SELECT
        c.client_id,
        c.full_name,
        SUM(a.balance) AS total_loan_balance
    FROM client c
    JOIN account a
        ON c.client_id = a.client_id
    JOIN account_type at
        ON a.account_type_id = at.account_type_id
    WHERE at.name = 'Loan'
    GROUP BY c.client_id, c.full_name
),
client_deposits AS (
    SELECT
        c.client_id,
        SUM(t.amount) AS total_deposits
    FROM transaction t
    JOIN transaction_type tt
        ON t.transaction_type_id = tt.transaction_type_id
    JOIN account a
        ON t.account_id = a.account_id
    JOIN client c
        ON a.client_id = c.client_id
    WHERE tt.name = 'Deposit'
      AND t.amount > 0
    GROUP BY c.client_id
)
SELECT
    l.client_id,
    l.full_name,
    l.total_loan_balance,
    COALESCE(d.total_deposits, 0.00) AS total_deposits
FROM client_loans l
LEFT JOIN client_deposits d
    ON l.client_id = d.client_id
WHERE l.total_loan_balance < 0
  AND ABS(l.total_loan_balance) > 2 * COALESCE(d.total_deposits, 0.00);

-- b) Calculate interest accrued per account type
-- Simple example: interest_accrued = balance * interest_rate (annual)
SELECT
    at.name AS account_type,
    SUM(a.balance * a.interest_rate) AS total_interest_accrued
FROM account a
JOIN account_type at
    ON a.account_type_id = at.account_type_id
GROUP BY at.name
ORDER BY total_interest_accrued DESC;
