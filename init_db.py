import sqlite3
import os

DB_PATH = os.environ.get("DB_PATH", "lab.db")

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT NOT NULL UNIQUE,
  password TEXT NOT NULL
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS customers (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  email TEXT NOT NULL
)
""")

cur.execute("DELETE FROM users")
cur.execute("DELETE FROM customers")

cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("alice", "alice"))

sample = [
    ("Alice Johnson", "alice.johnson@example.com"),
    ("Bob Smith", "bob.smith@example.com"),
    ("Charlie Brown", "charlie.brown@example.com"),
    ("David Lee", "david.lee@example.com"),
]
cur.executemany("INSERT INTO customers (name, email) VALUES (?, ?)", sample)

conn.commit()
conn.close()
print("Database initialized.")