#!/usr/bin/python

class Deck:
    #ndc=number of deck cards
    def __init__(self, ndc=24):
      self.ndc=ndc
      self.deck = {0:a, 1:b, 2:c, 3:d, 4:e, 5:f, 6:g, 7:h, 8:i, 9:j, 10:k, 11:l, 12:m, 13:n, 14:0, 15:p, 16:q, 17:r, 18:s, 19:t, 20:u, 21:v, 22:w, 23:x}

    
#mdc=move deck card
    self.deck[0]=card
    def mdc(self, card, dest)

      if dest==(stack0|stack1|stack2|stack3|stack4|stack5|stack6):
          if add_card_to_stack(dest, card)==1:
              add_card_to_stack(dest, card)
              del self.deck[0]
              i=1
              for i<len(self.deck):
                 self.deck[i-1] = self.deck[i]
                 del self.deck[i]
                 i=i+1
              self.ndc=self.ndc-1
          else:
              1==1
      elif dest==(cstack0|cstack1|cstack2|cstack3):
          if add_card(dest, card)==1:
              add_card(dest, card)
              del self.deck[0]
              i=1
              for i<len(self.deck):
                 self.deck[i-1] = self.deck.[i]
                 del self.deck[i]
                 i=i+1
              self.ndc=self.ndc-1
          else:
              1==1


        
class Card:
    def __init__(self, color="red", suit="diamond"):
        self.color=color
        self.suit=suite

    '''def is_even(card):
        if (card % 2==0):
          return True
        else:
          return False'''

class Stack:
    def __init__(self, num_up_cards=1, num_down_cards=0):
        self.num_up_cards=num_up_cards
        self.num_down_cards=num_down_cards
    
    stack={}
    dstack={}
    
    def add_card_to_stack(self, stack, next_card):
        if len(stack)==0 & next_card==13:
            stack[0]=next_card
            return 1 
        elif len(stack)!=0 & (stack[len(stack)]+next_card)==13 & (stack[len(stack)].color!=next_card.color):
            stack[len(stack)]=next_card
            return 1
        else:
            print ("Try again. If you're lucky, it might work")
                    
class Cstack:
    def __init__(self, up_cards=0):
        self.up_cards=up_cards
    
    cstack={}
    def add_card(self, cstack, nc):
      if len(cstack)==0 & nc==14:
        cstack[0]=nc
        return 1
      elif len(cstack)==1 & nc==2 & (cstack[0].suit==nc.suit):
        stack[1]=nc
        return 1
      elif len(cstack)>=2:
          if (nc-cstack[len(cstack)])==1 & (cstack[len(cstack)].suit==nc.suit):
            stack[len(stack)]=nc
            return 1
      else:
        print ("This is not a valid move... Better luck next time")

stack0= Stack(0, 0)
stack1= Stack(0, 1)
stack2= Stack(0, 2)
stack3= Stack(0, 3)
stack4= Stack(0, 4)
stack5= Stack(0, 5)
stack6= Stack(0, 6)
cstack0= Cstack()
cstack1= Cstack()
cstack2= Cstack()
cstack3= Cstack()


#print(stack0, stack1, stack2, stack3, stack4, stack5, stack6, cstack0, cstack1, cstack2, cstack3, deck)




'''at end, print that you win... get a life Michael'''
