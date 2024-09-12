from app.models.suppliers import Supplier
from typing import Union
from fastapi import APIRouter
from pydantic import BaseModel
from database import database
suppliers_collection = database.get_collection("suppliers")

router = APIRouter()

# ajouter un nouveau fournisseur
@router.post("/new/supplier/")
async def create_supplier(name:str,country:str,reference:int):
    supplier = {"name": name, "country": country, "reference": reference}
    await suppliers_collection.insert_one(supplier)
    return {"message": "nouveau fournisseur ajouté"}

# supprimer un fournisseur
@router.delete("/delete/suppliers")
async def delete_suppliers_by_reference(reference: int):
    result = await suppliers_collection.delete_one({'reference': reference})
    if result.deleted_count > 0:
        return {"message": "fournisseur supprimé"}
    else:
        return {"message": "fournisseur non trouvé"}

# mettre à jour un fournisseur
@router.put("/update/suppliers")
async def update_suppliers_by_reference(reference: int, name: str, country: str):
    result = await suppliers_collection.update_one({'reference': reference}, {'$set': {'name': name, 'country': country}})
    if result.modified_count > 0:
        return {"message": "fournisseur mis à jour"}
    else:
        return {"message": "fournisseur non trouvé"}

# afficher la liste des fournisseurs
@router.get("/list/suppliers/", response_model=Supplier)
async def list_suppliers(nombre_liste:int):
    cursor = suppliers_collection.find({},{"_id": 0})
    result = await cursor.to_list(nombre_liste)
    if result:
        return result
    else:
        return {"message": "aucun fournisseur trouvé"}

# rechercher un fournisseur par pays
@router.get("/list/suppliers/country")
async def find_suppliers_by_country(nombre_liste:int,search_country:str):
    cursor = suppliers_collection.find({'country': {'$regex': search_country, '$options': 'i'}},{"_id": 0})
    result = await cursor.to_list(nombre_liste)
    if result:
        return result
    else:
        return {"message": "fournisseur non trouvé"}

# rechercher un fournisseur par reference
@router.get("/list/suppliers/reference")
async def find_suppliers_by_reference(reference:int):
    result = await suppliers_collection.find_one({'reference': reference},{"_id": 0})
    if result:
        return result
    else:
        return {"message": "fournisseur non trouvé"}