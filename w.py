from aiogram import Bot,Dispatcher,F,types
import asyncio
import os
from dotenv import load_dotenv
from translate import Translator
from aiogram.filters import CommandStart


load_dotenv()
Bot_token = os.getenv("TOKEN")
bot = Bot(token=Bot_token)
dp = Dispatcher()
t = Translator(from_lang="ru",to_lang="en")

@dp.message(CommandStart())
async def start(message:types.Message):
    await message.answer(f"""Привет {message.from_user.first_name},ты можешь переводить текст в этом боте)""")
    
@dp.message()
async def la(message:types.Message):
    tt = message.text
    ttt = t.translate(tt)
    await message.answer(ttt)




async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())