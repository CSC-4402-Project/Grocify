USE test;

CREATE TABLE items (
    item_id INT NOT NULL PRIMARY KEY,
    item_name VARCHAR(255),
    supplier_name VARCHAR(255),
    department VARCHAR(255),
    aisle_location VARCHAR(255),
    price DECIMAL(10, 2)
);

SELECT * FROM items;

SELECT * FROM items WHERE item_id = 3;

SELECT * FROM items WHERE department = 'Meats & Poultry';

UPDATE items SET price = 5.00 WHERE item_name = 'Turkey Sandwich';

DELETE FROM items WHERE item_id = 1;


