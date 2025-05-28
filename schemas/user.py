from pydantic import BaseModel
from typing import Optional

#Clase de datos para definir un usuario
class UserCreate(BaseModel):
    name: str
    email: str
    postedProducts: str
    boughtProducts: str

#Forma de respuesta al solicitar un usuario
class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    postedProducts: str
    boughtProducts: str

    class Config:
        from_attributes = True

class UserUpdateProducts(BaseModel):
    postedProducts: Optional[str] = None
    boughtProducts: Optional[str] = None
