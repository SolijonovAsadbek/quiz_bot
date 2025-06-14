from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.utils.i18n import gettext as _


def languages_inline_btns():
    ikb = InlineKeyboardBuilder()
    langs = [(_("O'zbek"), 'uz'), (_("Rus"), 'ru'), (_("Ingliz"), 'en')]

    for lang_txt, lang_callback_data in langs:
        ikb.button(text=lang_txt, callback_data=lang_callback_data)

    ikb.adjust(2)
    return ikb.as_markup()
