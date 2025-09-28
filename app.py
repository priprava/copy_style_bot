from aiogram import Dispatcher, Bot, types
from config import BOT_TOKEN
from handlers.start import start_router 
from handlers.generate import generate_router
import asyncio, logging

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

async def startup():
    await bot.set_my_commands([
        types.BotCommand(command="start", description="запуск"),
        types.BotCommand(command="generate", description="сгенерировать"),
    ])
    dp.include_router(start_router)
    dp.include_router(generate_router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.DEBUG)
        asyncio.run(startup())
    except KeyboardInterrupt:
        logging.info("exit")