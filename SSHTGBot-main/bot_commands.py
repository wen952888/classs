from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from translations import get_translation

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    welcome_message = get_translation("welcome_message")
    await update.message.reply_text(welcome_message)

async def execute_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    command = " ".join(context.args)
    response = f"执行的命令是: {command}"
    await update.message.reply_text(response)

def setup_bot_commands():
    application = ApplicationBuilder().token("YOUR_TELEGRAM_BOT_TOKEN").build()

    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("exec", execute_command))

    application.run_polling()