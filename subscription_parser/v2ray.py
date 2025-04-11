import base64
import requests

def parse_v2ray_subscription(url):
    """
    解析 V2Ray 格式的订阅链接
    :param url: 订阅链接
    :return: 解析后的节点信息
    """
    response = requests.get(url)
    if response.status_code != 200:
        return f"无法获取订阅内容，HTTP 状态码：{response.status_code}"

    # 解码 Base64 内容
    try:
        decoded_content = base64.b64decode(response.text).decode("utf-8")
    except Exception as e:
        return f"订阅内容解析失败：{str(e)}"

    # 返回订阅内容
    return f"解析成功：V2Ray 订阅内容：\n{decoded_content[:500]}..."