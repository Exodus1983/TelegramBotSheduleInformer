from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/Информация')
b2 = KeyboardButton('/Расписание')


kb_client_start = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client_start.row(b1, b2)
