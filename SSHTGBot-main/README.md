# SSH Master

**轻量级 SSH/SFTP 远程管理工具**

## 功能

- 支持密码和密钥认证
- 浏览器中管理 SSH 连接
- 文件上传、下载和编辑功能
- 支持手机访问
- 批量服务器命令执行
- 定时任务管理
- 服务器分组功能
- 中文和英文界面支持

## 安装和运行

### 使用 Docker
```bash
docker build -t ssh-master .
docker run -d -p 10000:10000 ssh-master