# This is a repository for my service

Follow the Makefile.
```
make run_event_receiver
make package
make publish
make deploy
```

Refer wiki for pipi access token setup->


### Problem Statement :
* We want to build a parking lot management application. Multiple parking lots will be using this to manage their operations.
* There are two primary types of vehicles. Two Wheelers and Four Wheelers.
* Each parking lot can accommodate a number of 2 and 4 wheelers.
A parking lot can have its own rate card for these vehicles. A rate card will be hourly.

1. Create a parking lot with capacity for each type of vehicle
2. Create a rate card for each kind of vehicle to the above parking lot
3. Park a vehicle when there is capacity available
4. Attempt to park a vehicle when there is no capacity available
5. Exit a vehicle from the lot. Tell the amount due for the duration that the vehicle is parked
6. Given a vehicle number, see complete parking history across all lots


### User Scenarios (APIs)
* Create a parking lot
    * Request:
        1. name str
        2. address str (optional)
        3. capacity_0: int
        4. capacity_1: int
    * Response:
        1. parking_id
        2. created_at
* Create a rate card
    * Request:
        1. parking_id: str
        2. vehicle_type: int (0:2 wheeler | 1:4 wheeler)
        3. rate
    * Response:
        1. parking_id
        2. created_at
* Park a vehicle(when capacity is available and when capacity is not available)
    * Request:
        1. vehicle_type: int (0:2 wheeler | 1:4 wheeler)
        2. parking_id: str
        3. vehicle_no: str
    * Response: (200 status or 404 status code)
        1. message: str
        2. created_at
* Exit a vehicle from the lot & Tell the amount due.
    * Request:
        1. vehicle_type: int (0:2 wheeler | 1:4 wheeler)
        2. parking_id: str
        3. vehicle_no: str
    * Response: (200 status or 404 status code)
        1. message: str
        2. due:
        3. closed_at
* See complete parking history of a vehicle_no
    * Request:
        1. vehicle_no: str
    * Response: (200 status or 404 status code)
        1. history: [{
            * parking_id
            * vehicle_type
            * created_at
            * closed_at
            * due

### Models
* parking_lot:
    * id
    * name str
    * address str (optional)
    * created_at
    * capacity_0: int
    * capacity_1: int
    * current_capacity_0: int
    * current_capacity_1: int
* rate_card:
    * parking_id: str
    * vehicle_type: int (0:2 wheeler | 1:4 wheeler)
    * rate: int
    * created_at
* parking_info:
    * vehicle_type: int (0:2 wheeler | 1:4 wheeler)
    * parking_id: str
    * vehicle_no: str
    * created_at: date
    * closed_at: date
    * due

