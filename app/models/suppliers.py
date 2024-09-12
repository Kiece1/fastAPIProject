from pydantic import BaseModel

class Supplier(BaseModel):
    name: str
    country: str
    key: str