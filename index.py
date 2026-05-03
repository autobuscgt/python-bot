import asyncio  
import logging 
import os
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv


from handlers import subjects,notes,schedule,default_handlers
from config import token

logging.basicConfig(level=logging.INFO)

load_dotenv()

API_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def main():
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher()

    dp.include_router(subjects.router)
    dp.include_router(schedule.router)
    dp.include_router(notes.router)
    dp.include_router(default_handlers.router)

    print("🚀 Бот запускается...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())