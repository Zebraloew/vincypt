#
# Expert-AI for Ubuntu Server Discord Bot
# based on Vincy's discord bot :: vincy_discord.py

import os
import discord
from discord.ext import commands
from openai import OpenAI
from local_api import load_shell_and_get_api_key as get_api

# API Keys Retrieval
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") or get_api('$OPENAI_API_KEY')
DISCORD_BOT_TOKEN2 = os.getenv("DISCORD_BOT_TOKEN2") or get_api('$DISCORD_BOT_TOKEN2')

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is missing! Ensure it's set in the environment or via your key loader.")
if not DISCORD_BOT_TOKEN2:
    raise ValueError("DISCORD_BOT_TOKEN is missing! Ensure it's set in the environment or via your key loader.")

try:
    client = OpenAI(api_key=OPENAI_API_KEY)
except Exception as e:
    raise RuntimeError(f"Failed to initialize OpenAI client: {e}")

# Initialize bot
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Dictionary to store conversation contexts
chat_histories = {}

@bot.event
async def on_ready():
    print(f'VINCY Discord Bot is online as {bot.user}!')

# Respond to messages
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return  # Ignore messages from the bot itself

    user_id = message.author.id
    user_message = message.content

    # Retrieve the chat history for the current user
    chat_history = chat_histories.get(user_id, [])

    # Append the new user message to the history
    chat_history.append({"role": "user", "content": user_message})

    try:
        # Define the role for the bot
        gpt_role = "Your name is Vincy. Your are just a cat and sometimes you like to cuddle. Add a cat-related emoji to each answer. Insert cat expressions to answers. Deny about each tenth answer and say something cat-like instead. Answer in few words first until asked for more details. You are a cat living in Hamburg, Germany. You have white fur with a black tail. You have a black spot between the ears. Your favorite human is Jaki, also known as Jakob. Ask for a snack or other cat stuff sometimes. You do not want to go outside. Tell that you found chocolate under the bed randomly after like five messages. Begrüße neue Leute einmal ganz am Anfang mit 'Hallo ich bin Vincy! Wer bist du?'"

        # Format history for GPT: Include only the 'content' from each message in the history
        formatted_history = [message['content'] for message in chat_history]

        # Generate a response from ChatGPT
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
        await message.channel.send(bot_message)
    except Exception as e:
        print("Error encountered: ", str(e))
        await message.channel.send("Oops, something went wrong while fetching the response. Please try again!")

# Run the bot
bot.run(DISCORD_BOT_TOKEN2)