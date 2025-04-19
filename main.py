from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message
from aiogram.enums import ParseMode

import logging
import asyncio
from cfg import bot_token
from keyboards.bot_keyboard import create_kb1, create_kb2, create_kb3
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

uslugi = ["Мужская стрижка", "Fade", "Детская стрижка", "Стрижка бороды"]
menu = ['Инфо', 'Запись📅']

bot = Bot(token=bot_token)
dp = Dispatcher()

class Ms(StatesGroup):
    menu = State()
    usluga = State()
    data = State()
    vremya = State()
    podt = State()

@dp.message(Command("start"))
async def send_welcome(message: Message, state: FSMContext):
    await message.answer("Привет", reply_markup=create_kb1)
    await state.set_state(Ms.menu)

# @dp.message(Ms.menu, F.text.in_(menu))
# async def send_info(message: Message):
#     await message.answer("Инфо..", reply_markup=create_kb2)
#     await state.set_state(Ms.)

@dp.message(F.text=='Назад')
async def send_nazad(message: Message):
    await message.reply("Привет", reply_markup=create_kb1)


@dp.message(F.text=='Запись📅')
async def send_zapis(message: Message):
    await message.reply("Выберите услугу \nМужская стрижка - 2400р \nFade - 1800р\nДетская стрижка - 1700р\nСтрижка бороды - 2000р", reply_markup=create_kb3)
    state.set_state(Ms.usluga)


@dp.message(F.text in uslugi)
async def send_data(message: Message):
    await message.reply("2 2 2")

if __name__ == '__main__':
    dp.run_polling(bot, skip_updates=True)