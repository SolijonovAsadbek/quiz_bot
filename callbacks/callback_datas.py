from enum import Enum
from typing import Optional

from aiogram.filters.callback_data import CallbackData


class Level(Enum):
    CATEGORY = 'category'
    SUBCATEGORY = 'subcategory'


class CategoryCallbackData(CallbackData, prefix='category'):
    id: int


class SubCategoryCallbackData(CallbackData, prefix='subcategory'):
    id: int
    category_id: int


class QuizCallbackData(CallbackData, prefix='quiz'):
    id: int
    subcategory_id: int


class BackCallBackData(CallbackData, prefix='back'):
    level: Level
    category_id: Optional[int] = None
    subcategory_id: Optional[int] = None

