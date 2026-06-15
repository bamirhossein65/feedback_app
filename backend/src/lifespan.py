from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.config.database import SessionLocal
from src.auth.crud_login import create_initial_admin

@asynccontextmanager
async def database_lifespan(app: FastAPI):
    
    db = SessionLocal()
    try:
        create_initial_admin(db=db)
    finally:
        db.close()
        
    yield