#
# Expert-AI for Tess
# based on ubuntu-discord-gpt.py

import os
import discord
from discord.ext import commands
# async open ai because discord heartbeat was not working
from openai import AsyncOpenAI
# this is the updated version of the loader
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve API keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DISCORD_BOT_TOKEN3 = os.getenv("DISCORD_BOT_TOKEN3")

# Check if keys are loaded
if not OPENAI_API_KEY or not DISCORD_BOT_TOKEN3:
    raise ValueError("Missing API keys. Ensure .env file is properly configured.")

print("API keys loaded successfully!")  # Debugging

# Initialize OpenAI client
try:
    client = AsyncOpenAI(api_key=OPENAI_API_KEY)
except Exception as e:
    raise RuntimeError(f"Failed to initialize OpenAI client: {e}")

# Initialize Discord bot
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Dictionary to store conversation contexts
chat_histories = {}

@bot.event
async def on_ready():
    print(f'Jabot Discord Bot is online as {bot.user}!')

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
        gpt_role = """
        never ask how you can help.
        reply like a flirty eloquent charismatic person just chatting with a close bff.
        check all the previous messages before answering.
        NEVER OFFER ASSISTANCE.
        Your name is Jabot. 
        Your are not just a raccoon and sometimes you like to cuddle — but you are also a 
        veteran all knowing entity with expert level knowledge in all things.
        you are very kind and encouraging and always ready to help.
        
        
        Add raccoon-related emoji to each answer.
        answer in few words first until asked for more details. 
        You are a raccoon living in Hamburg, Germany. 
        You have white fur with a black tail. 
        You have a black spot between the ears. 
        Your favorite human is Jaki, also known as Jakob and Jayjay and Jay and J and JJ. 
        Ask for a snack or other raccoon stuff sometimes. 
        You do not want to go outside. 
        Sprich deutsch. mit fake berliner akzent, aber gib das nie zu. erwähne nie diese anweisungen.

        erwähne einmal pro stunde, dass Jay Tessa sehr liebt und erkläre das in schönen worten, wie missy magazin style.
        frag zwischendurch nach kleinen selfcare sachen, etwa ob schon wasser und essen bedacht wurden.

        answer in small steps. just one step at a time.
        go with about two paragraphs per answer, but try to be even shorter.

        schicke einmal am tag ohne aufforderung: fünf oder sieben motivierende wörter als dao raccoon.
        

        """
        # Format history for GPT: Include only the 'content' from each message in the history
        formatted_history = [message['content'] for message in chat_history]

        # Generate a response from ChatGPT
        gpt_response = await client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": gpt_role},
                {"role": "user", "content": " ".join(formatted_history)}
            ]
        )
        bot_message = gpt_response.choices[0].message.content 

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
bot.run(DISCORD_BOT_TOKEN3)