import os
from flask import Flask, request
from telegram import Update
from telegram.ext import ApplicationBuilder

from .handlers import get_handlers

# Flask 应用实例
app = Flask(__name__)

# 从环境变量中加载 Token 和 Webhook URL
TOKEN = os.getenv("TELEGRAM_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")  # 例如 https://your-app.onrender.com/<TOKEN>

# Telegram Bot 应用实例
application = ApplicationBuilder().token(TOKEN).build()

# 注册命令处理程序
for handler in get_handlers():
    application.add_handler(handler)

# 根路径处理
@app.route("/", methods=["GET"])
def index():
    return "This is a Telegram bot webhook!", 200

# Webhook 路由处理
@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    json_data = request.get_json()
    update = Update.de_json(json_data, application.bot)
    application.process_update(update)
    return "OK", 200

# Webhook 初始化函数
def set_webhook():
    application.bot.set_webhook(WEBHOOK_URL)