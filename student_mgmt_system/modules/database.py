#database setup and connection
import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
DB_PATH  = os.path.join(DATA_DIR, "students.db")

print("➡️  DEBUG — BASE_DIR:", BASE_DIR)
print("➡️  DEBUG — DATA_DIR:", DATA_DIR)
print("➡️  DEBUG — DB_PATH:", DB_PATH)

# make sure the folder exists before opening
os.makedirs(DATA_DIR, exist_ok=True)

def get_connection():
    print("Connecting to DB:", DB_PATH)   # temporary debug
    conn = sqlite3.connect(DB_PATH)
    cur  = conn.cursor()
    return conn, cur

def initialize_db():
    conn, cur = get_connection()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age  INTEGER,
            gpa  REAL
        )
    """)

    conn.commit()
    conn.close()