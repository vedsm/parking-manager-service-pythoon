from pydantic import BaseModel
from typing import Optional
from datetime import datetime


from src.dao.db_config import (
    myclient,
    mydb,
)

rate_card_collection = mydb.rate_card

class RateCard(BaseModel):
    parking_id: str
    vehicle_type: int
    rate: int
    created_at: datetime = datetime.now()

    def save(cls):
        print("saving rate_card", cls.dict())
        created_rate_card = rate_card_collection.insert_one(cls.dict())
        created_rate_card_id = created_rate_card.inserted_id
        return str(created_rate_card_id)

