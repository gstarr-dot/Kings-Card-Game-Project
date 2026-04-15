# King's Card 

Game Pitch: 
This project is for my game King's Card, which is a basic card game using a single 52-card deck. The game is broken into four levels, of which, if you fail, you return to level one. This game is all about a lucky guess or focusing on probabilities. 

Level 1- Choose the color of the random card. (red/black) \
Level 2 - Given the card, will the next card be higher or lower? (higher/lower) \
Level 3 - Is the value of the next card, inside or outside the values of the two previous cards? (inside/outside) \
Level 4 - Choose the suit of the final card. (hearts/diamonds/clubs/spades) \

How to Run:
python dist/main.py

Controls: 
The game uses mouse clicks to select a button on the screen. 

File Structure:

OOP Breakdown:
Classes - Card and deck 

Card Class - represents a single card in the deck. Specifies the suit and value, using 2-14, 11-14 representing Jack, Queen, King, and Ace, respectively. The card is printed on the screen using a string. 

Deck Class - represents a single full 52-card deck of playing cards. 
  random.shuffle() - shuffles the deck 
  deck.deal_card() - deals card 
  





