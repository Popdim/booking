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
