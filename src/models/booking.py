from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from core.database import Base

class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    confirmation_id = Column(String, unique=True, index=True)
    user_name = Column(String)
    user_email = Column(String)
    origin_city = Column(String)
    destination_city = Column(String)
    departure_date = Column(String)
    return_date = Column(String, nullable=True)
    passengers = Column(Integer)
    hotel_name = Column(String, nullable=True)
    total_price = Column(Float)
    status = Column(String, default="pending")  # pending, confirmed
    created_at = Column(DateTime(timezone=True), server_default=func.now())