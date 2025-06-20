from sqlalchemy import cast
from sqlalchemy.dialects.postgresql import JSONB

from utils.db.database import Session, Category, Subcategory, Quiz, Option

session = Session()

datas = [
    {
        "category": {
            "uz": "Matematika",
            "ru": "Математика",
            "en": "Mathematics"
        },
        "subcategory": {
            "uz": "Algebra",
            "ru": "Алгебра",
            "en": "Algebra"
        },
        "quiz": {
            "uz": "2 + 2 = ?",
            "ru": "2 + 2 = ?",
            "en": "2 + 2 = ?"
        },
        "options": [
            {"text": {"uz": "4", "ru": "4", "en": "4"}, "is_correct": True},
            {"text": {"uz": "3", "ru": "3", "en": "3"}, "is_correct": False},
            {"text": {"uz": "2", "ru": "2", "en": "2"}, "is_correct": False},
            {"text": {"uz": "1", "ru": "1", "en": "1"}, "is_correct": False}
        ]
    },
    {
        "category": {
            "uz": "Fizika",
            "ru": "Физика",
            "en": "Physics"
        },
        "subcategory": {
            "uz": "Optika",
            "ru": "Оптика",
            "en": "Optics"
        },
        "quiz": {
            "uz": "Yorug‘lik tezligi taxminan nechaga teng?",
            "ru": "Какова приблизительная скорость света?",
            "en": "What is the approximate speed of light?"
        },
        "options": [
            {
                "text": {
                    "uz": "300 000 km/soniyada",
                    "ru": "300 000 км/с",
                    "en": "300,000 km/s"
                },
                "is_correct": True
            },
            {
                "text": {
                    "uz": "150 000 km/soat",
                    "ru": "150 000 км/ч",
                    "en": "150,000 km/h"
                },
                "is_correct": False
            },
            {
                "text": {
                    "uz": "100 000 km/daqiqa",
                    "ru": "100 000 км/мин",
                    "en": "100,000 km/min"
                },
                "is_correct": False
            },
            {
                "text": {
                    "uz": "1 000 km/soniyada",
                    "ru": "1 000 км/с",
                    "en": "1,000 km/s"
                },
                "is_correct": False
            }
        ]
    },
    {
        "category": {
            "uz": "Tarix",
            "ru": "История",
            "en": "History"
        },
        "subcategory": {
            "uz": "O'zbekiston Tarixi",
            "ru": "История Узбекистана",
            "en": "History of Uzbekistan"
        },
        "quiz": {
            "uz": "Amir Temur qachon tug‘ilgan?",
            "ru": "Когда родился Амир Темур?",
            "en": "When was Amir Temur born?"
        },
        "options": [
            {"text": {"uz": "1336-yil", "ru": "1336 год", "en": "1336"}, "is_correct": True},
            {"text": {"uz": "1399-yil", "ru": "1399 год", "en": "1399"}, "is_correct": False},
            {"text": {"uz": "1405-yil", "ru": "1405 год", "en": "1405"}, "is_correct": False},
            {"text": {"uz": "1220-yil", "ru": "1220 год", "en": "1220"}, "is_correct": False}
        ]
    }
]
datas = [
    # Avvalgi savollar...

    {
        "category": {
            "uz": "Geografiya",
            "ru": "География",
            "en": "Geography"
        },
        "subcategory": {
            "uz": "Dunyo davlatlari",
            "ru": "Страны мира",
            "en": "Countries of the world"
        },
        "quiz": {
            "uz": "O'zbekiston poytaxti qaysi shahar?",
            "ru": "Какой город является столицей Узбекистана?",
            "en": "Which city is the capital of Uzbekistan?"
        },
        "options": [
            {"text": {"uz": "Toshkent", "ru": "Ташкент", "en": "Tashkent"}, "is_correct": True},
            {"text": {"uz": "Samarqand", "ru": "Самарканд", "en": "Samarkand"}, "is_correct": False},
            {"text": {"uz": "Buxoro", "ru": "Бухара", "en": "Bukhara"}, "is_correct": False},
            {"text": {"uz": "Andijon", "ru": "Андижан", "en": "Andijan"}, "is_correct": False}
        ]
    },
    {
        "category": {
            "uz": "Biologiya",
            "ru": "Биология",
            "en": "Biology"
        },
        "subcategory": {
            "uz": "Inson anatomiyasi",
            "ru": "Анатомия человека",
            "en": "Human anatomy"
        },
        "quiz": {
            "uz": "Inson qalbiga necha bo'lmacha?",
            "ru": "Сколько камер в сердце человека?",
            "en": "How many chambers are in the human heart?"
        },
        "options": [
            {"text": {"uz": "4", "ru": "4", "en": "4"}, "is_correct": True},
            {"text": {"uz": "2", "ru": "2", "en": "2"}, "is_correct": False},
            {"text": {"uz": "3", "ru": "3", "en": "3"}, "is_correct": False},
            {"text": {"uz": "1", "ru": "1", "en": "1"}, "is_correct": False}
        ]
    },
    {
        "category": {
            "uz": "Adabiyot",
            "ru": "Литература",
            "en": "Literature"
        },
        "subcategory": {
            "uz": "O'zbek adabiyoti",
            "ru": "Узбекская литература",
            "en": "Uzbek literature"
        },
        "quiz": {
            "uz": "Alisher Navoiy qaysi asar muallifi?",
            "ru": "Автором какого произведения является Алишер Навои?",
            "en": "Which work is authored by Alisher Navoi?"
        },
        "options": [
            {"text": {"uz": "Xamsa", "ru": "Хамса", "en": "Khamsa"}, "is_correct": True},
            {"text": {"uz": "O'tkan kunlar", "ru": "Минувшие дни", "en": "Bygone Days"}, "is_correct": False},
            {"text": {"uz": "Mehrobdan chayon", "ru": "Скорпион из михраба", "en": "Scorpion from the Mihrab"},
             "is_correct": False},
            {"text": {"uz": "Sariq devni minib", "ru": "На спине желтого дьявола", "en": "Riding the Yellow Devil"},
             "is_correct": False}
        ]
    },
    {
        "category": {
            "uz": "Kimyo",
            "ru": "Химия",
            "en": "Chemistry"
        },
        "subcategory": {
            "uz": "Elementlar",
            "ru": "Элементы",
            "en": "Elements"
        },
        "quiz": {
            "uz": "Suvning kimyoviy formulasi qanday?",
            "ru": "Какова химическая формула воды?",
            "en": "What is the chemical formula of water?"
        },
        "options": [
            {"text": {"uz": "H₂O", "ru": "H₂O", "en": "H₂O"}, "is_correct": True},
            {"text": {"uz": "CO₂", "ru": "CO₂", "en": "CO₂"}, "is_correct": False},
            {"text": {"uz": "NaCl", "ru": "NaCl", "en": "NaCl"}, "is_correct": False},
            {"text": {"uz": "O₂", "ru": "O₂", "en": "O₂"}, "is_correct": False}
        ]
    },
    {
        "category": {
            "uz": "Informatika",
            "ru": "Информатика",
            "en": "Computer Science"
        },
        "subcategory": {
            "uz": "Dasturlash",
            "ru": "Программирование",
            "en": "Programming"
        },
        "quiz": {
            "uz": "Quyidagilardan qaysi biri dasturlash tili?",
            "ru": "Какой из следующих является языком программирования?",
            "en": "Which of the following is a programming language?"
        },
        "options": [
            {"text": {"uz": "Python", "ru": "Python", "en": "Python"}, "is_correct": True},
            {"text": {"uz": "HTML", "ru": "HTML", "en": "HTML"}, "is_correct": False},
            {"text": {"uz": "CSS", "ru": "CSS", "en": "CSS"}, "is_correct": False},
            {"text": {"uz": "HTTP", "ru": "HTTP", "en": "HTTP"}, "is_correct": False}
        ]
    }
]

datas = [
    # Matematika (3 ta savol)
    {
        "category": {"uz": "Matematika", "ru": "Математика", "en": "Mathematics"},
        "subcategory": {"uz": "Algebra", "ru": "Алгебра", "en": "Algebra"},
        "quiz": {"uz": "5 × 7 = ?", "ru": "5 × 7 = ?", "en": "5 × 7 = ?"},
        "options": [
            {"text": {"uz": "35", "ru": "35", "en": "35"}, "is_correct": True},
            {"text": {"uz": "30", "ru": "30", "en": "30"}, "is_correct": False},
            {"text": {"uz": "42", "ru": "42", "en": "42"}, "is_correct": False},
            {"text": {"uz": "28", "ru": "28", "en": "28"}, "is_correct": False}
        ]
    },
    {
        "category": {"uz": "Matematika", "ru": "Математика", "en": "Mathematics"},
        "subcategory": {"uz": "Geometriya", "ru": "Геометрия", "en": "Geometry"},
        "quiz": {"uz": "To'g'ri to'rtburchakning maydoni qanday hisoblanadi?",
                 "ru": "Как вычисляется площадь прямоугольника?", "en": "How is the area of a rectangle calculated?"},
        "options": [
            {"text": {"uz": "Uzunlik × kenglik", "ru": "Длина × ширина", "en": "Length × width"}, "is_correct": True},
            {"text": {"uz": "Uzunlik + kenglik", "ru": "Длина + ширина", "en": "Length + width"}, "is_correct": False},
            {"text": {"uz": "Uzunlik - kenglik", "ru": "Длина - ширина", "en": "Length - width"}, "is_correct": False},
            {"text": {"uz": "Uzunlik / kenglik", "ru": "Длина / ширина", "en": "Length / width"}, "is_correct": False}
        ]
    },
    {
        "category": {"uz": "Matematika", "ru": "Математика", "en": "Mathematics"},
        "subcategory": {"uz": "Aritmetika", "ru": "Арифметика", "en": "Arithmetic"},
        "quiz": {"uz": "120 ni 8 ga bo'lganda qancha qoldiq qoladi?", "ru": "Каков остаток при делении 120 на 8?",
                 "en": "What is the remainder when 120 is divided by 8?"},
        "options": [
            {"text": {"uz": "0", "ru": "0", "en": "0"}, "is_correct": True},
            {"text": {"uz": "5", "ru": "5", "en": "5"}, "is_correct": False},
            {"text": {"uz": "10", "ru": "10", "en": "10"}, "is_correct": False},
            {"text": {"uz": "15", "ru": "15", "en": "15"}, "is_correct": False}
        ]
    },

    # Fizika (3 ta savol)
    {
        "category": {"uz": "Fizika", "ru": "Физика", "en": "Physics"},
        "subcategory": {"uz": "Dinamika", "ru": "Динамика", "en": "Dynamics"},
        "quiz": {"uz": "Nyutonning qancha qonuni bor?", "ru": "Сколько законов Ньютона существует?",
                 "en": "How many Newton's laws are there?"},
        "options": [
            {"text": {"uz": "3", "ru": "3", "en": "3"}, "is_correct": True},
            {"text": {"uz": "2", "ru": "2", "en": "2"}, "is_correct": False},
            {"text": {"uz": "4", "ru": "4", "en": "4"}, "is_correct": False},
            {"text": {"uz": "1", "ru": "1", "en": "1"}, "is_correct": False}
        ]
    },
    {
        "category": {"uz": "Fizika", "ru": "Физика", "en": "Physics"},
        "subcategory": {"uz": "Elektrodinamika", "ru": "Электродинамика", "en": "Electrodynamics"},
        "quiz": {"uz": "Tok kuchini o'lchash birligi?", "ru": "Единица измерения силы тока?",
                 "en": "Unit of electric current?"},
        "options": [
            {"text": {"uz": "Amper", "ru": "Ампер", "en": "Ampere"}, "is_correct": True},
            {"text": {"uz": "Volt", "ru": "Вольт", "en": "Volt"}, "is_correct": False},
            {"text": {"uz": "Vatt", "ru": "Ватт", "en": "Watt"}, "is_correct": False},
            {"text": {"uz": "Om", "ru": "Ом", "en": "Ohm"}, "is_correct": False}
        ]
    },
    {
        "category": {"uz": "Fizika", "ru": "Физика", "en": "Physics"},
        "subcategory": {"uz": "Termodinamika", "ru": "Термодинамика", "en": "Thermodynamics"},
        "quiz": {"uz": "Qanday haroratda suv muzlaydi?", "ru": "При какой температуре вода замерзает?",
                 "en": "At what temperature does water freeze?"},
        "options": [
            {"text": {"uz": "0°C", "ru": "0°C", "en": "0°C"}, "is_correct": True},
            {"text": {"uz": "10°C", "ru": "10°C", "en": "10°C"}, "is_correct": False},
            {"text": {"uz": "-10°C", "ru": "-10°C", "en": "-10°C"}, "is_correct": False},
            {"text": {"uz": "100°C", "ru": "100°C", "en": "100°C"}, "is_correct": False}
        ]
    },

    # Tarix (3 ta savol)
    {
        "category": {"uz": "Tarix", "ru": "История", "en": "History"},
        "subcategory": {"uz": "O'zbekiston tarixi", "ru": "История Узбекистана", "en": "History of Uzbekistan"},
        "quiz": {"uz": "O'zbekiston mustaqillikka erishgan yil?",
                 "ru": "В каком году Узбекистан получил независимость?",
                 "en": "In what year did Uzbekistan gain independence?"},
        "options": [
            {"text": {"uz": "1991", "ru": "1991", "en": "1991"}, "is_correct": True},
            {"text": {"uz": "1989", "ru": "1989", "en": "1989"}, "is_correct": False},
            {"text": {"uz": "1995", "ru": "1995", "en": "1995"}, "is_correct": False},
            {"text": {"uz": "2000", "ru": "2000", "en": "2000"}, "is_correct": False}
        ]
    },
    {
        "category": {"uz": "Tarix", "ru": "История", "en": "History"},
        "subcategory": {"uz": "Jahon tarixi", "ru": "Мировая история", "en": "World history"},
        "quiz": {"uz": "Ikkinchi jahon urushi qachon boshlangan?", "ru": "Когда началась Вторая мировая война?",
                 "en": "When did World War II begin?"},
        "options": [
            {"text": {"uz": "1939", "ru": "1939", "en": "1939"}, "is_correct": True},
            {"text": {"uz": "1941", "ru": "1941", "en": "1941"}, "is_correct": False},
            {"text": {"uz": "1914", "ru": "1914", "en": "1914"}, "is_correct": False},
            {"text": {"uz": "1945", "ru": "1945", "en": "1945"}, "is_correct": False}
        ]
    },
    {
        "category": {"uz": "Tarix", "ru": "История", "en": "History"},
        "subcategory": {"uz": "O'rta asrlar", "ru": "Средние века", "en": "Middle Ages"},
        "quiz": {"uz": "Bobur qaysi davlat asoschisi?", "ru": "Основателем какого государства был Бабур?",
                 "en": "Which state was founded by Babur?"},
        "options": [
            {"text": {"uz": "Boburiylar imperiyasi", "ru": "Империя Великих Моголов", "en": "Mughal Empire"},
             "is_correct": True},
            {"text": {"uz": "Usmonli imperiyasi", "ru": "Османская империя", "en": "Ottoman Empire"},
             "is_correct": False},
            {"text": {"uz": "Xorazmshohlar davlati", "ru": "Государство Хорезмшахов", "en": "Khwarazmian Empire"},
             "is_correct": False},
            {"text": {"uz": "Temuriylar davlati", "ru": "Государство Тимуридов", "en": "Timurid Empire"},
             "is_correct": False}
        ]
    },

    # Geografiya (3 ta savol)
    {
        "category": {"uz": "Geografiya", "ru": "География", "en": "Geography"},
        "subcategory": {"uz": "Dunyo davlatlari", "ru": "Страны мира", "en": "Countries of the world"},
        "quiz": {"uz": "Dunyodagi eng katta davlat maydoni?", "ru": "Самая большая страна по площади?",
                 "en": "Largest country by area?"},
        "options": [
            {"text": {"uz": "Rossiya", "ru": "Россия", "en": "Russia"}, "is_correct": True},
            {"text": {"uz": "Kanada", "ru": "Канада", "en": "Canada"}, "is_correct": False},
            {"text": {"uz": "AQSh", "ru": "США", "en": "USA"}, "is_correct": False},
            {"text": {"uz": "Xitoy", "ru": "Китай", "en": "China"}, "is_correct": False}
        ]
    },
    {
        "category": {"uz": "Geografiya", "ru": "География", "en": "Geography"},
        "subcategory": {"uz": "Tabiiy geografiya", "ru": "Физическая география", "en": "Physical geography"},
        "quiz": {"uz": "Dunyodagi eng uzun daryo?", "ru": "Самая длинная река в мире?",
                 "en": "Longest river in the world?"},
        "options": [
            {"text": {"uz": "Nil", "ru": "Нил", "en": "Nile"}, "is_correct": True},
            {"text": {"uz": "Amazonka", "ru": "Амазонка", "en": "Amazon"}, "is_correct": False},
            {"text": {"uz": "Yantszi", "ru": "Янцзы", "en": "Yangtze"}, "is_correct": False},
            {"text": {"uz": "Missisipi", "ru": "Миссисипи", "en": "Mississippi"}, "is_correct": False}
        ]
    },
    {
        "category": {"uz": "Geografiya", "ru": "География", "en": "Geography"},
        "subcategory": {"uz": "O'zbekiston geografiyasi", "ru": "География Узбекистана",
                        "en": "Geography of Uzbekistan"},
        "quiz": {"uz": "O'zbekistondagi eng baland tog'?", "ru": "Самая высокая гора в Узбекистане?",
                 "en": "Highest mountain in Uzbekistan?"},
        "options": [
            {"text": {"uz": "Hazrati Sulton", "ru": "Хазрати Султан", "en": "Hazrati Sultan"}, "is_correct": True},
            {"text": {"uz": "Chimyon", "ru": "Чимган", "en": "Chimgan"}, "is_correct": False},
            {"text": {"uz": "Zomin", "ru": "Заамин", "en": "Zaamin"}, "is_correct": False},
            {"text": {"uz": "Nurota", "ru": "Нурата", "en": "Nurata"}, "is_correct": False}
        ]
    },

    # Biologiya (3 ta savol)
    {
        "category": {"uz": "Biologiya", "ru": "Биология", "en": "Biology"},
        "subcategory": {"uz": "Botanika", "ru": "Ботаника", "en": "Botany"},
        "quiz": {"uz": "O'simliklarda fotosintez qanday rangda bo'ladi?", "ru": "Какого цвета хлорофилл у растений?",
                 "en": "What color is chlorophyll in plants?"},
        "options": [
            {"text": {"uz": "Yashil", "ru": "Зеленый", "en": "Green"}, "is_correct": True},
            {"text": {"uz": "Qizil", "ru": "Красный", "en": "Red"}, "is_correct": False},
            {"text": {"uz": "Sariq", "ru": "Желтый", "en": "Yellow"}, "is_correct": False},
            {"text": {"uz": "Ko'k", "ru": "Синий", "en": "Blue"}, "is_correct": False}
        ]
    },
    {
        "category": {"uz": "Biologiya", "ru": "Биология", "en": "Biology"},
        "subcategory": {"uz": "Zoologiya", "ru": "Зоология", "en": "Zoology"},
        "quiz": {"uz": "Qaysi hayvon dunyodagi eng katta sutemizuvchi?",
                 "ru": "Какое животное является самым крупным млекопитающим?",
                 "en": "Which animal is the largest mammal?"},
        "options": [
            {"text": {"uz": "Ko'k kit", "ru": "Синий кит", "en": "Blue whale"}, "is_correct": True},
            {"text": {"uz": "Fil", "ru": "Слон", "en": "Elephant"}, "is_correct": False},
            {"text": {"uz": "Jirafa", "ru": "Жираф", "en": "Giraffe"}, "is_correct": False},
            {"text": {"uz": "Oq ayiq", "ru": "Белый медведь", "en": "Polar bear"}, "is_correct": False}
        ]
    },
    {
        "category": {"uz": "Biologiya", "ru": "Биология", "en": "Biology"},
        "subcategory": {"uz": "Genetika", "ru": "Генетика", "en": "Genetics"},
        "quiz": {"uz": "DNK ning to'liq shakli?", "ru": "Полное название ДНК?", "en": "Full name of DNA?"},
        "options": [
            {"text": {"uz": "Dezoksiribonuklein kislota", "ru": "Дезоксирибонуклеиновая кислота",
                      "en": "Deoxyribonucleic acid"}, "is_correct": True},
            {"text": {"uz": "Ribonuklein kislota", "ru": "Рибонуклеиновая кислота", "en": "Ribonucleic acid"},
             "is_correct": False},
            {"text": {"uz": "Nuklein kislota", "ru": "Нуклеиновая кислота", "en": "Nucleic acid"}, "is_correct": False},
            {"text": {"uz": "Adenozin trifosfat", "ru": "Аденозинтрифосфат", "en": "Adenosine triphosphate"},
             "is_correct": False}
        ]
    }
]


def save_data(datas):
    for data in datas:
        category = session.query(Category).filter(cast(data["category"], JSONB) == cast(Category.name, JSONB)).first()
        if not category:
            category = Category(name=data["category"])
            session.add(category)
            session.flush()

        subcategory = session.query(Subcategory).filter(
            cast(data["subcategory"], JSONB) == cast(Subcategory.name, JSONB)).first()
        if not subcategory:
            subcategory = Subcategory(name=data["subcategory"], category_id=category.id)
            session.add(subcategory)
            session.flush()

        quiz = session.query(Quiz).filter(cast(data["quiz"], JSONB) == cast(Quiz.text, JSONB),
                                          Quiz.subcategory_id == subcategory.id).first()
        if not quiz:
            quiz = Quiz(text=data["quiz"], subcategory_id=subcategory.id)
            session.add(quiz)
            session.flush()

            options = data["options"]
            for opt_data in options:
                option = Option(text=opt_data['text'], is_correct=opt_data['is_correct'], quiz_id=quiz.id)
                session.add(option)
    try:
        session.commit()
    except Exception as e:
        session.rollback()
        print(f'Hatolik: {e}')
        raise
    finally:
        session.close()


save_data(datas)
