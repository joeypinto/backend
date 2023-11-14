from app.db.base_class import Base
from sqlalchemy import Column, DateTime, String, Text, Integer, DECIMAL
import datetime
from sqlalchemy.orm import relationship

class Module(Base):  
    __tablename__ = "module"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=100), nullable=True)
    description = Column(String(length=255), nullable=True)    
    created_on = Column(DateTime, default=datetime.datetime.utcnow)    
    updated_on = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
    )
    permissions = relationship("Permission", lazy="selectin")