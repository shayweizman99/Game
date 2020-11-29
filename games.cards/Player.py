from random import *
from games.cards import Card

class Player:
    def __init__(self,name, own_deck=10): #מגדירה שחקן עם מינימום 10 קלפים ביד
        self.name = name
        self.own_deck = []

    def set_hand(self, full_deck): #מחלקת חבילה חדשה ואקראית לשחקן, מינימום 10 קלפים מקסימום 26
        for i in self.own_deck:
            self.own_deck.append(full_deck.deal_one())

    def get_card(self): #מושכת קלף אקראי מהחבילה
        self.picked_card = random.sample(self.own_deck , 1)
        return self.picked_card

    def add_Card(self,given_card): #מקבלת קלף ומוסיפה לחבילה
        self.given_card = given_card
        self.own_deck.append(self.given_card)


    def show(self): #מדפיסה את שם השחקן ואת החבילה שלו
        print(f"Player {self.name} cards are:\n {self.own_deck}")