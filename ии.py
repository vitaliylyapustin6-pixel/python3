from aiogram import Bot,types,F,Dispatcher
import asyncio
import os
from dotenv import load_dotenv
from aiogram.filters import CommandStart
from gtts import gTTS
from aiogram.types import FSInputFile
import wikipedia


load_dotenv()
bb = os.getenv("TOKEN")
bot = Bot(token=bb)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message:types.Message):
    await message.answer(f"hello {message.from_user.first_name}, этот бот умеет озвучивать твой текст")

@dp.message(F.text)
async def m(message:types.Message):
    try:
        wikipedia.set_lang("ru")

        r = wikipedia.summary(message.text,sentences=3)
        await message.answer(r)
    except:
        await message.answer("можете уточнить запрос")
async def main():
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())