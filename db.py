from sqlalchemy import Column, String, Text, Integer
from init_db import Base


class CVData(Base):
    __tablename__= 'cv_data'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nama = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    telepon = Column(String(15), nullable=False)
    pengalaman = Column(Text, nullable=True)
    pendidikan_terakhir = Column(Text, nullable=True)
    pendidikan = Column(Text, nullable=True)
    skill = Column(Text, nullable=True)
