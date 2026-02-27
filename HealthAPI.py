from fastapi import FastAPI
from PathParameters import app as greeting
from MathAPI import app as mathApi
from QueryparamterApi import app as querydata


app = FastAPI()

# Include all routers
app.include_router(greeting)
app.include_router(mathApi)
app.include_router(querydata)


# Health check endpoint
@app.get('/health')
async def Status():
    return {
         "status": "OK",
         "server": "running"
    }