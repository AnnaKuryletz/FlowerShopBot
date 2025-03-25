from aiogram import Router
from aiogram.filters import Command
from aiogram import types
from .keyboards import get_main_menu

router = Router()


@router.message(Command("start"))
async def send_welcome(message: types.Message):
    """Отправляет приветственное сообщение с кнопками согласия."""
    user_name = (
        message.from_user.username
        if message.from_user.username
        else message.from_user.first_name
    )
    text = f"Привет, {user_name} 🙋‍♀️! FlowerShop приветствует тебя. К какому событию готовимся? Выберите один из вариантов, либо укажите свой"
    await message.answer(text, reply_markup=get_main_menu())
