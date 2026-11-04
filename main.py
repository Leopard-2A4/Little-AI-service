import os
import telebot
from dotenv import load_dotenv
from ai_part import ai_answer

load_dotenv()
API_TOKEN = os.getenv('TELEGRAM_API_TOKEN')
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я Тестовый ИИ бот. Напиши Мне что нибудь")


@bot.message_handler(content_types=['text'])
def answer(message):
    ai_response = ai_answer(message.text)
    bot.reply_to(message, ai_response)

if __name__ == '__main__':
    bot.polling(none_stop=True)