import datetime
from uuid import uuid4
from app.db.base_class import Base
from sqlalchemy import Column, DateTime, String, Text, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

class Permission(Base):
    __tablename__ = "permission"
    id = Column(
        Integer, primary_key=True, index=True
    )
    name = Column(String(100), index=True)
    description = Column(Text)
    module_id = Column(Integer, ForeignKey('module.id'), nullable=False)
    created_on = Column(DateTime, default=datetime.datetime.utcnow)
    updated_on = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
    )
    module = relationship("Module", lazy="selectin")