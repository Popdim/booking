from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
def get_data_kb(dates):
    button = []
    row = []
    for i, date in enumerate(dates):
        callback_data = f"data:{date}"
        row.append(InlineKeyboardButton(text=date, callback_data=callback_data))
        if len(row) == 2 or i == len(dates)-1:
            button.append(row)
            row = []
    keyboard = InlineKeyboardMarkup(inline_keyboard=button)
    return keyboard

def get_time_kb(times):
    button = []
    row = []
    for i, time in enumerate(times):
        callback_data = f"time:{time}"
        row.append(InlineKeyboardButton(text=time, callback_data=callback_data))
        if len(row) == 2 or i == len(time)-1:
            button.append(row)
            row = []
    keyboard = InlineKeyboardMarkup(inline_keyboard=button)
    return keyboard

def get_yesno():
    row = []
    row.append(InlineKeyboardButton(text="Да", callback_data="yesno:Да"))
    row.append(InlineKeyboardButton(text="Нет", callback_data="yesno:Нет"))
    button = [row]
    keyboard = InlineKeyboardMarkup(inline_keyboard=button)
    return keyboard