import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from models.parking_slot import ParkingSlot
from models.vehicle import Vehicle

def test_parking_slot_creation():
    slot = ParkingSlot(1)
    assert slot.slot_number == 1
    assert not slot.is_occupied
    assert slot.vehicle is None

def test_park_vehicle():
    slot = ParkingSlot(1)
    vehicle = Vehicle("KA-01-HH-1234", "White")
    
    assert slot.park_vehicle(vehicle) == True
    assert slot.is_occupied
    assert slot.vehicle == vehicle

def test_park_vehicle_in_occupied_slot():
    slot = ParkingSlot(1)
    vehicle1 = Vehicle("KA-01-HH-1234", "White")
    vehicle2 = Vehicle("KA-01-HH-9999", "Black")
    
    slot.park_vehicle(vehicle1)
    assert slot.park_vehicle(vehicle2) == False
    assert slot.vehicle == vehicle1

def test_remove_vehicle():
    slot = ParkingSlot(1)
    vehicle = Vehicle("KA-01-HH-1234", "White")
    
    slot.park_vehicle(vehicle)
    removed_vehicle = slot.remove_vehicle()
    
    assert removed_vehicle == vehicle
    assert not slot.is_occupied
    assert slot.vehicle is None

def test_remove_vehicle_from_empty_slot():
    slot = ParkingSlot(1)
    removed_vehicle = slot.remove_vehicle()
    
    assert removed_vehicle is None

if __name__ == "__main__":
    test_parking_slot_creation()
    test_park_vehicle()
    test_park_vehicle_in_occupied_slot()
    test_remove_vehicle()
    test_remove_vehicle_from_empty_slot()
    print("All ParkingSlot tests passed!")
