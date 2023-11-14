from datetime import datetime
from app.db.base_class import Base
from sqlalchemy import Column, DateTime, String, Text, Integer, DECIMAL, ForeignKey, Boolean
from sqlalchemy.dialects.postgresql import JSON

class Logging(Base):  
    __tablename__ = "logging"

    id = Column(
        Integer, primary_key=True, index=True
    )
    table = Column(String(50), index=True)
    record_id = Column(Integer)
    action = Column(String(50), index=True)
    old = Column(JSON)
    new = Column(JSON)
    user_id = Column(Integer)
    ip_address = Column(String(50), index=True)
    created_on = Column(DateTime, default=datetime.datetime.utcnow)
    updated_on = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
    )