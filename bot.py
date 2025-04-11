import os
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from handlers import (
    start_handler,
    menu_handler,
    echo_handler,
    convert_subscription_handler,
    generate_qr_code_handler,
    search_free_nodes_handler,
)

def main():
    # 从环境变量中获取 Telegram Bot Token
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise ValueError("Error: BOT_TOKEN is not set in environment variables.")

    # 初始化应用程序
    application = ApplicationBuilder().token(token).build()

    # 添加命令处理器
    application.add_handler(CommandHandler("start", start_handler))
    application.add_handler(CommandHandler("menu", menu_handler))
    application.add_handler(CommandHandler("help", start_handler))  # 帮助与 /start 共享逻辑
    application.add_handler(MessageHandler(filters.TEXT & filters.Regex("^生成二维码$"), generate_qr_code_handler))
    application.add_handler(MessageHandler(filters.TEXT & filters.Regex("^转换订阅$"), convert_subscription_handler))
    application.add_handler(MessageHandler(filters.TEXT & filters.Regex("^搜索免费节点$"), search_free_nodes_handler))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo_handler))

    # 启动 Bot
    application.run_polling()

if __name__ == "__main__":
    main()