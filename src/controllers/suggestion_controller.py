from integrations.weather import get_weather_for_cities
from integrations.ai_ranker import rank_destinations
from integrations.duffel import search_flights
from schemas.schema import CITY_RATINGS, CITY_TO_IATA, resolve_city, SuggestionRequest

async def get_best_destinations(req: SuggestionRequest):
    english_cities = ["cairo", "paris", "tokyo", "bali", "rome", "dubai"]
    destinations = [c for c in english_cities if c != req.origin_city.lower()]

    weather_data = await get_weather_for_cities(destinations)

    origin_code = resolve_city(req.origin_city)

    affordable = []
    for dest in weather_data:
        dest["rating"] = CITY_RATINGS.get(dest["city"])
        dest_code = CITY_TO_IATA.get(dest["city"])

        try:
            result = await search_flights(origin_code, dest_code, req.departure_date)
            offers = result.get("data", {}).get("offers", [])
            if offers:
                price = float(offers[0]["total_amount"])
                dest["price"] = price
                if price <= req.budget:
                    affordable.append(dest)
        except Exception:
            continue

    if not affordable:
        return {"destinations": [], "ai_suggestion": "No destinations found within your budget."}

    ai_suggestion = await rank_destinations(affordable)
    return {"destinations": affordable, "ai_suggestion": ai_suggestion}