import sqlite3
import os

DB_FILE = os.path.expanduser("~/venvs/gpt_shell/conversation_history.db")

def ensure_table_exists():
    """Ensure the necessary tables exist in the SQLite database."""
    try:
     conn = sqlite3.connect(DB_FILE, detect_types=sqlite3.PARSE_DECLTYPES)
     cursor = conn.cursor()
    except sqlite3.Error as e:
     print(f"Error connecting to SQLite database: {e}")
     exit(1)
    
    # Create `users` table if it doesn't exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL
    )
    """)

    # Create `conversations` table if it doesn't exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS conversations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        role TEXT NOT NULL,
        content TEXT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    ensure_table_exists()