from fastapi import FastAPI
from app.routers import auth
from app.db.database import engine, Base

app = FastAPI()

# Temporarily
# This line will create all tables based on your models
Base.metadata.create_all(bind=engine)


app.include_router(auth.router)
