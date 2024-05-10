from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types.web_app_info import WebAppInfo

def main_menu():
    keyboard = InlineKeyboardBuilder()

    keyboard.button(
        text="Veb ilovani ochish",
        web_app=WebAppInfo(url="https://bms.testai.uz/index.php")
    )

    return keyboard.as_markup()
