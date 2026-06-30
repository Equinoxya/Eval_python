from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

class Base(DeclarativeBase):
    pass

class Database:
    def __init__(self, url="sqlite:///training.db"):
        self.engine = create_engine(url)
        self.SessionLocal = sessionmaker(bind=self.engine)
        
    def create_tables(self):
        Base.metadata.create_all(self.engine)
        
    def create_session(self):
        return self.SessionLocal()
        