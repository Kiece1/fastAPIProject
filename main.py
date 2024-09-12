from fastapi import FastAPI
from app.api import suppliers, materials

server = FastAPI()
server.include_router(suppliers.router, prefix="", tags=["suppliers"])
server.include_router(materials.router, prefix="", tags=["materials"])

@server.get("/")
def read_root():
    return {"health": True}