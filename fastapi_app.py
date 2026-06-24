from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/hello/{name}")
def hello(name: str):
    return {"message": f"Привет, {name}"}

@app.post("/items")
def create_item(item: Item):
    return {"item": item, "total": item.price * 1.2}
