This is a game of solitaire to be played from the command line. To start, enter 'python' into the command line. Then enter 'from solitaire2 import *'. Finally, enter the 'new()' command. Your commands to play are:
1. move(from_location, number_of_cards, to_location) = move the number of cards in number_of_cards from the from_location to the to_location. Your options for the from_location are i: deck, ii: ns# where # is replaced with a number 0-6 refering to the normal stack of that number, iii: ws# where # is replaced with a number 0-3 referring to the winning stack of that number. Your options for the to_location are i: ns#, ii: ws#.

2. show() = shows your cards.

3. draw() = move the top deck card to the bottom of the deck and show your cards.

4. new() = start a new game.

5. help(command):
  i. help(move)
    move(from_location, number_of_cards, to_locaiton)
      Moves the number of cards in num_cards from prev to dest.
  
  ii. help(show)
    show()
      Shows your cards

  iii. help(draw)
    draw()
      Moves the top deck card to the bottom of the deck and shows your cards

  iv. help(new)
    new()
      Starts a new game 

Good luck!
