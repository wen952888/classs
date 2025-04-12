import json
import os

class ConfigManager:
    def __init__(self):
        self.config_file = os.getenv('CONFIG_FILE', 'config.json')
        self.load_config()

    def load_config(self):
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as f:
                self.config = json.load(f)
        else:
            self.config = {'hosts': []}

    def save_config(self):
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f)

    def get_hosts(self):
        return self.config.get('hosts', [])

    def add_host(self, host_data):
        self.config['hosts'].append(host_data)
        self.save_config()
        return {'status': 'success', 'message': 'Host added successfully'}

    def remove_host(self, customhostname):
        self.config['hosts'] = [
            host for host in self.config['hosts'] if host['customhostname'] != customhostname
        ]
        self.save_config()
        return {'status': 'success', 'message': 'Host removed successfully'}