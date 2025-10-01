from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import os

# ==============================
# 🔑 Bot Config
# ==============================
TOKEN = os.getenv("BOT_TOKEN")  # Render / local env variable
ADMIN_ID = 8043847617           # Apna Telegram ID

bot_active = True  # By default bot ON

# ==============================
# 🚀 Commands
# ==============================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Bundela Bot is running!")

async def toggle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global bot_active
    user_id = update.effective_user.id

    if user_id == ADMIN_ID:  # Sirf admin toggle kar sakta hai
        bot_active = not bot_active
        status = "ON ✅" if bot_active else "OFF ❌"
        await update.message.reply_text(f"⚡ Bundela Bot is now {status}")
    else:
        await update.message.reply_text("❌ You are not authorized to use /toggle.")

# ==============================
# 🤖 Auto Reply
# ==============================
async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if bot_active:
        text = update.message.text.lower()

        if "create" in text:
            await update.message.reply_text("👋 I do!")

        elif "bye" in text:
            await update.message.reply_text("Goodbye 👋")

# ==============================
# 🔥 Application Setup
# ==============================
def main():
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("toggle", toggle))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))

    print("🚀 Starting Bundela Bot...")
    app.run_polling()

if __name__ == "__main__":
    main()
