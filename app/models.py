from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, LargeBinary
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean(), default=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    created_at = Column(String)
    is_active_email = Column(Boolean(), default=False)
    userType = Column(String, default="free")
    userImage = Column(LargeBinary)