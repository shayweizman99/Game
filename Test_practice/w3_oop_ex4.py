class Vehicle:  #יצירת קלאס בשם רכב
    def __init__(self, name, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        self.name = name


    def seating_max(self, seats):
        self.seats = seats
        return f"max seats of a {self.name} are {self.seats}"

class Bus(Vehicle):
    def seating_max(self, seats=50):
        return super().seating_max(seats=50)

school_bus=Bus("volvo" , 100, 200)
print(school_bus.seating_max())