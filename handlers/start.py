from telegram import Update
from telegram.ext import ContextTypes

# 处理 /start 命令
async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "欢迎使用 Telegram Bot！\n"
        "输入 /menu 查看功能菜单。\n"
        "如需帮助，输入 /help。"
    )