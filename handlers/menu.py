from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.utils.i18n import gettext as _
from aiogram.utils.i18n import lazy_gettext as __

from keyboards.inline.button import languages_inline_btns
from utils.db.database import User, session

menu_router = Router()


@menu_router.message(F.text == __('Testlar'))
async def test_handler(message: Message):
    await message.answer(_("Barcha testlar"))


@menu_router.message(F.text == __('Natijalar'))
async def test_handler(message: Message):
    await message.answer(_("Barcha Natijalar"))


@menu_router.message(F.text == __('Tilni o`zgartirish'))
async def test_handler(message: Message):
    await message.answer(_("Biror tilni tanlang:"),
                         reply_markup=languages_inline_btns())


@menu_router.callback_query(F.data.in_({'uz', 'ru', 'en'}))
async def language_callback_data_handler(call: CallbackQuery):
    chat_id = call.message.chat.id
    User.update(session, chat_id=chat_id, lang=call.data)
    await call.answer(_("Til {lang} ga o`zgardi!").format(lang=call.data))
