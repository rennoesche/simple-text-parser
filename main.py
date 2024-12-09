import os
from core.converter import convert_pdf
from core.tokenize import tokenize
from core.parser import parser
from init_db import init_db as initial
from db import CVData as cvdat_
from init_db import init_db

def check_db():
    if not os.path.exists("database.db"):
        initial()
        print("Database telah dibuat!")
    else:
        print("Database sudah dibuat, lewati...")

def save(data):
    session = init_db()
    try:
        entry_data = cvdat_(
            nama = data["nama"],
            email = data["email"],
            telepon = data["ponsel"],
            pengalaman = "; ".join(data["pengalaman"]),
            pendidikan_terakhir = data["pend_last"],
            pendidikan = data["pendidikan"],
            skill = "; ".join(data["skill"])
        )
        session.add(entry_data)
        session.commit()
        print("Data berhasil disimpan di Database!")
    except Exception as e:
        session.rollback()
        print(f"Error menyimpan data: {e}")


if __name__=="__main__":
    check_db()

    file_path = "cv.pdf" #File path pdf
    praproses = convert_pdf(file_path)
    tokens = tokenize(praproses)
    data = parser(tokens)
    save(data)


    print(data)