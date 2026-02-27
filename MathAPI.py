from fastapi import FastAPI, APIRouter

app = APIRouter()

@app.get("/square/{number}")
def mathApi(number:int):
    return {
        "Result": f"The Square is {number*number}"
    }