import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from app.handlers import router
from dotenv import load_dotenv


async def main():
    logging.basicConfig(level=logging.INFO)
    load_dotenv()
    token = os.getenv('TOKEN')
    bot = Bot(token=token)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')
