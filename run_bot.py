import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "flower_bot.settings")

django.setup()

from bot_tools.handlers import router
import asyncio
from aiogram import Bot, Dispatcher


TOKEN = "7795792004:AAHtjant11V7Nq10kbYh91WxyDozle5qKo0"


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    dp.include_router(router)
    print("Бот запущен!")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
