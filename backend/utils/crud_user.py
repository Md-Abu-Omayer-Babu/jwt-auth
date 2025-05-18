from sqlalchemy.orm import Session
from ..models.alchemy_models import UserAlchemy
from ..models.user_model import UserInDB, User
from ..utils.password_utils import get_password_hash, verify_password
from ..db.database import get_db
from fastapi import Depends
from fastapi import HTTPException, status


def userCreator(user: User, password: str, email: str, db: Session = Depends(get_db)):
    if db.query(UserAlchemy).filter(UserAlchemy.username == user.username).first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists")
    
    hashed_password = get_password_hash(password)
    db_user = UserInDB(**user.model_dump(), hashed_password=hashed_password)
    user_with_hashed_pwd = UserAlchemy(**db_user.model_dump())
    
    db.add(user_with_hashed_pwd)
    db.commit()
    db.refresh(user_with_hashed_pwd)
    return user_with_hashed_pwd


def getUserByUsername(username: str, password: str, db: Session = Depends(get_db)):
    user = db.query(UserAlchemy).filter(UserAlchemy.username == username).first()
    if not user:
        return None
    if not verify_password(hashed_password=user.hashed_password, plain_password=password):
        return None
    return user

def getUserByUsernameWithoutPassword(username: str, db: Session):
    return db.query(UserAlchemy).filter(UserAlchemy.username == username).first()
