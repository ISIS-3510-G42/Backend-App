from database import supabase
from schemas.user import UserCreate

def create_user(user: UserCreate):
    response = supabase.table("user").insert({
        "name": user.name,
        "email": user.email,
        "postedProducts": user.postedProducts,
        "boughtProducts": user.boughtProducts
    }).execute()
    return response.data[0]

def get_user_id(user_id: int):
    response = supabase.table("user").select("*").eq("id", user_id).execute()
    return response.data[0] if response.data else None

