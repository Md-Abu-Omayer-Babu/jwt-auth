from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer
from ..utils.password_utils import verify_password, get_password_hash
from ..db.database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends
from datetime import datetime, timedelta, timezone
from ..models.alchemy_models import UserAlchemy
import os
from dotenv import load_dotenv
from typing import Annotated
from ..models.token import TokenData
from ..utils.utils import getUserByUsername
from ..models.user_model import UserInDB
from fastapi import HTTPException, status

load_dotenv()

SECRET_KEY=os.getenv("SECRET_KEY")
ALGORITHM=os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES=os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def authenticate_user(username: str, password: str, db: Session):
    user = db.query(UserAlchemy).filter(UserAlchemy.username == username).first()
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user




