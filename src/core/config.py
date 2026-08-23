import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    
    DUFFEL_API_KEY: str = os.getenv("DUFFEL_API_KEY")
    DUFFEL_BASE_URL: str = "https://api.duffel.com"

settings = Settings()