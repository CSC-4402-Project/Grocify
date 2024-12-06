import mysql.connector
from random import choice, randint

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234567",
    database="test"
)
cursor = conn.cursor()


items = [
    ("Banana", "Calandro's Supermarket", "Produce", "A1", 0.50),
    ("Turkey Sandwich", "Anthony's Italian Deli", "Deli", "B2", 8.50),
    ("Ribeye Steak", "Maxwell's Market", "Meats", "C1", 18.00),
    ("Whole Chicken", "Hebert's Specialty Meats", "Meats & Poultry", "A2", 12.00),
    ("Fresh Shrimp", "Tony's Seafood", "Seafood", "A2", 14.00),
    ("Whole Milk", "Bet-R Grocery", "Dairy", "A2", 3.50),
    ("Frozen Pizza", "Neighborhood Grocery", "Frozen Foods", "A2", 6.00),
    ("Black Beans (Canned)", "Bet-R Grocery", "Canned & Packaged Goods", "A2", 1.25),
    ("Coke", "Albertson's", "Beverages", "A2", 2.00)



]

for i, item in enumerate(items, start=1):
    cursor.execute("""
    INSERT INTO items (item_id, item_name, supplier_name, department, aisle_location, price)
    VALUES (%s, %s, %s, %s, %s, %s)
    """, (i, *item))

conn.commit()
cursor.close()
conn.close()




