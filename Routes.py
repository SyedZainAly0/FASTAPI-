
from fastapi import FastAPI
import json


app = FastAPI()



@app.get('/about')
def hello():
    return {'message':"Hello World"}

@app.get('/details')
def details():
    return f"This is normal detail"


@app.get('/Employee')
def userdata():
    return Load_data()


def Load_data():
    with open('PracticeData.json','r') as f:
        data = json.load(f)

        return data

@app.get('/Employee/{Employee_id}')
def viewEmp(Employee_id: str):
    data = Load_data()
    for keys in ['users','products','orders']:
        if Employee_id in data[keys]:
         return data[keys][Employee_id]
    else:
        return {"error": "Invalid ID"}
    
