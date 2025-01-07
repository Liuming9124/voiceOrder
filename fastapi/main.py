from fastapi import FastAPI
from pydantic import BaseModel
import requests
import llm


server = ""

with open("env", "r") as f:
    server =  f.read().strip()


app = FastAPI()

class DetailInput(BaseModel):
    msg: str

class Detail(BaseModel):
    input: DetailInput

class Item(BaseModel):
    detail: list[Detail]


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/asklm/")
async def asklm(data: Item):
    prompt = data.detail[0].input.msg

    # 發一個get request 到 取得menu
    response = requests.get( server +"/dbctl")
    menu = response.json()

    output = llm.askLLM(prompt, menu)
    return {"msg": output}