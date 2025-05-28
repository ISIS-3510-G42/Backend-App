from pydantic import BaseModel

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