# Parking Lot Management System

A comprehensive parking lot management system that handles automated ticketing, slot allocation, and vehicle tracking with support for both single and multiple parking lots.

## 🎯 Features

### Level 1: Single Parking Lot Management
- **Automated ticketing system** for cars entering the parking lot
- **Nearest slot allocation** from entry point
- **Vehicle exit management** with slot availability updates
- **Search functionality**:
  - Find registration numbers by color
  - Find slot number by registration number
  - Find slot numbers by color
- **Real-time status** display of all parking slots

### Level 2: Multi-Level Parking Lot Management
- **Multiple parking lots** support with unique identifiers
- **Advanced slot allocation** strategies across multiple lots
- **Global vehicle tracking** across all parking lots
- **Enhanced reporting** with occupancy rates and analytics
- **Smart lot selection** with best available lot recommendations
- **Lot-specific operations** and status monitoring

## 🏗️ Project Structure

```
realfast/
├── 📄 realfast - parking lot problem statement.pdf
├── 📖 README.md
├── 🚀 bin/                           # Executable scripts
│   ├── setup                        # Install dependencies and run tests
│   ├── parking_lot                  # Level 1 main program
│   └── run_functional_tests         # Functional test runner
├── 💻 src/                          # Source code
│   ├── models/                      # Data models
│   │   ├── vehicle.py              # Vehicle entity
│   │   ├── parking_slot.py         # Individual slot management
│   │   └── parking_lot.py          # Enhanced lot model (Level 2)
│   ├── services/                    # Business logic
│   │   ├── parking_lot_service.py  # Level 1 service
│   │   └── multi_parking_service.py # Level 2 service
│   ├── main.py                      # Level 1 CLI interface
│   └── main_level2.py               # Level 2 CLI interface
├── 🧪 tests/                        # Unit tests
│   ├── test_vehicle.py
│   ├── test_parking_slot.py
│   ├── test_parking_lot_service.py
│   └── test_parking_lot.py
└── 📋 functional_spec/              # Functional specifications
    ├── README.md
    └── test_inputs/                 # Test input files
        ├── level1_basic.txt
        ├── level1_edge_cases.txt
        ├── level2_basic.txt
        └── level2_advanced.txt
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Git

### Installation
```bash
# Clone the repository
git clone <repository-url>
cd realfast

# Make scripts executable
chmod +x bin/*

# Run setup
./bin/setup
```

## 📖 Usage

### Level 1: Single Parking Lot

#### Basic Commands
```bash
# Create a parking lot with 6 slots
create_parking_lot 6

# Park a vehicle
park KA-01-HH-1234 White

# Remove vehicle from slot
leave 1

# Check status
status

# Search operations
registration_numbers_for_cars_with_colour White
slot_number_for_registration_number KA-01-HH-1234
slot_numbers_for_cars_with_colour Black
```

#### Run Level 1
```bash
# Using executable script
./bin/parking_lot functional_spec/test_inputs/level1_basic.txt

# Direct Python execution
python3 src/main.py functional_spec/test_inputs/level1_basic.txt
```

### Level 2: Multiple Parking Lots

#### Enhanced Commands
```bash
# Create multiple parking lots
create_parking_lot A 4
create_parking_lot B 3

# Park with lot preference
park KA-01-HH-1234 White A

# Global status
status

# Lot-specific status
status A

# Lot information
lot_info A

# Find best available lot
best_lot
```

#### Run Level 2
```bash
python3 src/main_level2.py functional_spec/test_inputs/level2_basic.txt
```

## 🧪 Testing

### Unit Tests
```bash
cd tests
python3 test_vehicle.py
python3 test_parking_slot.py
python3 test_parking_lot_service.py
python3 test_parking_lot.py
```

### Functional Tests
```bash
# Test Level 1
./bin/parking_lot functional_spec/test_inputs/level1_edge_cases.txt

# Test Level 2
python3 src/main_level2.py functional_spec/test_inputs/level2_advanced.txt
```

## 📋 Input/Output Format

### Commands Reference
| Command | Level | Usage | Description |
|---------|-------|-------|-------------|
| `create_parking_lot` | 1 | `<slots>` | Create single parking lot |
| `create_parking_lot` | 2 | `<lot_id> <slots>` | Create named parking lot |
| `park` | 1 | `<reg> <color>` | Park vehicle in any slot |
| `park` | 2 | `<reg> <color> [lot]` | Park with optional lot preference |
| `leave` | 1 | `<slot>` | Remove vehicle from slot |
| `leave` | 2 | `<lot> <slot>` | Remove from specific lot |
| `status` | 1 | - | Show single lot status |
| `status` | 2 | `[lot_id]` | Show global or lot-specific status |
| `lot_info` | 2 | `<lot_id>` | Detailed lot information |
| `best_lot` | 2 | `[color]` | Find best available lot |

### Example Output
```
=== GLOBAL PARKING LOT STATUS ===
A: 2/4 slots occupied (50.0%)
B: 1/3 slots occupied (33.3%)

Total: 3/7 slots occupied

Lot A, Slot 1, Lot B, Slot 1
Best available parking lot: B (2 slots available)
```

## 🔧 Development

### Adding New Features
1. **Models**: Add new entities in `src/models/`
2. **Services**: Implement business logic in `src/services/`
3. **CLI**: Add command handlers in main files
4. **Tests**: Create corresponding unit tests
5. **Documentation**: Update this README

### Code Style
- **Clean, readable code** without excessive comments
- **Object-oriented design** with clear separation of concerns
- **Comprehensive testing** for all components
- **Realistic Git history** showing human development process

## 📊 Performance

- **Slot allocation**: O(n) where n is number of slots
- **Search operations**: O(n) for color/registration lookups
- **Memory usage**: Minimal overhead with efficient data structures
- **Scalability**: Designed to handle multiple parking lots efficiently

## 🎯 Future Enhancements

- **Database integration** for persistent storage
- **Web API** for remote access
- **Real-time notifications** for lot status changes
- **Advanced analytics** and reporting
- **Mobile app** support

## 📄 License

This project is part of a technical assessment and demonstrates software development best practices.

## 🤝 Contributing

This is a demonstration project showing progressive enhancement from Level 1 to Level 2 with realistic development patterns.

---

**Built with progressive enhancement and clean architecture principles!** 🚀
