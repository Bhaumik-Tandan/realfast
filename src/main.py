#!/usr/bin/env python3
"""
Main entry point for the Parking Lot Management System.
"""

import sys
from services.parking_lot_service import ParkingLotService

def process_command(service: ParkingLotService, command: str) -> str:
    parts = command.strip().split()
    if not parts:
        return ""
    
    cmd = parts[0].lower()
    
    if cmd == "create_parking_lot":
        if len(parts) != 2:
            return "Usage: create_parking_lot <number_of_slots>"
        try:
            slots = int(parts[1])
            return service.create_parking_lot(slots)
        except ValueError:
            return "Invalid number of slots"
    
    elif cmd == "park":
        if len(parts) != 3:
            return "Usage: park <registration_number> <color>"
        return service.park_vehicle(parts[1], parts[2])
    
    elif cmd == "leave":
        if len(parts) != 2:
            return "Usage: leave <slot_number>"
        try:
            slot = int(parts[1])
            return service.leave_slot(slot)
        except ValueError:
            return "Invalid slot number"
    
    elif cmd == "status":
        return service.get_status()
    
    elif cmd == "registration_numbers_for_cars_with_colour":
        if len(parts) != 2:
            return "Usage: registration_numbers_for_cars_with_colour <color>"
        return service.get_registration_numbers_by_color(parts[1])
    
    elif cmd == "slot_number_for_registration_number":
        if len(parts) != 2:
            return "Usage: slot_number_for_registration_number <registration_number>"
        return service.get_slot_number_by_registration(parts[1])
    
    elif cmd == "slot_numbers_for_cars_with_colour":
        if len(parts) != 2:
            return "Usage: slot_numbers_for_cars_with_colour <color>"
        return service.get_slot_numbers_by_color(parts[1])
    
    else:
        return f"Unknown command: {cmd}"

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <input_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    service = ParkingLotService()
    
    try:
        with open(input_file, 'r') as f:
            for line in f:
                line = line.strip()
                if line:
                    result = process_command(service, line)
                    if result:
                        print(result)
    except FileNotFoundError:
        print(f"Input file not found: {input_file}")
        sys.exit(1)

if __name__ == "__main__":
    main()
