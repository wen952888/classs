import logging
from quart import Quart
from bot_commands import setup_bot_commands

# 创建 Quart 应用
app = Quart(__name__)

# 配置日志
logging.basicConfig(level=logging.INFO)

# 设置机器人命令
setup_bot_commands()

@app.before_serving
async def start_services():
    # 在启动服务前运行任何初始化逻辑
    logging.info("服务已启动")

@app.after_serving
async def stop_services():
    # 在服务停止后运行清理逻辑
    logging.info("服务已停止")

if __name__ == "__main__":
    app.run()