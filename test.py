import telebot
from telebot import types

bot = telebot.TeleBot('7095217128:AAFc_-5FPzWBUdGi2ILdUdKYVVB0Zmm1qjU')

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет! Я твой бот-помошник! Я помогу сориентироваться в ГКБ им. М.Е. Жадкевича", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == '👋 Поздороваться':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('Где приемное отделение?')
        btn2 = types.KeyboardButton('Где покурить?')
        btn3 = types.KeyboardButton('Часы посещений')
        btn4 = types.KeyboardButton('Подключиться к Wi-Fi')
        btn4 = types.KeyboardButton('Где поесть?')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.from_user.id, '❓ Задайте интересующий вас вопрос', reply_markup=markup) #ответ бота


    elif message.text == 'Где приемное отделение?':
        bot.send_message(message.from_user.id, 'Вам необходимо пройти через проходную корпуса №1, пересечь небольшой сквер и подойти к торцу корпуса №7 .\n \nСхему можно посмотреть по ' + '[ссылке](https://gb71.ru/kontakty/)', parse_mode='Markdown')
        Photo_1 = open("PO_In.png","rb")
        bot.send_photo(message.chat.id,Photo_1)

    elif message.text == 'Где покурить?':
        bot.send_message(message.from_user.id, 'Согласно Закону N 15-ФЗ курение табака запрещено на территориях и в помещениях, предназначенных для оказания медицинских услуг, а также на рабочих местах и в рабочих зонах, организованных в помещениях. Но вы всегда можете выйти за территорию и предаться саморазрушению 😊' )

    elif message.text == 'Часы посещений':
        bot.send_message(message.from_user.id, 'К сожалнию из за сложной санитарно-эпидемиологической обстановки в Москве посещение пациентов, пока, запрещено.\n \nПодробности можно прочитать по ' + '[ссылке](https://gb71.ru/news/izmenen-poryadok-dopuska-posetiteley-k-patsientam_2/)', parse_mode='Markdown')

    elif message.text == 'Подключиться к Wi-Fi':
        bot.send_message(message.from_user.id, 'В нашей больнице вы всегда можете воспользоваться быстрым и стабильным подключением к сети интернет.\n \nПодробная инструкция:') 
        f = open("public.pdf","rb")
        bot.send_document(message.chat.id,f)
 
    elif message.text == 'Где поесть?':
        bot.send_message(message.from_user.id, 'На первом этаже корпусов №1 и №7, а также на 2 этаже корпуса №2 вы можете найти богато наполненые венденговые автоматы, если же вы хотите выпить горячий кофе приготовленный на професиональной кофеварочной машине - посетите кафе расположенное на первом этаже корпуса №4.\n \n Желаю приятного аппетита!')
        Photo_2 = open("coffee.jpg","rb")
        bot.send_photo(message.chat.id,Photo_2)

bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть