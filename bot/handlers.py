from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

# /start 命令的处理函数
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Hello! I am your bot. Use /help to see commands.')

# /help 命令的处理函数
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Available commands:\n/start - Start the bot\n/help - Get help')

# 注册所有命令
def get_handlers():
    return [
        CommandHandler("start", start),
        CommandHandler("help", help_command),
    ]