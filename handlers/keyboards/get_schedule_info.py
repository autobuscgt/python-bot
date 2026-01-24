from aiogram.types import ReplyKeyboardMarkup, KeyboardButton  

def get_schedule_keyboard():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Понедельник")],
            [KeyboardButton(text="Вторник")],
            [KeyboardButton(text="Среда")],
            [KeyboardButton(text="Четверг")],
            [KeyboardButton(text="Пятница")],
            [KeyboardButton(text="↩️ Назад")]
        ],
        resize_keyboard=True
    )
    return keyboard
