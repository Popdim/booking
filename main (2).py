from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message, CallbackQuery
from aiogram.enums import ParseMode
import logging
import asyncio
from cfg import bot_token
from keyboards.bot_keyboard import create_kb1, create_kb2, create_kb3, create_kb4
from keyboards.bot_keyboard_inline import get_data_kb
from utilits.get_data import get_dates

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

menu = ['Инфо', 'Запись📅']
uslugi = ["Мужская стрижка", "Fade", "Детская стрижка", "Стрижка бороды"]
danet = ['Да', 'Нет']


bot = Bot(token=bot_token)
dp = Dispatcher()


class Ms(StatesGroup):
    usluga = State()
    data = State()
    vremya = State()
    podt = State()
    finish = State()


@dp.message(Command("start"))
async def send_welcome(message: Message, state: FSMContext):
    await message.answer("Привет", reply_markup=create_kb1)
    await state.set_state(Ms.usluga)

@dp.message(Ms.usluga, F.text == 'Инфо')
async def send_info(message: Message, state: FSMContext):
    await message.reply(
        "С пощощью этого боте вы сможете записаться на стрижку в нашем барбершопе. "
        "\nЕсли нашли ошибку в работе телеграм бота - пишите сюда > @geekami")


@dp.message(Ms.usluga, F.text == 'Запись📅')
async def send_zapis(message: Message, state: FSMContext):
    await message.reply(
        "Выберите услугу \nМужская стрижка - 2400р \nFade - 1800р\nДетская стрижка - 1700р\nСтрижка бороды - 2000р",
        reply_markup=create_kb3)
    await state.set_state(Ms.data)

@dp.message(Ms.usluga)
async def incorrect_zapis(message: Message):
    await message.answer("Ты не выбрал действие! Нажми кнопку", reply_markup=create_kb3)

@dp.message(Ms.data)
# async def send_data(callback_query: CallbackQuery, state: FSMContext):
async def send_data(message: Message, state: FSMContext):
    k = get_dates()
    keyboard = get_data_kb(k)
    # await callback_query.message.answer(
    #     "Выберите дату", reply_markup=keyboard)
    await message.answer(
        "Выберите дату", reply_markup=keyboard)
    await state.set_state(Ms.vremya)


@dp.message(Ms.data)
async def incorrect_data(message: Message):
    await message.answer("Ты не указал время!")

# @dp.message(Ms.vremya)
@dp.callback_query(Ms.vremya)
async def send_vremya(callback_query: CallbackQuery, state: FSMContext):
    select_data = callback_query.data.split(':')[1]
    print(select_data)
    await message.reply(
        "Напишите время в формате 18:00")
    await state.set_state(Ms.podt)

@dp.message(Ms.vremya)
async def incorrect_vreamya(message: Message):
    await message.answer("Ты неправильно выбрал время!")

@dp.message(Ms.podt)
async def approve(message: Message, state: FSMContext):
    await message.answer("... Подтвердите запись", reply_markup=create_kb4)
    await state.set_state(Ms.finish)

@dp.message(Ms.podt)
async def incorrect_approve(message: Message):
    await message.answer("Ты не выбрал действие! Нажми кнопку", reply_markup=create_kb1)

@dp.message(Ms.finish, F.text == 'Да')
async def aprove(message: Message, state: FSMContext):
    await message.answer("Вы подтвердили запись", reply_markup=create_kb1)
    await state.set_state(Ms.usluga)

@dp.message(Ms.finish, F.text == 'Нет')
async def aprove(message: Message, state: FSMContext):
    await message.answer("Вы не подтвердили запись", reply_markup=create_kb1)
    await state.clear(Ms.usluga)




if __name__ == '__main__':
    dp.run_polling(bot, skip_updates=True)
