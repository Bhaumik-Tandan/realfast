from models.vehicle import Vehicle
from models.parking_slot import ParkingSlot

class ParkingLot:
    def __init__(self, lot_id: str, number_of_slots: int):
        self.lot_id = lot_id
        self.slots = [ParkingSlot(i + 1) for i in range(number_of_slots)]
        self.registration_to_slot = {}
        self.total_slots = number_of_slots
        self.occupied_slots = 0
    
    def get_available_slots(self) -> int:
        return self.total_slots - self.occupied_slots
    
    def get_occupancy_rate(self) -> float:
        return (self.occupied_slots / self.total_slots) * 100 if self.total_slots > 0 else 0
    
    def get_nearest_available_slot(self) -> int:
        for slot in self.slots:
            if not slot.is_occupied:
                return slot.slot_number
        return -1
    
    def park_vehicle(self, vehicle: Vehicle) -> tuple[bool, str]:
        if self.occupied_slots >= self.total_slots:
            return False, "Sorry, parking lot is full"
        
        if vehicle.registration_number in self.registration_to_slot:
            return False, f"Vehicle already parked"
        
        slot_number = self.get_nearest_available_slot()
        if slot_number == -1:
            return False, "No available slots"
        
        slot = self.slots[slot_number - 1]
        if slot.park_vehicle(vehicle):
            self.registration_to_slot[vehicle.registration_number] = slot_number
            self.occupied_slots += 1
            return True, f"Allocated slot number: {slot_number}"
        
        return False, "Failed to park vehicle"
    
    def remove_vehicle(self, slot_number: int) -> tuple[bool, str, Vehicle]:
        if slot_number < 1 or slot_number > len(self.slots):
            return False, f"Invalid slot number: {slot_number}", None
        
        slot = self.slots[slot_number - 1]
        if not slot.is_occupied:
            return False, f"Slot {slot_number} is already empty", None
        
        vehicle = slot.remove_vehicle()
        if vehicle:
            del self.registration_to_slot[vehicle.registration_number]
            self.occupied_slots -= 1
            return True, f"Slot number {slot_number} is free", vehicle
        
        return False, f"Error removing vehicle from slot {slot_number}", None
    
    def get_status(self) -> str:
        status_lines = [f"Parking Lot {self.lot_id} - {self.occupied_slots}/{self.total_slots} slots occupied"]
        status_lines.append("Slot No.    Registration No    Colour")
        
        for slot in self.slots:
            if slot.is_occupied and slot.vehicle:
                status_lines.append(f"{slot.slot_number:<12} {slot.vehicle.registration_number:<19} {slot.vehicle.color}")
        
        return "\n".join(status_lines)
    
    def get_vehicles_by_color(self, color: str) -> list[tuple[int, Vehicle]]:
        result = []
        for slot in self.slots:
            if slot.is_occupied and slot.vehicle and slot.vehicle.color.lower() == color.lower():
                result.append((slot.slot_number, slot.vehicle))
        return result
    
    def get_slot_by_registration(self, registration_number: str) -> int:
        return self.registration_to_slot.get(registration_number, -1)
