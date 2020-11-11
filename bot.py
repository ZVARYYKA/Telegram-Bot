import telebot
import config
bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('static/welcome.webp','rb')
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id, "Добро утро ёбана нахуй рот, {0.first_name}!\n Я - <b>{1.first_name}</b>, бот созданный для того,чтобы тебя отпиздить".format(message.from_user,bot.get_me()),
        parse_mode= 'html')

@bot.message_handler(content_types=['text'])
def lalala(message):
    bot.send_message(message.chat.id, message.text)

bot.polling(none_stop=True)