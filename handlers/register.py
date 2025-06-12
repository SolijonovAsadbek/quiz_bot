import re
from aiogram import Router, F, html
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext

from keyboards.reply.button import confirm_button, share_contact
from states.register import RegisterState
from utils.db.database import User, session
from utils.helper import check_register

register_router = Router()


@register_router.message(Command('register'))
@check_register
async def register_start(message: Message, state: FSMContext):
    await message.answer('To`liq ismingiz: ')
    # 1-qadam
    await state.set_state(RegisterState.fullname)


@register_router.message(RegisterState.fullname)
async def fullname_handler(message: Message, state: FSMContext):
    fullname = message.text
    # filter
    await state.update_data(fullname=fullname)
    await message.answer('Telefon raqamingizni kiriting!', reply_markup=share_contact())
    await state.set_state(RegisterState.phone)


@register_router.message(RegisterState.phone)
async def phone_handler(message: Message, state: FSMContext):
    phone_number = message.text  # filter qiling

    if message.contact:
        phone_number = message.contact.phone_number

    await state.update_data(phone=phone_number)

    datas = await state.get_data()
    fullname = datas.get('fullname')
    phone = phone_number
    user_chat_id = message.from_user.id
    user_data = (f"To'liq ism: {html.bold(fullname)}\n"
                 f"Telefon: {html.bold(phone)}\n"
                 f"Chat ID: {html.bold(user_chat_id)}\n")
    await message.answer(f'Ma`lumotlaringizni tasdiqlaysizmi?\n\n{user_data}', reply_markup=confirm_button())
    await state.set_state(RegisterState.confirm)


@register_router.message(RegisterState.confirm)
async def confirm_handler(message: Message, state: FSMContext):
    confirm = message.text

    if confirm.casefold() == 'ha':
        datas = await state.get_data()
        fullname = datas.get('fullname')
        phone = datas.get('phone')
        user_chat_id = message.from_user.id

        # database saqlashga tayyorlash
        user = User(fullname=fullname, phone=phone, chat_id=user_chat_id)
        user.save(session)

        await message.answer('Botdan foydalanishga xush kelibsiz!', reply_markup=ReplyKeyboardRemove())
        await state.clear()

    # Yoq: /register ga qaytaramiz!
    elif confirm.casefold() == 'yo`q':
        await message.answer('Qayta ro`yxatdan o`tish uchun  👉 /register kamandasini bosing',
                             reply_markup=ReplyKeyboardRemove())
        await state.clear()
    else:
        await message.reply('Ha yoki Yo`q bilan tasdiqlang iltimos!')
