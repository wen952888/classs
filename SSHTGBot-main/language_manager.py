import os
import threading

class LanguageManager:
    def __init__(self):
        self._language = os.getenv('LANGUAGE', 'zh')
        self._lock = threading.Lock()

    def get_language(self):
        with self._lock:
            return self._language

    def set_language(self, language):
        with self._lock:
            self._language = language

language_manager = LanguageManager()