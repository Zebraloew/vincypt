# telegram bot
# this is just testing the telegram api
# without gpt
"""
HTTP API:
7032664253:AAEhL-MHWPr1B_htHHCUNRCML_ckOLlIhB0
"""

from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final        = "7032664253:AAEhL-MHWPr1B_htHHCUNRCML_ckOLlIhB0"
BOT_USERNAME: Final = "@bananar_bot"

# commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Oh hi! Pleased to meet you!")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I am helping!")

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Oh hi! I am custom!")

# responses
def handle_response(text: str) -> str:
    processed: str = text.lower()
    
    if "hello" in processed:
        return "Yo hi!"
    
    return "Hm?"
 
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "text"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:   
            return
    else:
        response: str = handle_response(text)

    print('Bot', response)
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    print('Starting')
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    #Error
    app.add_error_handler(error)

    # Update constantly
    print('Polling')
    app.run_polling(poll_interval=3)