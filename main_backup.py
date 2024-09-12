from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from database import database
suppliers_collection = database.get_collection("suppliers")

app = FastAPI()

class Supplier(BaseModel):
    supplier_id: int
    name: str
    country: str

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

@app.post("/supplier")
def create_item(supplier: Supplier):
    return supplier

@app.get("/suppliers")
async def find_suppliers():
    cursor = suppliers_collection.find({"_id":0})
    result = await cursor.to_list(5)
    for item in result:
        print(item)
    return item

# @app.get("/suppliers")
# async def find_suppliers(search_country:str):
#     cursor = suppliers_collection.find({'country': { '$regex': search_country, '$options': 'i'}},{"_id":0})
#     result = await cursor.to_list(10)
#     return result

@app.get("/supplier")
async def find_supplier_by_id(supplier_id:int): 
    cursor = suppliers_collection.find_one({"i": supplier_id},{"_id":0})
    result = await cursor
    return result

@app.put("/supplier/{supplier_id}/{name}/{country}")
def update_item(supplier_id: int, item: Supplier):
    return {"name": item.name, "country": item.country}

# @app.get("/valeurs/{item_id}/{val}")
# def read_item(item_id: int, val: int, datum: Union[str, None] = None):
#     return {"item_id": item_id, "val": val,"datum": datum}