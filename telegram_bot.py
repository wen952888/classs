from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import os

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Welcome to SSH Master Bot! Use /help for commands.")

def help_command(update: Update, context: CallbackContext):
    update.message.reply_text("/start - Start Bot\n/help - Show Commands")

def ssh_command(update: Update, context: CallbackContext):
    update.message.reply_text("SSH Command feature coming soon!")

def main():
    updater = Updater(TELEGRAM_TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("ssh", ssh_command))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()