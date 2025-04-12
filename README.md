# SSH Master

**轻量级 SSH/SFTP 远程管理工具**

## 功能

- 支持密码和密钥认证
- 浏览器中管理 SSH 连接和文件
- 批量服务器命令执行
- 定时任务调度
- 多语言支持

## 安装和运行

### 使用 Docker
```bash
docker build -t ssh-master .
docker run -d -p 10000:10000 ssh-master
```

### 手动运行
1. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```
2. 启动应用：
   ```bash
   python app.py
   ```

## 配置
- 配置 SSH 账号：编辑 `accounts.json`
- 设置语言：通过环境变量 `LANGUAGE` 修改默认语言