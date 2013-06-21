#!/usr/bin/python
def rlc(self, loc):
    del self.loc[0]
    i=1
    while i < len(self.loc):
      self.deck[i-1] = self.loc[i]
      del self.loc[i]
      i=i+1

class Deck:
    #ndc=number of deck cards
    def __init__(self, ndc):
      self.ndc=len(deck)
      self.deck = {0:card(2, red, diamond), 1:card(2, red, heart), 2:card(2, black, spade), 3:card(2, black, club), 4:card(3, red, diamond), 5:card(3, red, heart), 6:card(3, black, spade), 7:card(3, black, club), 8:card(4, red, diamond), 9:card(4, red, heart), 10:card(4, black, spade), 11:card(4, black, club), 12:card(5, red, diamond), 13:card(5, red, heart), 14:card(5, black, spade), 15:card(5, black, club), 16:card(6, red, diamond), 17:card(6, red, heart), 18:card(6, black, spade), 19:card(6, black, club), 20:card(7, red, diamond), 21:card(7, red, heart), 22:card(7, black, spade), 23:card(7, black, club), 24:card(8, red, diamond), 25:card(8, red, heart), 26:card(8, black, spade), 27:card(8, black, club), 28:card(9, red, diamond), 29:card(9, red, heart), 30:card(9, black, spade), 31:card(9, black, club), 32:card(10, red, diamond), 33:card(10, red, heart), 34:card(10, black, spade), 35:card(10, black, club), 36:card(11, red, diamond), 37:card(11, red, heart), 38:card(11, black, spade), 39:card(11, black, club), 40:card(12, red, diamond), 41:card(12, red, heart), 42:card(12, black, spade), 43:card(12, black, club), 44:card(13, red, diamond), 45:card(13, red, heart), 46:card(13, black, spade), 47:card(13, black, club), 48:card(14, red, diamond), 49:card(14, red, heart), 50:card(14, black, spade), 51:card(14, black, club),}

#rlc=reorder location cards
           

#mdc=move deck card, dest is of form astack.stack_ or wstack.cstack_
    def mdc(self, card, dest):
      self.deck[0]=card
      if dest==(stack0|stack1|stack2|stack3|stack4|stack5|stack6):
          if add_card_to_stack(dest, card)==1:
              add_card_to_stack(dest, card)
              rlc(self.deck)
              show_cards()
          else:
              1==1
      elif dest==(cstack0|cstack1|cstack2|cstack3):
          if add_card(dest, card)==1:
              add_card(dest, card)
              rlc(self.deck)
              if len(wstack.cstack0)+len(wstack.cstack1)+len(wstack.cstack2)+len(wstack.cstack3)==52:
                print "you win... get a life Michael"
              else:
                show_cards()
          else:
              1==1

#ndc=next deck card
    def ndc(self, card):
      deck[len(deck)]=deck[0]
      del deck[0]
      i=0
      while i<=len(deck):
        deck[i]=deck[i+1]
        del deck[i+1]
        i=i+1
        
class Card:
    def __init__(self, value, color, suit):
        self.value=value
        self.color=color
        self.suit=suit

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
            if len(cstack0)+len(cstack1)+len(cstack2)+len(cstack3)==52:
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
      if len(cstack)==0 & nc.value==14:
        cstack[0]=nc
        return 1
      elif len(cstack)==1 & nc.value==2 & (cstack[0].suit==nc.suit):
        stack[1]=nc
        return 1
      elif len(cstack)>=2:
          if (nc.value-cstack[len(cstack)].vaue)==1 & (cstack[len(cstack)].suit==nc.suit):
            stack[len(stack)]=nc
            return 1
      else:
        print ("This is not a valid move... Better luck next time")
    
    def m2s(self, card, dest):
      if len(cstack)==0:
        print "there is nothing to move"
      else:
        card= cstack[0]
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
  



def show_cards(self):
  print("first stack face up cards are" stack0.stack)
 
  print("second stack face up cards are" stack1.stack)
  if stack.1.num_down_cards>0:
      print("second stack number of face down cards is" stack1.num_down_cards)
  else:
      1==1

  print("third stack face up cards are" stack2.stack)
  if stack.1.num_down_cards>0:
      print("third stack number of face down cards is" stack2.num_down_cards)
  else:
      1==1

  print("fourth stack face up cards are" stack3.stack)
  if stack.1.num_down_cards>0:
      print("fourth stack number of face down cards is" stack3.num_down_cards)
  else:
      1==1

  print("fifth stack face up cards are" stack4.stack)
  if stack.1.num_down_cards>0:
      print("fifth stack number of face down cards is" stack4.num_down_cards)
  else:
      1==1

  print("sixth stack face up cards are" stack5.stack)
  if stack.1.num_down_cards>0:
      print("sixth stack number of face down cards is" stack5.num_down_cards)
  else:
      1==1

  print("seventh stack face up cards are" stack6.stack)
  if stack.1.num_down_cards>0:
      print("seventh stack number of face down cards is" stack6.num_down_cards)
  else:
      1==1

  if len(cstack0.stack)>0:
      print("first winning stack cards are" cstack0.stack)
  else:
      print("first winning stack is empty")

  if len(cstack0.stack)>0:
      print("second winning stack cards are" cstack1.stack)
  else:
      print("second winning stack is empty")

  if len(cstack0.stack)>0:
      print("third winning stack cards are" cstack2.stack)
  else:
      print("third winning stack is empty")

  if len(cstack0.stack)>0:
      print("fourth winning stack cards are" cstack3.stack)
  else:
      print("fourth winning stack is empty")

  if len(deck)>=3:
      print("deck top three cards are" deck[0], deck[1], deck[2])
  elif len(deck)==2:
      print("deck top two cards are" deck[0], deck[1])
  elif len(deck)==1:
      print("deck card is" deck[0])
  else:
      print("deck is empty")





from random import shuffle

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
#print(stack0, stack1, stack2, stack3, stack4, stack5, stack6, cstack0, cstack1, cstack2, cstack3, deck)




'''at end, print that you win... get a life Michael'''

