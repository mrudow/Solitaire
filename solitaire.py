#!/usr/bin/python
#rlc=reorder location cards
from deck import *

def rlc(loc):
    del loc[0]
    i=1
    while i <= len(loc):
      loc[i-1] = loc[i]
      del loc[i]
      i=i+1

        

def move_up(stac):
  i=(len(stac.stack) - 1)
  while i >= 0:
      stac.stack[i+1]=stac.stack[i]
      del stac.stack[i]
      i=i-1
class Astack:
    def __init__(self):
        self.stack={}
        self.dstack={}
    
def flip_up(astack):
  if len(astack.stack)==0 and len(astack.dstack)>0:
      astack.stack[0]=astack.dstack[0]
      rlc(astack.dstack)
  else:
      0==0

def add_card_to_stack(astack, next_card):
    if len(astack.stack)==0 and next_card.value==13:
        astack.stack[0]=next_card
        return 1 
    elif len(astack.stack)!=0 and (astack.stack[0].value-next_card.value)==1 and (astack.stack[0].color!=next_card.color):
        move_up(astack)
        astack.stack[0]=next_card
        return 1
    elif len(astack.stack)!=0 and astack.stack[0].value==2 and next_card.value==14 and (astack.stack[0].color!=next_card.color):
        move_up(astack)
        astack.stack[0]=next_card
        return 1
    else:
        print ("Try again. If you're lucky, it might work")

#ss=switch stacks las and nex need to be of the form astack
def ss (las, card, nex):
    if len(las.stack)==0:
        print ("there is no card to move")
    else:
        if add_card_to_stack(nex, card)==1:
          if las.stack[0].value == card.value:
              rlc(las.stack)
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
              las.flip_up(las)
          show_cards()   
        else:
            print ("operation is invalid")

#m2cs=move to cstack origin is astack_
def m2cs(self, origin, card, dest):
  if len(origin.stack)==0:
      print("there is no card to move")
  else:
    card = origin.stack[0]
    if add_card(self, dest, card)==1:
      if len(origin.stack)==1:
        add_card(self, dest, card)
        del origin.stack[0]
        flip_up(self, origin.stack)
        if len(cstack0.cstack)+len(cstack1.cstack)+len(cstack2.cstack)+len(cstack3.cstack)==52:
            print "you win... get a life Michael"
        else:
            show_cards()
       

      else:
        add_card(self, dest, card)
        rlc(origin.stack)
        show_cards()
    else:
      print ("invalid move")

                    
stack0= Astack()
stack1= Astack()
stack2= Astack()
stack3= Astack()
stack4= Astack()
stack5= Astack()
stack6= Astack()

def shift_down_one(astack, starting_index):
    a=(len(astack.stack) - 1)
    if a==starting_index:
        del astack.stack[starting_index]
    else:
        while starting_index < a:
            del astack.stack[starting_index]
            astack.stack[starting_index]=astack.stack[starting_index + 1]
            del astack.stack[starting_index + 1]
            starting_index=starting_index + 1


class Wstack:
    def __init__(self,):
        self.cstack={}
    def add_card(self, cstack, nc):
      if len(self.cstack)==0 and nc.value==14:
        self.cstack[0]=nc
        return 1
      elif len(self.cstack)==1:
        if nc.value==2 and (self.cstack[0].suit==nc.suit):
          move_up(cstack) 
          self.cstack[0]=nc
          return 1
      elif len(self.cstack)>=2:
        if (nc.value-self.cstack[len(self.cstack)].vaue)==1 and (self.cstack[len(self.cstack)].suit==nc.suit):
          move_up(cstack)
          self.cstack[0]=nc
          return 1
      else:
        print ("This is not a valid move... Better luck next time")
    
    def m2s(self, card, dest):
      if len(self.cstack)==0:
        print "there is nothing to move"
      else:
        card= self.cstack[0]
        if add_card_to_stack(dest, card)==1:
          add_card_to_stack(dest, card)
          rlc(cstack)
          show_cards()
        else:
            print ("operation is against the rules")

    
    def switch_cstacks(self, card, dest):
        if card.value!=14:
            print ("operation is invalid")
        else:
          if dest.add_card(self, dest, card)==1:
              dest.add_card(self, dest, card)
              show_cards()
          else:
              print ("operation is invalid") 
  
cstack0= Wstack()
cstack1= Wstack()
cstack2= Wstack()
cstack3= Wstack()
#mdc=move deck card, dest is of form stack_ or cstack_
def mdc(dest):
  if str(dest)[11]=='A':
      if add_card_to_stack(dest, deck.deck[0])==1:
          rlc(deck.deck)
          show_cards()
      else:
          1==1
  elif str(dest)[11]=='W':
      if dest.add_card(dest, deck.deck[0])==1:
          rlc(deck.deck)
          if len(cstack0.cstack)+len(cstack1.cstack)+len(cstack2.cstack)+len(cstack3.cstack)==52:
            print "you win... get a life Michael"
          else:
            show_cards()
      else:
          1==1


def clear_pile(pile):
    i=0
    b=len(pile)
    while i < b:
        del pile[i]
        i=i+1
#ssc= show stack's cards
def ssc(astack):
    i=len(astack.stack)-1
    a=''
    while i >= 0:
        a= a + str(astack.stack[i].value)
        a= a + ' of '
        a= a + str(astack.stack[i].suit)
        if i > 1:
            a= a + ', '
        else:
            1==1
        i=i-1
    return a
def scsc(cstack):
    i=len(cstack.cstack)-1
    a=''
    while i >= 0:
        a= a + str(cstack.cstack[i].value)
        a= a + ' of '
        a=a + str(cstack.cstack[i].suit)
        if i > 1:
            a= a + ', '
        else:
            1==1
        i=i-1
    return a

def show_cards():
 
  print("first stack face up cards are " + ssc(stack0))

  print("second stack face up cards are " +ssc(stack1))
  if len(stack1.dstack)>0:
      print("second stack number of face down cards is " + str(len(stack1.dstack)))
  else:
      1==1

  print("third stack face up cards are " + ssc(stack2))
  if len(stack2.dstack)>0:
      print("third stack number of face down cards is " + str(len(stack2.dstack)))
  else:
      1==1

  print("fourth stack face up cards are " + ssc(stack3))
  if len(stack3.dstack)>0:
      print("fourth stack number of face down cards is " + str(len(stack3.dstack)))
  else:
      1==1

  print("fifth stack face up cards are " + ssc(stack4))
  if len(stack4.dstack)>0:
      print("fifth stack number of face down cards is " + str(len(stack4.dstack)))
  else:
      1==1

  print("sixth stack face up cards are " + ssc(stack5))
  if len(stack5.dstack)>0:
      print("sixth stack number of face down cards is " + str(len(stack5.dstack)))
  else:
      1==1

  print("seventh stack face up cards are " + ssc(stack6))
  if len(stack6.dstack)>0:
      print("seventh stack number of face down cards is " + str(len(stack6.dstack)))
  else:
      1==1

  if len(cstack0.cstack)>0:
      print("first winning stack cards are " + scsc(cstack0))
  else:
      print("first winning stack is empty")

  if len(cstack0.cstack)>0:
      print("second winning stack cards are " + scsc(cstack1))
  else:
      print("second winning stack is empty")

  if len(cstack0.cstack)>0:
      print("third winning stack cards are " + scsc(cstack2))
  else:
      print("third winning stack is empty")

  if len(cstack0.cstack)>0:
      print("fourth winning stack cards are " + scsc(cstack3))
  else:
      print("fourth winning stack is empty")

  if len(deck.deck) >=3:
      print("deck top three cards are " + str(deck.deck[0].value) + " of " + str(deck.deck[0].suit) + "," + ' ' + str(deck.deck[1].value) + " of " + str(deck.deck[1].suit) + "," + ' ' + str(deck.deck[2].value) + " of " + str(deck.deck[2].suit))
  elif len(deck.deck)==2:
      print("deck top two cards are " + str(deck.deck[0].value) + " of " + str(deck.deck[0].suit) + "," + ' ' + str(deck.deck[1].value) + " of " + str(deck.deck[1].suit))
  elif len(deck.deck)==1:
      print("deck card is the " + str(deck.deck[0].value ) + " of " + str(deck.deck[0].suit))
  else:
      print("deck is empty")







from random import shuffle
def new_game():
    clear_pile(deck.deck)
    i=0
    while i < 52:
        deck.deck[i]=fixdeck.deck[i]
        i=i+1
    shuffle(deck.deck)
    clear_pile(stack0.stack)
    clear_pile(stack1.stack)
    clear_pile(stack2.stack)
    clear_pile(stack3.stack)
    clear_pile(stack4.stack)
    clear_pile(stack5.stack)
    clear_pile(stack6.stack)

    stack0.stack[0]=deck.deck[0]
    rlc(deck.deck)

    stack1.stack[0]=deck.deck[0]
    rlc(deck.deck)
    stack1.dstack[0]=deck.deck[0]
    rlc(deck.deck) 

    stack2.stack[0]=deck.deck[0]
    rlc(deck.deck)
    stack2.dstack[0]=deck.deck[0]
    rlc(deck.deck)
    stack2.dstack[1]=deck.deck[0]
    rlc(deck.deck)

    stack3.stack[0]=deck.deck[0]
    rlc(deck.deck)
    stack3.dstack[0]=deck.deck[0]
    rlc(deck.deck)
    stack3.dstack[1]=deck.deck[0]
    rlc(deck.deck)
    stack3.dstack[2]=deck.deck[0]
    rlc(deck.deck)

    stack4.stack[0]=deck.deck[0]
    rlc(deck.deck)
    stack4.dstack[0]=deck.deck[0]
    rlc(deck.deck)
    stack4.dstack[1]=deck.deck[0]
    rlc(deck.deck)
    stack4.dstack[2]=deck.deck[0]
    rlc(deck.deck)
    stack4.dstack[3]=deck.deck[0]
    rlc(deck.deck)

    stack5.stack[0]=deck.deck[0]
    rlc(deck.deck)
    stack5.dstack[0]=deck.deck[0]
    rlc(deck.deck)
    stack5.dstack[1]=deck.deck[0]
    rlc(deck.deck)
    stack5.dstack[2]=deck.deck[0]
    rlc(deck.deck)
    stack5.dstack[3]=deck.deck[0]
    rlc(deck.deck)
    stack5.dstack[4]=deck.deck[0]
    rlc(deck.deck)
  
    stack6.stack[0]=deck.deck[0]
    rlc(deck.deck)
    stack6.dstack[0]=deck.deck[0]
    rlc(deck.deck)
    stack6.dstack[1]=deck.deck[0]
    rlc(deck.deck)
    stack6.dstack[2]=deck.deck[0]
    rlc(deck.deck)
    stack6.dstack[3]=deck.deck[0]
    rlc(deck.deck)
    stack6.dstack[4]=deck.deck[0]
    rlc(deck.deck)
    stack6.dstack[5]=deck.deck[0]
    rlc(deck.deck)
    
    clear_pile(cstack0.cstack)
    clear_pile(cstack1.cstack)
    clear_pile(cstack2.cstack)
    clear_pile(cstack3.cstack)

    show_cards()





