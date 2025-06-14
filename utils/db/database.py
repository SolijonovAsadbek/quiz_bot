from sqlalchemy import (create_engine, Column, Integer,
                        String, BigInteger, ForeignKey)
from sqlalchemy.orm import declarative_base, sessionmaker
from data.config import PG_USER, PG_PASS, PG_HOST, PG_PORT, PG_DB

engine = create_engine(f'postgresql+psycopg2://{PG_USER}:{PG_PASS}@{PG_HOST}:{PG_PORT}/{PG_DB}')

Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    chat_id = Column(BigInteger, unique=True)
    fullname = Column(String(50), nullable=False)
    phone = Column(String(12))
    lang = Column(String(2), server_default='uz', nullable=False)

    def save(self, session):
        session.add(self)
        session.commit()

    @classmethod
    def update(cls, session, chat_id, **kwargs):
        user = session.query(cls).filter(chat_id == cls.chat_id).first()  # None
        if user:
            for key, value in kwargs.items():
                if hasattr(user, key):
                    setattr(user, key, value)
            session.commit()
            return True
        return False

    @classmethod
    def check_register(cls, session, id_):
        obj = session.query(cls).filter(id_ == cls.chat_id).first()
        if not obj:
            return False
        return True

    def __repr__(self):
        return f"{self.__class__.__name__}({self.id}, {self.fullname!r})"


# class Category(Base):
#     __tablename__ = 'category'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String, nullable=False)
#
#     def __repr__(self):
#         return f"{self.__class__.__name__}({self.id}, {self.name!r})"
#
#
# class Subcategory(Base):
#     __tablename__ = 'subcategory'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     category_id = Column(Integer, ForeignKey('category.id'))
#     name = Column(String, nullable=False)
#
#     def __repr__(self):
#         return f"{self.__class__.__name__}({self.id}, {self.name!r})"


if __name__ == '__main__':
    user = User(chat_id=1836679375, fullname='Asadbek Solijonov', phone='998911779116')
    session.add(user)
    # user = session.query(User).filter(1836679375 == User.chat_id).first()
    # if user:
    # user.fullname = 'Solijonov Asadbek'
    # session.delete(user)
    session.commit()
