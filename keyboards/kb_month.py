from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('Январь')
b2 = KeyboardButton('Февраль')
b3 = KeyboardButton('Март')
b4 = KeyboardButton('Апрель')
b5 = KeyboardButton('Май')
b6 = KeyboardButton('Июнь')
b7 = KeyboardButton('Июль')
b8 = KeyboardButton('Август')
b9 = KeyboardButton('Сентябрь')
b10 = KeyboardButton('Октябрь')
b11 = KeyboardButton('Ноябрь')
b12 = KeyboardButton('Декабрь')

kb_client_month = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client_month.row(b1, b2, b3).row(b4, b5, b6).row(b7, b8, b9).row(b10, b11, b12)
