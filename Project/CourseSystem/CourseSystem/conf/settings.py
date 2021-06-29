# -*- coding:utf-8 -*-
import os

BASE_PATH = os.path.abspath(
    os.path.dirname(
        os.path.dirname(__file__)
    ))

DB_PATH = os.path.join(
    BASE_PATH, "db"
)

if __name__ == "__main__":
    print(BASE_PATH)
    print(DB_PATH)
