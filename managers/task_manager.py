import json
import os

class TaskManager:
    def __init__(self):
        self.tasks_file = os.getenv('TASKS_FILE', 'tasks.json')
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.tasks_file):
            with open(self.tasks_file, 'r') as f:
                self.tasks = json.load(f).get('tasks', [])
        else:
            self.tasks = []

    def save_tasks(self):
        with open(self.tasks_file, 'w') as f:
            json.dump({'tasks': self.tasks}, f)

    def get_tasks(self):
        return {'tasks': self.tasks}

    def add_task(self, task_data):
        task_data['id'] = str(len(self.tasks) + 1)
        self.tasks.append(task_data)
        self.save_tasks()
        return {'status': 'success', 'message': 'Task added successfully'}

    def remove_task(self, task_id):
        self.tasks = [task for task in self.tasks if task['id'] != task_id]
        self.save_tasks()
        return {'status': 'success', 'message': 'Task removed successfully'}