from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import get_db
from schemas.schema import BookingRequest
from controllers import create_booking, confirm_booking , get_booking_by_email_and_id

booking_router = APIRouter()

@booking_router.post("/create-booking")
def create_booking_route(req: BookingRequest, db: Session = Depends(get_db)):
    return create_booking(req, db)

@booking_router.get("/confirm-booking/{confirmation_id}")
def confirm_booking_route(confirmation_id: str, db: Session = Depends(get_db)):
    return confirm_booking(confirmation_id, db)




@booking_router.get("/booking/{email}/{confirmation_id}")
def get_booking_route(email: str, confirmation_id: str, db: Session = Depends(get_db)):
    return get_booking_by_email_and_id(email, confirmation_id, db)