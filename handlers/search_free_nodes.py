import requests
from telegram import Update
from telegram.ext import ContextTypes

# 搜索免费节点功能
async def search_free_nodes_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        api_url = "https://example.com/free-nodes-api"
        response = requests.get(api_url)
        
        if response.status_code == 200:
            free_nodes = response.json().get("nodes", [])
            if free_nodes:
                nodes_text = "\n".join(f"节点 {i+1}: {node}" for i, node in enumerate(free_nodes))
                await update.message.reply_text(f"找到以下免费节点：\n{nodes_text}")
            else:
                await update.message.reply_text("未找到免费节点。")
        else:
            await update.message.reply_text(f"获取免费节点失败，错误代码：{response.status_code}")
    except Exception as e:
        await update.message.reply_text(f"搜索免费节点时出错：{e}")