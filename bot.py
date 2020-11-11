import telebot
import config
import random
 
from telebot import types
 
bot = telebot.TeleBot(config.TOKEN)
 
@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('static/welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
 
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Число выстрелов тебе в ебало нахуй")
    item2 = types.KeyboardButton("Пойти нахуй")
 
    markup.add(item1, item2)
 
    bot.send_message(message.chat.id, "Добро пожаловать ёбана нахуй рот, {0.first_name}!\nЯ нахуй - <b>{1.first_name}</b>,  бот созданный для того, чтобы тебя отпиздить".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)
 
@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Число выстрелов тебе в ебало нахуй':
            bot.send_message(message.chat.id, str(random.randint(0,100)))
        elif message.text == 'Пойти нахуй':
 
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Гомодрил ебаный", callback_data='good')
            item2 = types.InlineKeyboardButton("Ну лан((", callback_data='bad')
 
            markup.add(item1, item2)
 
            bot.send_message(message.chat.id, 'Ну и иди нахуй картоха ебаная', reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'Чё за хуйню городишь дибил блять')
 
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Бля ну всё нахуй тебе пиздец, джанки мне звонят, диндириндиндон')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Ну ты и лох ебать')
 
            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Пойти нахуй",
                reply_markup=None)
 
            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                text="ТЕБЕ ПИЗДА Я В ТВОЁМ ТЕЛЕФОНЕ!!!!")
 
    except Exception as e:
        print(repr(e))
 
# RUN
bot.polling(none_stop=True)






