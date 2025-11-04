from fastapi import FastAPI
from pydantic import BaseModel
app= FastAPI()
class name(BaseModel):
	name:str
@app.post("/hello")
def hello(data:name):
	return {"message":f"hello {data.name}"}
