from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

import database.database as db

from tgbot.filters.chat_type import ChatTypeFilter
from tgbot.filters.admin import AdminFilter
from tgbot.keyboards.inline import main_menu

admin_router = Router()
admin_router.message.filter(
    ChatTypeFilter(chat_type=["private"])
)
admin_router.message.filter(AdminFilter())

@admin_router.message(CommandStart())
async def user_start(message: Message):

    db.cur.execute(f"SELECT * FROM users WHERE chat_id = {message.from_user.id}")
    row = db.cur.fetchone()

    if not row:
        await message.answer(f"✋ Assalomu alaykum, botga xush kelibsiz!", reply_markup=main_menu())
        insert = ("""INSERT INTO users (chat_id, status) VALUES (?, ?)""")
        
        insert_data = (message.from_user.id, "admin")

        db.cur.execute(insert, insert_data)
        
        db.db.commit()
    else:
        await message.answer(f"🖥 Asosiy menyudasiz", reply_markup=main_menu())
