from fastapi import FastAPI
from typing import Union, Optional

app = FastAPI(docs_url="/documentation")

@app.get("/hello")
def root():
    return {"mesage":"hello word"}

@app.get("/items/{item_id}")

async def read_item(item_id: Union[int, str]):

   return {"item_id": item_id}

# exo1
@app.get("/read_items/{item_id}")

async def read_item(item_id: int, q_name: Optional[str] = None):
   
   return {"item_id": item_id, "q name": q_name }

# exo2
@app.get("/pricer/{price}")

async def read_item(price: int, tax: Optional[int] = 0 ):
   
   def compute_total_price (price, tax):
    pttc = price+(price*tax)/100
    return (pttc)
   
   return {"prix ttc": compute_total_price(price, tax)}