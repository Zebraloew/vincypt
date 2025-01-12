#!/opt/venvs/gpt_env/bin/python

# GPT CLI with a database as memory

import openai
import sqlite3
import os
from argparse import ArgumentParser
from datetime import datetime, timezone

def adapt_datetime_iso(val):
    """Adapt datetime.datetime to ISO 8601 string."""
    return val.isoformat()

def convert_datetime(val):
    """Convert ISO 8601 string to datetime.datetime object."""
    return datetime.fromisoformat(val.decode())

# Register the adapter
sqlite3.register_adapter(datetime, adapt_datetime_iso)

# Register the converter
sqlite3.register_converter('timestamp', convert_datetime)

# Database file
DB_FILE = "/opt/venvs/gpt_env/conversation_history.db"

# Load OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Connect to the SQLite database
conn = sqlite3.connect(DB_FILE, detect_types=sqlite3.PARSE_DECLTYPES)
cursor = conn.cursor()

# Ensure the table exists
def ensure_table_exists():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS conversations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        role TEXT NOT NULL,
        content TEXT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)
    conn.commit()

ensure_table_exists()

# Log a conversation message
def log_conversation(role: str, content: str):
    cursor.execute("""
    INSERT INTO conversations (role, content, timestamp)
    VALUES (?, ?, ?)
    """, (role, content, datetime.now(timezone.utc)))

    conn.commit()

# Retrieve all conversation history
def get_conversation_history():
    cursor.execute("SELECT role, content FROM conversations ORDER BY id")
    return [{"role": row[0], "content": row[1]} for row in cursor.fetchall()]

# Chat with GPT
def chat_with_gpt(prompt: str):
    # Retrieve conversation history
    history = get_conversation_history()
    history.append({"role": "user", "content": prompt})

    # Call GPT API
    response = openai.chat.completions.create(
        model="gpt-4",
        messages=history
    )
    bot_reply = response.choices[0].message.content

    # Log conversation
    log_conversation("user", prompt)
    log_conversation("assistant", bot_reply)

    return bot_reply

# Main CLI
def main():
    parser = ArgumentParser(description="GPT Command Line Interface")
    parser.add_argument("input", nargs="+", help="Input message for GPT")
    args = parser.parse_args()

    input_text = " ".join(args.input)

    # Chat with GPT
    reply = chat_with_gpt(input_text)
    print(reply)

if __name__ == "__main__":
    main()