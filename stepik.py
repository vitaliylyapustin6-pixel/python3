from aiogram import Bot,Dispatcher,types,F
from dotenv import load_dotenv
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import (
    State,
    StatesGroup,)
import os
import asyncio
from aiogram.filters import CommandStart
import time
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,InlineKeyboardMarkup


load_dotenv()
bott = os.getenv("TOKEN")
bot = Bot(token=bott)
dp = Dispatcher()


@dp.message()
async def start(message:types.Message):
    #print(message.photo[-1].file_id)
    await message.answer_photo(photo="AgACAgIAAxkBAAIOjmo5RCG3D66IZe2NTcJQsCOyr0MwAAJfGmsbgK7QSV569BKB5HZXAQADAgADbQADPAQ",caption="Привет")
async def main():
    await dp.start_polling(bot) 
if __name__ == "__main__":
    asyncio.run(main())