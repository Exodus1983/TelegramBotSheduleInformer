from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('Все')
b2 = KeyboardButton('Звук')
b3 = KeyboardButton('Свет')
b4 = KeyboardButton('Экран')


kb_client_group = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client_group.row(b1, b2, b3, b4)
