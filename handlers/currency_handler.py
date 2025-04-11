from telegram import Update
from telegram.ext import ContextTypes
from utils.currency_api import convert_currency

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handle the /convert_currency command to convert between currencies.
    """
    if len(context.args) < 3:
        await update.message.reply_text("Usage: /convert_currency <amount> <from_currency> <to_currency>")
        return

    try:
        amount = float(context.args[0])
        from_currency = context.args[1].upper()
        to_currency = context.args[2].upper()

        result = convert_currency(amount, from_currency, to_currency)
        await update.message.reply_text(f"{amount} {from_currency} is approximately {result} {to_currency}.")
    except ValueError:
        await update.message.reply_text("Invalid amount. Please provide a valid number.")
    except Exception as e:
        await update.message.reply_text(f"Error during currency conversion: {e}")