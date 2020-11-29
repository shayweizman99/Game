class Person():
    def __init__(self, name, age, num_of_kids):
        self.name = name
        self.age = age
        self.num_of_kids = num_of_kids

    def __str__(self):
        return f"{self.name} is {self.age} years old and have {self.num_of_kids} kids"

    def has_kids(self):
        if self.num_of_kids <= 1:
            return True
        else:
            return False

    def group_age(self):
        if 0 <= self.age <= 18:
            return "Child"
        elif 18 < self.age <=60:
            return "Adult"
        elif 60 < self.age <=120:
            return "Senior"
        else:
            return "invalid age"

