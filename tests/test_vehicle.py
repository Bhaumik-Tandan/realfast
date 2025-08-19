import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from models.vehicle import Vehicle

def test_vehicle_creation():
    vehicle = Vehicle("KA-01-HH-1234", "White")
    assert vehicle.registration_number == "KA-01-HH-1234"
    assert vehicle.color == "White"

def test_vehicle_string():
    vehicle = Vehicle("KA-01-HH-9999", "Black")
    assert str(vehicle) == "Vehicle(KA-01-HH-9999, Black)"

if __name__ == "__main__":
    test_vehicle_creation()
    test_vehicle_string()
    print("Vehicle tests passed!")
