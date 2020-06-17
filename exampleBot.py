from telegram.ext import CommandHandler
from telegram.ext import Updater, MessageHandler, Filters
from os import getenv

TOKEN = getenv('TELEGRAMBOT_TOKEN')
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    print(update.effective_chat.id)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="I'm a bot, please talk to me!")


def echo(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=update.message.text)


def message(update, context, message):
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


start_handler = CommandHandler('start', start)
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(echo_handler)

updater.start_polling()

print("Started!")
