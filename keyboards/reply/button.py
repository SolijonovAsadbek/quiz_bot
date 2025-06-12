from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def confirm_button():
    keyboards = [

        [
            KeyboardButton(text='Ha'),
            KeyboardButton(text='Yo`q')
        ],

    ]
    kb = ReplyKeyboardMarkup(keyboard=keyboards,
                             resize_keyboard=True,
                             input_field_placeholder='Tugamadan foydalaning!')
    return kb


def share_contact():
    keyboards = [
        [
            KeyboardButton(text='📲 Telefon ulashish', request_contact=True),
        ]

    ]
    kb = ReplyKeyboardMarkup(keyboard=keyboards,
                             resize_keyboard=True,
                             input_field_placeholder='Tugamadan foydalaning!')
    return kb
