# 使用官方 Golang 镜像
FROM golang:1.20 as builder

# 设置工作目录
WORKDIR /app

# 复制 go.mod 和 go.sum（如果 go.sum 不存在会自动生成）
COPY go.mod ./
RUN go mod tidy

# 复制所有代码
COPY . .

# 构建二进制文件
RUN go build -o telegram-bot main.go

# 使用更小的基础镜像
FROM debian:bullseye-slim

# 设置工作目录
WORKDIR /root/

# 复制二进制文件
COPY --from=builder /app/telegram-bot .

# 暴露端口（如果需要）
EXPOSE 8080

# 设置启动命令
CMD ["./telegram-bot"]