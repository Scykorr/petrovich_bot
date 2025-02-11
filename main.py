import asyncio
import logging

from aiogram import Bot, Dispatcher
from main_info.token import token
from app.handlers import router

async def main():
    logging.basicConfig(level=logging.INFO)

    bot = Bot(token=token)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')

