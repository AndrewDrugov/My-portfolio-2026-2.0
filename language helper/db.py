import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
import random

engine = create_engine("postgresql+psycopg2://postgres:12345@localhost/Rebotica")
Base = declarative_base()

Session = sessionmaker(bind=engine)
s = Session()
class Word(Base):
    __tablename__ = 'lang_words2'
    id = Column(Integer, primary_key=True, autoincrement=True)
    word = Column(String, nullable=False)
    translation = Column(String, nullable=False)

Base.metadata.create_all(engine)

def add_word(word,translation):
    new_word = Word(word = word, translation = translation)
    s.merge(new_word)
    s.commit()

def get_random_word():
    data = s.query(Word).all()
    random_word = random.choice(data) if data else None
    return random_word