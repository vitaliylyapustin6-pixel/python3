from aiogram import Bot, Dispatcher, types, F
from dotenv import load_dotenv
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
import os
import asyncio
from aiogram.filters import CommandStart

load_dotenv()
bot = Bot(token=os.getenv("TOKEN"))
dp = Dispatcher()

class V(StatesGroup):
    name = State()
    age = State()
    da = State()

@dp.message(CommandStart())
async def start(message: types.Message, state: FSMContext):
    await message.answer(f'Привет {message.from_user.first_name}\nНапиши своё имя')
    await state.set_state(V.name)

@dp.message(V.name)
async def get_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer('Напиши свой возраст')
    await state.set_state(V.age)

@dp.message(V.age)
async def get_age(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    data = await state.get_data()
    await message.answer(f"Подтвердите данные:\nName: {data['name']}\nAge: {data['age']}\n\nда / нет")
    await state.set_state(V.da)

@dp.message(V.da, F.text.lower().strip() == "да")
async def confirm(message: types.Message, state: FSMContext):
    data = await state.get_data()
    await message.answer(f"Спасибо за покупку, {data['name']}!")
    await state.clear()

@dp.message(V.da, F.text.lower().strip() == "нет")
async def cancel(message: types.Message, state: FSMContext):
    await message.answer("До свидания!")
    await state.clear()

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
