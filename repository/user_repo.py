from database import supabase
from schemas.user import UserCreate

# Crear usuario en Supabase
def create_user(user: UserCreate):
    response = supabase.table("users").insert({
        "name": user.name,
        "email": user.email,
        "postedProducts": user.postedProducts,
        "boughtProducts": user.boughtProducts
    }).execute()
    return response.data[0]

# Actualizar productos publicados y comprados de un usuario
def update_user(user_email: str, postedProducts: list, boughtProducts: list):
    response = supabase.table("users").update({
        "postedProducts": str(postedProducts),  # Asegúrate de convertir en cadena
        "boughtProducts": str(boughtProducts)   # Asegúrate de convertir en cadena
    }).eq("email", user_email).execute()
    return response.data[0] if response.data else None

# Obtener todos los usuarios
def get_users():
    response = supabase.table("users").select("*").execute()
    return response.data

# Obtener usuario por email
def get_user_by_email(user_email: str):
    response = supabase.table("users").select("*").eq("email", user_email).execute()
    return response.data[0] if response.data else None

# Obtener usuario por ID
def get_user_id(user_id: int):
    response = supabase.table("users").select("*").eq("id", user_id).execute()
    return response.data[0] if response.data else None
