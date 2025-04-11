FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 复制项目文件到容器
COPY . .

# 安装 Python 依赖
RUN pip install --no-cache-dir -r requirements.txt

# 启动服务
CMD ["python", "bot.py"]