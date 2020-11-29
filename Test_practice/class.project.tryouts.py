# import random
import random
#
# def ranks():
#     return ['Ace' , "2", "3", "4", "5", "6", "7", "8", "9", "10", "Prince", "Queen", "King"]
#
# def suits():
#     return ["Clubs", "Diamonds", "Hearts", "Spades"]
#
# class Card:
#     def __init__(self, rank, suit):
#         self.rank = rank
#         self.suit= suit
#
#     def __str__(self):
#         return self.rank + " of " + self.suit
#
#
# class Deck:
#     def __init__(self):
#         self.contents = []
#         self.contents = [Card( rank, suit) for rank in ranks() for suit in suits()]
#         random.shuffle(self.contents)
#
#
# card=Card('2' , "spades")
# deck = Deck()
# print(card)
list1  = [1,2,3,4,5]
random.sample(list ,k=1)
print(list)