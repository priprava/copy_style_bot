from aiogram import types, Router
from aiogram.filters import CommandStart

start_router = Router()

@start_router.message(CommandStart())
async def start(message: types.Message):
    await message.answer("Привет! для генерации картинок используй /generate")
