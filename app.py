import logging
from quart import Quart
from bot_commands import setup_bot_commands
from sftp_manager import setup_sftp_routes

# 创建 Quart 应用
app = Quart(__name__)

# 配置日志
logging.basicConfig(level=logging.INFO)

# 设置 SFTP 路由
setup_sftp_routes(app)

# 设置机器人命令
setup_bot_commands()

@app.before_serving
async def start_services():
    logging.info("服务已启动")

@app.after_serving
async def stop_services():
    logging.info("服务已停止")

if __name__ == "__main__":
    app.run()