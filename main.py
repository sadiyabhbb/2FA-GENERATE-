import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import pyotp

BOT_TOKEN = os.getenv("BOT_TOKEN")

# /start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔐 Welcome to 2FA Code Bot!\nSend /generate to get your 2FA code.")

# /generate command handler
async def generate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Example TOTP key (base32 format). Replace this with your own.
    secret = "JBSWY3DPEHPK3PXP"
    totp = pyotp.TOTP(secret)
    code = totp.now()
    await update.message.reply_text(f"✅ Your 2FA Code: {code}")

# main function
if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("generate", generate))

    app.run_polling()
