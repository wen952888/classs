import paramiko
from threading import Lock

class SSHManager:
    def __init__(self):
        self.sessions = {}
        self.lock = Lock()

    def connect(self, hostname, username, password=None, private_key=None):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            if private_key:
                client.connect(hostname, username=username, key_filename=private_key)
            else:
                client.connect(hostname, username=username, password=password)
            return client
        except Exception as e:
            raise Exception(f"SSH connection failed: {str(e)}")

    def handle_ssh(self, ws, customhostname):
        try:
            client = self.sessions.get(customhostname)
            if not client:
                ws.send("No active SSH session for this host.")
                return

            while True:
                command = ws.receive()
                if command:
                    stdin, stdout, stderr = client.exec_command(command)
                    ws.send(stdout.read().decode() or stderr.read().decode())
        except Exception as e:
            ws.send(f"Error: {str(e)}")