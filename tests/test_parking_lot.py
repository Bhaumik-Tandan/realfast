import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from models.parking_lot import ParkingLot
from models.vehicle import Vehicle

def test_parking_lot_creation():
    lot = ParkingLot("A", 5)
    assert lot.lot_id == "A"
    assert len(lot.slots) == 5
    assert lot.total_slots == 5
    assert lot.occupied_slots == 0

def test_get_available_slots():
    lot = ParkingLot("A", 3)
    assert lot.get_available_slots() == 3
    
    vehicle = Vehicle("KA-01-HH-1234", "White")
    lot.park_vehicle(vehicle)
    assert lot.get_available_slots() == 2

def test_get_occupancy_rate():
    lot = ParkingLot("A", 4)
    assert lot.get_occupancy_rate() == 0.0
    
    vehicle = Vehicle("KA-01-HH-1234", "White")
    lot.park_vehicle(vehicle)
    assert lot.get_occupancy_rate() == 25.0

def test_get_nearest_available_slot():
    lot = ParkingLot("A", 3)
    assert lot.get_nearest_available_slot() == 1
    
    vehicle = Vehicle("KA-01-HH-1234", "White")
    lot.park_vehicle(vehicle)
    assert lot.get_nearest_available_slot() == 2

def test_park_vehicle():
    lot = ParkingLot("A", 3)
    vehicle = Vehicle("KA-01-HH-1234", "White")
    
    success, message = lot.park_vehicle(vehicle)
    assert success == True
    assert "Allocated slot number: 1" in message
    assert lot.occupied_slots == 1

def test_park_vehicle_full():
    lot = ParkingLot("A", 1)
    vehicle1 = Vehicle("KA-01-HH-1234", "White")
    vehicle2 = Vehicle("KA-01-HH-9999", "Black")
    
    lot.park_vehicle(vehicle1)
    success, message = lot.park_vehicle(vehicle2)
    assert success == False
    assert "Sorry, parking lot is full" in message

def test_remove_vehicle():
    lot = ParkingLot("A", 3)
    vehicle = Vehicle("KA-01-HH-1234", "White")
    
    lot.park_vehicle(vehicle)
    success, message, removed_vehicle = lot.remove_vehicle(1)
    
    assert success == True
    assert "Slot number 1 is free" in message
    assert removed_vehicle == vehicle
    assert lot.occupied_slots == 0

def test_get_status():
    lot = ParkingLot("A", 2)
    vehicle = Vehicle("KA-01-HH-1234", "White")
    lot.park_vehicle(vehicle)
    
    status = lot.get_status()
    assert "Parking Lot A - 1/2 slots occupied" in status
    assert "KA-01-HH-1234" in status

if __name__ == "__main__":
    test_parking_lot_creation()
    test_get_available_slots()
    test_get_occupancy_rate()
    test_get_nearest_available_slot()
    test_park_vehicle()
    test_park_vehicle_full()
    test_remove_vehicle()
    test_get_status()
    print("All ParkingLot tests passed!")
