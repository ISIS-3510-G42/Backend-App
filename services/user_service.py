from repository.user_repo import create_user, get_user_email, update_user_products_by_email
from schemas.user import UserCreate, UserUpdateProducts

# Funciones de servicio
def register_user(user: UserCreate):
    return create_user(user)

def get_user_by_email(email):
    return get_user_email(email)

def update_user_products(email: str, update_data: UserUpdateProducts):
    return update_user_products_by_email(email, update_data)
