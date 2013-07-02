class Card:
    def __init__(self, value, suit):
        self.value=value
        self.suit=suit
def opposite_color(card1, card2):
  if (card1.suit == "spades"|"clubs") & (card2.suit == "diamonds"|"hearts"):
    return True
  elif (card1.suit == "diamonds"|"hearts") & (card2.suit == "spades"|"clubs"):
    return True
  else:
    return False

    
class Deck:
    suit=['hearts', 'diamonds', 'clubs', 'spades']
    def __init__(self):
        self.deck = []
            for i in range(1, 14):
              for b in range(4):
                a=''
                a=a + str(i) + suit[b][0]
                a=Card(i, suit[b])
                self.deck.append(a)


    def next_deck_card(self):
      if len(deck) > 1:
        self.deck.append(self.deck[0])
        del self.deck[0]
      else:
          print("there is only one card")

def shift_deck():
    del deck.deck[2]
    if len(deck.deck) > 2:
        deck.deck.insert(0, deck.deck[len(deck.deck)-1])
        del deck.deck[len(deck.deck)-1]
def move_deck_card():
    if len(deck.deck) >= 4:
      if can_take_card(pile, card):
        pile.deck.insert(0, deck.deck[2])
        shift_deck()
      else:
          print("try again")

    elif 0 < len(deck.deck) < 4:
      if can_take_card(pile, card):
        pile.insert(0, deck.deck[len(deck.deck)-1]
        del deck.deck[len(deck.deck)-1]
      else:
        print("try again")
    else:
      print("try again")

class Winning_stack:
    def __init__(self):
        self.stack=[]
        self.identifier='winning stack'


class Normal_stack:
    def __init__(self):
        self.stack=[]
        self.identifier='normal stack'
        self.down_stack=[]


def can_take_card(pile, card):
    if pile.identifier='normal stack'
        if len(pile.stack)==0 and card.value==13:
          return True
        elif len(pile.stack)!=0 and (pile.stack[0].value-card.value)==1 and opposite_color(pile.stack[0], card):
          return True
        else:
          return False
    elif pile.identifier='winning stack'
      if len(pile.stack)==0 and card.value==1:
        return True
      elif len(pile.stack) > 0:
        if (card.value-pile.stack[0].value)==1 and opposite_color(pile.stack[0], card):
          return True
      else:
        return False
    else:
      print("select a normal stack or a winning stack")
      return False


def flip_up(normal_stack):
  if len(normal_stack.stack)==0 and len(normal_stack.down_stack)>0:
      normal_stack.stack.append(normal_stack.down_stack[0])
      del normalstack.down_stack[0]
  else:
      0==0

def switch_stacks(from_location, card, to_location):
    if len(from_location.stack)==0:
        print ("there is no card to move")
    else:
        if can_take_card(to_location, card)==1:
            #need to work here
            
            
            
            
            
            if las.stack[0].value == card.value:
              reorder_location_of_cards(las.stack)
          else:
            i=0
            while las.stack[i].value < card.value:
              i=i+1
            shift_down_one(las, i)
            a=i-1
            while a >= 0:
              add_card_to_stack(nex, las.stack[a])
              shift_down_one(las, a)
              a=a-1
          if len(las.stack)==0:
              flip_up(las)
          show_cards()   
        else:
            1==1

#from random import shuffle
#shuffle(deck) command can be used
deck= Deck()
fixdeck= Deck()







