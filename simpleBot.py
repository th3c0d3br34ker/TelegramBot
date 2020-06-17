from telegram.bot import Bot
from os import getenv

TOKEN = getenv("TELEGRAMBOT_TOKEN")
bot = Bot(token="1064607960:AAElkp1ausJNIGVC_n30s3cKbzOEVY_tV6I")

# User's Chat id and Message
CHAT_ID = "CHAT_ID OF THE TELEGRAM USER"
MESSAGE="Hi form Telegram Bot!"

message = bot.send_message(chat_id=CHAT_ID, text=MESSAGE)

print("Sent")