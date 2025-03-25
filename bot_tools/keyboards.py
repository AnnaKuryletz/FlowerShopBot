from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)


def get_main_menu():
    """Главное меню с кнопками (InlineKeyboard)."""
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🎂День рождения", callback_data="birth_day")],
            [InlineKeyboardButton(text="💍Свадьба",callback_data="wedding_day")],
            [InlineKeyboardButton(text="🏫В школу", callback_data="into_school")],
            [InlineKeyboardButton(text="❤️Без повода", callback_data="no_reason")],
            [InlineKeyboardButton(text="✍🏻Другой повод", callback_data="another_reason")]
        ]
    )
