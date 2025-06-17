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
        "category": "Matematika",
        "subcategory": "Algebra",
        "quiz": "5 * 3 = ?",
        "options": [
            ('15', True),
            ('10', False),
            ('8', False),
            ('18', False),
        ]
    },
    {
        "category": "Matematika",
        "subcategory": "Geometriya",
        "quiz": "Uchburchakning ichki burchaklari yig'indisi nechaga teng?",
        "options": [
            ('180°', True),
            ('360°', False),
            ('90°', False),
            ('270°', False),
        ]
    },
    {
        "category": "Matematika",
        "subcategory": "Geometriya",
        "quiz": "Kvadratning barcha tomonlari nechaga teng?",
        "options": [
            ('Bir xil', True),
            ('Turli-tuman', False),
            ('Ikkitasi teng', False),
            ('Hech biri teng emas', False),
        ]
    },
    {
        "category": "Matematika",
        "subcategory": "Algebra",
        "quiz": "10 - 4 = ?",
        "options": [
            ('6', True),
            ('5', False),
            ('7', False),
            ('8', False),
        ]
    },
    {
        "category": "Matematika",
        "subcategory": "Algebra",
        "quiz": "9 / 3 = ?",
        "options": [
            ('3', True),
            ('2', False),
            ('6', False),
            ('1', False),
        ]
    },
    {
        "category": "Matematika",
        "subcategory": "Geometriya",
        "quiz": "To'rtburchakda nechta burchak bo'ladi?",
        "options": [
            ('4', True),
            ('2', False),
            ('3', False),
            ('5', False),
        ]
    },
    {
        "category": "Matematika",
        "subcategory": "Algebra",
        "quiz": "Agar x = 2 bo‘lsa, 3x + 1 = ?",
        "options": [
            ('7', True),
            ('6', False),
            ('5', False),
            ('8', False),
        ]
    },
    {
        "category": "Matematika",
        "subcategory": "Geometriya",
        "quiz": "Doiraning markazidan chetiga bo‘lgan masofa nima deb ataladi?",
        "options": [
            ('Radius', True),
            ('Diametr', False),
            ('Perimetr', False),
            ('Koordinata', False),
        ]
    },
    {
        "category": "Matematika",
        "subcategory": "Algebra",
        "quiz": "0 ga istalgan sonni ko‘paytirsak nima bo‘ladi?",
        "options": [
            ('0', True),
            ('1', False),
            ('O‘sha son', False),
            ('Noma’lum', False),
        ]
    },
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
        "category": "Matematika",
        "subcategory": "Geometriya",
        "quiz": "Uchburchakning ichki burchaklari yig'indisi nechaga teng?",
        "options": [
            ('180°', True),
            ('360°', False),
            ('90°', False),
            ('270°', False),
        ]
    },
    {
        "category": "Matematika",
        "subcategory": "Algebra",
        "quiz": "Agar x = 3 bo‘lsa, 2x + 4 = ?",
        "options": [
            ('10', True),
            ('6', False),
            ('8', False),
            ('12', False),
        ]
    },
    {
        "category": "Fizika",
        "subcategory": "Mexanika",
        "quiz": "Tezlikning formulasi qanday?",
        "options": [
            ('s = v * t', False),
            ('v = s / t', True),
            ('t = v / s', False),
            ('a = v / t', False),
        ]
    },
    {
        "category": "Fizika",
        "subcategory": "Elektrodinamika",
        "quiz": "Elektr tokining o‘lchov birligi nima?",
        "options": [
            ('Amper', True),
            ('Volt', False),
            ('Ohm', False),
            ('Joul', False),
        ]
    },
    {
        "category": "Fizika",
        "subcategory": "Issiqlik",
        "quiz": "Suv 100°C da nima qiladi?",
        "options": [
            ('Qaynaydi', True),
            ('Muzlaydi', False),
            ('Bug‘lanmaydi', False),
            ('Soviydi', False),
        ]
    },
    {
        "category": "Tarix",
        "subcategory": "O'zbekiston Tarixi",
        "quiz": "Amir Temur qachon tug‘ilgan?",
        "options": [
            ('1336-yil', True),
            ('1399-yil', False),
            ('1405-yil', False),
            ('1220-yil', False),
        ]
    },
    {
        "category": "Tarix",
        "subcategory": "Jahon Tarixi",
        "quiz": "Ikkinchi Jahon Urushi qachon boshlangan?",
        "options": [
            ('1939-yil', True),
            ('1914-yil', False),
            ('1945-yil', False),
            ('1925-yil', False),
        ]
    },
    {
        "category": "Tarix",
        "subcategory": "Qadimgi Dunyo",
        "quiz": "Misrliklar qaysi daryoda yashagan?",
        "options": [
            ('Nil', True),
            ('Furat', False),
            ('Tigr', False),
            ('Amazonka', False),
        ]
    },
    {
        "category": "Fizika",
        "subcategory": "Optika",
        "quiz": "Yorug‘lik tezligi taxminan nechaga teng?",
        "options": [
            ('300 000 km/soniyada', True),
            ('150 000 km/soat', False),
            ('100 000 km/daqiqa', False),
            ('1 000 km/soniyada', False),
        ]
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


save_data(datas)
