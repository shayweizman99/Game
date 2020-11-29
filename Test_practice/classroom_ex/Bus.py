from Test_practice.classroom_ex import Person

class Bus:
    def __init__(self):
        self.bus_seats = []
        self.head_count = 0
        for i in range(int(input("how many seats?:"))):
            self.bus_seats += [None]

    def display(self):
        print(self.bus_seats)

    def get_on(self, person):
        if self.head_count == len(self.bus_seats):
            print("bus is full")
        else:
            for i in range(len(self.bus_seats)):
                if self.bus_seats[i] is None:
                    self.bus_seats[i] = person
                    print(f"the person {person} got on the bus")
                    self.head_count += 1
                    break

    def get_off(self, person_id):
        got_off = False
        for i in range (len(self.bus_seats)):
            if self.bus_seats[i].id == person_id:
                    self.bus_seats[i] = None
                    self.head_count -= 1
                    got_off = True
                    break
            if not got_off:
                print(f"person id{person_id} is not on the bus")
