from aiogram import Router
from aiogram.types import CallbackQuery

from callbacks.callback_datas import CategoryCallbackData, BackCallBackData, Level, SubCategoryCallbackData
from keyboards.inline.button import sub_category_kb_builder, category_kb_builder, quiz_kb_builder
from utils.db.database import session
from utils.helper.db import get_all_subcategory_by_id, get_all_category, get_all_quizs_by_sub_id
from aiogram.utils.i18n import gettext as _

from utils.helper.i18n_helper import i18n_current_locale_lang

callbacks_router = Router()


@callbacks_router.callback_query(CategoryCallbackData.filter())
async def category_handler(call: CallbackQuery, callback_data: CategoryCallbackData):
    subcategories = await get_all_subcategory_by_id(session, category_id=callback_data.id)
    lang = await i18n_current_locale_lang()
    kbs = sub_category_kb_builder(datas=subcategories, lang=lang)
    return call.message.edit_text(_("Subkategoriyalar"), reply_markup=kbs)


@callbacks_router.callback_query(SubCategoryCallbackData.filter())
async def sub_category_handler(call: CallbackQuery, callback_data: SubCategoryCallbackData):
    quizzes = await get_all_quizs_by_sub_id(session, subcategory_id=callback_data.id)
    lang = await i18n_current_locale_lang()
    kbs = quiz_kb_builder(quizzes, lang=lang)
    await call.message.edit_text(_("Barcha testlar"), reply_markup=kbs)


@callbacks_router.callback_query(BackCallBackData.filter())
async def back_level(call: CallbackQuery, callback_data: BackCallBackData):
    lang = await i18n_current_locale_lang()
    if callback_data.level == Level.CATEGORY:
        categories = await get_all_category(session)

        kbs = category_kb_builder(categories, lang=lang)
        await call.message.edit_text(_("Barcha testlar"), reply_markup=kbs)

    if callback_data.level == Level.SUBCATEGORY:
        subcategories = await get_all_subcategory_by_id(session, category_id=callback_data.category_id)
        kbs = sub_category_kb_builder(datas=subcategories, lang=lang)
        return call.message.edit_text(_("Subkategoriyalar"), reply_markup=kbs)
