from aiogram.types import ReplyKeyboardMarkup, KeyboardButton  

from ..assets.assets_for_default_keyboard import schedule,homework,help

def get_main_keyboard():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=schedule), 
                KeyboardButton(text=homework)
            ],
            [
                KeyboardButton(text="📊 Оценки"),
                KeyboardButton(text="📝 Добавить заметку")
            ],
            [
                KeyboardButton(text=help),
                KeyboardButton(text="⚙️ Настройки")
            ]
        ],
        resize_keyboard=True,
        one_time_keyboard=False
    )
    return keyboard
