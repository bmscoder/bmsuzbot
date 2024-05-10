from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

# Ma'lumotlar bazasini db'ga import qilish, keyinchalik db yordamida jadvallar tuzish uchun
import database.database as db

from tgbot.filters.chat_type import ChatTypeFilter
from tgbot.keyboards.inline import main_menu


user_router = Router()
user_router.message.filter(
    ChatTypeFilter(chat_type=["private"])
)

@user_router.message(CommandStart())
async def user_start(message: Message):

    db.cur.execute(f"SELECT * FROM users WHERE chat_id = {message.from_user.id}")
    row = db.cur.fetchone()

    if not row:
        await message.answer(f"✋ Assalomu alaykum, botga xush kelibsiz!", reply_markup=main_menu())
        insert = ("""INSERT INTO users (chat_id, status) VALUES (?, ?)""")
        
        insert_data = (message.from_user.id, "oddiy")

        db.cur.execute(insert, insert_data)
        
        db.db.commit()
    else:
        await message.answer(f"🖥 Asosiy menyudasiz", reply_markup=main_menu())
