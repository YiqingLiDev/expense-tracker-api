from pydantic import BaseModel, EmailStr
# Separate models = clear input vs output logic

# For reading user data (e.g., return from /me)
class UserOut(BaseModel):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True # tells Pydantic to work with ORM objects

# For registration input:
class UserCreate(BaseModel):
    email: EmailStr
    password: str

# For login input:
class UserLogin(BaseModel):
    email: EmailStr
    password: str

