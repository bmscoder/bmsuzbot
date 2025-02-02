from aiogram import types, Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.utils.markdown import hcode

from tgbot.filters.chat_type import ChatTypeFilter

echo_router = Router()
echo_router.message.filter(
    ChatTypeFilter(chat_type=["private"])
)


@echo_router.message(F.text, StateFilter(None))
async def bot_echo(message: types.Message):
    text = [message.text]

    await message.answer("\n".join(text))


@echo_router.message(F.text)
async def bot_echo_all(message: types.Message, state: FSMContext):
    state_name = await state.get_state()
    text = [
        hcode(message.text),
    ]
    await message.answer("\n".join(text))
