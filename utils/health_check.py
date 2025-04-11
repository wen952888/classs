import random

def check_node_health(subscription_content):
    """
    模拟节点健康检查
    :param subscription_content: 订阅内容
    :return: 健康检查报告
    """
    nodes = subscription_content.split("\n")[:5]
    health_report = []
    for node in nodes:
        status = "正常" if random.random() > 0.2 else "异常"
        latency = random.randint(50, 300)
        health_report.append(f"节点：{node[:30]}... 状态：{status} 延迟：{latency}ms")
    return "\n".join(health_report)