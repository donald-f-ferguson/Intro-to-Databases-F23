from src.db.db import DB
from src.resources.studentresource import StudentResource
import json


def get_DB():

    db = DB("localhost", 3306, "root", "dbuserdbuser", "db_book_hw1")
    return db


def get_student_resource():

    db = get_DB()
    student = StudentResource(db)
    return student


def t1():

    table = "student"
    my_filter = {"ID": 201, "name": "Bubba"}

    db = get_DB()
    q, args = db.build_select_query(table, my_filter)

    print("t1: q = ", q)
    print("t1: args = ", args)


def t2():

    table = "student"
    my_filter = {"ID": 128, "name": "Zhang"}

    db = get_DB()
    result = db.select(table, my_filter)

    print("t2: result = ", result)


def t3():

    table = "student"
    my_filter = {"dept_name": "Comp. Sci."}

    db = get_DB()
    result = db.select(table, my_filter)

    print("t3: result = ", json.dumps(result, indent=2, default=str))


def t4():

    s = get_student_resource()
    my_filter = {"dept_name": "Comp. Sci."}

    result = s.get_all(my_filter)
    print("t4: result = ", json.dumps(result, indent=2, default=str))


if __name__ == "__main__":
    # t1()
    # t2()
    # t3()
    t4()
