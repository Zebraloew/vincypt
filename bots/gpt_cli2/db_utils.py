import os
import sqlite3
from datetime import datetime, timezone
from config import DB_FILE

# Ensure database directory exists
DB_DIR = os.path.dirname(DB_FILE)
os.makedirs(DB_DIR, exist_ok=True)

# Register datetime converters
def adapt_datetime_iso(val):
    return val.isoformat()

def convert_datetime(val):
    return datetime.fromisoformat(val.decode())

sqlite3.register_adapter(datetime, adapt_datetime_iso)
sqlite3.register_converter("timestamp", convert_datetime)

# Create and connect to the database
def get_db_connection():
    if not os.path.exists(DB_FILE):
        print(f"Database '{DB_FILE}' does not exist. Creating...")
        conn = sqlite3.connect(DB_FILE)
        conn.close()
        print(f"Database '{DB_FILE}' created successfully!")
    conn = sqlite3.connect(DB_FILE, detect_types=sqlite3.PARSE_DECLTYPES)
    return conn

# Ensure the table exists
def ensure_table_exists(conn):
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS conversations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        role TEXT NOT NULL,
        content TEXT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)
    conn.commit()

# Log a conversation
def log_conversation(conn, role: str, content: str):
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO conversations (role, content, timestamp)
    VALUES (?, ?, ?)
    """, (role, content, datetime.now(timezone.utc)))
    conn.commit()

# Retrieve conversation history
def get_conversation_history(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT role, content FROM conversations ORDER BY id")
    return [{"role": row[0], "content": row[1]} for row in cursor.fetchall()]