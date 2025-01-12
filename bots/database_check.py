# database_check.py
import sqlite3

DB_FILE = "conversation_history.db"  # Path to your SQLite database

def ensure_table_exists():
    """Ensure the conversations table exists in the SQLite database."""
    conn = sqlite3.connect(DB_FILE)  # Create a new connection for this check
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS conversations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user TEXT NOT NULL,
        role TEXT NOT NULL,
        content TEXT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)
    conn.commit()
    conn.close()