from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes

# 自定义键盘菜单
async def menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        ["生成二维码", "转换订阅"],
        ["搜索免费节点", "帮助"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    await update.message.reply_text("请选择一个功能：", reply_markup=reply_markup)