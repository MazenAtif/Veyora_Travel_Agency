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

def resolve_city(name: str) -> str | None:
    return CITY_TO_IATA.get(name.strip().lower())


class FlightSearchRequest(BaseModel):
    origin_city: str
    destination_city: str
    departure_date: str
    return_date: str | None = None
    passengers: int = 1