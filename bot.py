import os
import logging
import asyncio
from flask import Flask
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes
from telegram import Update
from subscription_parser import clash, ssr, v2ray
from utils.health_check import check_node_health
from utils.language_support import translate
from utils.qr_generator import generate_qr_code

# 配置日志
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# 创建 Flask 应用实例
app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Telegram Bot is running!"


# Telegram Bot 命令处理函数
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
        # 根据订阅格式解析
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


# 启动 Telegram Bot
async def run_telegram_bot():
    token = os.getenv("TELEGRAM_TOKEN")
    application = ApplicationBuilder().token(token).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(None, handle_message))

    await application.run_polling()


# 主函数：同时运行 Flask 和 Telegram Bot
def main():
    loop = asyncio.get_event_loop()

    # 启动 Telegram Bot 任务
    loop.create_task(run_telegram_bot())

    # 启动 Flask 应用
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, use_reloader=False)

if __name__ == "__main__":
    main()