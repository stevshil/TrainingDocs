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