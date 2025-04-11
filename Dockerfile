# 使用 Python 3.9 的官方精简版镜像作为基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 复制项目文件到容器中
COPY . .

# 安装依赖项
RUN pip install --no-cache-dir -r requirements.txt

# 暴露端口
EXPOSE 5000

# 使用 Gunicorn 运行 Flask 应用程序
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "bot:app"]