from aiogram import Router, html
from aiogram.filters import CommandStart
from aiogram.types import Message

from utils.db.database import User, session
from utils.helper import check_register

start_router = Router()


@start_router.message(CommandStart())
@check_register
async def command_start_handler(message: Message):
    await message.answer(f"Salom, {html.bold(message.from_user.full_name)}!\n\n"
                         f"Ro'yxatdan o'tish uchun  👉 /register kamandasini bosing")
