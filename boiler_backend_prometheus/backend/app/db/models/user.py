from ast import List
import datetime
from uuid import uuid4
from app.db.models.role import Role
from sqlalchemy.dialects.postgresql import UUID
from app.db.base_class import Base
from sqlalchemy import Boolean, Column, DateTime, String, Integer
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "user"
    """
    Database Model for an application user
    """
    id = Column(
        Integer, primary_key=True, index=True
    )
    username = Column(String(255), index=True)
    email = Column(String(100), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)
    is_active = Column(Boolean(), default=True)    
    first_name = Column(String(255))
    last_name = Column(String(255))
    created_on = Column(DateTime, default=datetime.datetime.utcnow)
    updated_on = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
    )
    roles = relationship(
        "Role",
        secondary="user_role",
        lazy="selectin",
        back_populates="users_role",
    )