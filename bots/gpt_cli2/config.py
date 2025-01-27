# *Configuration file* 
# Set the API key and 
# database file path here

import os
from dotenv import load_dotenv

load_dotenv()

# Database file
# This file will be created if it doesn't exist
DB_FILE = os.path.expanduser("~/.gpt_shell/hero_conversation_history.db")

# API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("Error: OPENAI_API_KEY environment variable not set.")