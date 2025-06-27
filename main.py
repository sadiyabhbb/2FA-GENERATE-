import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Get bot token from environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN")

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Hello! I am your 2FA Code Generator Bot.")

# /check command
async def check(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Your 2FA code is: 123456")  # Static demo

# Main app run
if __name__ == "__main__":
    if not BOT_TOKEN:
        print("❌ BOT_TOKEN is missing in environment variables.")
        exit()

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("check", check))

    print("✅ Bot is running...")
    app.run_polling()
