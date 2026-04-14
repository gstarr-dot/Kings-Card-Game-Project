import pygame 
import random 

pygame.init()

#create window 
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))    #creates window 
pygame.display.set_caption("King's Card")            #title of window
clock = pygame.time.Clock()                          #controls frames per sec 
font = pygame.font.SysFont("Arial", 30)              #font for text in game 

#Creates a class for cards with suit and value  
class Card:
  def __init__(self, suit, value):
    self.suit = suit
    self.value = value

  def __str__(self):
    return f"{self.value} of {self.suit}"

#create the deck of cards used  
class Deck:
  def __init__(self):
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] #11=Jack, 12=Queen, 13=King, 14=Ace
    self.cards = [Card(suit, value) for suit in suits for value in values]

  def shuffle(self):            #randomly shuffle the deck 
    random.shuffle(self.cards)

  def deal_card(self):         #deals a card from deck 
    return self.cards.pop()

#create the deck and shuffle  
deck = Deck()
deck.shuffle()


#Level one - First Card 
stage = 1 
cards = []         #stores the cards drawn 
message = "Color of first Card? Red or Black?"

def is_red(card):
    return card.suit in ['Hearts', 'Diamonds']     #checks if card is red or not 

def reset():
  global deck, stage, cards, message 
  deck = Deck()
  deck.shuffle()
  stage = 1
  cards = []
  message = "Wrong! Try Again. Red of Black?"

#game loop 
running = True
while running:
  screen.fill((0, 120, 0))    #green background like solitare 

  #print text message 
  msg = font.render(message, True, (255, 255, 255))
  screen.blit(msg, (200, 50))

#print cards on screen 
  for i in range(len(cards)):
   text = font.render(str(cards[i]), True, (255, 255, 255))
   screen.blit(text, (300, 150 + i * 30))

  #buttons for stages 
  if stage == 1:
    b1 = pygame.Rect(200, 400, 150, 50)
    b2 = pygame.Rect(400, 400, 150, 50)
    pygame.draw.rect(screen, (255, 0, 0), b1)
    pygame.draw.rect(screen, (0, 0, 0), b2)

    screen.blit(font.render("Red", True, (255, 255, 255)), (220, 410))
    screen.blit(font.render("Black", True, (255, 255, 255)), (420, 410))

  #level 2 (higher/lower)
  elif stage == 2:
    b1 = pygame.Rect(200, 400, 150, 50)
    b2 = pygame.Rect(400, 400, 150, 50)
    pygame.draw.rect(screen, (255, 0, 0), b1)
    pygame.draw.rect(screen, (0, 0, 255), b2)

    screen.blit(font.render("Higher", True, (255, 255, 255)), (220, 410))
    screen.blit(font.render("Lower", True, (255, 255, 255)), (420, 410))
    
  #level 3 (inside/outside) 
  elif stage == 3:
    b1 = pygame.Rect(200, 400, 150, 50)
    b2 = pygame.Rect(400, 400, 150, 50)
    pygame.draw.rect(screen, (255, 0, 0), b1)
    pygame.draw.rect(screen, (0, 255, 0), b2)

    screen.blit(font.render("Inside", True, (255, 255, 255)), (220, 410))
    screen.blit(font.render("Outside", True, (255, 255, 255)), (420, 410))

  elif stage == 4:
    b1 = pygame.Rect(100, 400, 120, 50)
    b2 = pygame.Rect(250, 400, 120, 50)
    b3 = pygame.Rect(400, 400, 120, 50)
    b4 = pygame.Rect(550, 400, 120, 50)
    pygame.draw.rect(screen, (255, 0, 0), b1)
    pygame.draw.rect(screen, (0, 255, 0), b2)
    pygame.draw.rect(screen, (0, 0, 255), b3)
    pygame.draw.rect(screen, (255, 255, 0), b4)
    screen.blit(font.render("Hearts", True, (255, 255, 255)), (110, 410))
    screen.blit(font.render("Diamonds", True, (255, 255, 255)), (250, 410))
    screen.blit(font.render("Clubs", True, (255, 255, 255)), (410, 410))
    screen.blit(font.render("Spades", True, (255, 255, 255)), (560, 410))

  for events in pygame.event.get():
   if events.type == pygame.QUIT:
    running = False

   elif events.type == pygame.MOUSEBUTTONDOWN:

    new = deck.deal_card()

    #level 1 
    if stage == 1:
      if (b1.collidepoint(events.pos) and is_red(new)) or \
        (b2.collidepoint(events.pos) and not is_red(new)):
        cards.append(new)
        stage = 2
        message = "Higher or Lower?"
      else:
        reset()

    elif stage == 2:
        if (b1.collidepoint(events.pos) and new.value > cards[0].value) or \
        (b2.collidepoint(events.pos) and new.value < cards[0].value):
            cards.append(new)
            stage = 3
            message = "Inside or Outside?"
        else:
            reset()
    
    elif stage == 3:
      if (b1.collidepoint(events.pos) and cards[0].value < new.value < cards[1].value) or \
        (b2.collidepoint(events.pos) and (new.value < cards[0].value or new.value > cards[1].value)):
        cards.append(new)
        stage = 4
        message = "Pick a suit"
      else:
        reset()

    elif stage == 4:
      if (b1.collidepoint(events.pos) and new.suit == 'Hearts') or \
        (b2.collidepoint(events.pos) and new.suit == 'Diamonds') or \
        (b3.collidepoint(events.pos) and new.suit == 'Clubs') or \
        (b4.collidepoint(events.pos) and new.suit == 'Spades'):
        cards.append(new)
        message = "You Win"
        stage = 5 
      else:
        reset() 

  pygame.display.flip()
  clock.tick(60)

pygame.quit()

    

     


 










 

    

  







