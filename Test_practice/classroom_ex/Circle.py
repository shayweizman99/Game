class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.pi=3.14

    def area(self):
        return self.pi*self.radius**2

    def permimeter(self):
        return 2*self.pi*self.radius

    def __str__(self):
        return f"peri - {self.permimeter()},area - {self.area()} "