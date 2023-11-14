from ast import List
import datetime
from uuid import uuid4
from app.db.base_class import Base
from sqlalchemy import Column, DateTime, String, Text, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID


class Role(Base):
    __tablename__ = "role"
    id = Column(
        Integer, primary_key=True, index=True
    )
    name = Column(String(100), index=True)
    description = Column(Text)
    created_on = Column(DateTime, default=datetime.datetime.utcnow)
    updated_on = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
    )
    #users: List[User] = relationship(back_populates="user", secondary="user_role")
    #users = relationship("User", secondary="user_role", back_populates="role")
    users_role = relationship(
        "User",
        secondary="user_role",
        lazy="dynamic",
        back_populates="roles",
    )