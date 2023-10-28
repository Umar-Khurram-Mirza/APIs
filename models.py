from pydantic import BaseModel


class Person(BaseModel):
    person_id: int
    person_name: str
