import bcrypt
from jose import jwt
from datetime import datetime, timedelta, timezone
from src.config.config import settings
# در فایل token.py یا security.py
def get_password_hash(password: str) -> str:
    
    password_bytes = password.encode('utf-8')
    
    salt = bcrypt.gensalt()
    
    hashed_password_bytes = bcrypt.hashpw(password_bytes, salt)
    
    return hashed_password_bytes.decode('utf-8')

def verify_password(hashed_password:str,plain_password:str):
    hashed_password_bytes = hashed_password.encode('utf-8')
    plain_password_bytes = plain_password.encode('utf-8')
    
    return bcrypt.checkpw(plain_password_bytes, hashed_password_bytes)

def create_access_token(data: dict,)-> str: 
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt