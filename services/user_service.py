from repository.user_repo import create_user, get_user_email, get_user_id
from schemas.user import UserCreate

#Clase de funciones de servicio intermedio de los usuarios
def register_user(user: UserCreate):
    return create_user(user)

def get_user_by_email(email: str):
    return get_user_email(email)

def get_user_by_id(id: int):
    return get_user_id(id)