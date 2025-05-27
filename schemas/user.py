from pydantic import BaseModel

#Clase de datos para definir un usuario
class UserCreate(BaseModel):
    name: str
    email: str
    postedProducts: list[int]
    boughtProducts: list[int]

#Forma de respuesta al solicitar un usuario
class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    postedProducts: list[int]
    boughtProducts: list[int]

    class Config:
        from_attributes = True