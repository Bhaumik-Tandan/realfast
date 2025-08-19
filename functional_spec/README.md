# Functional Specifications

This directory contains functional tests and specifications for the Parking Lot Management System.

## Test Cases

### Level 1 Test Cases

1. **Create Parking Lot**
   - Create parking lot with valid number of slots
   - Handle invalid slot numbers

2. **Park Vehicle**
   - Park vehicle in nearest available slot
   - Handle duplicate registration numbers
   - Handle full parking lot

3. **Leave Slot**
   - Remove vehicle from occupied slot
   - Handle empty slots
   - Handle invalid slot numbers

4. **Status**
   - Display current parking lot status
   - Show empty parking lot

5. **Search Functions**
   - Find cars by color
   - Find slot by registration number
   - Find slots by color

## Running Functional Tests

```bash
chmod +x bin/run_functional_tests
./bin/run_functional_tests
```

## Test Input Files

Sample input files are provided in the `test_inputs/` directory for testing various scenarios.
