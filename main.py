from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

# /start কমান্ড হ্যান্ডলার
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Hello! I'm your 2FA code bot.\n\n✅ Code: 123456 (Demo)")

# /generate কমান্ড হ্যান্ডলার (ডেমো 2FA কোড)
async def generate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    import random
    code = random.randint(100000, 999999)
    await update.message.reply_text(f"🔐 Your 2FA Code: {code}")

# বট চালানোর অংশ
if __name__ == "__main__":
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    if not BOT_TOKEN:
        print("❌ BOT_TOKEN is not set!")
        exit()

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("generate", generate))

    print("✅ Bot is running...")
    app.run_polling()
