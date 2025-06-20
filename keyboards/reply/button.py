from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.i18n import gettext as _


def confirm_button():
    keyboards = [

        [
            KeyboardButton(text=_('Ha')),
            KeyboardButton(text=_('Yo`q'))
        ],

    ]
    kb = ReplyKeyboardMarkup(keyboard=keyboards,
                             resize_keyboard=True,
                             input_field_placeholder=_('Tugamadan foydalaning!'))
    return kb


def share_contact():
    keyboards = [
        [
            KeyboardButton(text=_('📲 Telefon ulashish'), request_contact=True),
        ]

    ]
    kb = ReplyKeyboardMarkup(keyboard=keyboards,
                             resize_keyboard=True,
                             input_field_placeholder=_('Tugamadan foydalaning!'))
    return kb


def menu(lang):
    keyboards = [
        [
            KeyboardButton(text=_("Testlar", locale=lang)),
            KeyboardButton(text=_("Natijalar", locale=lang)),
        ],
        [
            KeyboardButton(text=_("Tilni o`zgartirish", locale=lang)),
        ]
    ]
    kb = ReplyKeyboardMarkup(keyboard=keyboards, resize_keyboard=True)
    return kb
