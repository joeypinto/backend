import datetime
from app.db.base_class import Base
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime

    
class UserLocation(Base):
    __tablename__ = "user_location"
    
    id = Column(
        Integer, primary_key=True, index=True
    )
    user_id = Column(
        Integer,
        ForeignKey("user.id", ondelete="CASCADE"),
        primary_key=True,
        nullable=False,
    )
    location_id = Column(String(250), nullable=True)
    location = Column(String(250), nullable=True)
    created_on = Column(DateTime, default=datetime.datetime.utcnow)
    updated_on = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
    )