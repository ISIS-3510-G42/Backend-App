from typing import List
from fastapi import APIRouter, HTTPException
from services.user_service import register_user, get_user_by_email, get_user_by_id
from schemas.user import UserCreate, UserResponse

router = APIRouter()

"Endpoints de la API de usuarios"

@router.user("/create-user/", response_model=UserResponse)
def create_user(user: UserCreate):
    try:
        new_user = register_user(user)
        return new_user
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/users/{user_id}", response_model=UserResponse)
def get_user_by_id(user_id: int):
    user = get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")
    return user

@router.get("/emails/{user_email}", response_model=UserResponse)
def get_user_by_email(user_email: int):
    user = get_user_by_email(user_email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")
    return user