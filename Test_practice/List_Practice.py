from random import randint
"""תרגיל 1 ליצור רשימה עם 10 משתנים רנדומלים"""
# list = []
# for i in range(10):
#     list.append(randint(1,101))
# print(list)

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""להדפיס את שלושת המקומות האחרונים"""
# list = list [-1:-4:-1]
# print(list)

"""תרגיל 4 להדפיס ליסט הפוך"""
# list = list[::-1]
# print(list)

"""תרגיל 5 להדפיס מקומות במקומות הזוגיים"""
# list = list [1::2]
# print(list)

"""תרגיל 6 ליצור ליסט הכולל את חמשת המספרים הראשונים"""
# list = list[:5]
# print(list)

"""תרגיל 7 ליסט עם מספרים במקומות אי זוגיים"""
# list = list[::2]5
# print(list)

"""תרגיל 8 לקלוט מספר המשתמש ולהכניס אותו לליסט במקום מקומות שבע עד 9"""
# a = int(input("enter a number"))
# list= list[:6]
# list.append(a)
# print(list)
"""מצא את הערך 20 ואם הוא קיים תחליף אותו ב200"""
# list1= [5, 10 ,15,20 ,20, 25,50,20]
# for i in list1:
#     e = list1.index(20)
#     list1.pop(e)
# print(list1)

x = {1:"shay", 2: "noa", 3 : "arnold"}
x[1] = 2
print(x.keys())