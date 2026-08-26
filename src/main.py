from fastapi import FastAPI
from routes import flight_router ,suggestion_router , booking_router

app = FastAPI()

app.include_router(flight_router)
app.include_router(suggestion_router)
app.include_router(booking_router)