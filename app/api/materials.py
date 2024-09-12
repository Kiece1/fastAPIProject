from app.models.materials import Material
from app.utils.helpers import generate_qs, generate_short_code
from fastapi import APIRouter, HTTPException
from database import database
materials_collection = database.get_collection("materials")

router = APIRouter()

@router.post("/material", response_model=Material)
async def create_material(material: Material):
    try:
        material.key = generate_qs(material.name) + "-" + generate_short_code()
        await materials_collection.insert_one(material.model_dump())
        return material
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/material/{key}", response_model=Material)
async def read_material(key: str):
    try:
        material = await materials_collection.find_one({"key": key})
        if material is None:
            raise HTTPException(
                status_code=404, detail=f"Material with key {key} not found"
            )
        return material
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.delete("/material/{key}")
async def delete_material(key: str):
    try:
        result = await materials_collection.delete_one({"key": key})
        if result.deleted_count == 0:
            raise HTTPException(
                status_code=404, detail=f"Material with key {key} not found"
            )
        return {"message": f"Material with key {key} deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))