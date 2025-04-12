translations = {
    "zh": {
        "welcome_message": "欢迎使用 SSH 管理工具！"
    },
    "en": {
        "welcome_message": "Welcome to the SSH Management Tool!"
    }
}

def get_translation(key, language="zh"):
    return translations.get(language, {}).get(key, key)