# Create constructor and objects of ElectricVehicle class

class ElectricVehicle:
    def __init__(self, brand, material):
        print(f"ElectricVehicle constructor is running for {brand}")
        self.brand = brand
        self.material = material

ev1 = ElectricVehicle("Tata", "Steel")
ev2 = ElectricVehicle("Mahindra", "Aluminium")

print(ev1.brand)
print(ev2.material)