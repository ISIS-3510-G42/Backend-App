from fastapi import FastAPI
from routers import post_router
from routers import user_router

app = FastAPI()

# Include routes here:
app.include_router(post_router.router, prefix="", tags=["posts"])
app.include_router(user_router.router, prefix="", tags=["users"])


@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI + Supabase E-commerce API!"}
