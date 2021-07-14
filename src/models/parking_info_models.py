from pydantic import BaseModel
from typing import List, Dict, Optional
from datetime import datetime
from bson.objectid import ObjectId


from src.models.parking_lot_models import parking_lot_collection
from src.models.rate_card_models import rate_card_collection


from src.dao.db_config import (
    myclient,
    mydb,
)

parking_info_collection = mydb.parking_info

DEFAULT_RATE = 10

class NewParking(BaseModel):
    vehicle_type: int
    parking_id: str
    vehicle_no: str

class ExitParking(BaseModel):
    vehicle_type: int
    parking_id: str
    vehicle_no: str

class ParkingInfo(BaseModel):
    vehicle_type: int
    parking_id: str
    vehicle_no: str
    created_at: datetime = datetime.now()
    closed_at: Optional[datetime]
    due: Optional[int]

    def update_exit_parking(exit_parking, due):
        print("toupdate parkig info")
        print("toreduce the parking count")


    def check_exit_parking(exit_parking):
        print("check the available capacity of the parking lot", exit_parking.parking_id)
        parking_info = parking_info_collection.find_one({"parking_id": exit_parking.parking_id, "vehicle_no":exit_parking.vehicle_no})
        print("parking_info found", parking_info)
        if parking_info == None:
            return {
                "exist": False
            }
        else:
            return {
                "exist": True,
                "created_at": parking_info["created_at"]
            }
    
    def get_rate(exit_parking):
        rate_card = rate_card_collection.find_one({"parking_id": exit_parking.parking_id, "vehicle_type": exit_parking.vehicle_type})
        print("rate_card found", rate_card)
        if rate_card == None:
            return DEFAULT_RATE
        else:
            return rate_card["rate"]


    
    def check_parking(new_parking):
        print("check the available capacity of the parking lot", new_parking.parking_id)
        parking_lot = parking_lot_collection.find_one({"_id": ObjectId(new_parking.parking_id)})
        print("parking_lot found", parking_lot)
        parking_capacity = 0
        if new_parking.vehicle_type == 0:
            parking_capacity = parking_lot["capacity_0"]
        else:
            parking_capacity = parking_lot["capacity_1"]
        print("parking_capacity found", parking_capacity)
        if parking_capacity == 0:
            return {
                "parking_available": False
            }
        else:
            rate_card = rate_card_collection.find_one({"parking_id": new_parking.parking_id, "vehicle_type": new_parking.vehicle_type})
            print("rate_card found", rate_card)
            if rate_card == None:
                return {
                    "parking_available": True,
                    "rate": DEFAULT_RATE
                }
            return {
                "parking_available": True,
                "rate": rate_card["rate"]
            }
    def save(cls):
        print("saving parking_info", cls.dict())
        created_parking_info = parking_info_collection.insert_one(cls.dict())
        created_parking_info_id = created_parking_info.inserted_id
        return str(created_parking_info_id)
    
    def update_new_parking(parking_info):
        print("To update parking info", parking_info)
        if parking_info.vehicle_type==0:
            parking_lot = parking_lot_collection.update_one(
                {"_id": ObjectId(parking_info.parking_id)},
                {
                    '$inc': {
                        "capacity_0": -1
                    }
                }
                )
        else:
            parking_lot = parking_lot_collection.update_one(
                {"_id": ObjectId(parking_info.parking_id)},
                {
                    '$inc': {
                        "capacity_1": -1
                    }
                }
                )






class SettlementEntry(BaseModel):
    payer: str
    payee: str
    amount: int
    currency: Optional[str] = "INR"

class Balance(BaseModel):
    payer: str
    payee: str
    amount: int
    currency: Optional[str] = "INR"

    def save(cls):
        print("saving balance", cls.dict())
        created_balance = balance_collection.insert_one(cls.dict())
        created_balance_id = created_balance.inserted_id
        return str(created_balance_id)
    
    def search_for_payer(user_id):
        balances = list(balance_collection.find({"payer": str(user_id)}))
        print("found balances", balances, user_id)
        return_balances = []
        for balance in balances:
            return_balances.append(Balance(**balance))
        print("found return_balances", return_balances)
        return return_balances

    def search_for_payee(user_id):
        balances = list(balance_collection.find({"payee": str(user_id)}))
        print("found balances", balances, user_id)
        return_balances = []
        for balance in balances:
            return_balances.append(Balance(**balance))
        print("found return_balances", return_balances)
        return return_balances

class ExpenseMaster(BaseModel):
    type_of_expense: int
    amount: int
    currency: Optional[str] = "INR"
    created_by: str
    share_type: Optional[int]
    share_division: Optional[Dict]

    def save(cls):
        print("saving expense_master", cls.dict())
        created_expense_master = expense_master_collection.insert_one(cls.dict())
        created_expense_master_id = created_expense_master.inserted_id
        return str(created_expense_master_id)
