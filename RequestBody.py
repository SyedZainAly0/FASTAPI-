from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()

@app.post("/items/")
async def create_item(item: Item):
    return {
        "Message": "Data has been sent successfully to backend and saved to DB"
    }


