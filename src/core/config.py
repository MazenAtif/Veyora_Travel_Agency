import os
from dotenv import load_dotenv

load_dotenv()

class Settings:

    DUFFEL_API_KEY: str = os.getenv("DUFFEL_API_KEY")
    WEATHER_API_KEY: str =  os.getenv("WEATHER_API_KEY")
    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY")

    DUFFEL_BASE_URL: str = "https://api.duffel.com"
    WEATHER_BASE_URL: str = "https://www.weatherapi.com"

settings = Settings()