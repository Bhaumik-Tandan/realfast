from .vehicle import Vehicle

class ParkingSlot:
    def __init__(self, slot_number: int):
        self.slot_number = slot_number
        self.vehicle = None
        self.is_occupied = False
    
    def park_vehicle(self, vehicle: Vehicle) -> bool:
        if self.is_occupied:
            return False
        
        self.vehicle = vehicle
        self.is_occupied = True
        return True
    
    def remove_vehicle(self) -> Vehicle:
        if not self.is_occupied:
            return None
        
        vehicle = self.vehicle
        self.vehicle = None
        self.is_occupied = False
        return vehicle
    
    def get_vehicle(self) -> Vehicle:
        return self.vehicle
    
    def __str__(self):
        status = "Occupied" if self.is_occupied else "Available"
        vehicle_info = f" - {self.vehicle}" if self.vehicle else ""
        return f"Slot {self.slot_number}: {status}{vehicle_info}"
    
    def __repr__(self):
        return self.__str__()
