from telegram.ext import ApplicationBuilder, CommandHandler
from handlers import (
    qr_code_handler,
    subscription_handler,
    currency_handler,
    rss_handler,
    permission_handler,
)

# Initialize the bot
TOKEN = "7661820240:AAHJp_qqg9KBcswYtBIwnlTmHIPj5cH22zk"
app = ApplicationBuilder().token(TOKEN).build()

# Add command handlers
app.add_handler(CommandHandler("generate_qr", qr_code_handler.handle))
app.add_handler(CommandHandler("convert_subscription", subscription_handler.handle))
app.add_handler(CommandHandler("convert_currency", currency_handler.handle))
app.add_handler(CommandHandler("rss", rss_handler.handle))
app.add_handler(CommandHandler("set_permission", permission_handler.handle))

if __name__ == "__main__":
    print("Bot is running...")
    app.run_polling()