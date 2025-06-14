from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
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
    chat_id = message.chat.id
    await message.answer_dice(emoji='🎲', reply_markup=ReplyKeyboardRemove())
    lang = session.query(User.lang).filter(chat_id == User.chat_id).scalar()
    await message.answer(_("Biror tilni tanlang:"),
                         reply_markup=languages_inline_btns(lang=lang))


@menu_router.callback_query(F.data.in_({'uz', 'ru', 'en'}))
async def language_callback_data_handler(call: CallbackQuery, bot: Bot):
    chat_id = call.message.chat.id

    if call.message.text != _("Biror tilni tanlang:", locale=call.data):
        User.update(session, chat_id=chat_id, lang=call.data)
        await call.answer(_("Til {lang} ga o`zgardi!", locale=call.data).format(lang=call.data))
        await call.message.edit_text(_("Biror tilni tanlang:", locale=call.data),
                                     reply_markup=languages_inline_btns(lang=call.data))
    else:
        await call.answer(_("Siz avval bu tilni tanlagansiz!").format(lang=call.data))
