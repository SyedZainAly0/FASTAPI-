from fastapi import FastAPI
from PathParameters import app as greeting
from MathAPI import app as mathApi
from QueryparamterApi import app as querydata
from QueryParamter import route as system_testing
from PathQuery import app as get_product
from FilterfunctioninQuery import app as get_product
from BodyParams import app as create_order
from HTTPExceptions import app as read_item

app = FastAPI()

# Include all routers
app.include_router(greeting)
app.include_router(mathApi)
app.include_router(querydata)
app.include_router(system_testing)
app.include_router(get_product)
app.include_router(get_product)
app.include_router(create_order)
app.include_router(read_item)

# Health check endpoint
@app.get('/health')
async def Status():
    return {
         "status": "OK",
         "server": "running"
    }