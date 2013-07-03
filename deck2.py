from card2 import *
class Deck:
    def __init__(self):
        self.deck = []
        self.identifier='deck'
            
    def fill_deck(self):
        for i in range(1, 14):
          for b in range(4):
            choose_suit=['hearts', 'diamonds', 'clubs', 'spades']
            a=''
            a=a + str(i) + choose_suit[b][0]
            a=Card(i, choose_suit[b])
            self.deck.append(a)


    def next_deck_card(self):
      if len(deck) > 1:
        self.deck.append(self.deck.pop(0))
      else:
          print("there is only one card")


#from random import shuffle will allow the shuffle(deck) command to be used
from random import shuffle
deck=Deck()
deck.fill_deck()
shuffle(deck.deck)
