from aiogram.utils.i18n import get_i18n


async def i18n_current_locale_lang():
    lang = get_i18n().current_locale
    return lang
