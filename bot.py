import os
from telegram.ext import ApplicationBuilder, CommandHandler
from handlers import (
    qr_code_handler,
    subscription_handler,
    currency_handler,
    rss_handler,
    permission_handler,
)

# 从环境变量中加载 Telegram Bot Token
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not TOKEN:
    raise ValueError("环境变量 TELEGRAM_BOT_TOKEN 未设置！请设置有效的 Telegram Bot Token。")

# 初始化 Telegram Bot 应用
app = ApplicationBuilder().token(TOKEN).build()

# 添加命令处理程序
app.add_handler(CommandHandler("generate_qr", qr_code_handler.handle))  # 生成二维码
app.add_handler(CommandHandler("convert_subscription", subscription_handler.handle))  # 转换订阅链接
app.add_handler(CommandHandler("convert_currency", currency_handler.handle))  # 货币转换
app.add_handler(CommandHandler("rss", rss_handler.handle))  # 获取 RSS 源
app.add_handler(CommandHandler("set_permission", permission_handler.handle))  # 设置权限

if __name__ == "__main__":
    print("Bot is running...")

    # 使用轮询（Polling）方式运行 Bot
    try:
        app.run_polling()
    except Exception as e:
        print(f"Bot 运行时遇到错误：{e}")