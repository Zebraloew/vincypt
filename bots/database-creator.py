# this initializes a database for storing conversations
# just needed once

import sqlite3

# Connect to the database (creates it if it doesn't exist)
conn = sqlite3.connect("conversation_history.db")
cursor = conn.cursor()

# Create a table for storing the conversation
cursor.execute("""
CREATE TABLE IF NOT EXISTS conversations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user TEXT NOT NULL,
    role TEXT NOT NULL,
    content TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")

# Commit changes and close the connection
conn.commit()
conn.close()

print("Database and table created successfully!")