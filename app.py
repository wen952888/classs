from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from werkzeug.security import check_password_hash
from flask_sock import Sock
from managers.ssh_manager import SSHManager
from managers.task_manager import TaskManager
from managers.config_manager import ConfigManager

import os

# Flask App Initialization
app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'default_secret_key')
sock = Sock(app)

# Managers Initialization
ssh_manager = SSHManager()
task_manager = TaskManager()
config_manager = ConfigManager()

# Routes
@app.route('/')
def index():
    if not session.get('authenticated'):
        return redirect(url_for('login'))
    return render_template('ssh-panel.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        password = request.form['password']
        hashed_password = os.getenv('LOGIN_PASSWORD_HASH', '')
        if check_password_hash(hashed_password, password):
            session['authenticated'] = True
            return redirect(url_for('index'))
        return render_template('login.html', error='Invalid password')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/api/get_hosts', methods=['GET'])
def get_hosts():
    return jsonify(config_manager.get_hosts())

@app.route('/api/add_host', methods=['POST'])
def add_host():
    data = request.json
    return jsonify(config_manager.add_host(data))

@app.route('/api/remove_host', methods=['POST'])
def remove_host():
    data = request.json
    return jsonify(config_manager.remove_host(data['customhostname']))

@app.route('/api/get_tasks', methods=['GET'])
def get_tasks():
    return jsonify(task_manager.get_tasks())

@app.route('/api/add_task', methods=['POST'])
def add_task():
    data = request.json
    return jsonify(task_manager.add_task(data))

@app.route('/api/remove_task', methods=['POST'])
def remove_task():
    return jsonify(task_manager.remove_task(request.json['id']))

@sock.route('/ws/ssh/<string:customhostname>')
def ssh_websocket(ws, customhostname):
    ssh_manager.handle_ssh(ws, customhostname)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)