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