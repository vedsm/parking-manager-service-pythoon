from fastapi import APIRouter
from pydantic import BaseModel

from src.models.parking_lot_models import ParkingLot

parking_lot_router = APIRouter()


@parking_lot_router.post("/parking_lot")
def create_parking_lot(parking_lot: ParkingLot):
    created_parking_lot_id = parking_lot.save()
    print("New parking_lot successfully created with id", created_parking_lot_id)
    return {"status": "ok", "parking_lot_id": created_parking_lot_id, "parking_lot": parking_lot}
