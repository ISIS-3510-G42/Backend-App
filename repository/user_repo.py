from database import supabase
from schemas.user import UserCreate

# Crear usuario en Supabase
def create_user(user: UserCreate):
    response = supabase.table("user").insert({
        "name": user.name,
        "email": user.email,
        "postedProducts": user.postedProducts,
        "boughtProducts": user.boughtProducts
    }).execute()
    return response.data[0]

# Obtener usuario por email
def get_user_email(user_email: str):
    response = supabase.table("user").select("*").eq("email", user_email).execute()
    return response.data[0] if response.data else None