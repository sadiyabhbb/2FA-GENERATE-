import pyotp
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")  # safer than hardcoding

USER_SECRETS = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Welcome! Use /set <secret> to set your 2FA secret.")

async def set_secret(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if len(context.args) != 1:
        await update.message.reply_text("❌ Usage: /set <your_secret>")
        return
    USER_SECRETS[user_id] = context.args[0]
    await update.message.reply_text("✅ 2FA secret set! Now use /code to get the current code.")

async def get_code(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in USER_SECRETS:
        await update.message.reply_text("⚠️ Please set your secret first using /set command.")
        return
    totp = pyotp.TOTP(USER_SECRETS[user_id])
    code = totp.now()
    await update.message.reply_text(f"🔐 Your 2FA code: `{code}`", parse_mode="Markdown")

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("set", set_secret))
    app.add_handler(CommandHandler("code", get_code))

    print("Bot running...")
    app.run_polling()
