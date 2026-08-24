from fastapi import APIRouter
from schemas.schema import SuggestionRequest
from controllers.suggestion_controller import get_best_destinations

suggestion_router = APIRouter()

@suggestion_router.post("/best-destination")

async def best_destination(req: SuggestionRequest):
    return await get_best_destinations(req)