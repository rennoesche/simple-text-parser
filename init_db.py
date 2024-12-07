from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db import Base

def init_db():
    URL_DB = "sqlite:///database.db"
    engine = create_engine(URL_DB)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()