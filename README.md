This is a game of solitaire to be played from the command line. To start, enter 'python' into the command line. Then enter 'from solitaire2 import *'. Finally, enter the 'new()' command. Your commands to play are:

1. move(prev, num_cards, dest) = move the number of cards in num_cards from prev to dest.

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
