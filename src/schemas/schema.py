from pydantic import BaseModel

CITY_TO_IATA = {
    "cairo": "CAI",
    "القاهرة": "CAI",

    "paris": "CDG",
    "باريس": "CDG",

    "tokyo": "HND",
    "طوكيو": "HND",

    "kyoto": "UKY",  # no major airport, nearest is Osaka (KIX)
    "كيوتو": "UKY",

    "bali": "DPS",
    "بالي": "DPS",

    "rome": "FCO",
    "روما": "FCO",

    "amalfi": "NAP",  # nearest airport Naples
    "أمالفي": "NAP",

    "dubai": "DXB",
    "دبي": "DXB",
}
CITY_RATINGS = {
    "cairo": 4.3,
    "paris": 4.7,
    "tokyo": 4.6,
    "bali": 4.5,
    "rome": 4.6,
    "dubai": 4.4,
}

def resolve_city(name: str) -> str | None:
    return CITY_TO_IATA.get(name.strip().lower())


class FlightSearchRequest(BaseModel):
    origin_city: str
    destination_city: str
    departure_date: str
    return_date: str | None = None
    passengers: int = 1


class SuggestionRequest(BaseModel):
    origin_city: str
    budget: float
    departure_date: str


class BookingRequest(BaseModel):
    user_name: str
    user_email: str
    origin_city: str
    destination_city: str
    departure_date: str
    return_date: str | None = None
    passengers: int = 1
    hotel_name: str | None = None
    total_price: float