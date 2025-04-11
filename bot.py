from telegram.ext import ApplicationBuilder, CommandHandler
from handlers import (
    qr_code_handler,
    subscription_handler,
    currency_handler,
    rss_handler,
    permission_handler,
)

# Telegram Bot Token (请将 "your_telegram_bot_token_here" 替换为从 @BotFather 获取的实际 Bot Token)
TOKEN = "7661820240:AAHJp_qqg9KBcswYtBIwnlTmHIPj5cH22zk"

# 初始化应用程序
app = ApplicationBuilder().token(TOKEN).build()

# 添加命令处理程序
app.add_handler(CommandHandler("generate_qr", qr_code_handler.handle))  # 生成二维码
app.add_handler(CommandHandler("convert_subscription", subscription_handler.handle))  # 转换订阅链接
app.add_handler(CommandHandler("convert_currency", currency_handler.handle))  # 货币转换
app.add_handler(CommandHandler("rss", rss_handler.handle))  # 获取 RSS 源
app.add_handler(CommandHandler("set_permission", permission_handler.handle))  # 设置权限

if __name__ == "__main__":
    print("Bot is running...")
    # 启动轮询以接收消息
    app.run_polling()
