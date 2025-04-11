from telegram import Update
from telegram.ext import ContextTypes
from utils.rss_feed_reader import fetch_rss_feed

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not context.args:
        await update.message.reply_text("Please provide an RSS feed URL.")
        return

    rss_url = " ".join(context.args)
    try:
        feed_items = fetch_rss_feed(rss_url)
        if not feed_items:
            await update.message.reply_text("No items found in the RSS feed.")
            return

        response = "\n\n".join([f"• {item['title']}\n{item['link']}" for item in feed_items[:5]])
        await update.message.reply_text(response)
    except Exception as e:
        await update.message.reply_text(f"Error fetching RSS feed: {e}")