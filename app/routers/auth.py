from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserLogin, UserOut
from app.models.user import User
from app.db.database import get_db # todo
from app.core.security import hash_password, verify_password, create_access_token
from fastapi.security import OAuth2PasswordRequestForm
from app.core.oauth2 import get_current_user # todo


router = APIRouter(prefix="/auth", tags=["Auth"])
# Register a new user
# Depends(): Before running this route, automatically run the get_db() function, and give me a SQLAlchemy session (db) to use in the function.”
@router.post("/register", response_model=UserOut)
def register(user_data: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.email == user_data.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    user = User(
        email = user_data.email,
        hashed_password=hash_password(user_data.password)
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

# Login and return a JWT token
# @router.post("/login")
# def login(user_data: UserLogin, db: Session = Depends(get_db)):
#     user = db.query(User).filter(User.email == user_data.email).first()
#     if not user or not verify_password(user_data.password, user.hashed_password):
#         raise HTTPException(status_code=401, detail="Invalid credentials")
    
#     token = create_access_token(data={"sub": str(user.id)})
#     return {"access_token": token, "token_type": "bearer"}
@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # OAuth2PasswordRequestForm expects 'username' and 'password' fields in form-data
    user = db.query(User).filter(User.email == form_data.username).first()
    
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = create_access_token(data={"sub": str(user.id)})
    return {"access_token": token, "token_type": "bearer"}

# Get the current logged-in user's info
@router.get("/me", response_model=UserOut)
def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user


