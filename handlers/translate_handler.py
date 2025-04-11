from telegram import Update
from telegram.ext import ContextTypes
from utils.translate_api import translate_text

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handle the /translate command to translate text.
    """
    if not context.args:
        await update.message.reply_text("Please provide text to translate.")
        return

    try:
        text_to_translate = " ".join(context.args)
        translated_text = translate_text(text_to_translate)
        await update.message.reply_text(f"Translated Text:\n{translated_text}")
    except Exception as e:
        await update.message.reply_text(f"Error during translation: {e}")