from openai import OpenAI
import sqlite3
import os
from datetime import datetime, timezone
from database_check import ensure_table_exists

# Load OpenAI API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Adapter for Python datetime to SQLite
def adapt_datetime_iso(dt: datetime) -> str:
    return dt.isoformat()

# Converter for SQLite datetime string to Python datetime
def convert_datetime_iso(s: bytes) -> datetime:
    return datetime.fromisoformat(s.decode("utf-8"))

# Register adapter and converter
sqlite3.register_adapter(datetime, adapt_datetime_iso)
sqlite3.register_converter("DATETIME", convert_datetime_iso)

# Connect to the SQLite database
DB_FILE = "conversation_history.db"
conn = sqlite3.connect(
    DB_FILE,
    detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES
)
cursor = conn.cursor()

# Ensure the conversations table exists
ensure_table_exists()

# Function to log conversations
def log_conversation(user: str, role: str, content: str):
    cursor.execute("""
    INSERT INTO conversations (user, role, content, timestamp)
    VALUES (?, ?, ?, ?)
    """, (user, role, content, datetime.now(timezone.utc)))
    conn.commit()

# Function to retrieve conversation history
def get_conversation_history(user: str):
    cursor.execute("SELECT role, content FROM conversations WHERE user = ? ORDER BY id", (user,))
    return cursor.fetchall()

# GPT interaction function
def chat_with_gpt(user: str, prompt: str):
    # Retrieve history
    history = get_conversation_history(user)

    # Build the GPT messages payload
    messages = [{"role": role, "content": content} for role, content in history]
    messages.append({"role": "user", "content": prompt})

    # Call OpenAI API using the provided format
    client = OpenAI(api_key=OPENAI_API_KEY)
    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages
    )

    # Extract bot's reply
    bot_reply = response.choices[0].message.content

    # Log the conversation
    log_conversation(user, "user", prompt)
    log_conversation(user, "assistant", bot_reply)

    return bot_reply

# Main function for shell interface
def main():
    print("Welcome to the GPT Shell Interface! Type 'exit' to quit.")
    user = input("Enter your username: ").strip()

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        reply = chat_with_gpt(user, user_input)
        print(f"GPT: {reply}")

    # Close the database connection
    conn.close()

if __name__ == "__main__":
    main()