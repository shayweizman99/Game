class Vehicle:  # יצירת קלאס בשם רכב

    def __init__(self, name, mileage, capacity):
        self.mileage = mileage
        self.name = name
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100


# class Bus(Vehicle):

school_bus=Vehicle("volvo" , 100, 50)
print(f"Total bus fare is {school_bus.fare() + school_bus.fare() * 0.1}")
