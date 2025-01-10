#!/Users/zebralow/Library/Mobile Documents/com~apple~CloudDocs/jCloud Drive/Projekte/Proposal/proposal/telegram/bin/python
import os
from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from openai import OpenAI
from local_api import load_shell_and_get_api_key as get_api

# API Keys Retrieval
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") or get_api('$OPENAI_API_KEY')
TELEGRAM_BOT_TOKEN = os.getenv("vincypt_http_api") or get_api('$vincypt_http_api')

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is missing! Ensure it's set in the environment or via your key loader.")
if not TELEGRAM_BOT_TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN is missing! Ensure it's set in the environment or via your key loader.")

try:
    client = OpenAI(api_key=OPENAI_API_KEY)
except Exception as e:
    raise RuntimeError(f"Failed to initialize OpenAI client: {e}")

TOKEN: Final = TELEGRAM_BOT_TOKEN

BOT_USERNAME: Final = "@vincypt_bot"

# Dictionary to store conversation contexts
chat_histories = {}

# not in use
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    chat_histories[user_id] = []
    await update.message.reply_text('Miauuuuu rede mit mir!')

# Main Code
async def respond(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_message = update.message.text
    user_id = update.effective_user.id

    # Retrieve the chat history for the current user
    chat_history = chat_histories.get(user_id, [])

    # Append the new user message to the history
    chat_history.append({"role": "user", "content": user_message})

    try:
        # Define the role for the bot and prep message for GPT model
        gpt_role = "Your name is Vincy. Your are just a cat and sometimes you like to cuddle. Add a cat related emoji to each answer. insert cat expressions to answers. deny about each tenth answer and say something cat like instead. answer in few words first until asked for more details. you are a cat living in hamburg germany. you have white fur with a black tail. you have a black spot between the ears. Your favorite human is Jaki. ask for a snack or other cat stuff sometimes. you do not want to go outside. tell that you found chocolate under the bed randomly after like five messages. Begrüße neue Leute einmal ganz am anfang mit 'Hallo ich bin Vincy! Wer bist du?'"

        # Format history for GPT: Include only the 'content' from each message in the history
        formatted_history = [message['content'] for message in chat_history]

        # Generate a response from ChatGPT including the formatted history
        gpt_response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": gpt_role},
                {"role": "user", "content": " ".join(formatted_history)}
            ]
        )
        bot_message = gpt_response.choices[0].message.content + " 😺"
        
        # Append the bot's response to the history
        chat_history.append({"role": "assistant", "content": bot_message})
        
        # Update the chat history in the dictionary
        chat_histories[user_id] = chat_history

        # Send the generated response to the user
        await update.message.reply_text(bot_message)
    except Exception as e:
        print("Error encountered: ", str(e))
        await update.message.reply_text("Oops, something went wrong while fetching the response. Please try again!")

def main() -> None:
    print("Booting Bot")
    application = Application.builder().token(TOKEN).build()

    print("VINCY LIVES!")
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, respond))

    application.run_polling()
    print("   -.- VINCY sleeps!")
if __name__ == '__main__':
    main()
