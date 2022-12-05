import telebot
import sqlite3
from geopy import geocoders
from os import environ
import googlesearch
import DB_reader as reader

API_TOKEN = '5897033982:AAEuizb2FglrTRiRw4qEruKzWlbJyuAJnh8'

bot = telebot.TeleBot(API_TOKEN)

value = ''
old_value = ''
calc_ratio = False
calc_complex = False
phone = False

x = 0
y = 0
act = 0

keyboard = telebot.types.InlineKeyboardMarkup()
keyboard.row(telebot.types.InlineKeyboardButton(' ', callback_data='no'),
             telebot.types.InlineKeyboardButton('c', callback_data='c'),
             telebot.types.InlineKeyboardButton('<=', callback_data='<='),
             telebot.types.InlineKeyboardButton('/', callback_data='/'))

keyboard.row(telebot.types.InlineKeyboardButton('7', callback_data='7'),
             telebot.types.InlineKeyboardButton('8', callback_data='8'),
             telebot.types.InlineKeyboardButton('9', callback_data='9'),
             telebot.types.InlineKeyboardButton('*', callback_data='*'))

keyboard.row(telebot.types.InlineKeyboardButton('4', callback_data='4'),
             telebot.types.InlineKeyboardButton('5', callback_data='5'),
             telebot.types.InlineKeyboardButton('6', callback_data='6'),
             telebot.types.InlineKeyboardButton('-', callback_data='-'))

keyboard.row(telebot.types.InlineKeyboardButton('1', callback_data='1'),
             telebot.types.InlineKeyboardButton('2', callback_data='2'),
             telebot.types.InlineKeyboardButton('3', callback_data='3'),
             telebot.types.InlineKeyboardButton('+', callback_data='+'))

keyboard.row(telebot.types.InlineKeyboardButton(' ', callback_data='no'),
             telebot.types.InlineKeyboardButton('0', callback_data='0'),
             telebot.types.InlineKeyboardButton(',', callback_data=','),
             telebot.types.InlineKeyboardButton('=', callback_data='='))


@bot.message_handler(commands=['start'])
def get_message(message):
    global value, old_value
    if message.text == "/start":
        bot.send_message(message.chat.id,
                         'ЧУДЕСНЫЙ КАЛЬКУЛЯТОР.\nВозможности:\n1. Калькулятор комплексных чисел /complex\n2. Калькулятор рациональных чисел /ratio\n\nЧто будем делать? \n\nТак же все мои возможности есть в "Меню"')


@bot.message_handler(commands=['ratio'])
def calc_ratio(message):
    global calc_ratio
    if message.text == "/ratio":
        calc_ratio = True
        bot.send_message(message.from_user.id, '0', reply_markup=keyboard)
        bot.send_message(message.chat.id,
                         'Для переключения между режимами работы калькулятора воспользуйтесь кнопкой "Меню"')
    else:
        bot.send_message(message.from_user.id, value, reply_markup=keyboard)
        calc_ratio = False


@bot.message_handler(commands=['complex'])
def calc_complex(message):
    if message.text == "/complex":
        bot.send_message(message.chat.id, 'Нужна ли справка по комплексным числам? /yes или /no: ')


@bot.message_handler(commands=['yes'])
def calc_complex(message):
    if message.text == "/yes":
        bot.send_message(message.chat.id,
                         'Комплексные числа — числа вида a + bj,где a, b — вещественные числа, Действия с '
                         'комплексными числами: пару комплексных чисел можно суммировать и вычитать.Это просто, '
                         'они работают подобно двумерным векторам на плоскости. Комплексные числа можно умножать и '
                         'делить. Комплексные числа можно сравнивать на равенство и неравенство (== или !=).Но нельзя '
                         'к ним применять знаки больше, меньше (< или >).\n\n/continue')


@bot.message_handler(commands=['no', 'continue'])  # основной блок для вычисления комплексных чисел
def calc_complex(message):
    if message.text == "/no" or message.text == "/continue":
        enter_first_complex(message)


@bot.message_handler(content_types='text')
def enter_first_complex(message):
    global x, y, calc_complex, act
    calc_complex = True
    act = bot.send_message(message.chat.id,
                           'Введите выражение с комплексными числами в формате \n(a+bj)+(c+dj),\n где вместо знака '
                           'сложения может быть любое из доступных действий (+, -, *, /): ')  # вводим выражение
    bot.register_next_step_handler(act, action_with_complex_numbers)
    calc_complex = False

def action_with_complex_numbers(message):
    bot.send_message(message.chat.id,'Результат:')
    bot.send_message(message.chat.id, eval(message.text))
    bot.send_message(message.chat.id,'\nДля переключения между режимами работы калькулятора воспользуйтесь кнопкой "Меню"')
    

@bot.callback_query_handler(func=lambda call: True)
def callback_func(query):
    global value, old_value
    data = query.data

    if data == 'no':
        pass
    elif data == 'c':
        value = ''
    elif data == '<=':
        if value != '':
            value = value[:len(value) - 1]
    elif data == '=':
        try:
            value = str(eval(value))
        except:
            value = 'Ошибка!'
    else:
        value += data

    if (value != old_value and value != '') or ('0' != old_value and value == ''):
        if value == '':
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text='0',
                                  reply_markup=keyboard)
            old_value = '0'
        else:
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text=value,
                                  reply_markup=keyboard)
            old_value = value

    old_value = value
    if value == 'Ошибка!': value = ''


bot.polling()
