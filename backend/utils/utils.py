from jose import JWTError, jwt
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

from backend.models.alchemy_models import UserAlchemy
from ..models.token import TokenData
from backend.utils.crud_user import getUserByUsername
from ..models.user_model import UserInDB
from typing import Annotated
from dotenv import load_dotenv
import os
from fastapi import status
from ..db.database import get_db
from sqlalchemy.orm import Session
from backend.auth.token_handler import get_current_user



oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


load_dotenv()

SECRET_KEY=os.getenv("SECRET_KEY")
ALGORITHM=os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES=os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")


async def get_current_active_user(
    current_user: Annotated[UserAlchemy, Depends(get_current_user)]
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

