from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker


Base = declarative_base()
DB_URL = 'postgresql+psycopg2://bidder:bidder@localhost:5432/football'


def create_session():
    Engine = create_engine(DB_URL, echo=False)
    SessionMaker = sessionmaker(bind=Engine, autoflush=False)
    Session = scoped_session(SessionMaker)
    return Session
