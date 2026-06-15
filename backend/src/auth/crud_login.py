from sqlalchemy.orm import Session
from src.models.admin import Admin
from .token import get_password_hash
from src.auth.schemas import RegisterRequest

def create_initial_admin(db: Session):
    DEFAULT_USERNAME = "admin"
    DEFAULT_PASSWORD = "admin1234"  
    
    existing_admin = db.query(Admin).filter(Admin.username == DEFAULT_USERNAME).first()
    
    if not existing_admin:

        print("--- DEBUG START (Initial Admin) ---")
        print(f"Password Value: {DEFAULT_PASSWORD}")
        print(f"Password Length: {len(DEFAULT_PASSWORD)}")

        hashed_pass = get_password_hash(DEFAULT_PASSWORD)
        
        new_admin = Admin(
            username=DEFAULT_USERNAME,
            hashed_password=hashed_pass
        )
        
        db.add(new_admin)
        db.commit()
        db.refresh(new_admin)
        print(f"✅ ادمین پیش‌فرض ({DEFAULT_USERNAME}) با موفقیت ساخته شد.")
    else:
        print(f"ℹ️ ادمین پیش‌فرض ({DEFAULT_USERNAME}) از قبل در دیتابیس موجود است.")


def create_admin(db: Session, admin_data: RegisterRequest):

    existing_admin = db.query(Admin).filter(Admin.username == admin_data.username).first()
    
    if not existing_admin:
        hashed_pass = get_password_hash(admin_data.password)
        
        new_admin = Admin(
            username=admin_data.username,
            hashed_password=hashed_pass
        )
        
        db.add(new_admin)
        db.commit()
        db.refresh(new_admin)
        print("✅ ادمین پیش‌فرض با موفقیت ساخته شد.")
    else:
        print("ℹ️ ادمین پیش‌فرض از قبل در دیتابیس موجود است.")

def get_admin_by_username(db: Session, username: str):
    existing_admin = db.query(Admin).filter(Admin.username == username).first()
    return existing_admin