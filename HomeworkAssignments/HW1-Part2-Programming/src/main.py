from typing import List, Optional

# Simple starter project to test installation and environment.
# Based on https://fastapi.tiangolo.com/tutorial/first-steps/
from fastapi import FastAPI, Request
# Explicitly included uvicorn to enable starting within main program.
# Starting within main program is a simple way to enable running
# the code within the PyCharm debugger
import uvicorn

from db import DB
from models import Student
from resources import StudentResource

app = FastAPI()

# NOTE: In a prod environment, never put this information in code!
# There are design patterns for passing confidential information to
# application.
# TODO: You may need to change the password
db = DB(
    host="localhost",
    port=3306,
    user="root",
    password="dbuserdbuser",
    database="db_book_hw1",
)

student_resource = StudentResource(db)

@app.get("/")
async def healthcheck() -> str:
    return "I'm alive!"

@app.get("/students")
async def get_students(req: Request) -> List[Student]:
    """Gets all students that satisfy the specified filters.

    :param req: The request that optionally contains filters in its body
    :returns: A list of students that satisfy the filters
    """
    query_params = dict(req.query_params)
    return student_resource.get_all(query_params)

# TODO: all methods below

@app.get("/students/{student_id}")
async def get_student(student_id: int) -> Optional[Student]:
    """Gets a student by ID.

    :param student_id: The ID to be matched
    :returns: The student with ID student_id, or None if none exists
    """
    pass

@app.post("/students")
async def post_student(student: Student) -> int:
    """Creates a student.

    :param student: The student to be created
    :returns: The number of students created
    """
    pass

@app.put("/students/{student_id}")
async def put_student(student_id: int, req: Request) -> int:
    """Updates a student.

    You can assume the request body contains a dict-like object
    mapping some or all student attributes to their new values.

    You must ensure that the request does not attempt to change the
    student's ID. If so, don't execute any database operations and
    immediately return 0.

    :param student_id: The ID of the student to be updated
    :param req: The request that contains the new values in its body
    :returns: The number of rows affected
    """

    # Use `await req.json()` to access the request body
    pass

@app.delete("/students/{student_id}")
async def delete_student(student_id: int) -> int:
    """Deletes a student.

    :param student_id: The ID of the student to be deleted
    :returns: The number of rows affected
    """
    pass

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8002)
