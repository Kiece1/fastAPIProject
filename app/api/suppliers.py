from app.models.suppliers import Supplier
from fastapi import APIRouter, HTTPException
from database import database
suppliers_collection = database.get_collection("suppliers")

router = APIRouter()

# create a new supplier
@router.post("/supplier", response_model=Supplier)
async def create_supplier(supplier: Supplier):
    try:
        await suppliers_collection.insert_one(supplier.model_dump())
        return supplier
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))   

# search a supplier by key
@router.get("/supplier/{key}", response_model=Supplier)
async def read_supplier(key:str):
    try:
        result = await suppliers_collection.find_one({'key': key})
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
# delete a supplier
@router.delete("/supplier/{key}")
async def delete_supplier(key:str):
    try:
        result = await suppliers_collection.delete_one({"key": key})
        if result.deleted_count == 0:
            raise HTTPException(
                status_code=404, detail=f"Supplier with key {key} not found"
            )
        return {"message": f"Supplier with key {key} deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))