from starlette.testclient import TestClient

from src.main import app


client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_parking_lot():
    response = client.post(
        "/parking_lot",
        json={
            "name": "my_parking",
            "capacity_0": 10,
            "capacity_1": 5
        }
        )
    assert response.status_code == 200

def test_create_rate_card():
    response = client.post(
        "/rate_card",
        json={
            "parking_id": "60ca11d0c8e0c31183ac11bf",
            "vehicle_type": 0,
            "rate":100
        }
        )
    assert response.status_code == 200

def test_create_new_parking_when_available():
    response = client.post(
        "/parking_info/park",
        json={
            "vehicle_type": 0,
            "parking_id": "60ca11d0c8e0c31183ac11bf",
            "vehicle_no": "1234"
        }
        )
    assert response.status_code == 200

# def test_exit_parking():
#     response = client.post(
#         "/parking_info/exit_park",
#         json={
#             "vehicle_type": 0,
#             "parking_id": "60ca18ca86d567d1e5fe02b7",
#             "vehicle_no": "1234"
#         }
#         )
#     assert response.status_code == 200

