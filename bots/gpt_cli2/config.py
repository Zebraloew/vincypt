import os
from dotenv import load_dotenv

load_dotenv()

# Paths
DB_FILE = os.path.expanduser("~/.gpt_shell/conversation_history.db")

# API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("Error: OPENAI_API_KEY environment variable not set.")