from fastapi import APIRouter, HTTPException
from services.user_service import register_user, get_user_by_email, update_user_products
from schemas.user import UserCreate, UserResponse, UserUpdateProducts
from typing import List


router = APIRouter()

@router.post("/create-user/", response_model=UserResponse)
def create_user(user: UserCreate):
    try:
        new_user = register_user(user)
        return new_user
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/users/email/{user_email}", response_model=UserResponse)
def get_user_by_email_route(user_email: str):
    user_by_email = get_user_by_email(user_email)
    if not user_by_email:
        raise HTTPException(status_code=404, detail="User not found.")
    return user_by_email

@router.put("/users/email/{user_email}", response_model=UserResponse)
def update_user_products_route(user_email: str, update_data: UserUpdateProducts):
    try:
        updated_user = update_user_products(user_email, update_data)
        return updated_user
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

