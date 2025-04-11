import os
import logging
import asyncio
from flask import Flask
from threading import Thread
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes
from telegram import Update
from subscription_parser import clash, ssr, v2ray
from utils.health_check import check_node_health
from utils.language_support import translate
from utils.qr_generator import generate_qr_code

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Flask app for Render's port binding
app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Telegram Bot is running!"


# Define Telegram Bot command handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    language = update.message.from_user.language_code
    await update.message.reply_text(
        translate("欢迎使用订阅转换机器人！支持以下功能：\n"
                  "- Clash、SSR、V2Ray 订阅解析\n"
                  "- 节点健康检查\n"
                  "- 多语言支持\n"
                  "- 生成订阅二维码\n\n"
                  "发送您的订阅链接以开始。", language)
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text.strip()
    language = update.message.from_user.language_code

    if not user_message.startswith("http"):
        await update.message.reply_text(translate("请输入有效的订阅链接（以 http/https 开头）。", language))
        return

    try:
        # Parse subscription based on format
        if "clash" in user_message.lower():
            result = clash.parse_clash_subscription(user_message)
        elif "ssr" in user_message.lower():
            result = ssr.parse_ssr_subscription(user_message)
        elif "v2ray" in user_message.lower():
            result = v2ray.parse_v2ray_subscription(user_message)
        else:
            result = translate("无法识别的订阅格式，请提供 Clash、SSR 或 V2Ray 格式的链接。", language)

        await update.message.reply_text(result)

        # Add health check functionality
        if result.startswith("解析成功"):
            health_report = check_node_health(result)
            await update.message.reply_text(translate("节点健康检查报告：", language) + health_report)

        # Generate and send QR code
        qr_path = generate_qr_code(user_message)
        await update.message.reply_photo(photo=open(qr_path, 'rb'))
        os.remove(qr_path)  # Clean up temporary QR code file

    except Exception as e:
        logging.error(f"Error processing subscription: {e}")
        await update.message.reply_text(translate("处理订阅链接时出错，请稍后再试。", language))


# Run Telegram Bot using asyncio
async def run_telegram_bot():
    token = os.getenv("TELEGRAM_TOKEN")
    application = ApplicationBuilder().token(token).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(None, handle_message))

    await application.run_polling()


# Main entry point: Run Flask and Telegram bot concurrently
if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))

    # Run Flask in a separate thread
    flask_thread = Thread(target=lambda: app.run(host="0.0.0.0", port=port))
    flask_thread.start()

    # Run Telegram Bot in the main event loop
    asyncio.run(run_telegram_bot())