import telebot
from telebot import types

bot = telebot.TeleBot('7095217128:AAE0YnvTNRoQiXNqgjBRJ20j2HJnSP9sKL0')

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет! Я твой бот-помошник! Я помогу сориентироваться в нашей больнице", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == '👋 Поздороваться':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('Где приемное отделение?')
        btn2 = types.KeyboardButton('Где покурить?')
        btn3 = types.KeyboardButton('Часы посещения')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, '❓ Задайте интересующий вас вопрос', reply_markup=markup) #ответ бота


    elif message.text == 'Где приемное отделение?':
        bot.send_message(message.from_user.id, 'Вам необходимо пройти через проходную 1 корпуса, пересечь небольшой сквер и подойти к торцу корпуса №7 .\n \nСему можно посмотреть по ' + '[ссылке](https://ibb.co/CnxKvPd)', parse_mode='Markdown')

    elif message.text == 'Правила сайта':
        bot.send_message(message.from_user.id, 'Прочитать правила сайта вы можете по ' + '[ссылке](https://habr.com/ru/docs/help/rules/)', parse_mode='Markdown')

    elif message.text == 'Советы по оформлению публикации':
        bot.send_message(message.from_user.id, 'Подробно про советы по оформлению публикаций прочитать по ' + '[ссылке](https://habr.com/ru/docs/companies/design/)', parse_mode='Markdown')


bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть