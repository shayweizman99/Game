class Vehicle:  #יצירת קלאס בשם רכב
    def __init__(self, name, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        self.name = name


audi = Vehicle("b", 100, 20) #יצירת אובייקט אאודי בקלאס רכב
print(audi.max_speed , audi.mileage)

class Bus(Vehicle): #יצירת קלאס אוטובוס אשר יורש את קלאס רכב
    pass

childern_bus= Bus ("volvo", 50, 10000)
print(f'bus type {childern_bus.name} max speed {childern_bus.max_speed} mileage {childern_bus.mileage}')