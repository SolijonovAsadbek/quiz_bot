from utils.db.database import Session, Category, Subcategory, Quiz, Option

session = Session()

datas = [
    {
        "category": "Matematika",
        "subcategory": "Algebra",
        "quiz": "2 + 2 = ?",
        "options": [
            ('4', True),
            ('3', False),
            ('2', False),
            ('1', False),
        ]
    },
    {

    }
]


def save_data(datas):
    for data in datas:
        category = session.query(Category).filter(data["category"] == Category.name).first()
        if not category:
            category = Category(name=data["category"])
            session.add(category)
            session.flush()

        subcategory = session.query(Subcategory).filter(data["subcategory"] == Subcategory.name).first()
        if not subcategory:
            subcategory = Subcategory(name=data["subcategory"], category_id=category.id)
            session.add(subcategory)
            session.flush()

        quiz = session.query(Quiz).filter(data["quiz"] == Quiz.text).first()
        if not quiz:
            quiz = Quiz(text=data["quiz"], subcategory_id=subcategory.id)
            session.add(quiz)
            session.flush()

            options = data["options"]
            for opt_text, opt_bool in options:
                option = Option(text=opt_text, is_correct=opt_bool, quiz_id=quiz.id)
                session.add(option)

    session.commit()
