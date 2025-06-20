from utils.db.database import User, Category, session, Subcategory, Quiz


async def get_user_db_lang(session, chat_id):
    user = session.query(User).filter(chat_id == User.chat_id).first()
    return user.lang if user else None


async def get_all_category(session):
    categories = session.query(Category).all()
    return categories


async def get_all_subcategory_by_id(session, category_id):
    subcategories = session.query(Subcategory).filter(category_id == Subcategory.category_id).all()
    return subcategories


async def get_all_quizs_by_sub_id(session, subcategory_id):
    quizzes = session.query(Quiz).filter(subcategory_id == Quiz.subcategory_id).all()
    return quizzes


if __name__ == '__main__':
    # subcategory = get_all_category(session)
    # print(subcategory)  # [Category(1, 'Matematika'), Category(2, 'Fizika'), Category(3, 'Tarix')]
    pass
