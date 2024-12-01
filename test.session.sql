
DROP DATABASE IF EXISTS test;
CREATE DATABASE test;
USE test;

CREATE TABLE items (
    item_id INT NOT NULL PRIMARY KEY,
    item_name VARCHAR(255),
    company VARCHAR(255),
    department VARCHAR(255),
    aisle_location VARCHAR(255),
    price DECIMAL(10, 2)
);





