import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from services.parking_lot_service import ParkingLotService

def test_create_parking_lot():
    service = ParkingLotService()
    result = service.create_parking_lot(6)
    assert result == "Created a parking lot with 6 slots"
    assert len(service.slots) == 6

def test_create_parking_lot_invalid():
    service = ParkingLotService()
    result = service.create_parking_lot(0)
    assert result == "Invalid number of slots"
    result = service.create_parking_lot(-1)
    assert result == "Invalid number of slots"

def test_park_vehicle():
    service = ParkingLotService()
    service.create_parking_lot(3)
    
    result = service.park_vehicle("KA-01-HH-1234", "White")
    assert result == "Allocated slot number: 1"
    
    result = service.park_vehicle("KA-01-HH-9999", "Black")
    assert result == "Allocated slot number: 2"

def test_park_vehicle_duplicate():
    service = ParkingLotService()
    service.create_parking_lot(3)
    
    service.park_vehicle("KA-01-HH-1234", "White")
    result = service.park_vehicle("KA-01-HH-1234", "Black")
    assert result == "Vehicle already parked"

def test_park_vehicle_full():
    service = ParkingLotService()
    service.create_parking_lot(2)
    
    service.park_vehicle("KA-01-HH-1234", "White")
    service.park_vehicle("KA-01-HH-9999", "Black")
    
    result = service.park_vehicle("KA-01-HH-7777", "Red")
    assert result == "Sorry, parking lot is full"

def test_leave_slot():
    service = ParkingLotService()
    service.create_parking_lot(3)
    
    service.park_vehicle("KA-01-HH-1234", "White")
    result = service.leave_slot(1)
    assert result == "Slot number 1 is free"

def test_leave_slot_invalid():
    service = ParkingLotService()
    service.create_parking_lot(3)
    
    result = service.leave_slot(5)
    assert result == "Invalid slot number: 5"
    
    result = service.leave_slot(0)
    assert result == "Invalid slot number: 0"

def test_get_status():
    service = ParkingLotService()
    service.create_parking_lot(2)
    
    service.park_vehicle("KA-01-HH-1234", "White")
    service.park_vehicle("KA-01-HH-9999", "Black")
    
    status = service.get_status()
    assert "KA-01-HH-1234" in status
    assert "KA-01-HH-9999" in status
    assert "White" in status
    assert "Black" in status

def test_search_by_color():
    service = ParkingLotService()
    service.create_parking_lot(3)
    
    service.park_vehicle("KA-01-HH-1234", "White")
    service.park_vehicle("KA-01-HH-9999", "White")
    service.park_vehicle("KA-01-BB-0001", "Black")
    
    registrations = service.get_registration_numbers_by_color("White")
    assert "KA-01-HH-1234" in registrations
    assert "KA-01-HH-9999" in registrations
    
    slots = service.get_slot_numbers_by_color("White")
    assert "1" in slots
    assert "2" in slots

def test_search_by_registration():
    service = ParkingLotService()
    service.create_parking_lot(3)
    
    service.park_vehicle("KA-01-HH-1234", "White")
    
    slot = service.get_slot_number_by_registration("KA-01-HH-1234")
    assert slot == "1"
    
    result = service.get_slot_number_by_registration("KA-01-HH-9999")
    assert result == "Vehicle with registration number KA-01-HH-9999 not found"

if __name__ == "__main__":
    test_create_parking_lot()
    test_create_parking_lot_invalid()
    test_park_vehicle()
    test_park_vehicle_duplicate()
    test_park_vehicle_full()
    test_leave_slot()
    test_leave_slot_invalid()
    test_get_status()
    test_search_by_color()
    test_search_by_registration()
    print("All ParkingLotService tests passed!")
