from fastapi import APIRouter, HTTPException
from services.user_service import register_user, get_user_by_email, get_user_by_id, get_all_users
from schemas.user import UserCreate, UserResponse
from typing import List


router = APIRouter()

@router.post("/create-user/", response_model=UserResponse)
def create_user(user: UserCreate):
    try:
        new_user = register_user(user)
        return new_user
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/users", response_model=List[UserResponse])
def get_all_usersClothing():
    try:
        all_users = get_all_users()
        return all_users
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/users/email/{user_email}", response_model=UserResponse)
def get_user_by_email_route(user_email: str):
    user_by_email = get_user_by_email(user_email)
    if not user_by_email:
        raise HTTPException(status_code=404, detail="User not found.")
    return user_by_email

@router.get("/users/{user_id}", response_model=UserResponse)
def get_user_by_id_route(user_id: int):
    user = get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")
    return user
