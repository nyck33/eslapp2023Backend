from fastapi import FastAPI
from pydantic import  BaseModel
from typing import Optional
from fastapi import HTTPException

class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None 
    

app = FastAPI()

users_db = {}

@app.get("/")
async def root():
    return {"message": "Hello World"}

#parses User model from request body JSON
@app.post("/users/")
async def create_user(user: User):
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="Username already registered")
    users_db[user.username] = user
    return user

@app.get("/users/{username}")
async def read_user(username: str):
    if username not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return users_db[username]

