import qrcode
import io
from telegram import Update
from telegram.ext import ContextTypes

# 生成二维码功能
async def generate_qr_code_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        message = update.message.text
        if not message.startswith("http"):
            await update.message.reply_text("请发送有效的链接以生成二维码！")
            return

        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(message)
        qr.make(fit=True)

        img = qr.make_image(fill="black", back_color="white")
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)

        await update.message.reply_photo(buffer)
    except Exception as e:
        await update.message.reply_text(f"生成二维码时出错：{e}")