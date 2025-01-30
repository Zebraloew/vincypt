import openai
from config import OPENAI_API_KEY
from db_utils import get_conversation_history, log_conversation

openai.api_key = OPENAI_API_KEY

# Chat with GPT
def chat_with_gpt(conn, prompt: str):
    # Retrieve conversation history
    history = get_conversation_history(conn)
    history.append({"role": "user", "content": prompt})


    # Call GPT API
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=history
    )
    bot_reply = response.choices[0].message.content

    # Log conversation
    log_conversation(conn, "user", prompt)
    log_conversation(conn, "assistant", bot_reply)

    return bot_reply