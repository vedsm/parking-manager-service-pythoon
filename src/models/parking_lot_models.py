from pydantic import BaseModel
from typing import Optional
from datetime import datetime


from src.dao.db_config import (
    myclient,
    mydb,
)

parking_lot_collection = mydb.parking_lot

class ParkingLot(BaseModel):
    name: str
    address: Optional[str] = None
    capacity_0: int = 0
    capacity_1: int = 0
    created_at: datetime = datetime.now()

    def save(cls):
        print("saving parking_lot", cls.dict())
        created_parking_lot = parking_lot_collection.insert_one(cls.dict())
        created_parking_lot_id = created_parking_lot.inserted_id
        return str(created_parking_lot_id)

