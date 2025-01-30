import openai
from config import OPENAI_API_KEY
from db_utils import get_conversation_history, log_conversation
from promptgen import create_prompt_from_yaml

openai.api_key = OPENAI_API_KEY

# Chat with GPT
def chat_with_gpt(conn, prompt: str):
    # Create a prompt using the promptgen function
    prime_prompt = create_prompt_from_yaml()

    # Retrieve conversation history
    history = get_conversation_history(conn)
    history.append({"role": "user", "content": prompt})

    # Add the prime prompt to the beginning of the conversation
    history.insert(0, {"role": "assistant", "content": prime_prompt})

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