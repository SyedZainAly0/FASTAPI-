from fastapi import FastAPI, APIRouter

app = APIRouter()

@app.get("/hello/{username}")
def greeting(username:str):
    return {
        "message": f"Hello,{username} How have you been?"
    }



