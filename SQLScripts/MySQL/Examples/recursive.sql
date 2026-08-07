CREATE TABLE employees (
  id INT PRIMARY KEY,
  name VARCHAR(50),
  manager_id INT
);

INSERT INTO employees (id, name, manager_id) VALUES
  (1, 'Alice', NULL),     -- top-level manager
  (2, 'Bob', 1),          -- reports to Alice
  (3, 'Carol', 2),        -- reports to Bob
  (4, 'Dave', 2),         -- reports to Bob
  (5, 'Eve', 3),          -- reports to Carol
  (6, 'Frank', 3);        -- reports to Carol

SELECT 
  e1.id AS level1_id,
  e1.name AS level1_name,
  e2.id AS level2_id,
  e2.name AS level2_name,
  e3.id AS level3_id,
  e3.name AS level3_name
FROM employees e1
LEFT JOIN employees e2 ON e2.manager_id = e1.id
LEFT JOIN employees e3 ON e3.manager_id = e2.id
WHERE e1.id = 1;

-- MySQL RECURSIVE command
WITH RECURSIVE hierarchy AS (
  -- Anchor
  SELECT 
    e.id,
    e.name,
    e.manager_id,
    CAST(NULL AS CHAR(50)) AS manager_name,
    0 AS level
  FROM employees e
  WHERE e.id = 1

  UNION ALL

  -- Recursive
  SELECT 
    e.id,
    e.name,
    e.manager_id,
    m.name AS manager_name,
    h.level + 1
  FROM employees e
  JOIN hierarchy h
    ON e.manager_id = h.id
  LEFT JOIN employees m
    ON m.id = e.manager_id
)
SELECT * FROM hierarchy;

