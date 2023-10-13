import sqlite3

conn = sqlite3.connect("ecommerce.db")
cursor = conn.cursor()

# Create tables if they don't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS cart (
        id INTEGER PRIMARY KEY,
        product_id INTEGER,
        quantity INTEGER
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        total_amount REAL
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS discount_codes (
        id INTEGER PRIMARY KEY,
        code TEXT UNIQUE,
        is_used INTEGER DEFAULT 0
    )
""")
