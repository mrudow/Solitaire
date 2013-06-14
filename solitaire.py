#!/usr/bin/python

class Deck:
    #ndc=number of deck cards
    def __init__(self, ndc=24):
      self.ndc=ndc
      self.deck = {1:a, 2:b, 3}

    def ch_ndc(self, up=True):
      if up:
          self.ndc=self.ndc-1
class Card:
    def __init__(self, color="red"):
        self.color=color

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
        elif len(stack)!=0:
            #see if next_card.color actually gives color
            if (stack[len(stack)]+next_card)==13 & (stack[len(stack)].color!=next_card.color);
                stack[len(stack)]=next_card
       

        
class Cstack:
    def __init__(self, up_cards=0):
        self.up_cards=up_cards
    
    cstack={}
   #elifs need need be edited for nc not next_card, cstack not stack numbers etc. 
    def add_card(self, nc):
      if len(cstack)==0 & nc==14:
        cstack[0]=nc
      elif len(cstack)==1:
          if (nc-cstack[len(cstack)]==14 & (stack[len(stack)].color!=next_card.color);
                stack[len(stack)]=next_card

      elif len(cstack)!=0:
          if (cstack[nc-len(cstack))==13 & (stack[len(stack)].color!=next_card.color);
                stack[len(stack)]=next_card

          

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


print(stack0, stack1, stack2, stack3, stack4, stack5, stack6, cstack0, cstack1, cstack2, cstack3, deck)
