from motor.motor_asyncio import AsyncIOMotorClient
import os

MONGO_DETAILS = f"mongodb+srv://{'erickremer'}:{'dz0MKWC4nmsP2Dof'}@cluster0.dg783.mongodb.net/texia-dev?retryWrites=true&w=majority&tls=true"

client = AsyncIOMotorClient(MONGO_DETAILS)
database = client.get_database("texia-dev")