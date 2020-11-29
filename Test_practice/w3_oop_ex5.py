class Vehicle:  # יצירת קלאס בשם רכב
    color = 'white'
    banana = 8
    def __init__(self, name, max_speed, mileage, color="White"):
        self.max_speed = max_speed
        self.mileage = mileage
        self.name = name
        # self.color = color


bus = Vehicle("Volvo", 80, 10000)
print(bus.color, bus.name, bus.mileage, bus.max_speed, bus.banana)

car = Vehicle("Tesla", 150, 2000)
print(car.color, car.name, car.mileage, car.max_speed)
