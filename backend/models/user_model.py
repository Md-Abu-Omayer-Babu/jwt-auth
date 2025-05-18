from pydantic import BaseModel

class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


class UserInDB(User):
    hashed_password: str
    

class UserRegisterRequest(BaseModel):
    username: str
    email: str
    password: str
    confirmPassword: str

    
