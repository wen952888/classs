FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 复制项目文件到容器中
COPY . .

# 安装 Python 依赖
RUN pip install --no-cache-dir -r requirements.txt

# 暴露端口
EXPOSE 5000

# 使用 Gunicorn 运行 Flask 应用
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "bot:app"]