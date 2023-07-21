from fastapi import FastAPI
from pydantic import  BaseModel
from typing import Optional
from fastapi import HTTPException

class Student(BaseModel):
    userid: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None