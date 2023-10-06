from typing import Optional

from pydantic import BaseModel

class Student(BaseModel):
    ID: int
    name: str
    dept_name: Optional[str] = None
    tot_cred: Optional[int] = None
