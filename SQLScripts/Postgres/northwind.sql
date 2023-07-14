DROP DATABASE northwind;
CREATE DATABASE northwind;
\connect northwind;

CREATE TABLE  customers (
  id SERIAL NOT NULL,
  company VARCHAR(50) NULL DEFAULT NULL,
  last_name VARCHAR(50) NULL DEFAULT NULL,
  first_name VARCHAR(50) NULL DEFAULT NULL,
  email_address VARCHAR(50) NULL DEFAULT NULL,
  job_title VARCHAR(50) NULL DEFAULT NULL,
  business_phone VARCHAR(25) NULL DEFAULT NULL,
  home_phone VARCHAR(25) NULL DEFAULT NULL,
  mobile_phone VARCHAR(25) NULL DEFAULT NULL,
  fax_number VARCHAR(25) NULL DEFAULT NULL,
  address TEXT NULL DEFAULT NULL,
  city VARCHAR(50) NULL DEFAULT NULL,
  state_province VARCHAR(50) NULL DEFAULT NULL,
  zip_postal_code VARCHAR(15) NULL DEFAULT NULL,
  country_region VARCHAR(50) NULL DEFAULT NULL,
  web_page TEXT NULL DEFAULT NULL,
  notes TEXT NULL DEFAULT NULL,
  attachments BYTEA,
  PRIMARY KEY (id));
  CREATE INDEX customers_city ON customers (city ASC);
  CREATE INDEX customers_company ON customers (company ASC);
  CREATE INDEX customers_first_name ON customers (first_name ASC);
  CREATE INDEX customers_last_name ON customers (last_name ASC);
  CREATE INDEX customers_zip_postal_code ON customers (zip_postal_code ASC);
  CREATE INDEX customers_state_province ON customers (state_province ASC);

CREATE TABLE  employees (
  id SERIAL NOT NULL,
  company VARCHAR(50) NULL DEFAULT NULL,
  last_name VARCHAR(50) NULL DEFAULT NULL,
  first_name VARCHAR(50) NULL DEFAULT NULL,
  email_address VARCHAR(50) NULL DEFAULT NULL,
  job_title VARCHAR(50) NULL DEFAULT NULL,
  business_phone VARCHAR(25) NULL DEFAULT NULL,
  home_phone VARCHAR(25) NULL DEFAULT NULL,
  mobile_phone VARCHAR(25) NULL DEFAULT NULL,
  fax_number VARCHAR(25) NULL DEFAULT NULL,
  address TEXT NULL DEFAULT NULL,
  city VARCHAR(50) NULL DEFAULT NULL,
  state_province VARCHAR(50) NULL DEFAULT NULL,
  zip_postal_code VARCHAR(15) NULL DEFAULT NULL,
  country_region VARCHAR(50) NULL DEFAULT NULL,
  web_page TEXT NULL DEFAULT NULL,
  notes TEXT NULL DEFAULT NULL,
  attachments BYTEA,
  PRIMARY KEY (id));
  CREATE INDEX employees_city ON employees (city ASC);
  CREATE INDEX employees_company ON employees (company ASC);
  CREATE INDEX employees_first_name ON employees (first_name ASC);
  CREATE INDEX employees_last_name ON employees (last_name ASC);
  CREATE INDEX employees_zip_postal_code ON employees (zip_postal_code ASC);
  CREATE INDEX employees_state_province ON employees (state_province ASC);

CREATE TABLE  privileges (
  id SERIAL NOT NULL,
  privilege_name VARCHAR(50) NULL DEFAULT NULL,
  PRIMARY KEY (id));

CREATE TABLE  employee_privileges (
  employee_id INT NOT NULL,
  privilege_id INT NOT NULL,
  PRIMARY KEY (employee_id, privilege_id),
  CONSTRAINT fk_employee_privileges_employees1
    FOREIGN KEY (employee_id)
    REFERENCES employees (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_employee_privileges_privileges1
    FOREIGN KEY (privilege_id)
    REFERENCES privileges (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
  CREATE INDEX employee_privileges_employee_id ON employee_privileges (employee_id ASC);
  CREATE INDEX employee_privileges_privilege_id ON employee_privileges (privilege_id ASC);
  CREATE INDEX employee_privileges_privilege_id_2 ON employee_privileges (privilege_id ASC);

CREATE TABLE  inventory_transaction_types (
  id INT NOT NULL,
  type_name VARCHAR(50) NOT NULL,
  PRIMARY KEY (id));

CREATE TABLE  shippers (
  id SERIAL NOT NULL,
  company VARCHAR(50) NULL DEFAULT NULL,
  last_name VARCHAR(50) NULL DEFAULT NULL,
  first_name VARCHAR(50) NULL DEFAULT NULL,
  email_address VARCHAR(50) NULL DEFAULT NULL,
  job_title VARCHAR(50) NULL DEFAULT NULL,
  business_phone VARCHAR(25) NULL DEFAULT NULL,
  home_phone VARCHAR(25) NULL DEFAULT NULL,
  mobile_phone VARCHAR(25) NULL DEFAULT NULL,
  fax_number VARCHAR(25) NULL DEFAULT NULL,
  address TEXT NULL DEFAULT NULL,
  city VARCHAR(50) NULL DEFAULT NULL,
  state_province VARCHAR(50) NULL DEFAULT NULL,
  zip_postal_code VARCHAR(15) NULL DEFAULT NULL,
  country_region VARCHAR(50) NULL DEFAULT NULL,
  web_page TEXT NULL DEFAULT NULL,
  notes TEXT NULL DEFAULT NULL,
  attachments BYTEA,
  PRIMARY KEY (id));
  CREATE INDEX shippers_city ON shippers (city ASC);
  CREATE INDEX shippers_company ON shippers (company ASC);
  CREATE INDEX shippers_first_name ON shippers (first_name ASC);
  CREATE INDEX shippers_last_name ON shippers (last_name ASC);
  CREATE INDEX shippers_zip_postal_code ON shippers (zip_postal_code ASC);
  CREATE INDEX shippers_state_province ON shippers (state_province ASC);

CREATE TABLE  orders_tax_status (
  id INT NOT NULL,
  tax_status_name VARCHAR(50) NOT NULL,
  PRIMARY KEY (id));

CREATE TABLE  orders_status (
  id INT NOT NULL,
  status_name VARCHAR(50) NOT NULL,
  PRIMARY KEY (id));

CREATE TABLE  orders (
  id SERIAL NOT NULL,
  employee_id INT NULL DEFAULT NULL,
  customer_id INT NULL DEFAULT NULL,
  order_date TIMESTAMP NULL DEFAULT NULL,
  shipped_date TIMESTAMP NULL DEFAULT NULL,
  shipper_id INT NULL DEFAULT NULL,
  ship_name VARCHAR(50) NULL DEFAULT NULL,
  ship_address TEXT NULL DEFAULT NULL,
  ship_city VARCHAR(50) NULL DEFAULT NULL,
  ship_state_province VARCHAR(50) NULL DEFAULT NULL,
  ship_zip_postal_code VARCHAR(50) NULL DEFAULT NULL,
  ship_country_region VARCHAR(50) NULL DEFAULT NULL,
  shipping_fee DECIMAL(19,4) NULL DEFAULT '0.0000',
  taxes DECIMAL(19,4) NULL DEFAULT '0.0000',
  payment_type VARCHAR(50) NULL DEFAULT NULL,
  paid_date TIMESTAMP NULL DEFAULT NULL,
  notes TEXT NULL DEFAULT NULL,
  tax_rate DOUBLE PRECISION NULL DEFAULT '0',
  tax_status_id INT NULL DEFAULT NULL,
  status_id INT NULL DEFAULT '0',
  PRIMARY KEY (id),
  FOREIGN KEY (customer_id)
    REFERENCES customers (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  FOREIGN KEY (employee_id)
    REFERENCES employees (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  FOREIGN KEY (shipper_id)
    REFERENCES shippers (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  FOREIGN KEY (tax_status_id)
    REFERENCES orders_tax_status (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  FOREIGN KEY (status_id)
    REFERENCES orders_status (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
  CREATE INDEX orders_customer_id ON orders (customer_id ASC);
  CREATE INDEX orders_employee_id ON orders (employee_id ASC);
  CREATE INDEX orders_id ON orders (id ASC);
  CREATE INDEX orders_shipper_id ON orders (shipper_id ASC);
  CREATE INDEX orders_tax_status ON orders (tax_status_id ASC);
  CREATE INDEX orders_ship_zip_postal_code ON orders (ship_zip_postal_code ASC);


CREATE TABLE  products (
  supplier_ids TEXT NULL DEFAULT NULL,
  id SERIAL NOT NULL,
  product_code VARCHAR(25) NULL DEFAULT NULL,
  product_name VARCHAR(50) NULL DEFAULT NULL,
  description TEXT NULL DEFAULT NULL,
  standard_cost DECIMAL(19,4) NULL DEFAULT '0.0000',
  list_price DECIMAL(19,4) NOT NULL DEFAULT '0.0000',
  reorder_level INT NULL DEFAULT NULL,
  target_level INT NULL DEFAULT NULL,
  quantity_per_unit VARCHAR(50) NULL DEFAULT NULL,
  discontinued INT NOT NULL DEFAULT '0',
  minimum_reorder_quantity INT NULL DEFAULT NULL,
  category VARCHAR(50) NULL DEFAULT NULL,
  attachments BYTEA,
  PRIMARY KEY (id));
  CREATE INDEX products_product_code ON products (product_code ASC);


CREATE TABLE  purchase_order_status (
  id INT NOT NULL,
  status VARCHAR(50) NULL DEFAULT NULL,
  PRIMARY KEY (id));

CREATE TABLE  suppliers (
  id SERIAL NOT NULL,
  company VARCHAR(50) NULL DEFAULT NULL,
  last_name VARCHAR(50) NULL DEFAULT NULL,
  first_name VARCHAR(50) NULL DEFAULT NULL,
  email_address VARCHAR(50) NULL DEFAULT NULL,
  job_title VARCHAR(50) NULL DEFAULT NULL,
  business_phone VARCHAR(25) NULL DEFAULT NULL,
  home_phone VARCHAR(25) NULL DEFAULT NULL,
  mobile_phone VARCHAR(25) NULL DEFAULT NULL,
  fax_number VARCHAR(25) NULL DEFAULT NULL,
  address TEXT NULL DEFAULT NULL,
  city VARCHAR(50) NULL DEFAULT NULL,
  state_province VARCHAR(50) NULL DEFAULT NULL,
  zip_postal_code VARCHAR(15) NULL DEFAULT NULL,
  country_region VARCHAR(50) NULL DEFAULT NULL,
  web_page TEXT NULL DEFAULT NULL,
  notes TEXT NULL DEFAULT NULL,
  attachments BYTEA,
  PRIMARY KEY (id));
  CREATE INDEX suppliers_city on suppliers (city ASC);
  CREATE INDEX suppliers_company ON suppliers (company ASC);
  CREATE INDEX suppliers_first_name ON suppliers (first_name ASC);
  CREATE INDEX suppliers_last_name ON suppliers (last_name ASC);
  CREATE INDEX suppliers_zip_postal_code ON suppliers(zip_postal_code ASC);
  CREATE INDEX suppliers_state_province ON suppliers (state_province ASC);

CREATE TABLE  purchase_orders (
  id SERIAL NOT NULL,
  supplier_id INT NULL DEFAULT NULL,
  created_by INT NULL DEFAULT NULL,
  submitted_date TIMESTAMP NULL DEFAULT NULL,
  creation_date TIMESTAMP NULL DEFAULT NULL,
  status_id INT NULL DEFAULT '0',
  expected_date TIMESTAMP NULL DEFAULT NULL,
  shipping_fee DECIMAL(19,4) NOT NULL DEFAULT '0.0000',
  taxes DECIMAL(19,4) NOT NULL DEFAULT '0.0000',
  payment_date TIMESTAMP NULL DEFAULT NULL,
  payment_amount DECIMAL(19,4) NULL DEFAULT '0.0000',
  payment_method VARCHAR(50) NULL DEFAULT NULL,
  notes TEXT NULL DEFAULT NULL,
  approved_by INT NULL DEFAULT NULL,
  approved_date TIMESTAMP NULL DEFAULT NULL,
  submitted_by INT NULL DEFAULT NULL,
  PRIMARY KEY (id),
  CONSTRAINT fk_purchase_orders_employees
    FOREIGN KEY (created_by)
    REFERENCES employees (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_purchase_orders_purchase_order_status
    FOREIGN KEY (status_id)
    REFERENCES purchase_order_status (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_purchase_orders_suppliers
    FOREIGN KEY (supplier_id)
    REFERENCES suppliers (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
  CREATE INDEX purchase_orders_created_by ON purchase_orders (created_by ASC);
  CREATE INDEX purchase_orders_status_id ON purchase_orders (status_id ASC);
  CREATE INDEX purchase_orders_supplier_id ON purchase_orders (supplier_id ASC);

CREATE TABLE  inventory_transactions (
  id SERIAL NOT NULL,
  transaction_type INT NOT NULL,
  transaction_created_date TIMESTAMP NULL DEFAULT NULL,
  transaction_modified_date TIMESTAMP NULL DEFAULT NULL,
  product_id INT NOT NULL,
  quantity INT NOT NULL,
  purchase_order_id INT NULL DEFAULT NULL,
  customer_order_id INT NULL DEFAULT NULL,
  comments VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (id),
  CONSTRAINT fk_inventory_transactions_orders
    FOREIGN KEY (customer_order_id)
    REFERENCES orders (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_inventory_transactions_products
    FOREIGN KEY (product_id)
    REFERENCES products (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_inventory_transactions_purchase_orders
    FOREIGN KEY (purchase_order_id)
    REFERENCES purchase_orders (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_inventory_transactions_inventory_transaction_types
    FOREIGN KEY (transaction_type)
    REFERENCES inventory_transaction_types (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
  CREATE INDEX inventory_transactions_customer_order_id ON inventory_transactions (customer_order_id ASC);
  CREATE INDEX inventory_transactions_product_id ON inventory_transactions (product_id ASC);
  CREATE INDEX inventory_transactions_purchase_order_id ON inventory_transactions (purchase_order_id ASC);
  CREATE INDEX inventory_transactions_transaction_type ON inventory_transactions (transaction_type ASC);

CREATE TABLE  invoices (
  id SERIAL NOT NULL,
  order_id INT NULL DEFAULT NULL,
  invoice_date TIMESTAMP NULL DEFAULT NULL,
  due_date TIMESTAMP NULL DEFAULT NULL,
  tax DECIMAL(19,4) NULL DEFAULT '0.0000',
  shipping DECIMAL(19,4) NULL DEFAULT '0.0000',
  amount_due DECIMAL(19,4) NULL DEFAULT '0.0000',
  PRIMARY KEY (id),
  CONSTRAINT fk_invoices_orders
    FOREIGN KEY (order_id)
    REFERENCES orders (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
  CREATE INDEX invoices_id ON invoices (id ASC);
  CREATE INDEX fk_invoices_orders1_idx ON invoices (order_id ASC);

CREATE TABLE  order_details_status (
  id INT NOT NULL,
  status_name VARCHAR(50) NOT NULL,
  PRIMARY KEY (id));

CREATE TABLE  order_details (
  id SERIAL NOT NULL,
  order_id INT NOT NULL,
  product_id INT NULL DEFAULT NULL,
  quantity DECIMAL(18,4) NOT NULL DEFAULT '0.0000',
  unit_price DECIMAL(19,4) NULL DEFAULT '0.0000',
  discount DOUBLE PRECISION NOT NULL DEFAULT '0',
  status_id INT NULL DEFAULT NULL,
  date_allocated TIMESTAMP NULL DEFAULT NULL,
  purchase_order_id INT NULL DEFAULT NULL,
  inventory_id INT NULL DEFAULT NULL,
  PRIMARY KEY (id),
  CONSTRAINT fk_order_details_orders
    FOREIGN KEY (order_id)
    REFERENCES orders (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_order_details_products
    FOREIGN KEY (product_id)
    REFERENCES products (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_order_details_order_details_status
    FOREIGN KEY (status_id)
    REFERENCES order_details_status (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
  CREATE INDEX order_details_id ON order_details (id ASC);
  CREATE INDEX order_details_inventory_id ON order_details (inventory_id ASC);
  CREATE INDEX order_details_product_id ON order_details (product_id ASC);
  CREATE INDEX order_details_purchase_order_id ON order_details (purchase_order_id ASC);
  CREATE INDEX fk_order_details_orders_idx ON order_details(order_id ASC);
  CREATE INDEX fk_order_details_order_details_status_idx ON order_details (status_id ASC);

CREATE TABLE  purchase_order_details (
  id SERIAL NOT NULL,
  purchase_order_id INT NOT NULL,
  product_id INT NULL DEFAULT NULL,
  quantity DECIMAL(18,4) NOT NULL,
  unit_cost DECIMAL(19,4) NOT NULL,
  date_received TIMESTAMP NULL DEFAULT NULL,
  posted_to_inventory INT NOT NULL DEFAULT '0',
  inventory_id INT NULL DEFAULT NULL,
  PRIMARY KEY (id),
  CONSTRAINT fk_purchase_order_details_inventory_transactions
    FOREIGN KEY (inventory_id)
    REFERENCES inventory_transactions (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_purchase_order_details_products
    FOREIGN KEY (product_id)
    REFERENCES products (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_purchase_order_details_purchase_orders
    FOREIGN KEY (purchase_order_id)
    REFERENCES purchase_orders (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
  CREATE INDEX purchase_order_details_id ON purchase_order_details (id ASC);
  CREATE INDEX purchase_order_details_inventory_id ON purchase_order_details (inventory_id ASC);
  CREATE INDEX purchase_order_details_purchase_order_id ON purchase_order_details (purchase_order_id ASC);
  CREATE INDEX purchase_order_details_product_id ON purchase_order_details (product_id ASC);

CREATE TABLE  sales_reports (
  group_by VARCHAR(50) NOT NULL,
  display VARCHAR(50) NULL DEFAULT NULL,
  title VARCHAR(50) NULL DEFAULT NULL,
  filter_row_source TEXT NULL DEFAULT NULL,
  "default" INT NOT NULL DEFAULT '0',
  PRIMARY KEY (group_by));

CREATE TABLE  strings (
  string_id SERIAL NOT NULL,
  string_data VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (string_id));