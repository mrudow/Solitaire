from card import *
class Deck:
    suit=['hearts', 'diamonds', 'clubs', 'spades']
    def __init__(self):
        self.deck = []
            
    def fill_deck(self)
        for i in range(1, 14):
          for b in range(4):
            a=''
            a=a + str(i) + suit[b][0]
            a=Card(i, suit[b])
            self.deck.append(a)


    def next_deck_card(self):
      if len(deck) > 1:
        self.deck.append(self.deck.pop(0))
      else:
          print("there is only one card")


#from random import shuffle will allow the shuffle(deck) command to be used
deck=Deck()
deck.fill_deck()
