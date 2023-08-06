from fastapi import FastAPI
from pydantic import  BaseModel
from typing import Optional
from fastapi import HTTPException

from database import init_db


app = FastAPI(title="eslapp_backend", description="Backend for ESL App", version="1.0.0")

init_db(app)




