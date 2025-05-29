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
from keyboards.bot_keyboard_inline import get_data_kb, get_time_kb, get_yesno
from utilits.get_data import get_dates, get_times

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

menu = ['Инфо', 'Запись📅']
uslugi = ["Мужская стрижка", "Fade", "Детская стрижка", "Стрижка бороды"]
danet = ['Да', 'Нет']

storage = MemoryStorage()

bot = Bot(token=bot_token)
dp = Dispatcher(storage=storage)


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
async def send_data(callback_query: CallbackQuery, state: FSMContext):
# async def send_data(message: Message, state: FSMContext):
    print(state.update_data(usluga=callback_query.text))
    user_temp=await state.get_data()
    print('65')
    print(user_temp)
    k = get_dates()
    ikeyb = get_data_kb(k)
    # await callback_query.message.answer(
    #     "Выберите дату", reply_markup=keyboard)
    print(ikeyb)
    await callback_query.answer(
        "Выберите дату", reply_markup=ikeyb)
    await state.set_state(Ms.vremya)



# @dp.message(Ms.data)
# async def incorrect_data(message: Message):
#     await message.answer("Ты не указал время!")

# F.data.startswith("data")
@dp.callback_query(F.data.startswith("data:"), Ms.vremya)
async def process_selected_time(callback: CallbackQuery, state: FSMContext):
    date_str = callback.data.split(":")[1]
    state.update_data(usdata=date_str)
    k = get_dates()
    ikeyb = get_time_kb(k)
    print(k)
    print(ikeyb)
    await callback.answer(f"Вы выбрали дату: {date_str}")
    await callback.message.answer(f"Теперь выберите время для {date_str}", reply_markup=ikeyb)

    # Сохраняем дату в состояние
    # await state.update_data(selected_date=date_str)
    await state.set_state(Ms.podt)
    print('*' * 50)
    print(f"Дата выбрана {date_str}")
    print('*' * 50)


@dp.callback_query(F.data.startswith("time:"), Ms.podt)
async def process_selected_yesno(callback: CallbackQuery, state: FSMContext):
    date_str = callback.data.split(":")[1]
    state.update_data(ustime=date_str)
    yn_kb = get_yesno()
    print("Xd")
    print(date_str)
    print(yn_kb)

    await callback.answer()  # Просто закрыть спиннер

    # Отправляем новое сообщение с клавиатурой
    hsm = await state.get_data()
    print(hsm)
    await bot.send_message(
        chat_id=callback.from_user.id,
        text=f"""Теперь подтвердите вашу запись
             {hsm['usluga']}-{hsm['usdata']}-{hsm['ustime']}""",
        reply_markup=yn_kb
    )
    await state.set_state(Ms.usluga)
    # await state.update_data(selected_date=date_str)
    # await state.set_state(Ms.finish)

#
# @dp.message(Ms.vremya)
# async def incorrect_vreamya(message: Message):
#     await message.answer("Ты неправильно выбрал время!")
#
# @dp.message(Ms.podt)
# async def approve(message: Message, state: FSMContext):
#     await message.answer("... Подтвердите запись", reply_markup=create_kb4)
#     await state.set_state(Ms.finish)
#
# @dp.message(Ms.podt)
# async def incorrect_approve(message: Message):
#     await message.answer("Ты не выбрал действие! Нажми кнопку", reply_markup=create_kb1)
#





if __name__ == '__main__':
    dp.run_polling(bot, skip_updates=True)
