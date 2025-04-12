# 使用官方 Golang 镜像
FROM golang:1.20 as builder

# 设置工作目录
WORKDIR /app

# 复制 go.mod 和 go.sum
COPY go.mod go.sum ./

# 下载依赖
RUN go mod download

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