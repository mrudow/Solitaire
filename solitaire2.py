#!/usr/bin/python
from deck2 import *

class Winning_stack:
    def __init__(self):
        self.stack=[]
        self.identifier='winning stack'
  
winning_stacks=[]
for i in range(4):
  winning_stacks.append(Winning_stack())

class Normal_stack:
    def __init__(self):
        self.stack=[]
        self.identifier='normal stack'
        self.down_stack=[]

normal_stacks=[]
for i in range(7):
  normal_stacks.append(Normal_stack())

def color(card):
    if (card.suit == "Spades") | (card.suit == "Clubs"):
        return 'black'
    else:
        return 'red'


def move_deck_card(pile):
    if len(deck.deck) >= 4:
      if can_take_card(pile, deck.deck[2]):
        pile.stack.insert(0, deck.deck.pop(2))
        deck.deck.insert(0, deck.deck.pop(len(deck.deck)-1))
      else:
          print("try again")
    elif 0 < len(deck.deck) < 4:
      if can_take_card(pile, deck.deck[len(deck.deck)-1]):
        pile.stack.insert(0, deck.deck.pop(len(deck.deck)-1))
      else:
        print("try again")
    else:
      print("try again")

def can_take_card(pile, card):
    if pile.identifier == 'normal stack':
        if len(pile.stack)==0 and card.value==13:
          return True
        elif len(pile.stack)!=0 and (pile.stack[0].value-card.value)==1 and color(pile.stack[0]) != color(card):
          return True
        else:
          return False
    elif pile.identifier == 'winning stack':
      if len(pile.stack)==0 and card.value==1:
        return True
      elif len(pile.stack) > 0:
        if (card.value-pile.stack[0].value)==1 and (pile.stack[0].suit == card.suit):
          return True
      else:
        return False
    else:
      print("select a normal stack or a winning stack")
      return False

def flip_up(normal_stacks):
  if len(normal_stacks.stack)==0 and len(normal_stacks.down_stack)>0:
      normal_stacks.stack.append(normal_stacks.down_stack.pop(0))
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
          elif to_location.identifier == 'normal stack':
            i=0
            while from_location.stack[i].value < card.value:
              i=i+1
            while i >= 0:
                to_location.stack.insert(0, from_location.stack.pop(i))
                i=i-1
            if len(from_location.stack)==0:
              flip_up(from_location)
        else:
            print("This move is against the rules. Sucks to suck.")

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

def show_stack_cards(pile):
    if len(pile.stack)>0:
        i=len(pile.stack)-1
        a='|'
        while i >= 0:
          if color(pile.stack[i])=='black':
            a=a + '\033[1;30m' + show_card_value(pile.stack[i]) + str(pile.stack[i].suit[0]) + '\033[1;m' + '|'
            i=i-1
          else:
            a=a + '\033[1;31m' + show_card_value(pile.stack[i]) + str(pile.stack[i].suit[0]) + '\033[1;m' + '|'
            i=i-1
        return a
    else:
        return ''

def show_down_cards(down_stack):
    if len(down_stack.down_stack)>0:
        i=len(down_stack.down_stack)
        a='|**'
        a=a * i
        return a
    else:
        return ''

def clear_stacks(stacks_type):
  if stacks_type[0].identifier == 'normal stack':
    for f in range(7):
      i=0
      b=len(stacks_type[f].stack)
      while i < b:
        del stacks_type[f].stack[0]
        i=i+1
      d=0
      c=len(stacks_type[f].down_stack)
      while d < c:
        del stacks_type[f].down_stack[0]
        d=d+1
  else:
    for f in range(4):
      i=0
      b=len(stacks_type[f].stack)
      while i < b:
        del stacks_type[f].stack[0]
        i=i+1

def check_for_win():
  a=0
  for i in range(4):
    a=a+len(winning_stacks[i].stack)
  if a == 52:
    print("You win. Stop playing solitaire and get a life... just saying.")
  l=0
  for i in range(7):
    l=l+len(normal_stacks[i].stack)
  for i in range(4):
    l=l+len(winning_stacks[i].stack)
  if l==52:
    print("You are set up to win")

from random import shuffle

#variables for making the move command easier
ns0 = normal_stacks[0]
ns1 = normal_stacks[1]
ns2 = normal_stacks[2]
ns3 = normal_stacks[3]
ns4 = normal_stacks[4]
ns5 = normal_stacks[5]
ns6 = normal_stacks[6]
ws0 = winning_stacks[0]
ws1 = winning_stacks[1]
ws2 = winning_stacks[2]
ws3 = winning_stacks[3]

def move(from_location, to_location, number_of_cards=1) :
  '''Moves the number of cards in number_of_cards (deck, ns#, or ws#) from the from_location to the to_location (ns# or ws#). The default number of cards is 1.'''
  if from_location.identifier == 'deck':
    if number_of_cards == 1:
      try:
          move_deck_card(to_location)
      except(IndexError):
        print("you tried to move more cards than you have")
      check_for_win()
      show()
    else:
      i=number_of_cards - 1
      while (i >= 0):
        if len(deck.deck) >2 and can_take_card(to_location, deck.deck[2]):
          try:
            move_deck_card(to_location)
            i=i-1
          except(IndexError):
            print("you tried to move more cards than you have")
        elif 2>len(deck.deck)>0 and can_take_card(to_location, deck.deck[len(deck.deck)-1]):
          try:
            move_deck_card(to_location)
            i=i-1
          except(IndexError):
            print("you tried to move more cards than you have")
        else:
          i=-1
      check_for_win()
      show()
  else:
    try:
      switch_stacks(from_location, from_location.stack[number_of_cards -1], to_location)
    except(IndexError):
      print("you tried to move more cards than you have")
    check_for_win()
    show()
    

def show():
  '''Shows your cards'''
  for i in range(7):
    print('normal stack' + str(i) + ': ' + show_down_cards(normal_stacks[i]) + show_stack_cards(normal_stacks[i]))
    i=i+1
  for i in range(4):
    print('winning stack' + str(i) + ': ' + show_stack_cards(winning_stacks[i]))
    i=i+1
  i=0
  a=''
  a=a + 'deck: '
  if len(deck.deck) > 0:
      a=a + '|'
  while ((i < 3) and (i < len(deck.deck))):
      if color(deck.deck[i])=='black':
          a=a + '\033[1;30m' + show_card_value(deck.deck[i]) + str(deck.deck[i].suit[0]) + '\033[1;m' + '|'
          i=i + 1
      else:
          a=a + '\033[1;31m' + show_card_value(deck.deck[i]) + str(deck.deck[i].suit[0]) + '\033[1;m' + '|'
          i=i + 1

  print(a)

def draw():
  '''Moves the top deck card to the bottom of the deck and shows your cards'''
  deck.next_deck_card()
  show()

def new():
  '''Starts a new game'''
  print ("Your commands are: 1. move(from_location, number_of_cards, to_location) = Moves the number of cards in number_of_cards from the from_locaiton to the to_location. 2. show() = Shows your cards. 3. draw() = Move the top deck card to the bottom of the deck and shows your cards. 4. new() = Starts a new game.")
  deck.deck = []
  deck.fill_deck()
  shuffle(deck.deck)
  clear_stacks(normal_stacks) 
  for i in range(7):
    normal_stacks[i].stack.append(deck.deck.pop(0))
    a=i
    while a > 0:
      normal_stacks[i].down_stack.append(deck.deck.pop(0))
      a=a-1
  clear_stacks(winning_stacks)
  show()
