from Game.Card import Card
from random import *

# from random import randint


class DeckOfCards:    #make a new deck_cards
    def __init__(self):
        self.level_suit = ["Diamond", "Spade", "Heart", "Club"]
        self.level_value = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
        self.lst_cards = []
        for i in self.level_value:
            for z in self.level_suit:
                card = Card(i, z)
                self.lst_cards += [card]
        print(self.lst_cards)
        print(len(self.lst_cards))

    def shuffle(self):
        shuffle(self.lst_cards)
        return self.lst_cards

    def deal_one(self):
        return sample(self.lst_cards, 1)

    def show(self):
        return self.lst_cards


