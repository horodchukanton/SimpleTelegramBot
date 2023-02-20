import telebot
from telebot.types import Message

from sample_bot.settings import Settings

settings = Settings()

bot = telebot.TeleBot(settings.BOT_TOKEN)


@bot.message_handler()
def echo(message: Message):
    bot.send_message(message.chat.id, message.text)


def main():
    bot.infinity_polling()
