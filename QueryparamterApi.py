from fastapi import FastAPI, APIRouter,Request
app = APIRouter()

# @app.get("/search")
# def querydata(q: str, limit: int):  
#     return {
#         "Q": q,
#         "limit": limit
#     }




@app.get("/search")
def querydata(request: Request):
    query_params = dict(request.query_params)
    return query_params