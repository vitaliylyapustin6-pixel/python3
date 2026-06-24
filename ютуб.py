import os
import asyncio
from aiogram import Bot,Dispatcher,types,F
from gtts import gTTS
from aiogram.filters import CommandStart,StateFilter
from aiogram.types import FSInputFile
from dotenv import load_dotenv
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import (
    State,
    StatesGroup,)
from aiogram.utils.keyboard import InlineKeyboardBuilder

load_dotenv()
boot = os.getenv("TOKEN")
bot = Bot(token=boot)

dp = Dispatcher()

class VoiceOrder(StatesGroup):
    b = State()
    b1 = State()

@dp.message(CommandStart())
async def start(message:types.Message,state:FSMContext):
    await state.clear()
    f = FSInputFile("images.jpeg")
    ff = f"Привет {message.from_user.first_name}.\nTы сможешь писать текст,\nи он будет озвучиваться."
    await message.answer_photo(photo=f,caption=ff)

    await state.set_state(VoiceOrder.b)
@dp.message(VoiceOrder.b)
async def b2_3(message:types.Message,state:FSMContext):
    bb = InlineKeyboardBuilder()
    bb.add(
    types.InlineKeyboardButton(text="ru",callback_data="la_ru"),
    types.InlineKeyboardButton(text="en",callback_data="la_en")
    )
    await state.update_data(bb=message.text)
    await message.answer("мы записаои твой текст)",reply_markup=bb.as_markup())
    await state.set_state(VoiceOrder.b1)
@dp.message(VoiceOrder.b1)
async def b3(message:types.Message,state:FSMContext):

    v = message.text.lower().strip()

    data = await state.get_data()
    user_text = data.get("m")

    filee = f"vv_{message.from_user.id}.mp3"
    tts = gTTS(text=user_text,lang=v,slow=False)
    tts.save(filee)
    await message.answer_voice(FSInputFile(filee))
    if os.path.exists(filee):
        os.remove(filee)



    await state.clear()

async def main():
    await dp.start_polling(bot) 
if __name__ == "__main__":
    asyncio.run(main())