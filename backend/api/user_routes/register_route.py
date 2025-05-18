from fastapi import APIRouter
from sqlalchemy.orm import Session
from backend.db.database import get_db
from backend.utils.crud_user import userCreator
from ...models.user_model import User, UserRegisterRequest
from fastapi import Depends
from fastapi import HTTPException

router = APIRouter(
    prefix="/register",
    tags=["register_operations"]
)


@router.post("/")
async def create_user(payload: UserRegisterRequest, db: Session = Depends(get_db)):
    if payload.password != payload.confirmPassword:
        raise HTTPException(status_code=400, detail="Passwords do not match")

    user = User(username=payload.username, email=payload.email, full_name="")
    userCreator(user, payload.password, payload.email, db=db)
    return {"message": "User created successfully"}


