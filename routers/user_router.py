from fastapi import APIRouter, HTTPException
from services.user_service import register_user, get_user_by_email
from schemas.user import UserCreate, UserResponse

router = APIRouter()

@router.post("/create-user/", response_model=UserResponse)
def create_user(user: UserCreate):
    try:
        new_user = register_user(user)
        return new_user
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/users/{user_email}", response_model=UserResponse)
def get_user_by_email_route(user_email: str):
    user = get_user_by_email(user_email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")
    return user
