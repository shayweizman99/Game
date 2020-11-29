class Person:
    def __init__(self,id,name,age):
        self.id = id
        self.name = name
        self.age = age

    def info(self):
        self.name = input("what is your name?")
        self.id = int(input("what is your id?"))
        self.age = int(input('what is your age?'))
    def __str__(self):
        return f"{self.name} id number:{self.id} age:{self.age}"

    def __eq__(self, other):
        if self.id == other:
            return True
        else:
            return False

