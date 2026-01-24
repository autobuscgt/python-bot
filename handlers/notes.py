from aiogram import Router, types, F
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from .keyboards.get_main_keyboard import get_main_keyboard

router = Router()

class AddNote(StatesGroup):
    waiting_for_note = State()

@router.message(F.text == "📝 Добавить заметку")
async def start_add_note(message: types.Message, state: FSMContext):
    """
    Начинает процесс добавления заметки
    """ 
    await state.set_state(AddNote.waiting_for_note)
    
    await message.answer(
        "📝 *Добавление заметки*\n\n"
        "Напишите текст вашей заметки:\n"
        "(Например: 'Сдать доклад по математике до пятницы')",
        parse_mode="Markdown"
    )
    await message.delete() 

@router.message(AddNote.waiting_for_note)
async def save_note(message: types.Message, state: FSMContext):
    """
    Сохраняет заметку (в памяти, без БД)
    """
    note_text = message.text 
    
    await message.answer(
        f"✅ *Заметка сохранена!*\n\n"
        f"Содержание:\n"
        f"`{note_text}`\n\n",
        parse_mode="Markdown",
        reply_markup=get_main_keyboard()
    )
    await state.clear()