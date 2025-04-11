from telegram import Update
from telegram.ext import ContextTypes

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    help_text = """
    Available Commands:
    /help - Show this help message
    /shell <command> - Execute a remote shell command
    /convert_subscription <url> - Convert subscription formats
    /generate_qr <text> - Generate a QR code
    /translate <text> - Translate text to another language
    /convert_currency <amount> <from> <to> - Convert currency
    /joke - Get a random joke
    /generate_image <text> - Generate an image or meme
    /set_permission <user> <level> - Set user permissions
    /rss <url> - Subscribe to an RSS feed
    /file <upload|download> - Manage files
    /schedule <task> - Schedule a task
    """
    await update.message.reply_text(help_text)