from Test_practice.classroom_ex.Bus import Bus
from Test_practice.classroom_ex.Person import Person

bus1 = Bus()
bus1.display()
action = int(input("1-get on the bus \n2-get of the bus \n3-exit from the program\n what do you choose?:"))
while action != 3:
    if action == 1:
        new_person = Person(int(input("id?:")),input("name?:"), int(input('age?:')) )
        bus1.get_on(new_person)
        bus1.display()
    if action == 2:
        bus1.get_off(int(input("what is the id you want to kick out:")))
        bus1.display()
    if action == 3:
        break
    if action<=0 or action>3:
        print("invalid input, try again")
        break
    action = int(input("1-get on the bus \n 2-get of the bus \n 3-exit from the program"))