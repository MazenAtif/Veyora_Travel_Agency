import httpx
from core.config import settings

async def search_flights(origin: str, destination: str, departure_date: str, return_date: str = None, passengers: int = 1, cabin_class: str = "economy"):
    headers = {
        "Authorization": f"Bearer {settings.DUFFEL_API_KEY}",
        "Duffel-Version": "v2",
        "Content-Type": "application/json"
    }

    slices = [{"origin": origin, "destination": destination, "departure_date": departure_date}]
    if return_date:
        slices.append({"origin": destination, "destination": origin, "departure_date": return_date})

    payload = {
        "data": {
            "slices": slices,
            "passengers": [{"type": "adult"} for _ in range(passengers)],
            "cabin_class": cabin_class
        }
    }

    async with httpx.AsyncClient() as client:
        resp = await client.post(f"{settings.DUFFEL_BASE_URL}/air/offer_requests", json=payload, headers=headers)
        resp.raise_for_status()
        return resp.json()