from sqlalchemy import (create_engine, Column, Integer,
                        String, BigInteger, Boolean, DateTime, func, ForeignKey)
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from data.config import PG_USER, PG_PASS, PG_HOST, PG_PORT, PG_DB

engine = create_engine(f'postgresql+psycopg2://{PG_USER}:{PG_PASS}@{PG_HOST}:{PG_PORT}/{PG_DB}')

Base = declarative_base()
Session = sessionmaker(bind=engine)



class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    chat_id = Column(BigInteger, unique=True)
    fullname = Column(String(50), nullable=False)
    phone = Column(String(12))
    lang = Column(String(2), server_default='uz', nullable=False)

    user_answers = relationship('UserAnswer', back_populates='user', cascade='all, delete-orphan')

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


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    subcategories = relationship('Subcategory', back_populates='category', cascade='all, delete-orphan')

    def __repr__(self):
        return f"{self.__class__.__name__}({self.id}, {self.name!r})"


class Subcategory(Base):
    __tablename__ = 'subcategory'
    id = Column(Integer, primary_key=True, autoincrement=True)
    category_id = Column(Integer, ForeignKey('category.id', ondelete='cascade'))
    name = Column(String, nullable=False)

    category = relationship('Category', back_populates='subcategories')
    quizzes = relationship('Quiz', back_populates='subcategory', cascade='all, delete-orphan')

    def __repr__(self):
        return f"{self.__class__.__name__}({self.id}, {self.name!r})"


class Quiz(Base):
    __tablename__ = 'quiz'
    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String(256), nullable=False)
    subcategory_id = Column(Integer, ForeignKey('subcategory.id', ondelete='cascade'))

    subcategory = relationship('Subcategory', back_populates='quizzes')
    options = relationship('Option', back_populates='quiz', cascade='all, delete-orphan')
    user_answers = relationship('UserAnswer', back_populates='quiz')

    def __repr__(self):
        return f"{self.__class__.__name__}({self.id}, {self.text!r})"


class Option(Base):
    __tablename__ = 'option'
    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String(50), nullable=False)
    quiz_id = Column(Integer, ForeignKey('quiz.id', ondelete='cascade'))
    is_correct = Column(Boolean, default=False)

    quiz = relationship('Quiz', back_populates='options')
    user_answers = relationship('UserAnswer', back_populates='option')

    def __repr__(self):
        return f"{self.__class__.__name__}({self.id}, {self.text!r})"


class UserAnswer(Base):
    __tablename__ = 'user_answer'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='cascade'))
    quiz_id = Column(Integer, ForeignKey('quiz.id', ondelete='cascade'))
    option_id = Column(Integer, ForeignKey('option.id'))
    answered_at = Column(DateTime, default=func.now())

    user = relationship('User', back_populates='user_answers')
    option = relationship('Option', back_populates='user_answers')
    quiz = relationship('Quiz', back_populates='user_answers')

    def __repr__(self):
        return f"{self.__class__.__name__}({self.id})"
