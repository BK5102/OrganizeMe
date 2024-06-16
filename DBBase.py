from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.orm import DeclarativeBase

class DBBase(DeclarativeBase):    
    engine = create_engine("mysql+mysqlconnector://root:root123@localhost:3306/agenda_planner", echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()