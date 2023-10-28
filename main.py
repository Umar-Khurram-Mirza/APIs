from fastapi import FastAPI
from typing import Union
from models import Person

app = FastAPI()

persons = []


@app.get("/")
async def read_root():
    return {"message": "Hello World"}


@app.get("/persons")
async def read_all_persons():
    return persons


@app.post("/persons")
async def add_one_person(person: Person):
    persons.append(person)
    return {"message": "Added person"}


@app.delete("/persons/{person_id}")
async def delete_one_person(person_id: int):
    for person in persons:
        if person.person_id == person_id:
            persons.remove(person)
            return {"message": "person deleted"}
    return {"message": "person not found"}
