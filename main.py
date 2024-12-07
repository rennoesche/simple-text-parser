import os

from init_db import init_db as initial


def check_db():
    if not os.path.exists("database.db"):
        initial()
        print("Database telah dibuat!")
    else:
        print("Database sudah dibuat, lewati...")


if __name__=="__main__":
    check_db()