import os
import logging
import asyncio
from flask import Flask
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
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
    """Flask 根路由，用于检查服务状态"""
    return "Telegram Bot is running!"


async def start(update: Update, context):
    """处理 /start 命令"""
    language = update.message.from_user.language_code or "en"
    welcome_message = translate(
        (
            "欢迎使用订阅转换机器人！支持以下功能：\n"
            "- Clash、SSR、V2Ray 订阅解析\n"
            "- 节点健康检查\n"
            "- 多语言支持\n"
            "- 生成订阅二维码\n\n"
            "发送您的订阅链接以开始。"
        ),
        language,
    )
    await update.message.reply_text(welcome_message)


async def handle_message(update: Update, context):
    """处理用户发送的消息"""
    user_message = update.message.text.strip()
    language = update.message.from_user.language_code or "en"

    # 检查链接是否有效
    if not user_message.startswith("http"):
        invalid_message = translate("请输入有效的订阅链接（以 http/https 开头）。", language)
        await update.message.reply_text(invalid_message)
        return

    try:
        # 根据订阅格式解析链接
        if "clash" in user_message.lower():
            result = clash.parse_clash_subscription(user_message)
        elif "ssr" in user_message.lower():
            result = ssr.parse_ssr_subscription(user_message)
        elif "v2ray" in user_message.lower():
            result = v2ray.parse_v2ray_subscription(user_message)
        else:
            result = translate("无法识别的订阅格式，请提供 Clash、SSR 或 V2Ray 格式的链接。", language)

        # 回复解析结果
        await update.message.reply_text(result)

        # 节点健康检查
        if result.startswith("解析成功"):
            health_report = check_node_health(result)
            health_report_message = translate("节点健康检查报告：", language) + health_report
            await update.message.reply_text(health_report_message)

        # 生成二维码并发送
        qr_path = generate_qr_code(user_message)
        await update.message.reply_photo(photo=open(qr_path, "rb"))
        os.remove(qr_path)  # 删除临时文件

    except Exception as e:
        logging.error(f"Error processing subscription: {e}")
        error_message = translate("处理订阅链接时出错，请稍后再试。", language)
        await update.message.reply_text(error_message)


async def run_telegram_bot():
    """启动 Telegram Bot"""
    token = os.getenv("TELEGRAM_TOKEN")
    if not token:
        raise ValueError("TELEGRAM_TOKEN 环境变量未设置，请设置后重试。")

    application = ApplicationBuilder().token(token).build()

    # 添加命令和消息处理器
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # 启动轮询模式
    await application.run_polling()


def main():
    """主函数，运行 Flask 和 Telegram Bot"""
    loop = asyncio.get_event_loop()

    # 启动 Telegram Bot
    loop.create_task(run_telegram_bot())

    # 启动 Flask 应用
    port = int(os.getenv("PORT", 5000))  # 使用环境变量 PORT
    app.run(host="0.0.0.0", port=port, use_reloader=False)


if __name__ == "__main__":
    main()