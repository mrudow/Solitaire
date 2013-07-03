#!/usr/bin/python
from deck import *

class Winning_stack:
    def __init__(self):
        self.stack=[]
        self.identifier='winning stack'

winning_stack=[]
for i in range(4):
    winning_stack.append(Winning_stack)

class Normal_stack:
    def __init__(self):
        self.stack=[]
        self.identifier='normal stack'
        self.down_stack=[]

normal_stack=[]
for i in range(7):
    normal_stack.append(Normal_stack)

def opposite_color(card1, card2):
  if (card1.suit == "spades"|"clubs") & (card2.suit == "diamonds"|"hearts"):
    return True
  elif (card1.suit == "diamonds"|"hearts") & (card2.suit == "spades"|"clubs"):
    return True
  else:
    return False

def move_deck_card(pile):
    if len(deck.deck) >= 4:
      if can_take_card(pile, card):
        pile.stack.insert(0, deck.deck.pop(2))
        deck.deck.insert(0, deck.deck.pop(len(deck.deck)-1))
      else:
          print("try again")
    elif 0 < len(deck.deck) < 4:
      if can_take_card(pile, card):
        pile.stack.insert(0, deck.deck.pop(len(deck.deck)-1))
      else:
        print("try again")
    else:
      print("try again")

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
      normal_stack.stack.append(normal_stack.down_stack.pop(0))
  else:
      0==0

def switch_stacks(from_location, card, to_location):
    if len(from_location.stack)==0:
        print ("there is no card to move")
    else:
        if can_take_card(to_location, card)==1:
          if from_location.stack[0].value == card.value:
            to_location.stack.insert(0, from_location.stack.pop(0))
            if len(from_location.stack)==0:
                flip_up(from_location)
          elif to_location.identifier='normal stack':
            i=0
            while las.stack[i].value < card.value:
              i=i+1
            while i >= 0:
                to_location.stack.insert(0, from_location.stack.pop(i))
                i=i-1
            if len(from_location.stack)==0:
              flip_up(from_location)
        else:
            print("This move is against the rules. Sucks to suck.")

def clear_pile(pile):
    i=0
    b=len(pile)
    while i < b:
        del pile[i]
        i=i+1

#show card number or face
def show_card_value(card):
    if 1 < card.value < 11:
        return str(card.value)
    elif card.value == 11:
        return 'J'
    elif card.value == 12:
        return 'Q'
    elif card.value == 13:
        return 'K'
    else:
        return 'A'

def show_stack_cards(stack):
    if len(stack)>0:
        i=len(stack)-1
        a='|'
        while i >= 0:
          a= a + show_card_value(stack[i])+str(stack[i].suit[0]) + '|'
          i=i-1
        return a
    else:
        return ''

def show_down_cards(down_stack):
    if len(down_stack)>0:
        i=len(down)stack)-1
        a=''
        while i >= 0:
            a=a + "|**"
            i=i-1
        return a


