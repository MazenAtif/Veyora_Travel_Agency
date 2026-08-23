from fastapi import APIRouter
from schemas.schema import FlightSearchRequest
from controllers import handle_flight_search

flight_router = APIRouter()

@flight_router.post("/search-flight")
async def search_flight(req: FlightSearchRequest):
    return await handle_flight_search(req)