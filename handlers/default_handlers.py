from aiogram import Router
from aiogram.filters import Command 
from aiogram import types, F 

router = Router()

from .keyboards.get_main_keyboard import get_main_keyboard
from .keyboards.get_schedule_info import get_schedule_keyboard
from .keyboards.get_subjects import get_subjects_keyboard

from .assets.assets_for_default_keyboard import start,settings,schedule,grades,homework,help,backward

@router.message(Command(start))
async def cmd_start(message: types.Message):
    """
    Обрабатывает команду /start
    message: объект сообщения от пользователя
    """
    await message.answer(
        "📚 Добро пожаловать в электронный школьный дневник!\n\n"
        "Я помогу вам следить за:\n"
        "• Расписанием уроков\n"
        "• Домашними заданиями\n"
        "• Оценками\n"
        "• Личными заметками\n\n"
        "Выберите действие на клавиатуре ниже:",
        reply_markup = get_main_keyboard()
    )
    await message.delete() 

@router.message(F.text == settings)
async def show_settings(message:types.Message):
    await message.answer("Доступные настройки")
    await message.delete() 

@router.message(F.text == schedule)
async def show_schedule_menu(message: types.Message):
    await message.answer(
        "Выберите день недели:",
        reply_markup=get_schedule_keyboard()
    )
    await message.delete() 

@router.message(F.text == grades)
async def show_grades(message: types.Message):
    """
    Показывает оценки по предметам
    """
    grades_text = (
        "*📊 Ваши оценки:*\n\n"
        "• *Математика:* 5, 4, 5\n"
        "   *Средний балл:* 4.67\n\n"
        "• *Физика:* 4, 5, 4\n"
        "   *Средний балл:* 4.33\n\n"
        "• *Литература:* 5, 5, 5\n"
        "   *Средний балл:* 5.00\n\n"
        "• *История:* 4, 4, 3\n"
        "   *Средний балл:* 3.67\n\n"
        "📈 *Общий средний балл:* 4.42"
    )
    
    await message.answer(
        grades_text,
        parse_mode="Markdown",
        reply_markup=get_main_keyboard()
    )
    await message.delete() 

@router.message(F.text == homework)
async def show_homework_menu(message: types.Message):
    """
    Показывает меню домашних заданий
    """
    homework_text = (
        "*📚 Домашнее задание на завтра:*\n\n"
        "1. *Математика:*\n"
        "   - №154, 155 (стр. 45)\n"
        "   - Подготовить доклад\n\n"
        "2. *Литература:*\n"
        "   - Прочитать главу 5\n"
        "   - Ответить на вопросы\n\n"
        "3. *Физика:*\n"
        "   - Лабораторная работа №3\n\n"
        "⏰ *Срок сдачи:* до пятницы"
    )
    
    await message.answer(
        homework_text,
        parse_mode="Markdown",
        reply_markup=get_subjects_keyboard()
    )
    await message.delete() 

@router.message(F.text == help)
async def show_help(message: types.Message):
    """
    Показывает справку по использованию бота
    """
    help_text = (
        "<b>ℹ️ Справка по использованию дневника:</b>\n\n"
        "📅 <b>Расписание</b> - просмотр уроков по дням\n"
        "📚 <b>Домашнее задание</b> - задания по предметам\n"
        "📊 <b>Оценки</b> - ваши текущие оценки\n"
        "📝 <b>Добавить заметку</b> - создать напоминание\n\n"
        "<b>Команды:</b>\n"
        "/start - перезапустить бота\n"
        "/help - эта справка\n\n"
        "<b>Контакты:</b>\n"
        "Вопросы и предложения: @ваш_логин"
    )
    
    await message.answer(
        help_text,
        parse_mode="HTML"
    )
    await message.delete() 

@router.message(F.text == backward)
async def go_back(message: types.Message):
    """
    Возвращает к главному меню
    """
    await message.answer(
        "Главное меню:",
        reply_markup=get_main_keyboard()
    )
    await message.delete()   

@router.message()
async def handle_unknown(message: types.Message):
    """
    Обрабатывает неизвестные сообщения
    """
    await message.answer(
        "Я не понял ваш запрос 😕\n"
        "Используйте кнопки ниже или команду /help",
        reply_markup=get_main_keyboard()
    )