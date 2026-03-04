from fastapi import FastAPI,APIRouter
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from datetime import datetime

app = APIRouter()

class Item(BaseModel):
    name: str
    price: float
    created_at: datetime


db = {}

@app.post("/items/{item_id}")
async def create_item(item_id: str, item: Item):
    item_data = jsonable_encoder(item)
    db[item_id] = item_data
    
    return {"stored_item": item_data}