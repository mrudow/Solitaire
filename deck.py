from card import *
car0=Card(2, 'red', 'diamonds')
car1=Card(2, 'red', 'hearts')
car2=Card(2, 'black', 'spades')
car3=Card(2, 'black', 'clubs')
car4=Card(3, 'red', 'diamonds')
car5=Card(3, 'red', 'hearts')
car6=Card(3, 'black', 'spades')
car7=Card(3, 'black', 'clubs')
car8=Card(4, 'red', 'diamonds')
car9=Card(4, 'red', 'hearts')
car10=Card(4, 'black', 'spades')
car11=Card(4, 'black', 'clubs')
car12=Card(5, 'red', 'diamonds')
car13=Card(5, 'red', 'hearts')
car14=Card(5, 'black', 'spades')
car15=Card(5, 'black', 'clubs')
car16=Card(6, 'red', 'diamonds')
car17=Card(6, 'red', 'hearts')
car18=Card(6, 'black', 'spades')
car19=Card(6, 'black', 'clubs')
car20=Card(7, 'red', 'diamonds')
car21=Card(7, 'red', 'hearts')
car22=Card(7, 'black', 'spades')
car23=Card(7, 'black', 'clubs')
car24=Card(8, 'red', 'diamonds')
car25=Card(8, 'red', 'hearts')
car26=Card(8, 'black', 'spades')
car27=Card(8, 'black', 'clubs')
car28=Card(9, 'red', 'diamonds')
car29=Card(9, 'red', 'hearts')
car30=Card(9, 'black', 'spades')
car31=Card(9, 'black', 'clubs')
car32=Card(10, 'red', 'diamonds')
car33=Card(10, 'red', 'hearts')
car34=Card(10, 'black', 'spades')
car35=Card(10, 'black', 'clubs')
car36=Card(11, 'red', 'diamonds')
car37=Card(11, 'red', 'hearts')
car38=Card(11, 'black', 'spades')
car39=Card(11, 'black', 'clubs')
car40=Card(12, 'red', 'diamonds')
car41=Card(12, 'red', 'hearts')
car42=Card(12, 'black', 'spades')
car43=Card(12, 'black', 'clubs')
car44=Card(13, 'red', 'diamonds')
car45=Card(13, 'red', 'hearts')
car46=Card(13, 'black', 'spades')
car47=Card(13, 'black', 'clubs')
car48=Card(14, 'red', 'diamonds')
car49=Card(14, 'red', 'hearts')
car50=Card(14, 'black', 'spades')
car51=Card(14, 'black', 'clubs')
class Deck:
    def __init__(self):
        self.deck = {0:car0, 1:car1, 2:car2, 3:car3, 4:car4, 5:car5, 6:car6, 7:car7, 8:car8, 9:car9, 10:car10, 11:car11, 12:car12, 13:car13, 14:car14, 15:car15, 16:car16, 17:car17, 18:car18, 19:car19, 20:car20, 21:car21, 22:car22, 23:car23, 24:car24, 25:car25, 26:car26, 27:car27, 28:car28, 29:car29, 30:car30, 31:car31, 32:car32, 33:car33, 34:car34, 35:car35, 36:car36, 37:car37, 38:car38, 39:car39, 40:car40, 41:car41, 42:car42, 43:car43, 44:car44, 45:car45, 46:car46, 47:car47, 48:car48, 49:car49, 50:car50, 51:car51}



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
