from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
b1 = KeyboardButton(text="Инфо")
b2 = KeyboardButton(text="Запись📅")
b3 = KeyboardButton(text="Назад")
b4 = KeyboardButton(text="Мужская стрижка")
b5 = KeyboardButton(text="Fade")
b6 = KeyboardButton(text="Детская стрижка")
b7 = KeyboardButton(text="Стрижка бороды")
b8 = KeyboardButton(text="Да")
b9 = KeyboardButton(text="Нет")
b10 = KeyboardButton(text="Отменить")

kb1 = [[b1, b2]]
kb2 = [[b3]]
kb3 = [[b4, b5, b6, b7, b10]]
kb4 = [[b8, b9]]

create_kb1 = ReplyKeyboardMarkup(keyboard=kb1, resize_keyboard=True)
create_kb2 = ReplyKeyboardMarkup(keyboard=kb2, resize_keyboard=True)
create_kb3 = ReplyKeyboardMarkup(keyboard=kb3, resize_keyboard=True)
create_kb4 = ReplyKeyboardMarkup(keyboard=kb4, resize_keyboard=True)

