import requests
import telebot
from telebot import types

TOKEN = '5545444136:AAH4a9Fz71iqufJrAJEy6bfTjmnhxJ1X0aE'
bot = telebot.TeleBot(TOKEN)

page = 1

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Персонаж')
    markup.add(item1)
    bot.send_message(message.chat.id, 'Нажми на кнопку "Персонаж"')



@bot.message_handler(content_types=['text'])
def get_data(message):
    try:
        if message.text == 'Персонаж':
            r = requests.get("https://naruto-details.herokuapp.com/clan?name=uzumaki").json()[0]
            for i, j in r.items():
                bot.send_message(message.chat.id, f'{i}: {j}')
        else:
            bot.send_message(message.chat.id, 'Неизвестная команда')
    except:
        bot.send_message(message.chat.id, 'Исключение')


# r = requests.get("https://naruto-details.herokuapp.com/clan?name=uzumaki").json()[0]['1. Name']
# print(r)
if __name__ == '__main__':
    bot.polling(none_stop=True)