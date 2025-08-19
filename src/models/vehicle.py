class Vehicle:
    def __init__(self, registration_number: str, color: str):
        self.registration_number = registration_number
        self.color = color
    
    def __str__(self):
        return f"Vehicle({self.registration_number}, {self.color})"
