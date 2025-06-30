import json
import random
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# Загружаем треки из файла
with open("tracks.json", "r", encoding="utf-8") as f:
    MOODS = json.load(f)

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[mood] for mood in MOODS.keys()]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "🎧 Привет! Я Эмо DJ.\nВыбери своё настроение, и я подберу трек!",
        reply_markup=reply_markup
    )

# Команда /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = (
        "🤖 *Эмо DJ* – бот, который подбирает музыку под настроение!\n\n"
        "📌 *Команды:*\n"
        "/start – начать заново и выбрать настроение\n"
        "/help – показать это сообщение\n\n"
        "Или просто нажми кнопку с настроением! 🎵"
    )
    await update.message.reply_text(help_text, parse_mode="Markdown")

# Обработка сообщений (выбор настроения)
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_mood = update.message.text
    if user_mood in MOODS:
        track = random.choice(MOODS[user_mood])
        await update.message.reply_text(
            f"🎭 *{user_mood}*\n🎵 *{track[0]}*\n{track[1]}",
            parse_mode="Markdown"
        )
    else:
        await update.message.reply_text("Выбери настроение с клавиатуры ниже!")

# Создаём и запускаем бота
app = ApplicationBuilder().token("8190690928:AAG2o10BVhz1d_mLV3zXsqv5hdiKP6aXUxw").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

app.run_polling()
