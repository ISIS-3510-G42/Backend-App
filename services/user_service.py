from repository.user_repo import create_user, get_user_by_emai, get_user_id, get_users
from schemas.user import UserCreate

# Funciones de servicio
def register_user(user: UserCreate):
    return create_user(user)

def get_all_users():
    return get_users()  

def get_user_by_email(email):
    return get_user_by_emai(email)

def get_user_by_id(user_id):
    return get_user_id(user_id)