from fastapi import APIRouter
from pydantic import BaseModel
from starlette.responses import Response, JSONResponse
import datetime
import math


from src.models.parking_info_models import (
    NewParking,
    ParkingInfo,
    ExitParking
)

parking_info_router = APIRouter()


@parking_info_router.post("/parking_info/park")
def create_new_parking(new_parking: NewParking):
    # check if parking is available
    parking_availability = ParkingInfo.check_parking(new_parking)
    if parking_availability["parking_available"]:
        parking_info = ParkingInfo(
            vehicle_type = new_parking.vehicle_type,
            parking_id = new_parking.parking_id,
            vehicle_no= new_parking.vehicle_no,
        )
        created_parking_info_id = parking_info.save()
        print("New parking_info successfully created with id", parking_info)
        ParkingInfo.update_new_parking(new_parking)
        return {"status": "ok", "parking_info_id": created_parking_info_id, "parking_info": parking_info}
    else:
        return JSONResponse(status_code=404, content="No Parking Found")


@parking_info_router.post("/parking_info/exit_park")
def exit_parking(exit_parking: ExitParking):
    # fetch parking details parking is available
    parking_status = ParkingInfo.check_exit_parking(exit_parking)
    if parking_status["exist"]:
        print("parking_status[created_at]", parking_status["created_at"])
        hour_diff = datetime.datetime.now() - parking_status["created_at"]
        hour_diff = math.ceil(hour_diff.total_seconds()/3600)
        print("hour difference", hour_diff)
        rate = ParkingInfo.get_rate(exit_parking)
        due = hour_diff*rate
        ParkingInfo.update_exit_parking(exit_parking, due)
        return {"status": "ok", "due": due}
    else:
        return JSONResponse(status_code=404, content="No Parking Found")


@parking_info_router.get("/parking_info/vehicle_history")
def exit_parking(vehicle_no: str):
    return {"status": "ok"}
