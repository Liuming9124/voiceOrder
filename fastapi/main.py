from fastapi import FastAPI
from pydantic import BaseModel
import requests
import llm
import whisper

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

@app.post("/translate/")
async def translate(data: Item):
    audio64 = data.detail[0].input.msg
    output = whisper.transcribe_audio_from_base64(audio64, language="zh", prompt=None, response_format="text")
    print(output)
    return {"msg": output}