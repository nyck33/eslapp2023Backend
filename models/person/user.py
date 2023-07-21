from fastapi import FastAPI
from pydantic import  BaseModel
from typing import Optional
from fastapi import HTTPException

class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None 
    

users_db = {}