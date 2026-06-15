from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.auth.admin_auth import get_current_admin
from src.auth import schemas
from src.config.database import get_db
from src.auth.schemas import LoginRequest, TokenResponse
from src.auth.token import create_access_token, verify_password
from src.models.admin import Admin
from src.auth import crud_login

router = APIRouter(prefix="/login", tags=["login"])

# Login route
@router.post("/", response_model=TokenResponse)
def login(login_data: LoginRequest, db: Session = Depends(get_db)):

    admin = crud_login.get_admin_by_username(db, login_data.username)
    if not admin or not verify_password(login_data.password, admin.hashed_password):
        raise HTTPException(status_code=401, detail="نام کاربری یا رمز عبور اشتباه است")
    
    token_data = {"sub": admin.username}
    access_token = create_access_token(data=token_data)

    return {"access_token": access_token, "token_type": "bearer"}

# Logout route

# Register route
@router.post("/register")
def register(register_data: schemas.RegisterRequest, db: Session = Depends(get_db)):
    if register_data.password != register_data.confirm_password:
        raise HTTPException(status_code=400, detail="رمز عبور و تأیید رمز عبور مطابقت ندارند")
    crud_login.create_admin(get_db(), register_data)
    
    return {"message": "ثبت نام با موفقیت انجام شد"}

@router.get("/me")
def get_me(current_admin: Admin = Depends(get_current_admin)):
    return {
        "id": current_admin.id,
        "username": current_admin.username
    }