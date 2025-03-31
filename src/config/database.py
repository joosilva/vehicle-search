import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

def get_engine():
    if not os.path.exists('database'):
        os.makedirs('database')
    
    return create_engine("sqlite:///database/veiculos.db")

SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = get_engine())

class Database:

    def __init__(self):
        self.criar_tabelas()

        self.session = SessionLocal()

    def get_session(self):
        return SessionLocal

    def criar_tabelas(self):
        engine = get_engine()

        Base.metadata.create_all(bind = engine)
