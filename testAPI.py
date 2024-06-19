from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    description: str
    price: int
    on_offer: bool

@app.get("/")
def get_root():
    return {"message": "Hello World"}

@app.get("/greet/{name}")
def get_name(name:str):
    return{"greeting": f"Hello {name}"}

@app.put("/item/{item_id}")
def update_item(item_id: int, item:Item):
    return {
        'id': item_id,
        'name': item.name,
        'description': item.description,
        'price': item.price,
        'on_offer': item.on_offer

    }

@app.get("/greet")
def greet_optional_name(name:Optional[str]="user"):
    return {"message":f"Hello {name}"}

