from typing import Optional
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union

class Item(BaseModel):
    item_id: int
    name: str
    description: Optional[str] = None
    price: float

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/items/")
async def create_item(item: Item):
    return item

  

if __name__ == '__main__':
    uvicorn.run("main:app", port=8000, host='127.0.0.1')
