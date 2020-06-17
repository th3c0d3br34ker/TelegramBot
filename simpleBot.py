from telegram.bot import Bot
from os import getenv

TOKEN = getenv("TELEGRAMBOT_TOKEN")
bot = Bot(token=TOKEN)

# User's Chat id and Message
CHAT_ID = "CHAT_ID OF THE TELEGRAM USER"
MESSAGE="Hi form Telegram Bot!"

message = bot.send_message(chat_id=CHAT_ID, text=MESSAGE)

print("Sent")