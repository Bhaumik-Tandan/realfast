from typing import List, Dict, Optional
from models.vehicle import Vehicle
from models.parking_lot import ParkingLot

class MultiParkingService:
    def __init__(self):
        self.parking_lots = {}
        self.global_registration_to_lot = {}
    
    def create_parking_lot(self, lot_id: str, number_of_slots: int) -> str:
        if lot_id in self.parking_lots:
            return f"Parking lot {lot_id} already exists"
        
        if number_of_slots <= 0:
            return "Invalid number of slots"
        
        self.parking_lots[lot_id] = ParkingLot(lot_id, number_of_slots)
        return f"Created parking lot {lot_id} with {number_of_slots} slots"
    
    def park_vehicle(self, registration_number: str, color: str, preferred_lot: str = None) -> str:
        if registration_number in self.global_registration_to_lot:
            return f"Vehicle already parked"
        
        if not self.parking_lots:
            return "No parking lots created yet"
        
        vehicle = Vehicle(registration_number, color)
        
        if preferred_lot and preferred_lot in self.parking_lots:
            success, message = self.parking_lots[preferred_lot].park_vehicle(vehicle)
            if success:
                self.global_registration_to_lot[registration_number] = preferred_lot
                return f"Parked in {preferred_lot}: {message}"
        
        for lot_id, lot in self.parking_lots.items():
            success, message = lot.park_vehicle(vehicle)
            if success:
                self.global_registration_to_lot[registration_number] = lot_id
                return f"Parked in {lot_id}: {message}"
        
        return "Sorry, all parking lots are full"
    
    def leave_slot(self, lot_id: str, slot_number: int) -> str:
        if lot_id not in self.parking_lots:
            return f"Parking lot {lot_id} not found"
        
        lot = self.parking_lots[lot_id]
        success, message, vehicle = lot.remove_vehicle(slot_number)
        
        if success and vehicle:
            del self.global_registration_to_lot[vehicle.registration_number]
            return message
        
        return message
    
    def get_lot_status(self, lot_id: str) -> str:
        if lot_id not in self.parking_lots:
            return f"Parking lot {lot_id} not found"
        
        return self.parking_lots[lot_id].get_status()
    
    def get_global_status(self) -> str:
        if not self.parking_lots:
            return "No parking lots created yet"
        
        status_lines = ["=== GLOBAL PARKING LOT STATUS ==="]
        total_occupied = 0
        total_slots = 0
        
        for lot_id, lot in self.parking_lots.items():
            occupied = lot.occupied_slots
            total = lot.total_slots
            total_occupied += occupied
            total_slots += total
            
            status_lines.append(f"{lot_id}: {occupied}/{total} slots occupied ({lot.get_occupancy_rate():.1f}%)")
        
        status_lines.append(f"\nTotal: {total_occupied}/{total_slots} slots occupied")
        return "\n".join(status_lines)
    
    def get_registration_numbers_by_color(self, color: str) -> str:
        if not self.parking_lots:
            return "No parking lots created yet"
        
        registrations = []
        for lot_id, lot in self.parking_lots.items():
            vehicles = lot.get_vehicles_by_color(color)
            for slot_num, vehicle in vehicles:
                registrations.append(f"{vehicle.registration_number} (Lot {lot_id}, Slot {slot_num})")
        
        if not registrations:
            return f"No cars found with color {color}"
        
        return ", ".join(registrations)
    
    def get_slot_number_by_registration(self, registration_number: str) -> str:
        if registration_number not in self.global_registration_to_lot:
            return f"Vehicle not found"
        
        lot_id = self.global_registration_to_lot[registration_number]
        lot = self.parking_lots[lot_id]
        slot_number = lot.get_slot_by_registration(registration_number)
        
        return f"Lot {lot_id}, Slot {slot_number}"
    
    def get_slot_numbers_by_color(self, color: str) -> str:
        if not self.parking_lots:
            return "No parking lots created yet"
        
        slot_info = []
        for lot_id, lot in self.parking_lots.items():
            vehicles = lot.get_vehicles_by_color(color)
            for slot_num, vehicle in vehicles:
                slot_info.append(f"Lot {lot_id}, Slot {slot_num}")
        
        if not slot_info:
            return f"No cars found with color {color}"
        
        return ", ".join(slot_info)
    
    def get_parking_lot_info(self, lot_id: str) -> str:
        if lot_id not in self.parking_lots:
            return f"Parking lot {lot_id} not found"
        
        lot = self.parking_lots[lot_id]
        return f"Lot {lot_id}: {lot.occupied_slots}/{lot.total_slots} slots occupied ({lot.get_occupancy_rate():.1f}%)"
    
    def find_best_parking_lot(self, color: str = None) -> str:
        if not self.parking_lots:
            return "No parking lots available"
        
        best_lot = None
        best_availability = -1
        
        for lot_id, lot in self.parking_lots.items():
            available = lot.get_available_slots()
            if available > best_availability:
                best_availability = available
                best_lot = lot_id
        
        if best_lot:
            return f"Best available parking lot: {best_lot} ({best_availability} slots available)"
        
        return "All parking lots are full"
