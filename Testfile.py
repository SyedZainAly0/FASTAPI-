from fastapi import FastAPI, APIRouter,Body,Query,Path
from typing import Annotated
from pydantic import BaseModel, Field


app = FastAPI()

@app.get('/tickets')
def Tickets():
    return {
        "Message": "No Record Found, Fetch another URL for tickets"
    }

@app.get('/tickets/{ticket_id}')
def Ticket_id(  
    ticket_id: Annotated[
        int, Path(gt=0, lt=100)
    ]):
       return{
          "Message": f"The ticket ID: {ticket_id} has not found"  
       }
    

@app.get('/tickets/{ticket_id}/Products/{product_id}')
def Ticket_id(  
       
    ticket_id: Annotated[
        int, Path(gt=0, lt=100)
    ],
    
    product_id: Annotated[
        int, Path(gt=10, lt=100)
    ],

    ):
         return{
          "Message": f"The ticket ID: {ticket_id} and {product_id} has not found"  
    }
    


@app.get("/salay/{salary_id}/Products/{product_id}")
def Queryfunction(
        salary_id: Annotated[
        int, Path(gt=0, lt=100)
    ],
    
    product_id: Annotated[
        int, Path(gt=10, lt=100)
    ],

    search: Annotated[
           str | None , Query(max_length=100, min_length=10, include_in_schema=False, alias="keyword-search", title="value") 
    ] = None,

    Max_value: Annotated[int | None , Query(gt=5, lt=15000, alias="value-for-ticket")] = None,
):
       return{
              salary_id : salary_id,
              product_id: product_id,
              search: search,
              Max_value : Max_value
       }

class Customfield(BaseModel):
    productname: str | None = Field(max_length=100, min_length=3, alias="Pro-Name")
    productdescription: str | None = Field(max_length=1000, min_length=10, alias="pro-desc")
    product_loaction: str | None = Field(max_length=20, min_length=5, alias="Location")
    product_price: float | None = Field(gt=150, lt=20000)
    product_quantity: int = Field(gt=5, lt=10)


@app.get("/Details")
def Details(values: Customfield = Query()):
    return {
        f"This is for Detail---" 
        "Entered URL": values
    }


@app.get("/Record")
def Record(
        Values: Annotated[Customfield,Query()]
):
       return{
           f"This is for Record---"
           "Entered URL": Values      
       }

@app.get('/items')
def Items(
        Values: Annotated[Customfield,Query()]
):
       return{
               f"This is for item---"
           "Entered URL": Values      
       }

@app.get('/History')
def History(
         Values: Annotated[Customfield,Query()]
):
       return{
               f"This is for history---"
           "Entered URL": Values      
       }

'''
Testing URL:
http://127.0.0.1:8500/History?Pro-Name=PenBox&pro-desc=This%20is%20a%20good%20quality%20pen%20box&Location=Lahore&product_price=500&product_quantity=7


Body paramter send in post or put request

This files run seperately not linked with HealthAPi file
'''

# if we multiple base models for single url:

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
async def create_order( item: Item, user: User, address: Address , Body):
    return {
        "item": item,
        "user": user,
        "address": address
    }


# Model nesting:

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

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

class Payment(BaseModel):
    card_number: str
    amount: float

class Coupon(BaseModel):
    code: str
    discount: float

# One main model that contains all others
class Order(BaseModel):
    item: Item       
    user: User          
    address: Address    
    payment: Payment   
    coupon: Coupon      

@app.post("/order")
async def create_order(order: Order):   # just one model!
    return order


# ------------------------------------------------------------------------------------------------------------------------------------------------


'''
Request Example Data
'''

class Item(BaseModel):
    name: str = Field(examples=["Foo0000000000000"])
    description: str | None = Field(default=None, examples=["A very nice Itemmmmmmmmmmmmm"])
    price: float = Field(examples=[35.44444])
    tax: float | None = Field(default=None, examples=[3.222222222222])


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results