CREATE DATABASE user_accounts;

use user_accounts

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    password VARCHAR(255) NOT NULL
);

INSERT INTO users (username, email, password)
VALUES
    ('john_doe', 'john@example.com', PASSWORD('secret')),
    ('jane_smith', 'jane@example.com', PASSWORD('letmein'));
