import httpx
from core.config import settings
import asyncio

async def get_weather(city: str):
    params = {
        "key": settings.WEATHER_API_KEY,
        "q": city,
        "days": 1
    }
    async with httpx.AsyncClient() as client:
        resp = await client.get("http://api.weatherapi.com/v1/forecast.json", params=params)
        resp.raise_for_status()
        data = resp.json()
        return {
            "city": city,
            "temp_c": data["current"]["temp_c"],
            "condition": data["current"]["condition"]["text"]
        }

#parallel fetch
async def get_weather_for_cities(cities: list[str]):
    results = await asyncio.gather(*[get_weather(c) for c in cities])
    return results