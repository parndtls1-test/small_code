# setup FastAPI
# create requirements.txt and run --or-- pip install items
# fastapi
# uvicorn or hypercorn
# cd source folder
# run command uvicorn pyfile:app --reload

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
db = []

#create model
class Thing(BaseModel):
    name: str
    age: int

@app.get('/')
def index():
    return {'key': 'value'}

@app.get('/thing')
def get_thing():
    return db

@app.get('/thing/{thing_id}')
def get_thingid(thing_age: int):
    return db[thing_age - 1]

@app.post('/thing')
def create_thing(thing: Thing):
    db.append(thing.dict())
    return db[-1]

@app.delete('/thing/{thing_id}')
def delete_thing(thing_age: int):
    db.pop(thing_id - 1)
    return

# swaggerUI url ip/docs