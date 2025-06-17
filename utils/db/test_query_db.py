from utils.db.database import Session, Subcategory, Category

session = Session()
category = session.query(Category).filter('Fizika' == Category.name).first()
subcategory = session.query(Subcategory).filter('Geometriya' == Subcategory.name).first()

print(subcategory.category.name)
print(subcategory.quizzes)
print(category.subcategories)
categories = session.query(Category).all()
for category in categories:
    print(category.id, category.name)
    for subcategory in session.query(Subcategory).filter(category.id == Subcategory.category_id).all():
        print(subcategory.id, subcategory.name)
