from fastapi import HTTPException
from schemas.schema import resolve_city, FlightSearchRequest
from integrations.duffel import search_flights



async def handle_flight_search(req: FlightSearchRequest):
    origin_code = resolve_city(req.origin_city)
    dest_code = resolve_city(req.destination_city)

    if not origin_code or not dest_code:
        raise HTTPException(status_code=400, detail="City not recognized")

    result = await search_flights(
        origin_code, dest_code, req.departure_date, req.return_date, req.passengers
    )

    offers = result.get("data", {}).get("offers", [])[:3]
    simplified = [
        {
            "airline": o["slices"][0]["segments"][0]["operating_carrier"]["name"],
            "price": o["total_amount"],
            "currency": o["total_currency"],
            "duration": o["slices"][0]["duration"]
        }
        for o in offers
    ]
    return {"flights": simplified}