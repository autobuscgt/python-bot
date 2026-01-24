from aiogram.types import ReplyKeyboardMarkup, KeyboardButton  

def get_subjects_keyboard():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Математика")],
            [KeyboardButton(text="Физика")],
            [KeyboardButton(text="Литература")],
            [KeyboardButton(text="История")],
            [KeyboardButton(text="↩️ Назад")]
        ],
        resize_keyboard=True
    )
    return keyboard