from fastapi import APIRouter
from backend.auth.auth import authenticate_user
from fastapi import HTTPException
from fastapi import status
from backend.models.user_model import UserInDB
from backend.models.alchemy_models import UserAlchemy
from backend.auth.token_handler import create_access_token
from backend.utils.utils import get_current_active_user
from backend.auth.token_handler import Depends
from backend.auth.token_handler import Session
from backend.db.database import get_db
from backend.utils.crud_user import getUserByUsername

router = APIRouter(
    prefix="/login",
    tags=["login_operations"]
)

@router.post("/")
async def login(username: str, password: str, db: Session = Depends(get_db)):
    user = authenticate_user(username, password, db)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/get-user")
async def get_user(current_user: UserAlchemy = Depends(get_current_active_user)):
    return {
        "username": current_user.username,
        "email": current_user.email,
        "fullname": current_user.full_name,
        "hashed_password": current_user.hashed_password
    }
    
@router.post("/get-user")
async def getUser(username: str, password: str, db: Session = Depends(get_db), current_user: UserInDB = Depends(get_current_active_user)):
    user = getUserByUsername(username, password, db=db)
    if not user:
        return {"message": "Invalid username or password"}
    return user
