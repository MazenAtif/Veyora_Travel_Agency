from fastapi import FastAPI
from routes import flight_router 

app = FastAPI()

app.include_router(flight_router)