from telegram import Update
from telegram.ext import ContextTypes

async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("欢迎使用 Telegram Bot！")