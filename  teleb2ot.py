import asyncio
import os
import sys
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv
import aiosqlite

logging.basicConfig(level=logging.INFO)

# Загружаем переменные окружения
load_dotenv()
bott = os.getenv("TOKEN")
bot = Bot(token=bott)
dp = Dispatcher()

@dp.message(F.text == "/add_book")
async def add_book_handler(message: types.Message):
    print("Хендлер /add_book сработал!", flush=True)
    username = message.from_user.username
    async with aiosqlite.connect("b.db") as conn:
        async with conn.cursor() as cursor:
            await cursor.execute("DROP TABLE IF EXISTS boook")
            await cursor.execute("CREATE TABLE boook(name TEXT UNIQUE)")
            await cursor.execute("INSERT OR IGNORE INTO boook(name)VALUES(?)",(username,))
            await conn.commit()
            await cursor.execute("SELECT name FROM boook")
            rows = await cursor.fetchall()
            print(rows)

@dp.message(CommandStart())
async def start_commanddd(message: types.Message):
    # Используем InlineKeyboardButton напрямую для читаемости
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Статистика", callback_data="status_callback")]
    ])
    await message.answer("Привет! Выберите действие:", reply_markup=kb)

# Переименовали функцию в status_callback_handler, чтобы избежать конфликтов с Pydantic
@dp.callback_query(F.data == "status_callback")
async def status_callback_handler(callback: types.CallbackQuery):
    await callback.answer() # Обязательно гасим часики на кнопке
    await callback.message.edit_text("Привет! Это ваша статистика.")

async def main():
    await dp.start_polling(bot, skip_updates=True)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот остановлен.", flush=True)
