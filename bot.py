# -*- coding: utf-8 -*-
import telebot
from telebot import types
import urllib.request as urllib2

# токен боту
bot = telebot.TeleBot('1130800870:AAEeQ6SZvJP9gYFotYOKMfUuvn9oeLU27XQ')

# Основне меню
@bot.message_handler(commands=['start'])
def handler_start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('Відділення(Розклад)')
    btn2 = types.KeyboardButton('Посилання на сайт')
    btn3 = types.KeyboardButton('Посилання на Instagram акаунт')
    btn4 = types.KeyboardButton('Контакти')
    markup.add(btn1, btn2, btn3, btn4)
    send_mess = f"<b>Привіт {message.from_user.first_name}</b>!\nВибери один з пунктів меню"
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)

# Відділення
@bot.message_handler(content_types=['text'])
def all_button(message):
    if message.text == 'Відділення(Розклад)':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton('Відділення механіко-технологічне')
        btn2 = types.KeyboardButton('Відділення архітектури та мистецтва')
        btn3 = types.KeyboardButton('Кваліфікований робітник')
        btn4 = types.KeyboardButton('Повернутися в меню')
        markup.add(btn1, btn2, btn3, btn4)
        send_mess = "Ваше відділення"
        bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)

# (Механіко-технологічне)
    elif message.text == 'Відділення механіко-технологічне':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('1 Курc')
        btn2 = types.KeyboardButton('2 Курc')
        btn3 = types.KeyboardButton('3 Курc')
        btn4 = types.KeyboardButton('4 Курc')
        btn5 = types.KeyboardButton('Повернутися до відділень')
        btn6 = types.KeyboardButton('Повернутися в меню')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        send_mess = "Виберіть курс"
        bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)

        
        btn4 = types.KeyboardButton('Повернутися до курсів') # ua
# 1 курс (Механіко-технологічне)
    elif message.text == '1 Курc':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('МС-12/17')
        btn2 = types.KeyboardButton('МС-14/15')
        btn3 = types.KeyboardButton('Повернутися до курcів')
        btn4 = types.KeyboardButton('Повернутися в меню')
        markup.add(btn1, btn2, btn3, btn4)
        send_mess = "Виберіть групу"
        bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)

    elif message.text == 'МС-12/17':
        url = 'http://www.chtk.ck.ua/main/images/Rozklad/II_sem/12_17.jpg'
        urllib2.urlretrieve(url, 'url_image.jpg')
        img = open('url_image.jpg', 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()
    elif message.text == 'МС-14/15':
        url = 'http://www.chtk.ck.ua/main/images/Rozklad/II_sem/14_15.jpg'
        urllib2.urlretrieve(url, 'url_image.jpg')
        img = open('url_image.jpg', 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()

# 2 курс (Механіко-технологічне)
    elif message.text == '2 Курc':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('МС-21')
        btn2 = types.KeyboardButton('МС-22')
        btn3 = types.KeyboardButton('МС-24')
        btn4 = types.KeyboardButton('МС-27')
        btn5 = types.KeyboardButton('Повернутися до курcів')
        btn6 = types.KeyboardButton('Повернутися в меню')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        send_mess = "Виберіть групу"
        bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)

    elif message.text == 'МС-21':
        url = 'http://www.chtk.ck.ua/main/images/Rozklad/II_sem/21.jpg'
        urllib2.urlretrieve(url, 'url_image.jpg')
        img = open('url_image.jpg', 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()

    elif message.text == 'МС-22':
        url = 'http://www.chtk.ck.ua/main/images/Rozklad/II_sem/22.jpg'
        urllib2.urlretrieve(url, 'url_image.jpg')
        img = open('url_image.jpg', 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()

    elif message.text == 'МС-24':
        url = 'http://www.chtk.ck.ua/main/images/Rozklad/II_sem/24.jpg'
        urllib2.urlretrieve(url, 'url_image.jpg')
        img = open('url_image.jpg', 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()

    elif message.text == 'МС-27':
        url = 'http://www.chtk.ck.ua/main/images/Rozklad/II_sem/27.jpg'
        urllib2.urlretrieve(url, 'url_image.jpg')
        img = open('url_image.jpg', 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()

# 3 курс (Механіко-технологічне)
    elif message.text == '3 Курc':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('МС-31')
        btn2 = types.KeyboardButton('МС-32')
        btn3 = types.KeyboardButton('МС-34')
        btn4 = types.KeyboardButton('МС-37')
        btn5 = types.KeyboardButton('Повернутися до курcів')
        btn6 = types.KeyboardButton('Повернутися в меню')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        send_mess = "Виберіть групу"
        bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)

    elif message.text == 'МС-31':
        url = 'http://www.chtk.ck.ua/main/images/Rozklad/II_sem/31.jpg'
        urllib2.urlretrieve(url, 'url_image.jpg')
        img = open('url_image.jpg', 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()

    elif message.text == 'МС-32':
        url = 'http://www.chtk.ck.ua/main/images/Rozklad/II_sem/32.jpg'
        urllib2.urlretrieve(url, 'url_image.jpg')
        img = open('url_image.jpg', 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()

    elif message.text == 'МС-34':
        url = 'http://www.chtk.ck.ua/main/images/Rozklad/II_sem/34.jpg'
        urllib2.urlretrieve(url, 'url_image.jpg')
        img = open('url_image.jpg', 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()

    elif message.text == 'МС-37':
        url = 'http://www.chtk.ck.ua/main/images/Rozklad/II_sem/37.jpg'
        urllib2.urlretrieve(url, 'url_image.jpg')
        img = open('url_image.jpg', 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()

# 4 курс (Механіко-технологічне)
    elif message.text == '4 Курc':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('МС-41')
        btn2 = types.KeyboardButton('МС-42')
        btn3 = types.KeyboardButton('МС-44')
        btn4 = types.KeyboardButton('Повернутися до курcів')
        btn5 = types.KeyboardButton('Повернутися в меню')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        send_mess = "Виберіть групу"
        bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)

    elif message.text == 'МС-41':
        url = 'http://www.chtk.ck.ua/main/images/Rozklad/II_sem/41.jpg'
        urllib2.urlretrieve(url, 'url_image.jpg')
        img = open('url_image.jpg', 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()

    elif message.text == 'МС-42':
        url = 'http://www.chtk.ck.ua/main/images/Rozklad/II_sem/42.jpg'
        urllib2.urlretrieve(url, 'url_image.jpg')
        img = open('url_image.jpg', 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()

    elif message.text == 'МС-44':
        url = 'http://www.chtk.ck.ua/main/images/Rozklad/II_sem/44.jpg'
        urllib2.urlretrieve(url, 'url_image.jpg')
        img = open('url_image.jpg', 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()

# (Архітектура та мистецтва(Повторення))
    elif message.text == 'Відділення архітектури та мистецтва':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('1 Курс')
        btn2 = types.KeyboardButton('2 Курс')
        btn3 = types.KeyboardButton('3 Курс')
        btn4 = types.KeyboardButton('4 Курс')
        btn5 = types.KeyboardButton('Повернутися до відділень')
        btn6 = types.KeyboardButton('Повернутися в меню')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        send_mess = "Виберіть курс"
        bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)

# 1 курс (Архітектура та мистецтва)
    elif message.text == '1 Курс':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('МС-13')
        btn2 = types.KeyboardButton('МС-16')
        btn3 = types.KeyboardButton('МС-18')
        btn4 = types.KeyboardButton('МС-19')
        btn5 = types.KeyboardButton('МС-108')
        btn6 = types.KeyboardButton('Повернутися до курсів')
        btn7 = types.KeyboardButton('Повернутися в меню')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        send_mess = "Виберіть групу"
        bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)

    elif message.text == 'МС-13':
        url = 'http://www.chtk.ck.ua/main/images/Rozklad/II_sem/13.jpg'
        urllib2.urlretrieve(url, 'url_image.jpg')
        img = open('url_image.jpg', 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()

    elif message.text == 'МС-16':
        url = 'http://www.chtk.ck.ua/main/images/Rozklad/II_sem/16.jpg'
        urllib2.urlretrieve(url, 'url_image.jpg')
        img = open('url_image.jpg', 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()

    elif message.text == 'МС-18':
        url = 'http://www.chtk.ck.ua/main/images/Rozklad/II_sem/18.jpg'
        urllib2.urlretrieve(url, 'url_image.jpg')
        img = open('url_image.jpg', 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()

    elif message.text == 'МС-19':
        url = 'http://www.chtk.ck.ua/main/images/Rozklad/II_sem/19.jpg'
        urllib2.urlretrieve(url, 'url_image.jpg')
        img = open('url_image.jpg', 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()

    elif message.text == 'МС-108':
        url = 'http://www.chtk.ck.ua/main/images/Rozklad/II_sem/108.jpg'
        urllib2.urlretrieve(url, 'url_image.jpg')
        img = open('url_image.jpg', 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()

# 2 курс (Архітектура та мистецтво)
    elif message.text == '2 Курс':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('МС-23')
        btn2 = types.KeyboardButton('МС-26')
        btn3 = types.KeyboardButton('МС-28')
        btn4 = types.KeyboardButton('МС-29')
        btn5 = types.KeyboardButton('МС-208')
        btn6 = types.KeyboardButton('Повернутися до курсів')
        btn7 = types.KeyboardButton('Повернутися в меню')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        send_mess = "Виберіть групу"
        bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)

    elif message.text == 'МС-23':
        url = 'http://www.chtk.ck.ua/main/images/Rozklad/II_sem/23.jpg'
        urllib2.urlretrieve(url, 'url_image.jpg')
        img = open('url_image.jpg', 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()

    elif message.text == 'МС-26':
        url = 'http://www.chtk.ck.ua/main/images/Rozklad/II_sem/26.jpg'
        urllib2.urlretrieve(url, 'url_image.jpg')
        img = open('url_image.jpg', 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()

    elif message.text == 'МС-28':
        url = 'http://www.chtk.ck.ua/main/images/Rozklad/II_sem/28.jpg'
        urllib2.urlretrieve(url, 'url_image.jpg')
        img = open('url_image.jpg', 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()

    elif message.text == 'МС-29':
        url = 'http://www.chtk.ck.ua/main/images/Rozklad/II_sem/29.jpg'
        urllib2.urlretrieve(url, 'url_image.jpg')
        img = open('url_image.jpg', 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()

    elif message.text == 'МС-208':
        url = 'http://www.chtk.ck.ua/main/images/Rozklad/II_sem/208.jpg'
        urllib2.urlretrieve(url, 'url_image.jpg')
        img = open('url_image.jpg', 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()

# 3 курс (Архітектура та мистецтво)
    elif message.text == '3 Курс':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('МС-33')
        btn2 = types.KeyboardButton('МС-36')
        btn3 = types.KeyboardButton('МС-38')
        btn4 = types.KeyboardButton('МС-39')
        btn5 = types.KeyboardButton('Повернутися до курсів')
        btn6 = types.KeyboardButton('Повернутися в меню')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        send_mess = "Виберіть групу"
        bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)

    elif message.text == 'МС-33':
        url = 'http://www.chtk.ck.ua/main/images/Rozklad/II_sem/33.jpg'
        urllib2.urlretrieve(url, 'url_image.jpg')
        img = open('url_image.jpg', 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()

    elif message.text == 'МС-36':
        url = 'http://www.chtk.ck.ua/main/images/Rozklad/II_sem/36.jpg'
        urllib2.urlretrieve(url, 'url_image.jpg')
        img = open('url_image.jpg', 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()

    elif message.text == 'МС-38':
        url = 'http://www.chtk.ck.ua/main/images/Rozklad/II_sem/38.jpg'
        urllib2.urlretrieve(url, 'url_image.jpg')
        img = open('url_image.jpg', 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()

    elif message.text == 'МС-39':
        url = 'http://www.chtk.ck.ua/main/images/Rozklad/II_sem/39.jpg'
        urllib2.urlretrieve(url, 'url_image.jpg')
        img = open('url_image.jpg', 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()

# 4 курс (Архітектура та мистецтво)
    elif message.text == '4 Курс':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('МС-43')
        btn2 = types.KeyboardButton('МС-46')
        btn3 = types.KeyboardButton('МС-49')
        btn4 = types.KeyboardButton('Повернутися до курсів')
        btn5 = types.KeyboardButton('Повернутися в меню')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        send_mess = "Виберіть групу"
        bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)

    elif message.text == 'МС-43':
        url = 'http://www.chtk.ck.ua/main/images/Rozklad/II_sem/43.jpg'
        urllib2.urlretrieve(url, 'url_image.jpg')
        img = open('url_image.jpg', 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()

    elif message.text == 'МС-46':
        url = 'http://www.chtk.ck.ua/main/images/Rozklad/II_sem/46.jpg'
        urllib2.urlretrieve(url, 'url_image.jpg')
        img = open('url_image.jpg', 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()

    elif message.text == 'МС-49':
        url = 'http://www.chtk.ck.ua/main/images/Rozklad/II_sem/49.jpg'
        urllib2.urlretrieve(url, 'url_image.jpg')
        img = open('url_image.jpg', 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()

# (Кваліфікований робітник)
    elif message.text == 'Кваліфікований робітник':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton('Групи КР')
        btn2 = types.KeyboardButton('Повернутися в меню')
        markup.add(btn1, btn2)
        send_mess = "Виберіть курс"
        bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)

# Загалом (Кваліфікований робітник)
    elif message.text == 'Групи КР':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton('КР-28')
        btn2 = types.KeyboardButton('Повернутися в меню')
        markup.add(btn1, btn2)
        send_mess = "Виберіть групу"
        bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)

    elif message.text == 'КР-28':
        url = 'http://www.chtk.ck.ua/main/images/Rozklad/II_sem/kr_28.jpg'
        urllib2.urlretrieve(url, 'url_image.jpg')
        img = open('url_image.jpg', 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()

# Повернення в меню
    elif message.text == 'Повернутися в меню':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton('Відділення(Розклад)')
        btn2 = types.KeyboardButton('Посилання на сайт')
        btn3 = types.KeyboardButton('Посилання на Instagram акаунт')
        btn4 = types.KeyboardButton('Контакти')
        markup.add(btn1, btn2, btn3, btn4)
        send_mess = "Вибери один з пунктів меню"
        bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)

# Посилання на сайт
    elif message.text == 'Посилання на сайт':
        send_mess = f"<b>Ось ваше посилання на сайт</b>!\nhttp://www.chtk.ck.ua/main/"
        bot.send_message(message.chat.id, send_mess, parse_mode='html')

# Instagram
    elif message.text == 'Посилання на Instagram акаунт':
        send_mess = f"<b>Ось ваше посилання на Instagram</b>!\nhttps://www.instagram.com/chtk_cherkassy/"
        bot.send_message(message.chat.id, send_mess, parse_mode='html')

# Контакти
    elif message.text == 'Контакти':
        send_mess = f"<b>Електронна пошта:</b> chhtk@ukr.net<b>\nНомер телефону:</b> (0472) 66-17-33\n<b>Адреса:</b> м.Черкаси, вул.Сумгаїтська, 13"
        bot.send_message(message.chat.id, send_mess, parse_mode='html')

# Повернення до відділень
    elif message.text == 'Повернутися до відділень':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton('Відділення механіко-технологічне')
        btn2 = types.KeyboardButton('Відділення архітектури та мистецтва')
        btn3 = types.KeyboardButton('Кваліфікований робітник')
        btn4 = types.KeyboardButton('Повернутися в меню')
        markup.add(btn1, btn2, btn3, btn4)
        send_mess = "Ваше відділення"
        bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)
        
# (Механіко-технологічне(Повернення))
    elif message.text == 'Повернутися до курcів':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('1 Курc')
        btn2 = types.KeyboardButton('2 Курc')
        btn3 = types.KeyboardButton('3 Курc')
        btn4 = types.KeyboardButton('4 Курc')
        btn5 = types.KeyboardButton('Повернутися до відділень')
        btn6 = types.KeyboardButton('Повернутися в меню')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        send_mess = "Виберіть курс"
        bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)
        
 # (Архітектура та мистецтва(Повторення))
    elif message.text == 'Повернутися до курсів':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('1 Курс')
        btn2 = types.KeyboardButton('2 Курс')
        btn3 = types.KeyboardButton('3 Курс')
        btn4 = types.KeyboardButton('4 Курс')
        btn5 = types.KeyboardButton('Повернутися до відділень')
        btn6 = types.KeyboardButton('Повернутися в меню')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        send_mess = "Виберіть курс"
        bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)


# не дає зупинити бота при виникненні помилки
bot.polling(none_stop=True)
