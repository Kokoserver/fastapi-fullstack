from pydantic import BaseModel, EmailStr

class UserRegister(BaseModel):
    firstname:str
    lastname:str
    email:EmailStr
    phone:int
    password1:bytes
    password2:bytes

class UserLogin(BaseModel):
    email:EmailStr
    password:bytes


class ChangePassword(BaseModel):
    email:EmailStr
    password1:bytes
    password2:bytes


