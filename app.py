from flask import Flask, render_template, request, redirect, url_for
from flask_sockets import Sockets
import paramiko
import threading
import os

app = Flask(__name__)
sockets = Sockets(app)

# SSH 会话管理
sessions = {}

@app.route("/")
def index():
    return render_template("index.html")

@sockets.route('/webssh')
def webssh(ws):
    """WebSocket 处理 WebSSH"""
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(
            hostname=request.args.get('hostname'),
            port=int(request.args.get('port', 22)),
            username=request.args.get('username'),
            password=request.args.get('password', None),
            key_filename=request.args.get('keyfile', None)
        )
        channel = ssh.invoke_shell()
        sessions[ws] = channel

        def forward_data():
            while True:
                data = channel.recv(1024)
                if not data:
                    break
                ws.send(data.decode())

        thread = threading.Thread(target=forward_data)
        thread.start()

        while not ws.closed:
            message = ws.receive()
            if message:
                channel.send(message)
    except Exception as e:
        ws.send(f"Error: {str(e)}")
    finally:
        if ws in sessions:
            sessions.pop(ws)
        ws.close()

@app.route("/sftp", methods=["GET", "POST"])
def sftp():
    """SFTP 文件管理"""
    if request.method == "POST":
        hostname = request.form['hostname']
        username = request.form['username']
        password = request.form.get('password')
        keyfile = request.form.get('keyfile')
        try:
            transport = paramiko.Transport((hostname, 22))
            if password:
                transport.connect(username=username, password=password)
            else:
                transport.connect(username=username, pkey=paramiko.RSAKey.from_private_key_file(keyfile))
            sftp = paramiko.SFTPClient.from_transport(transport)
            files = sftp.listdir(".")
            return render_template("sftp.html", files=files, hostname=hostname)
        except Exception as e:
            return f"Error: {str(e)}"
    return render_template("sftp.html", files=[])

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)