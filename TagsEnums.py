from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

class User(BaseModel):
    username: str
    email: str

class Order(BaseModel):
    item: Item
    user: User


class UserTags(Enum):
    orders = "Orders"
    users = "Users"
    items = "Items"


@app.post(
    "/orders/",
    tags=[UserTags.orders],                       
    summary="Create a new order",             
    description="""
Create a new order in the system.

- **item**: The item being ordered
- **user**: The user placing the order
- **price**: Total price of the item
- This endpoint stores the order and returns the created object.
""",                                       
    response_description="The created order object with item and user details", 
)
async def create_order(order: Order):
    return order