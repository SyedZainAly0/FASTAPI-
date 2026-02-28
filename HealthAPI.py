from fastapi import FastAPI
from PathParameters import app as greeting
from MathAPI import app as mathApi
from QueryparamterApi import app as querydata
from QueryParamter import route as system_testing

app = FastAPI()

# Include all routers
app.include_router(greeting)
app.include_router(mathApi)
app.include_router(querydata)
app.include_router(system_testing)


# Health check endpoint
@app.get('/health')
async def Status():
    return {
         "status": "OK",
         "server": "running"
    }