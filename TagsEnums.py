# from enum import Enum
# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# class Item(BaseModel):
#     name: str
#     price: float

# class User(BaseModel):
#     username: str
#     email: str

# class Order(BaseModel):
#     item: Item
#     user: User


# class UserTags(Enum):
#     orders = "Orders"
#     users = "Users"
#     items = "Items"


# @app.post(
#     "/orders/",
#     tags=[UserTags.orders],                       
#     summary="Create a new order",             
#     description="""
# Create a new order in the system.

# - **item**: The item being ordered
# - **user**: The user placing the order
# - **price**: Total price of the item
# - This endpoint stores the order and returns the created object.
# """,                                       
#     response_description="The created order object with item and user details", 
# )
# async def create_order(order: Order):
#     return order


from fastapi import FastAPI,APIRouter
from pydantic import BaseModel

app = APIRouter()

class Item(BaseModel):
    name: str
    price: float

# GET: Retrieve all items
@app.get("/items/", tags=["Items"], summary="Get items", description='abcdefghijklmnopqrstuvwxyz123456')
def get_items():
    return [{"name": "Item1", "price": 100}]

# POST: Create a new item
@app.post("/items/", tags=["Items"], summary="Create item" , description='abcdefghijklmnopqrstuvwxyz123456')
def create_item(item: Item):
    return item

# PUT: Update an item fully
@app.put("/items/", tags=["Items"], summary="Update item fully" , description='abcdefghijklmnopqrstuvwxyz123456')
def update_item(item: Item):
    return item

# PATCH: Update an item partially
@app.patch("/items/", tags=["Items"], summary="Update item partially" , description='abcdefghijklmnopqrstuvwxyz123456')
def patch_item(item: Item):
    return item

# DELETE: Delete an item
@app.delete("/items/", tags=["Items"], summary="Delete item" , description='abcdefghijklmnopqrstuvwxyz123456')
def delete_item(item_id: int):
    return {"deleted_id": item_id}