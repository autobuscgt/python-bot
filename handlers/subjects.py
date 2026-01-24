from aiogram import Router
from aiogram import types, F 

router = Router()

@router.message(F.text == "Математика")
async def show_math_homework(message: types.Message):
    """
    Показывает детали по математике
    """
    await message.answer(
        "*📐 Математика:*\n\n"
        "Задание:\n"
        "1. Решить задачи №154, 155 на странице 45\n"
        "2. Подготовить доклад на тему 'Теорема Пифагора'\n\n"
        "Требования:\n"
        "• Объем: 2-3 страницы\n"
        "• Сдать: до пятницы\n"
        "• Формат: электронный документ\n\n"
        "📌 *Консультация:* завтра после 3 урока",
        parse_mode="Markdown"
    )
    await message.delete() 
