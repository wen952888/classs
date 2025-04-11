from telegram import Update
from telegram.ext import ContextTypes

async def echo_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"您发送了: {update.message.text}")