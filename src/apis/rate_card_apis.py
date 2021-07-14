from fastapi import APIRouter
from pydantic import BaseModel

from src.models.rate_card_models import RateCard

rate_card_router = APIRouter()


@rate_card_router.post("/rate_card")
def create_rate_card(rate_card: RateCard):
    # checkif parking_id
    created_rate_card_id = rate_card.save()
    print("New rate_card successfully created with id", created_rate_card_id)
    return {"status": "ok", "rate_card_id": created_rate_card_id, "rate_card": rate_card}


