from aiogram import Router, types, F
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

uslugi = ["Стрижка", "Бритье", "Кондиционирование"]
day = ["07.04.25", "08.04.25", "09.04.25", "10.04.25"]
time = ["17:00", "18:00", "19:00", "20:00"]