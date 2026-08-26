import uuid
from sqlalchemy.orm import Session
from models.booking import Booking
from schemas.schema import BookingRequest
from integrations.email_service import send_confirmation_request_email, send_final_confirmation_email

def create_booking(req: BookingRequest, db: Session):
    booking = Booking(
        confirmation_id=str(uuid.uuid4())[:8],
        user_name=req.user_name,
        user_email=req.user_email,
        origin_city=req.origin_city,
        destination_city=req.destination_city,
        departure_date=req.departure_date,
        return_date=req.return_date,
        passengers=req.passengers,
        hotel_name=req.hotel_name,
        total_price=req.total_price,
        status="pending"
    )
    db.add(booking)
    db.commit()
    db.refresh(booking)

    confirm_link = f"http://127.0.0.1:8000/confirm-booking/{booking.confirmation_id}"
    send_confirmation_request_email(booking.user_email, confirm_link)

    return {"message": "Confirmation email sent", "confirmation_id": booking.confirmation_id}


def confirm_booking(confirmation_id: str, db: Session):
    booking = db.query(Booking).filter(Booking.confirmation_id == confirmation_id).first()
    if not booking:
        return {"error": "Booking not found"}

    booking.status = "confirmed"
    db.commit()

    send_final_confirmation_email(booking.user_email, booking.confirmation_id)
    return {"message": "Booking confirmed", "confirmation_id": booking.confirmation_id}


def get_booking_by_email_and_id(email: str, confirmation_id: str, db: Session):
    booking = db.query(Booking).filter(
        Booking.user_email == email,
        Booking.confirmation_id == confirmation_id
    ).first()
    if not booking:
        return {"message": "Booking not found"}
    return {
        "confirmation_id": booking.confirmation_id,
        "origin_city": booking.origin_city,
        "destination_city": booking.destination_city,
        "departure_date": booking.departure_date,
        "return_date": booking.return_date,
        "hotel_name": booking.hotel_name,
        "total_price": booking.total_price,
        "status": booking.status
    }