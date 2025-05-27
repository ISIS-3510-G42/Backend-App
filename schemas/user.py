from pydantic import BaseModel
from typing import List

class UserCreate(BaseModel):
    name: str
    email: str
    postedProducts: List[int] = []
    boughtProducts: List[int] = []

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    postedProducts: List[int] = []
    boughtProducts: List[int] = []

    class Config:
        from_attributes = True