
from pydantic import BaseModel

class ProductoCreate(BaseModel):
    nombre: str
    precio: float

class ProductoResponse(BaseModel):
    id: int
    nombre: str
    precio: float

    class Config:
        orm_mode = True