from repository.user_repo import create_user, get_user_id
from schemas.user import UserCreate

def register_user(user: UserCreate):
    return create_user(user)

def get_user_by_id(id):
    return get_user_id(id)