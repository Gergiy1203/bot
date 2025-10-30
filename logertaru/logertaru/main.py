import telebot
import httpx
from fastapi import FastAPI
from typing import Union




token = ""
app = FastAPI()



r = httpx.get('https://ru.chaturbate.com/')
r = httpx.get('https://ru.stripchat.com/')
r
r.status_code
r.headers['content-type']
'text/html; charset=UTF-8'
r.text



@app.get("/")
def read_root():
    return {"Hello": "World"}



@app.get("/items/{item_id")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}




@app.put("/items/{item_id}")
def update_item(item_name: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}




