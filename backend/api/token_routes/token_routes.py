from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from backend.auth.token_handler import create_access_token
from ...utils.utils import get_current_active_user
from ...models.alchemy_models import UserAlchemy
from ...models.token import Token
from ...auth.auth import authenticate_user
from ...models.user_model import UserInDB
from fastapi import Depends
from datetime import timedelta
from typing import Annotated
import os
from dotenv import load_dotenv
from ...db.database import get_db
from sqlalchemy.orm import Session

load_dotenv()

router = APIRouter(
    prefix="/token",
    tags=["token_operations"]
)

@router.post("/")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Annotated[Session, Depends(get_db)],
) -> Token:
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")))
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")


@router.get("/me", response_model=UserInDB)
async def read_users_me(
    current_user: Annotated[UserAlchemy, Depends(get_current_active_user)],
):
    return current_user