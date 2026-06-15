from sqlalchemy.orm import Session
from src.models.admin import Admin
from .token import get_password_hash
from src.auth.schemas import RegisterRequest
from src.config.config import settings

def create_initial_admin(db: Session):
    
    
    existing_admin = db.query(Admin).filter(Admin.username == settings.DEFAULT_ADMIN_USERNAME).first()
    
    if not existing_admin:

        hashed_pass = get_password_hash(settings.DEFAULT_ADMIN_PASSWORD)
        
        new_admin = Admin(
            username=settings.DEFAULT_ADMIN_USERNAME,
            hashed_password=hashed_pass
        )
        
        db.add(new_admin)
        db.commit()
        db.refresh(new_admin)
        print(f"✅ ادمین پیش‌فرض ({settings.DEFAULT_ADMIN_USERNAME}) با موفقیت ساخته شد.")
    else:
        print(f"ℹ️ ادمین پیش‌فرض ({settings.DEFAULT_ADMIN_USERNAME}) از قبل در دیتابیس موجود است.")


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
        print(f"✅ ادمین ({admin_data.username}) با موفقیت ساخته شد.")
    else:
        print(f"ℹ️ ادمین ({admin_data.username}) از قبل در دیتابیس موجود است.")

def get_admin_by_username(db: Session, username: str):
    existing_admin = db.query(Admin).filter(Admin.username == username).first()
    return existing_admin