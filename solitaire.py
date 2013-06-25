#!/usr/bin/python
#rlc=reorder location cards
from deck import *

def rlc(loc):
    del loc[0]
    i=1
    while i < len(loc):
      loc[i-1] = loc[i]
      del loc[i]
      i=i+1

        


class Astack:
    def __init__(self):
        self.stack={}
        self.dstack={}
    
    def flip_up(self, astack):
      if len(astack.stack)==0 & len(astack.dstack)>0:
          astack.stack[0]=astack.dstack[0]
          rlc(astack.dstack)
      else:
          0==0

    def add_card_to_stack(self, astack, next_card):
        if len(astack.stack)==0 & next_card.value==13:
            astack.stack[0]=next_card
            return 1 
        elif len(astack.stack)!=0 & (atack.stack[len(astack.stack)-1].value-next_card.value)==1 & (astack.stack[len(astack.stack)-1].color!=next_card.color):
            astack.stack[len(astack.stack)]=next_card
            return 1
        elif len(astack.stack)!=0 & astack.stack[len(astack.stack)-1].value==2 & next_card.value==14 & (astack.stack[len(astack.stack)-1].color!=next_card.color):
            astack.stack[len(astack.stack)]=next_card
            return 1
        else:
            print ("Try again. If you're lucky, it might work")

#ss=switch stacks las and card need to be of the form astack.stack_ where _ is a number
    def ss (self, las, card, nex):
        if len(las)==0:
            print ("there is no card to move")
        else:
            if add_card_to_stack(self, nex, card)==1:
              i=0
              a=1
              while i < len(las):
                  if las[i]==card:
                    add_card_to_stack(self, nex, card)
                    a=a-1
                    while a>0:
                        add_card_to_stack(self, nex, las[a])
                        a=a-1
                  else:
                    i=i+1
                    a=a+1
              if len(las)==0:
                  flip_up(self, las)
              show_cards()   
            else:
                print ("operation is invalid")

#m2cs=move to cstack origin is astack_
    def m2cs(self, origin, card, dest):
      if len(origin.stack)==0:
          if len(origin.dstack)==0:
            print("there is no card to move")
          else:
            flip_up(dest)
            m2cs(self, card, dest)
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

class Wstack:
    def __init__(self,):
        self.cstack={}
    def add_card(self, cstack, nc):
      if len(self.cstack)==0 & nc.value==14:
        self.cstack[0]=nc
        return 1
      elif len(self.cstack)==1 & nc.value==2 & (self.cstack[0].suit==nc.suit):
        self.cstack[1]=nc
        return 1
      elif len(self.cstack)>=2:
          if (nc.value-self.cstack[len(self.cstack)].vaue)==1 & (self.cstack[len(self.cstack)].suit==nc.suit):
            self.cstack[len(self.cstack)]=nc
            return 1
      else:
        print ("This is not a valid move... Better luck next time")
    
    def m2s(self, card, dest):
      if len(self.cstack)==0:
        print "there is nothing to move"
      else:
        card= self.cstack[0]
        if add_card_to_stack(self, dest, card)==1:
          add_card_to_stack(self, dest, card)
          rlc(cstack)
          show_cards()
        else:
            print ("operation is against the rules")

    
    def switch_cstacks(self, card, dest):
        if card.value!=14:
            print ("operation is invalid")
        else:
          if add_card(self, dest, card)==1:
              add_card(self, dest, card)
              show_cards()
          else:
              print ("operation is invalid")
  
cstack0= Wstack()
cstack1= Wstack()
cstack2= Wstack()
cstack3= Wstack()



def clear_pile(pile):
    i=0
    while i < len(pile):
        del pile[i]
        i=i+1
#ssc= show stack's cards
def ssc(stack):
    i=len(stack.stack)-1
    a=''
    while i >= 0:
        a= a + str(stack.stack[i].value)
        a= a + ' of '
        a= a + str(stack.stack[i].suit)
        if i > 1:
            a= a + ', '
        else:
            1==1
        i=i-1
    return a
def scsc(cstack):
    i=len(cstack.stack)-1
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





