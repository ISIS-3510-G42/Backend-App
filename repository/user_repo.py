from database import supabase
from schemas.user import UserCreate, UserUpdateProducts

# Crear usuario en Supabase
def create_user(user: UserCreate):
    response = supabase.table("users").insert({
        "name": user.name,
        "email": user.email,
        "postedProducts": user.postedProducts,
        "boughtProducts": user.boughtProducts
    }).execute()
    return response.data[0]

# Obtener usuario por email
def get_user_email(user_email: str):
    response = supabase.table("users").select("*").eq("email", user_email).execute()
    return response.data[0] if response.data else None

# Actualizar productos del usuario segun el email
def update_user_products_by_email(email: str, update_data: UserUpdateProducts):
    update_fields = {}
    if update_data.postedProducts is not None:
        update_fields["postedProducts"] = update_data.postedProducts
    if update_data.boughtProducts is not None:
        update_fields["boughtProducts"] = update_data.boughtProducts

    if not update_fields:
        raise ValueError("No fields to update.")

    response = supabase.table("users").update(update_fields).eq("email", email).execute()
    if not response.data:
        raise ValueError("User update failed.")
    return response.data[0]
