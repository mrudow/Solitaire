#!/usr/bin/python

class Deck:
    #ndc=number of deck cards
    def __init__(self, ndc=24):
      self.ndc=ndc
      self.deck = {0:a, 1:b, 2:c, 3:d, 4:e, 5:f, 6:g, 7:h, 8:i, 9:j, 10:k, 11:l, 12:m, 13:n, 14:0, 15:p, 16:q, 17:r, 18:s, 19:t, 20:u, 21:v, 22:w, 23:x}

    
#mdc=move deck card
    self.deck[0]=card
    def mdc(self, card, dest):

      if dest==(stack0|stack1|stack2|stack3|stack4|stack5|stack6):
          if add_card_to_stack(dest, card)==1:
              add_card_to_stack(dest, card)
              del self.deck[0]
              i=1
              while i < len(self.deck):
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
              while i<len(self.deck):
                 self.deck[i-1] = self.deck[i]
                 del self.deck[i]
                 i=i+1
              self.ndc=self.ndc-1
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
    
    def flip_up(self, stack):
      if len(stack)==0 & len(dstack)>0:
          stack[0]=dstack[0]
          del dstack[0]
          i=1
          while i<len(dstack):
            dstack[i-1] = dstack[i]
            del dstack[i]
            i=i+1
      else:
          0==0

    def add_card_to_stack(self, stack, next_card):
        if len(stack)==0 & next_card==13:
            stack[0]=next_card
            return 1 
        elif len(stack)!=0 & (stack[len(stack)]+next_card)==13 & (stack[len(stack)].color!=next_card.color):
            stack[len(stack)]=next_card
            return 1
        else:
            print ("Try again. If you're lucky, it might work")

#ss=switch stacks (need to be able to do it for one OR MORE cards)
    def ss (self, stack, card, next_stack):
        if len(stack)==0:
            print ("there is no card to move")
        else:
            if add_card_to_stack(self, next_stack, card)==1:
              i=0
              a=1
              while i < len(stack):
                  if stack[i]==card:
                    add_card_to_stack(self, next_stack, card)
                    a=a-1
                    while a>0:
                        add_card_to_stack(self, next_stack, stack[a])
                        a=a-1
                  else:
                    i=i+1
                    a=a+1
              if len(stack)==0:
                  flip_up(self, stack)
                    
            else:
                print ("operation is invalid")

#m2cs=move to cstack
    def m2cs(self, card, dest):
      if len(stack)==0:
          if len(dstack)==0:
            print("there is no card to move")
          else:
            flip_up(dest)
            m2cs(self, card, dest)
      else:
        card = stack[0]
        if add_card(self, dest, card)==1:
          if len(stack)==1:
            add_card(self, dest, card)
            del stack[0]
            flip_up(self, stack)
           

          else:
            add_card(self, dest, card)
            del stack[0]
            i=1
            while i<len(stack):
              stack[i-1] = stack[i]
              del stack[i]
              i=i+1
        else:
          print ("invalid move")

                    
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
    
    def m2s(self, card, dest):
      if len(cstack)==0:
        print "there is nothing to move"
      else:
        card= cstack[0]
        if add_card_to_stack(self, dest, card)==1:
          add_card_to_stack(self, dest, card)
          del cstack[0]
          i=1
          while i<len(cstack):
            cstack[i-1] = cstack[i]
            del cstack[i]
            i=i+1
        else:
            print ("operation is against the rules")

    
    def switch_cstacks(self, card, dest):
        if card!=14:
            print ("operation is invalid")
        else:
          if add_card(self, dest, card)==1:
              add_card(self, dest, card)
          else:
              print ("operation is invalid")


def new_game(self):
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
