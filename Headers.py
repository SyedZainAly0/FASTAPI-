from typing import Annotated
from fastapi import FastAPI, Header, HTTPException

app = FastAPI()

VALID_TOKEN = "mysecrettoken123"


@app.get("/dashboard/")
async def get_dashboard(
    x_token: Annotated[str | None, Header()] = None
):
    # Check if token is missing
    if x_token is None:
       return{
           f"X-Token header is missing!"
       }
    # Check if token is wrong
    if x_token != VALID_TOKEN:
      return{
         f"Invalid token! Access denied."
      }
    
    # Token is correct — allow access
    return {"message": "Welcome to dashboard!", "status": "Access granted"}



'''
1. Open Postman
2. Enter URL: http://127.0.0.1:8000/dashboard/
3. Click "Headers" tab
4. Add:
   Key:   X-Token
   Value: mysecrettoken123
5. Click Send
'''
