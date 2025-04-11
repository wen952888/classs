import os
import logging
from flask import Flask
from threading import Thread
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes
from subscription_parser import clash, ssr, v2ray
from utils.health_check import check_node_health
from utils.language_support import translate
from utils.qr_generator import generate_qr_code

# 设置日志
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Flask app for Render port binding
app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Telegram Bot is running!"


# Telegram Bot Functions
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

    # 检查是否为有效链接
    if not user_message.startswith("http"):
        await update.message.reply_text(translate("请输入有效的订阅链接（以 http/https 开头）。", language))
        return

    # 根据订阅格式进行处理
    try:
        if "clash" in user_message.lower():
            result = clash.parse_clash_subscription(user_message)
        elif "ssr" in user_message.lower():
            result = ssr.parse_ssr_subscription(user_message)
        elif "v2ray" in user_message.lower():
            result = v2ray.parse_v2ray_subscription(user_message)
        else:
            result = translate("无法识别的订阅格式，请提供 Clash、SSR 或 V2Ray 格式的链接。", language)

        await update.message.reply_text(result)

        # 添加健康检查功能
        if result.startswith("解析成功"):
            health_report = check_node_health(result)
            await update.message.reply_text(translate("节点健康检查报告：", language) + health_report)

        # 生成二维码并发送
        qr_path = generate_qr_code(user_message)
        await update.message.reply_photo(photo=open(qr_path, 'rb'))
        os.remove(qr_path)  # 删除临时二维码文件

    except Exception as e:
        logging.error(f"Error processing subscription: {e}")
        await update.message.reply_text(translate("处理订阅链接时出错，请稍后再试。", language))

def run_telegram_bot():
    token = os.getenv("TELEGRAM_TOKEN")

    # 创建 Telegram Bot 实例
    telegram_app = ApplicationBuilder().token(token).build()

    # 添加命令和消息处理程序
    telegram_app.add_handler(CommandHandler("start", start))
    telegram_app.add_handler(MessageHandler(None, handle_message))

    # Explicitly create and set an asyncio event loop for this thread
    asyncio.set_event_loop(asyncio.new_event_loop())
    telegram_app.run_polling()

# Run Telegram Bot in a separate thread
Thread(target=run_telegram_bot).start()

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)