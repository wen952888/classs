import os
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from handlers import (
    start_handler,
    menu_handler,
    convert_subscription_handler,
    generate_qr_code_handler,
    search_free_nodes_handler,
)

def main():
    token = os.getenv("BOT_TOKEN")
    webhook_url = os.getenv("WEBHOOK_URL")

    if not token:
        raise ValueError("Error: BOT_TOKEN is not set in environment variables.")
    if not webhook_url:
        raise ValueError("Error: WEBHOOK_URL is not set in environment variables.")

    application = ApplicationBuilder().token(token).build()

    # 添加命令处理器
    application.add_handler(CommandHandler("start", start_handler))
    application.add_handler(CommandHandler("menu", menu_handler))
    application.add_handler(MessageHandler(filters.TEXT & filters.Regex("^生成二维码$"), generate_qr_code_handler))
    application.add_handler(MessageHandler(filters.TEXT & filters.Regex("^转换订阅$"), convert_subscription_handler))
    application.add_handler(MessageHandler(filters.TEXT & filters.Regex("^搜索免费节点$"), search_free_nodes_handler))

    # 使用 Webhook 运行
    application.run_webhook(
        listen="0.0.0.0",
        port=int(os.getenv("PORT", 8443)),
        url_path=token,
        webhook_url=f"{webhook_url}/{token}",
    )

if __name__ == "__main__":
    main()