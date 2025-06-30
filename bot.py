
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import random

# Настроения и треки (для примера несколько, можно добавить больше)
MOODS = {
    "Грустно": [
        ("Billie Eilish – idontwannabeyouanymore", "https://youtu.be/pbMwTqkKSps"),
        ("Joji – Slow Dancing in the Dark", "https://youtu.be/K3Qzzggn--s")
    ],
    "Счастье": [
        ("Pharrell Williams – Happy", "https://youtu.be/ZbZSe6N_BXs"),
        ("Justin Timberlake – Can't Stop the Feeling", "https://youtu.be/ru0K8uYEZWw")
    ],
    "Влюблён": [
        ("Ed Sheeran – Perfect", "https://youtu.be/2Vv-BfVoq4g"),
        ("The Weeknd – Earned It", "https://youtu.be/waU75jdUnYw")
    ],
    "Мотивация": [
        ("Eminem – Lose Yourself", "https://youtu.be/_Yhyp-_hX2s"),
        ("Imagine Dragons – Believer", "https://youtu.be/7wtfhZwyrcc")
    ],
    "Злость": [
        ("Kanye West – Black Skinhead", "https://youtu.be/RrEzrJgG5y8")
    ],
    "Уют": [
        ("Norah Jones – Don't Know Why", "https://youtu.be/tO4dxvguQDk")
    ],
    "Чилл": [
        ("Post Malone – Circles", "https://youtu.be/wXhTHyIgQ_U")
    ],
    "Энергия": [
        ("AC/DC – Thunderstruck", "https://youtu.be/v2AC41dglnM")
    ]
}

# Приветствие при /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[mood] for mood in MOODS.keys()]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "🎧 Привет! Я Эмо DJ.
Выбери своё настроение, и я подберу трек!",
        reply_markup=reply_markup
    )

# Ответ на выбор настроения
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_mood = update.message.text
    if user_mood in MOODS:
        track = random.choice(MOODS[user_mood])
        await update.message.reply_text(f"🎭 *{user_mood}*
🎵 *{track[0]}*
{track[1]}", parse_mode="Markdown")
    else:
        await update.message.reply_text("Выбери настроение с клавиатуры ниже!")

app = ApplicationBuilder().token("8190690928:AAG2o10BVhz1d_mLV3zXsqv5hdiKP6aXUxw").build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.run_polling()
