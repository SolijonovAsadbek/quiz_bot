from aiogram import Bot, Router
from aiogram.types import BotCommand
from aiogram.utils.i18n import gettext as _


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command='start', description='Botni ishga tushirish - '
                                                'Bot has started! - '
                                                'Бот запущен! '),
        BotCommand(command='help', description='Yordam - '
                                               'Help - '
                                               'Помощь'),
    ]
    await bot.set_my_commands(commands=commands)
