from sqlalchemy import Column, String, Boolean
from ..db.database import Base as UserBase
    
class UserAlchemy(UserBase):
    __tablename__ = "User"
    
    username = Column(String, primary_key=True, index=True)
    email = Column(String)
    full_name = Column(String)
    disabled = Column(Boolean, default=False)
    hashed_password = Column(String)