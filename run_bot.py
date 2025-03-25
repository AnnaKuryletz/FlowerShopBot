import os
import django

# Устанавливаем настройки Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "flower_bot.settings")

# Инициализируем Django
django.setup()

import asyncio
from aiogram import Bot, Dispatcher

# Импортируйте ваш бот и другие компоненты только после настройки Django
TOKEN = "7795792004:AAHtjant11V7Nq10kbYh91WxyDozle5qKo0"


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()


    print("Бот запущен!")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())