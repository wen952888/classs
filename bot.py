import os
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from handlers import start_handler, help_handler, echo_handler

def main():
    # 从环境变量中获取 Telegram Bot Token
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise ValueError("Error: BOT_TOKEN is not set in environment variables.")

    # 初始化应用程序
    application = ApplicationBuilder().token(token).build()

    # 添加命令处理器
    application.add_handler(CommandHandler("start", start_handler))
    application.add_handler(CommandHandler("help", help_handler))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo_handler))

    # 启动 Bot
    application.run_polling()

if __name__ == "__main__":
    main()