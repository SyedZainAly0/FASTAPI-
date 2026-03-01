from fastapi import FastAPI,APIRouter
from pydantic import BaseModel

app = APIRouter()

class Item(BaseModel):
    name: str
    price: float

class User(BaseModel):
    username: str
    email: str

class Address(BaseModel):
    street: str
    city: str
    country: str

@app.post("/order")
async def create_order(
    item: Item,
    user: User,
    address: Address
):
    return {
     "Mesage": "This is just testing endpoint"
    }