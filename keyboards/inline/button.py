from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.utils.i18n import gettext as _

from callbacks.callback_datas import CategoryCallbackData, SubCategoryCallbackData, BackCallBackData, Level, \
    QuizCallbackData


def languages_inline_btns(lang):
    ikb = InlineKeyboardBuilder()
    langs = [(_("O'zbek", locale=lang), 'uz'), (_("Rus", locale=lang), 'ru'), (_("Ingliz", locale=lang), 'en')]

    for lang_txt, lang_callback_data in langs:
        ikb.button(text=lang_txt, callback_data=lang_callback_data)

    ikb.adjust(2)
    return ikb.as_markup()


def category_kb_builder(datas, lang):
    ikb = InlineKeyboardBuilder()
    for category in datas:
        ikb.button(text=category.name[lang], callback_data=CategoryCallbackData(id=category.id).pack())
    ikb.adjust(2)
    return ikb.as_markup()


def sub_category_kb_builder(datas, lang):
    ikb = InlineKeyboardBuilder()
    for subcategory in datas:
        ikb.button(text=subcategory.name[lang],
                   callback_data=SubCategoryCallbackData(id=subcategory.id, category_id=subcategory.category_id).pack())

    ikb.button(text='⬅️', callback_data=BackCallBackData(level=Level.CATEGORY))
    ikb.adjust(2)
    return ikb.as_markup()


def quiz_kb_builder(datas, lang):
    ikb = InlineKeyboardBuilder()
    for quiz in datas:
        ikb.button(text=quiz.text[lang],
                   callback_data=QuizCallbackData(id=quiz.id, subcategory_id=quiz.subcategory_id).pack())  # category:10
    ikb.button(text='⬅️',
               callback_data=BackCallBackData(level=Level.SUBCATEGORY, category_id=datas[0].subcategory.category_id))
    ikb.adjust(2)
    return ikb.as_markup()
