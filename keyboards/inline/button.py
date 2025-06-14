from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.utils.i18n import gettext as _


def languages_inline_btns(lang):
    ikb = InlineKeyboardBuilder()
    langs = [(_("O'zbek", locale=lang), 'uz'), (_("Rus", locale=lang), 'ru'), (_("Ingliz", locale=lang), 'en')]

    for lang_txt, lang_callback_data in langs:
        ikb.button(text=lang_txt, callback_data=lang_callback_data)

    ikb.adjust(2)
    return ikb.as_markup()
