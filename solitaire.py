#!/usr/bin/python
#rlc=reorder location cards
from deck import *
def rlc(self, loc):
    del self.loc[0]
    i=1
    while i < len(self.loc):
      self.deck[i-1] = self.loc[i]
      del self.loc[i]
      i=i+1

        


class Astack:
    def __init__(self, num_up_cards=0, num_down_cards=0, stack={}, dstack={}):
        self.num_up_cards=len(stack)
        self.num_down_cards=len(dstack)
        self.stack=stack
        self.dstack=dstack
    
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

                    
class Wstack:
    def __init__(self, up_cards=0, cstack={}):
        self.up_cards=up_cards
        self.cstack=cstack
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
  



def show_cards():
 
  print("first stack face up cards are" + str(stack0.stack))

  print("second stack face up cards are" +str(stack1.stack))
  if stack1.num_down_cards>0:
      print("second stack number of face down cards is" + str(stack1.num_down_cards))
  else:
      1==1

  print("third stack face up cards are" + str(stack2.stack))
  if stack2.num_down_cards>0:
      print("third stack number of face down cards is" + str(stack2.num_down_cards))
  else:
      1==1

  print("fourth stack face up cards are" + str(stack3.stack))
  if stack3.num_down_cards>0:
      print("fourth stack number of face down cards is" + str(stack3.num_down_cards))
  else:
      1==1

  print("fifth stack face up cards are" + str(stack4.stack))
  if stack4.num_down_cards>0:
      print("fifth stack number of face down cards is" + str(stack4.num_down_cards))
  else:
      1==1

  print("sixth stack face up cards are" + str(stack5.stack))
  if stack5.num_down_cards>0:
      print("sixth stack number of face down cards is" + str(stack5.num_down_cards))
  else:
      1==1

  print("seventh stack face up cards are" + str(stack6.stack))
  if stack6.num_down_cards>0:
      print("seventh stack number of face down cards is" + str(stack6.num_down_cards))
  else:
      1==1

  if len(cstack0.stack)>0:
      print("first winning stack cards are" + str(cstack0.cstack))
  else:
      print("first winning stack is empty")

  if len(cstack0.stack)>0:
      print("second winning stack cards are" + str(cstack1.cstack))
  else:
      print("second winning stack is empty")

  if len(cstack0.stack)>0:
      print("third winning stack cards are" + str(cstack2.cstack))
  else:
      print("third winning stack is empty")

  if len(cstack0.stack)>0:
      print("fourth winning stack cards are" + str(cstack3.cstack))
  else:
      print("fourth winning stack is empty")

  if len(deck) >=3:
      print("deck top three cards are" + str(deck[0], deck[1], deck[2]))
  elif len(deck)==2:
      print("deck top two cards are" + str(deck[0], deck[1]))
  elif len(deck)==1:
      print("deck card is" + str(deck[0]))
  else:
      print("deck is empty")








def new_game(self):
    deck= Deck(52)
    shuffle(deck)
    
    stack0= Stack(0, 0)
    stack0.stack.append(deck[0])
    rlc(self.deck)

    stack1= Stack()
    stack1.stack.append(deck[0])
    rlc(self.deck)
    stack1.dstack.append(deck[0])
    rlc(self.deck) 

    stack2= Stack()
    stack2.stack.append(deck[0])
    rlc(self.deck)
    stack2.dstack.append(deck[0])
    rlc(self.deck)
    stack2.dstack.append(deck[0])
    rlc(self.deck)

    stack3= Stack()
    stack3.stack.append(deck[0])
    rlc(self.deck)
    stack3.dstack.append(deck[0])
    rlc(self.deck)
    stack3.dstack.append(deck[0])
    rlc(self.deck)
    stack3.dstack.append(deck[0])
    rlc(self.deck)

    stack4= Stack()
    stack4.stack.append(deck[0])
    rlc(self.deck)
    stack4.dstack.append(deck[0])
    rlc(self.deck)
    stack4.dstack.append(deck[0])
    rlc(self.deck)
    stack4.dstack.append(deck[0])
    rlc(self.deck)
    stack4.dstack.append(deck[0])
    rlc(self.deck)

    stack5= Stack()
    stack5.stack.append(deck[0])
    rlc(self.deck)
    stack5.dstack.append(deck[0])
    rlc(self.deck)
    stack5.dstack.append(deck[0])
    rlc(self.deck)
    stack5.dstack.append(deck[0])
    rlc(self.deck)
    stack5.dstack.append(deck[0])
    rlc(self.deck)
    stack5.dstack.append(deck[0])
    rlc(self.deck)
  
    stack6= Stack()
    stack6.stack.append(deck[0])
    rlc(self.deck)
    stack6.dstack.append(deck[0])
    rlc(self.deck)
    stack6.dstack.append(deck[0])
    rlc(self.deck)
    stack6.dstack.append(deck[0])
    rlc(self.deck)
    stack6.dstack.append(deck[0])
    rlc(self.deck)
    stack6.dstack.append(deck[0])
    rlc(self.deck)
    stack6.dstack.append(deck[0])
    rlc(self.deck)

    cstack0= Wstack()
    
    cstack1= Wstack()
    
    cstack2= Wstack()
    
    cstack3= Wstack()

    show_cards()





