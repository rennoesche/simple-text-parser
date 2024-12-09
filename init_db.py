from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

Base = declarative_base()

def init_db():
    URL_DB = "sqlite:///database.db"
    engine = create_engine(URL_DB)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    return Session()

session = None # Hanya dipakai ketika di inisialisasi session=init_db()