import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.environ["BOT_TOKEN"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🎉 Selamat Datang di 567TV!\n\n"
        "📺 Live Streaming 24 Jam\n"
        "🎬 Video & Hiburan\n"
        "🎮 Hiburan Seru\n"
        "🎁 Event Terbaru\n"
        "💬 Customer Service 24 Jam\n\n"
        "👇 Pilih menu di bawah ini:"
    )

    keyboard = [
        [
            InlineKeyboardButton(
                "🚀 Masuk 567TV",
                web_app=WebAppInfo(url="https://567tv.id/")
            )
        ],
        [
            InlineKeyboardButton(
                "🌐 Website Resmi",
                url="https://567tv.id/"
            )
        ]
    ]

    await update.message.reply_text(
        text,
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
