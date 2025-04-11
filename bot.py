from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from handlers import start_handler, help_handler, echo_handler

def main():
    # 初始化应用程序
    application = ApplicationBuilder().token("YOUR_BOT_TOKEN").build()

    # 添加命令处理器
    application.add_handler(CommandHandler("start", start_handler))
    application.add_handler(CommandHandler("help", help_handler))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo_handler))

    # 启动 Bot
    application.run_polling()

if __name__ == "__main__":
    main()