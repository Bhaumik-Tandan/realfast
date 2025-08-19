from typing import List, Optional, Dict
from models.vehicle import Vehicle
from models.parking_slot import ParkingSlot

class ParkingLotService:
    def __init__(self):
        self.slots = []
        self.registration_to_slot = {}
    
    def create_parking_lot(self, number_of_slots: int) -> str:
        if number_of_slots <= 0:
            return "Invalid number of slots"
        
        self.slots = [ParkingSlot(i + 1) for i in range(number_of_slots)]
        self.registration_to_slot.clear()
        return f"Created a parking lot with {number_of_slots} slots"
    
    def park_vehicle(self, registration_number: str, color: str) -> str:
        if not self.slots:
            return "Parking lot not created yet"
        
        if registration_number in self.registration_to_slot:
            return f"Vehicle already parked"
        
        for slot in self.slots:
            if not slot.is_occupied:
                vehicle = Vehicle(registration_number, color)
                if slot.park_vehicle(vehicle):
                    self.registration_to_slot[registration_number] = slot.slot_number
                    return f"Allocated slot number: {slot.slot_number}"
        
        return "Sorry, parking lot is full"
    
    def leave_slot(self, slot_number: int) -> str:
        if not self.slots:
            return "Parking lot not created yet"
        
        if slot_number < 1 or slot_number > len(self.slots):
            return f"Invalid slot number: {slot_number}"
        
        slot = self.slots[slot_number - 1]
        if not slot.is_occupied:
            return f"Slot {slot_number} is already empty"
        
        vehicle = slot.remove_vehicle()
        if vehicle:
            del self.registration_to_slot[vehicle.registration_number]
            return f"Slot number {slot_number} is free"
        
        return f"Error removing vehicle from slot {slot_number}"
    
    def get_status(self) -> str:
        if not self.slots:
            return "Parking lot not created yet"
        
        status_lines = ["Slot No.    Registration No    Colour"]
        for slot in self.slots:
            if slot.is_occupied and slot.vehicle:
                status_lines.append(f"{slot.slot_number:<12} {slot.vehicle.registration_number:<19} {slot.vehicle.color}")
        
        return "\n".join(status_lines)
    
    def get_registration_numbers_by_color(self, color: str) -> str:
        if not self.slots:
            return "Parking lot not created yet"
        
        registrations = []
        for slot in self.slots:
            if slot.is_occupied and slot.vehicle and slot.vehicle.color.lower() == color.lower():
                registrations.append(slot.vehicle.registration_number)
        
        if not registrations:
            return f"No cars found with color {color}"
        
        return ", ".join(registrations)
    
    def get_slot_number_by_registration(self, registration_number: str) -> str:
        if not self.slots:
            return "Parking lot not created yet"
        
        slot_number = self.registration_to_slot.get(registration_number)
        if slot_number is None:
            return f"Vehicle with registration number {registration_number} not found"
        
        return str(slot_number)
    
    def get_slot_numbers_by_color(self, color: str) -> str:
        if not self.slots:
            return "Parking lot not created yet"
        
        slot_numbers = []
        for slot in self.slots:
            if slot.is_occupied and slot.vehicle and slot.vehicle.color.lower() == color.lower():
                slot_numbers.append(str(slot.slot_number))
        
        if not slot_numbers:
            return f"No cars found with color {color}"
        
        return ", ".join(slot_numbers)
