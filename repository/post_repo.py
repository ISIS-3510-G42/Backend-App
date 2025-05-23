from database import supabase
from schemas.post import PostCreate

def create_post(post: PostCreate):
    response = supabase.table("post").insert({
        "name": post.name,
        "brand": post.brand,
        "category": post.category,
        "image": post.image,
        "color": post.color,
        "size": post.size,
        "group": post.group,
        "price": post.price
    }).execute()
    return response.data[0]

def get_posts():
    response = supabase.table("post").select("*").execute()
    return response.data

def get_posts_by_categ(category_name):
    print(category_name)
    # Query to fetch clothing items by category
    response = supabase.table("post").select("*").eq("category", category_name).execute()
    return response.data

def get_post_id(post_id: int):
    response = supabase.table("post").select("*").eq("id", post_id).execute()
    return response.data[0] if response.data else None
