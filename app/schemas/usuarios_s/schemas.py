from typing import Optional
from pydantic import BaseModel
class User(BaseModel):
    id:Optional [int] 
    username:str
    password:str
    email:str

    class Config:
        orm_mode = True

class UserUpdate(BaseModel):
    username:str

    class Config:
        orm_mode = True

class User_Validate(BaseModel):
    username:str
    password:str

    class Config:
        orm_mode = True

class Respuesta(BaseModel):
    mensaje:str

    