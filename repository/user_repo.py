from database import supabase
from schemas.user import UserCreate

#Crear los usuarios en la base de datos de supabase
def create_user(user: UserCreate):
    response = supabase.table("user").insert({
        "name": user.name,
        "email": user.email,
        "postedProducts": user.postedProducts,
        "boughtProducts": user.boughtProducts
    }).execute()
    return response.data[0]

#Retornar un usuario por email
def get_user_email(user_email: str):
    response = supabase.table("user").select("*").eq("email", user_email).execute()
    return response.data[0] if response.data else None

#Retornar un usuario por id
def get_user_id(user_id: int):
    response = supabase.table("user").select("*").eq("id", user_id).execute()
    return response.data[0] if response.data else None