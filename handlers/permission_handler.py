from telegram import Update
from telegram.ext import ContextTypes

USER_PERMISSIONS = {}

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if len(context.args) < 2:
        await update.message.reply_text("Usage: /set_permission <user_id> <level>")
        return

    try:
        user_id = int(context.args[0])
        permission_level = context.args[1].lower()

        if permission_level not in ["admin", "user", "guest"]:
            await update.message.reply_text("Invalid permission level. Choose from: admin, user, guest.")
            return

        USER_PERMISSIONS[user_id] = permission_level
        await update.message.reply_text(f"Set user {user_id}'s permission to {permission_level}.")
    except ValueError:
        await update.message.reply_text("Invalid user ID. Please provide a valid integer.")
    except Exception as e:
        await update.message.reply_text(f"Error setting permission: {e}")

def get_permission(user_id: int) -> str:
    return USER_PERMISSIONS.get(user_id, "guest")