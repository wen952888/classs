import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes

# 日志配置
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# 启动命令处理函数
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("欢迎使用订阅转换机器人！\n发送您的订阅链接以开始。")

# 处理消息函数（订阅转换逻辑）
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text

    # 模拟订阅转换逻辑
    if "http" in user_message:
        converted_message = f"转换后的订阅内容：\n{user_message.replace('http', 'https')}"
    else:
        converted_message = "请输入有效的订阅链接。"

    await update.message.reply_text(converted_message)

# 主程序入口
if __name__ == "__main__":
    # 从环境变量中获取 Telegram Bot Token
    token = os.getenv("TELEGRAM_TOKEN")

    # 创建 Telegram Bot 应用实例
    app = ApplicationBuilder().token(token).build()

    # 添加命令和消息处理程序
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(None, handle_message))

    # 开始运行
    app.run_polling()