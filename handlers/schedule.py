from aiogram import Router, types, F
from aiogram.types import FSInputFile
from pathlib import Path

router = Router()

from .keyboards.get_schedule_info import get_schedule_keyboard

IMAGES_DIR = Path(__file__).parent.resolve().joinpath('images')

print(IMAGES_DIR)  

@router.message(F.text == "Понедельник")
async def show_monday_schedule(message: types.Message):
    image_path = IMAGES_DIR / 'file1.jpg'  
    # C:\python\lessons-app\handlers\images\file1.jpg
    if image_path.is_file():
        await message.answer_photo(
            photo=FSInputFile(image_path),
            caption="Расписание на понедельник",
            reply_markup=get_schedule_keyboard()
        )
    else:
        await message.reply("Фото не найдено!")

@router.message(F.text == "Вторник")
async def show_monday_schedule(message: types.Message):
    image_path = IMAGES_DIR / 'file2.jpg'  
    if image_path.is_file():
        await message.answer_photo(
            photo=FSInputFile(image_path),
            caption="Расписание на вторник",
            reply_markup=get_schedule_keyboard()
        )
    else:
        await message.reply("Фото не найдено!")

@router.message(F.text == "Среда")
async def show_monday_schedule(message: types.Message):
    image_path = IMAGES_DIR / 'file3.jpg'  
    if image_path.is_file():
        await message.answer_photo(
            photo=FSInputFile(image_path),
            caption="Расписание на среду",
            reply_markup=get_schedule_keyboard()
        )
    else:
        await message.reply("Фото не найдено!")

@router.message(F.text == "Четверг")
async def show_monday_schedule(message: types.Message):
    image_path = IMAGES_DIR / 'file4.jpg'  
    if image_path.is_file():
        await message.answer_photo(
            photo=FSInputFile(image_path),
            caption="Расписание на четверг",
            reply_markup=get_schedule_keyboard()
        )
    else:
        await message.reply("Фото не найдено!")

@router.message(F.text == "Пятница")
async def show_monday_schedule(message: types.Message): 
    image_path = IMAGES_DIR / 'file5.jpg'  
    if image_path.is_file():
        await message.answer_photo(
            photo=FSInputFile(image_path),
            caption="Расписание на пятницу",
            reply_markup=get_schedule_keyboard()
        )
    else:
        await message.reply("Фото не найдено!")



