from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

# The central connection layer between your FastAPI app and your database
# It connects to the DB via SQLALchemy engine
# creating sessions (used in routes and services)
#  creating the base class for your models 

# 1. load env variables
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

# 2. Create the SQLAlchemy engine using your DB URL
# Connects to the database (opens the door)
engine = create_engine(DATABASE_URL)

# 3. Create a session factory to interact with the DB
# SessionLocal - Prepares individual waiters (sessions) to serve customers
# SessionLocal() will be called in route to create a new database connection instance 
# that lets your code read/write data using SQLAlchemy.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. Base class for all your models:
Base = declarative_base()


# This is a FastAPI dependency that provides a DB session per request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


