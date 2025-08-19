import sys
from services.multi_parking_service import MultiParkingService

def process_command(service: MultiParkingService, command: str) -> str:
    parts = command.strip().split()
    if not parts:
        return ""
    
    cmd = parts[0].lower()
    
    if cmd == "create_parking_lot":
        if len(parts) != 3:
            return "Usage: create_parking_lot <lot_id> <number_of_slots>"
        try:
            lot_id = parts[1]
            slots = int(parts[2])
            return service.create_parking_lot(lot_id, slots)
        except ValueError:
            return "Invalid number of slots"
    
    elif cmd == "park":
        if len(parts) < 3:
            return "Usage: park <registration_number> <color> [preferred_lot]"
        registration = parts[1]
        color = parts[2]
        preferred_lot = parts[3] if len(parts) > 3 else None
        return service.park_vehicle(registration, color, preferred_lot)
    
    elif cmd == "leave":
        if len(parts) != 3:
            return "Usage: leave <lot_id> <slot_number>"
        try:
            lot_id = parts[1]
            slot = int(parts[2])
            return service.leave_slot(lot_id, slot)
        except ValueError:
            return "Invalid slot number"
    
    elif cmd == "status":
        if len(parts) == 1:
            return service.get_global_status()
        elif len(parts) == 2:
            return service.get_lot_status(parts[1])
        else:
            return "Usage: status [lot_id]"
    
    elif cmd == "lot_info":
        if len(parts) != 2:
            return "Usage: lot_info <lot_id>"
        return service.get_parking_lot_info(parts[1])
    
    elif cmd == "best_lot":
        color = parts[1] if len(parts) > 1 else None
        return service.find_best_parking_lot(color)
    
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
        print("Usage: python main_level2.py <input_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    service = MultiParkingService()
    
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
