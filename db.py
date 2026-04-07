import sqlite3

DB_NAME = "accounting.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)

    # Accounts table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS accounts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        type TEXT,  -- Asset, Liability, Income, Expense
        balance REAL DEFAULT 0
    )
    """)

    # Transactions table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        account_id INTEGER,
        debit REAL,
        credit REAL,
        narration TEXT,
        gst REAL DEFAULT 0,
        tds REAL DEFAULT 0,
        FOREIGN KEY(account_id) REFERENCES accounts(id)
    )
    """)

    # Inventory table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS inventory (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item_name TEXT,
        hsn_code TEXT,
        quantity REAL,
        rate REAL,
        value REAL
    )
    """)

    conn.commit()
    conn.close()

def get_connection():
    return sqlite3.connect(DB_NAME)
