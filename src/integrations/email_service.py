import resend
from core.config import settings

resend.api_key = settings.RESEND_API_KEY

def send_confirmation_request_email(to_email: str, confirm_link: str):
    resend.Emails.send({
        "from": "onboarding@resend.dev",
        "to": to_email,
        "subject": "Confirm Your Veyora Trip Booking",
        "html": f"<p>Please confirm your trip booking by clicking the link below:</p><a href='{confirm_link}'>Confirm Booking</a>"
    })

def send_final_confirmation_email(to_email: str, confirmation_id: str):
    resend.Emails.send({
        "from": "onboarding@resend.dev",
        "to": to_email,
        "subject": "Booking Confirmed - Veyora Travel Agency",
        "html": f"<p>Your trip is confirmed!</p><p>Confirmation ID: <b>{confirmation_id}</b></p>"
    })