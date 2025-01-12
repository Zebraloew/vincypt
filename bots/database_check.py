import sqlite3

DB_FILE = "/opt/venvs/gpt_env/conversation_history.db"

def ensure_table_exists():
    """Ensure the necessary tables exist in the SQLite database."""
    conn = sqlite3.connect(DB_FILE)  # Create a new connection for this check
    cursor = conn.cursor()

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