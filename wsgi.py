from bot import app, start_telegram_bot

# 启动 Telegram Bot
start_telegram_bot()

# WSGI 入口
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))