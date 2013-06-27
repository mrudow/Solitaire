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

        
#stac of form cstack_.cstack or stack_.stack
def move_up(stac):
  i=(len(stac) - 1)
  while i >= 0:
      stac[i+1]=stac[i]
      del stac[i]
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
        move_up(astack.stack)
        astack.stack[0]=next_card
        return 1
    elif len(astack.stack)!=0 and astack.stack[0].value==2 and next_card.value==14 and (astack.stack[0].color!=next_card.color):
        move_up(astack.stack)
        astack.stack[0]=next_card
        return 1
    else:
        print ("Try again...")

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
              flip_up(las)
          show_cards()   
        else:
            1==1

#m2cs=move to cstack origin is astack_



def m2cs(origin, dest):
  if len(origin.stack)==0:
      print("there is no card to move")
  else:
    card = origin.stack[0]
    if add_card(dest, card)==1:
      if len(origin.stack)==1:
        del origin.stack[0]
        flip_up(origin)
        show_cards()
      else:
        rlc(origin.stack)
        show_cards()
    else:
      1==1

                    
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
def add_card(wstack, nc):
  if len(wstack.cstack)==0 and nc.value==14:
    wstack.cstack[0]=nc
    return 1
  elif len(wstack.cstack)==1:
    if nc.value==2 and (wstack.cstack[0].suit==nc.suit):
      move_up(wstack.cstack) 
      wstack.cstack[0]=nc
      return 1
  elif len(wstack.cstack)>=2:
    if (nc.value-wstack.cstack[0].value)==1 and (wstack.cstack[0].suit==nc.suit):
      move_up(wstack.cstack)
      wstack.cstack[0]=nc
      
      if len(cstack0.cstack)+len(cstack1.cstack)+len(cstack2.cstack)+len(cstack3.cstack)==52:
        print "you win. Stop playing solitaire and get a life... just saying"
        return 1
      else:
        return 1
  else:
    print ("This is not a valid move")

def m2s(prev, dest):
  if len(prev.cstack)==0:
    print "there is nothing to move"
  else:
    card= prev.cstack[0]
    if add_card_to_stack(dest, card)==1:
      rlc(prev.cstack)
      show_cards()
    else:
        1==1


def switch_cstacks(prev, dest):
    if len(prev.cstack)==1:
      card= prev.cstack[0]
      if add_card(dest, card)==1:
        del prev.cstack[0]
        show_cards()
      else:
        print ("operation is invalid")
    else:
        print ("operation is invalid")
cstack0= Wstack()
cstack1= Wstack()
cstack2= Wstack()
cstack3= Wstack()     

#mdc=move deck card, dest is of form stack_ or cstack_
def mdc(dest):
  if str(dest)[11] == 'A':
      if add_card_to_stack(dest, deck.deck[0])==1:
          rlc(deck.deck)
          show_cards()
      else:
          1==1
  elif str(dest)[11] == 'W':
      if add_card(dest, deck.deck[0])==1:
          rlc(deck.deck)
          show_cards()
      else:
          1==1


def clear_pile(pile):
    i=0
    b=len(pile)
    while i < b:
        del pile[i]
        i=i+1

#scnof=show card number or face
def scnof(card):
    if card.value <11:
        return str(card.value)
    elif card.value == 11:
        return 'Jack'
    elif card.value == 12:
        return 'Queen'
    elif card.value == 13:
        return 'King'
    else:
        return 'Ace'
#ssc= show stack's cards, lstack=cstack_.cstack or stack_.stack
def ssc(lstack):
    i=len(lstack)-1
    a=''
    while i >= 0:
        if i > 0:
          a= a + scnof(lstack[i])
          a= a + ' of '
          a=a + str(lstack[i].suit)
          a= a + ', '
          i=i-1
        else:
          a= a + scnof(lstack[i])
          a= a + ' of '
          a=a + str(lstack[i].suit)
          i=i-1
    return a

def show_cards():
 
  print("stack0 cards include: " + ssc(stack0.stack))

  print("stack1 cards include: " + ssc(stack1.stack))
  if len(stack1.dstack)>0:
      print("stack1 number of face down cards is " + str(len(stack1.dstack)))
  else:
      1==1

  print("stack2 cards include: " + ssc(stack2.stack))
  if len(stack2.dstack)>0:
      print("stack2 number of face down cards is " + str(len(stack2.dstack)))
  else:
      1==1

  print("stack3 cards include: " + ssc(stack3.stack))
  if len(stack3.dstack)>0:
      print("stack3 number of face down cards is " + str(len(stack3.dstack)))
  else:
      1==1

  print("stack4 cards include: " + ssc(stack4.stack))
  if len(stack4.dstack)>0:
      print("stack4 number of face down cards is " + str(len(stack4.dstack)))
  else:
      1==1

  print("stack5 cards include: " + ssc(stack5.stack))
  if len(stack5.dstack)>0:
      print("stack5 number of face down cards is " + str(len(stack5.dstack)))
  else:
      1==1

  print("stack6 cards include: " + ssc(stack6.stack))
  if len(stack6.dstack)>0:
      print("stack6 number of face down cards is " + str(len(stack6.dstack)))
  else:
      1==1

  if len(cstack0.cstack)>0:
      print("cstack0 (winning stack) cards include: " + ssc(cstack0.cstack))
  else:
      print("cstack0 (winning stack) is empty")

  if len(cstack1.cstack)>0:
      print("cstack1 (winning stack) cards include: " + ssc(cstack1.cstack))
  else:
      print("cstack1 (winning stack) is empty")

  if len(cstack2.cstack)>0:
      print("cstack 2 (winning stack) cards include: " + ssc(cstack2.cstack))
  else:
      print("cstack 2 (winning stack) is empty")

  if len(cstack3.cstack)>0:
      print("cstack3 (winning stack) cards include: " + ssc(cstack3.cstack))
  else:
      print("cstack3 (winning stack) is empty")

  if len(deck.deck) >=3:
      print("deck top three cards are " + scnof(deck.deck[0]) + " of " + str(deck.deck[0].suit) + "," + ' ' + scnof(deck.deck[1]) + " of " + str(deck.deck[1].suit) + "," + ' ' + scnof(deck.deck[2]) + " of " + str(deck.deck[2].suit))
  elif len(deck.deck)==2:
      print("deck top two cards are " + scnof(deck.deck[0]) + " of " + str(deck.deck[0].suit) + "," + ' ' + scnof(deck.deck[1]) + " of " + str(deck.deck[1].suit))
  elif len(deck.deck)==1:
      print("deck card is the " + scnof(deck.deck[0]) + " of " + str(deck.deck[0].suit))
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




#commands

def ndc():
    deck.ndc()
    show_cards()

def move(prev, num_cards, dest):
    if prev == deck:
        if (str(dest)[11] == 'A') | (str(dest)[11] == 'W'):
          mdc(dest)
        else:
            print "select a stack or cstack as the destination"
    elif str(prev)[11] == 'A':
        if str(dest)[11] == 'A':
          ss(prev, prev.stack[num_cards - 1], dest)
        elif str(dest)[11] == 'W':
          m2cs(prev, dest)
        else:
            print "select a stack or cstack as the destination"
    elif str(prev)[11] == 'W':
        if str(dest)[11] == 'A':
          m2s(prev, dest)
        elif str(prev)[11] == 'W':
          switch_cstacks(prev, dest)
        else:
            print "select a stack or cstack as the destination"
    else:
        print ('select a valid place to move the card from')

def new():
    new_game()
