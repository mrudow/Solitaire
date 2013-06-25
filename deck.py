from card import *
car0=Card(2, 'red', 'diamond')
car1=Card(2, 'red', 'heart')
car2=Card(2, 'black', 'spade')
car3=Card(2, 'black', 'club')
car4=Card(3, 'red', 'diamond')
car5=Card(3, 'red', 'heart')
car6=Card(3, 'black', 'spade')
car7=Card(3, 'black', 'club')
car8=Card(4, 'red', 'diamond')
car9=Card(4, 'red', 'heart')
car10=Card(4, 'black', 'spade')
car11=Card(4, 'black', 'club')
car12=Card(5, 'red', 'diamond')
car13=Card(5, 'red', 'heart')
car14=Card(5, 'black', 'spade')
car15=Card(5, 'black', 'club')
car16=Card(6, 'red', 'diamond')
car17=Card(6, 'red', 'heart')
car18=Card(6, 'black', 'spade')
car19=Card(6, 'black', 'club')
car20=Card(7, 'red', 'diamond')
car21=Card(7, 'red', 'heart')
car22=Card(7, 'black', 'spade')
car23=Card(7, 'black', 'club')
car24=Card(8, 'red', 'diamond')
car25=Card(8, 'red', 'heart')
car26=Card(8, 'black', 'spade')
car27=Card(8, 'black', 'club')
car28=Card(9, 'red', 'diamond')
car29=Card(9, 'red', 'heart')
car30=Card(9, 'black', 'spade')
car31=Card(9, 'black', 'club')
car32=Card(10, 'red', 'diamond')
car33=Card(10, 'red', 'heart')
car34=Card(10, 'black', 'spade')
car35=Card(10, 'black', 'club')
car36=Card(11, 'red', 'diamond')
car37=Card(11, 'red', 'heart')
car38=Card(11, 'black', 'spade')
car39=Card(11, 'black', 'club')
car40=Card(12, 'red', 'diamond')
car41=Card(12, 'red', 'heart')
car42=Card(12, 'black', 'spade')
car43=Card(12, 'black', 'club')
car44=Card(13, 'red', 'diamond')
car45=Card(13, 'red', 'heart')
car46=Card(13, 'black', 'spade')
car47=Card(13, 'black', 'club')
car48=Card(14, 'red', 'diamond')
car49=Card(14, 'red', 'heart')
car50=Card(14, 'black', 'spade')
car51=Card(14, 'black', 'club')
class Deck:
    def __init__(self):
        self.deck = {0:car0, 1:car1, 2:car2, 3:car3, 4:car4, 5:car5, 6:car6, 7:car7, 8:car8, 9:car9, 10:car10, 11:car11, 12:car12, 13:car13, 14:car14, 15:car15, 16:car16, 17:car17, 18:car18, 19:car19, 20:car20, 21:car21, 22:car22, 23:car23, 24:car24, 25:car25, 26:car26, 27:car27, 28:car28, 29:car29, 30:car30, 31:car31, 32:car32, 33:car33, 34:car34, 35:car35, 36:car36, 37:car37, 38:car38, 39:car39, 40:car40, 41:car41, 42:car42, 43:car43, 44:car44, 45:car45, 46:car46, 47:car47, 48:car48, 49:car49, 50:car50, 51:car51}

#mdc=move deck card, dest is of form astack.stack_ or wstack.cstack_
    def mdc(self, dest):
      self.deck[0]=card
      if dest==(stack0.stack|stack1.stack|stack2.stack|stack3.stack|stack4.stack|stack5.stack|stack6.stack):
          if add_card_to_stack(dest, card)==1:
              add_card_to_stack(dest, card)
              rlc(self.deck)
              show_cards()
          else:
              1==1
      elif dest==(cstack0.cstack|cstack1.cstack|cstack2.cstack|cstack3.cstack):
          if add_card(dest, card)==1:
              add_card(dest, card)
              rlc(self.deck)
              if len(cstack0.cstack)+len(cstack1.cstack)+len(cstack2.cstack)+len(cstack3.cstack)==52:
                print "you win... get a life Michael"
              else:
                show_cards()
          else:
              1==1

#ndc=next deck card
    def ndc(self):
      self.deck[len(self.deck)]=self.deck[0]
      del self.deck[0]
      i=0
      while i< len(self.deck):
        self.deck[i]=self.deck[i+1]
        del self.deck[i+1]
        i=i+1

#from random import shuffle
#shuffle(deck) command can be used
deck= Deck()
fixdeck= Deck()
