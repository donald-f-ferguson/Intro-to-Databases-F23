from typing import Any, Dict, List, Optional

from pydantic import ValidationError

from src.resources import BaseResource
from src.db.db import DB
from src.models.models import Student

KV = Dict[str, Any]


class StudentResource(BaseResource):
    TABLE_NAME = "student"

    def __init__(self, db: DB):
        self.db = db

    @staticmethod
    def parse_student(raw_dict: KV) -> Optional[Student]:
        """Attempts to fit key-value pairs into a Student model.

        :param raw_dict: The key-value pairs
        :returns: A Student model if raw_dict represents a valid one;
                  otherwise, None
        """
        try:
            if raw_dict.get("tot_cred", None):
                raw_dict["tot_cred"] = int(raw_dict["tot_cred"])
            return Student(**raw_dict)
        except ValidationError:
            return None

    def get_all(self, filters: KV) -> List[Student]:
        """Gets all students that satisfy the specified filters.

        :param filters: Key-value pairs that the returned rows must satisfy.
                        An empty dict and None are treated the same.
        :returns: A list of students that satisfy filters
        """
        rows = self.db.select(self.TABLE_NAME, filters)
        res = [self.parse_student(row) for row in rows]
        return res

    # TODO: all methods below

    def get_by_id(self, student_id: int) -> Optional[Student]:
        """Gets a student by their ID.

        :param student_id: The ID to be matched
        :returns: The student with ID student_id, or None if none exists
        """
        pass

    def create(self, student: Student) -> int:
        """Creates a student.

        :param student: The student to be created
        :returns: The number of students created
        """
        pass

    def update(self, student_id: int, values: KV) -> int:
        """Updates a student.

        :param student_id: The ID of the student to be updated
        :param values: The new values for the student
        :returns: The number of rows affected. If student_id != student.ID,
                  then immediately return 0 without any updating.
        """
        pass

    def delete(self, student_id: int) -> int:
        """Deletes a student.

        :param student_id: The ID of the student to be deleted
        :returns: The number of rows affected
        """
        pass
