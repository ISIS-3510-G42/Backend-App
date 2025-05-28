from repository.user_repo import create_user, get_user_by_email, get_user_id, get_users, update_user
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

# Actualizar productos publicados y comprados de un usuario
def update_user_products(email: str, postedProducts: list, boughtProducts: list):
    return update_user(email, postedProducts, boughtProducts)
