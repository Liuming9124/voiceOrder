from fastapi import FastAPI
from pydantic import BaseModel
import requests
import llm

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
    response = requests.get("http://127.0.0.1:80/dbctl")
    menu = response.json()

    output = llm.askLLM(prompt, menu)
    return {"msg": output}