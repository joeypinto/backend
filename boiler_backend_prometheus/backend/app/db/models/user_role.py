from app.db.base_class import Base
import datetime
from sqlalchemy import Column, ForeignKey, UniqueConstraint, Integer, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class UserRole(Base):
    __tablename__ = "user_role"
    user_id = Column(
        Integer,
        ForeignKey("user.id", ondelete="CASCADE"),
        primary_key=True,
        nullable=False,
    )
    role_id = Column(
        Integer,
        ForeignKey("role.id", ondelete="CASCADE"),
        primary_key=True,
        nullable=False,
    )
    created_on = Column(DateTime, default=datetime.datetime.utcnow)
    updated_on = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
    )
    __table_args__ = (
        UniqueConstraint("user_id", "role_id", name="unique_user_role"),
    )
