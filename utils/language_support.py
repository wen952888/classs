def translate(text, language):
    """
    简单的多语言翻译功能
    :param text: 原始文本
    :param language: 用户语言
    :return: 翻译后的文本
    """
    translations = {
        "zh": text,  # 默认中文
        "en": {
            "欢迎使用订阅转换机器人！支持以下功能：": "Welcome to the Subscription Converter Bot! Supported features:",
            "处理订阅链接时出错，请稍后再试。": "An error occurred while processing the subscription link. Please try again later.",
            "请输入有效的订阅链接（以 http/https 开头）。": "Please enter a valid subscription link (starting with http/https).",
            "节点健康检查报告：": "Node Health Check Report:",
        },
    }
    if language not in translations:
        language = "zh"  # 默认中文
    return translations.get(language, {}).get(text, text)