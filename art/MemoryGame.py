from tealight.art import (color, line, spot, circle, box, image, text, background)
from tealight.art import (screen_width, screen_height)
import random
from random import shuffle

#define background/colors/title
background("paper.jpg")
color("brown")
image(245, 50, "http://i.imgur.com/uwIg3Du.png")

#create the card class
class Card:
  def __init__(self):
    self.name1 = "misc/Card.png"
    self.name2= ""
    self.turnedOver=False
    
#create global array for storing the animal locations    
global animals
animals = ["animals/Bear.png", "animals/Bear.png", "animals/Cat.png", "animals/Cat.png", "animals/Dog.png", "animals/Dog.png", "animals/Elephant.png", "animals/Elephant.png", "animals/Frog.png", "animals/Frog.png", "animals/Horse.png", "animals/Horse.png", "animals/Ladybird.png", "animals/Ladybird.png", "animals/Lion.png", "animals/Lion.png", "animals/Lobster.png", "animals/Lobster.png", "animals/Penguin.png", "animals/Penguin.png", "animals/Puffin.png", "animals/Puffin.png", "animals/Seagull.png", "animals/Seagull.png", "animals/Seal.png", "animals/Seal.png", "animals/Sheep.png", "animals/Sheep.png", "animals/Swan.png", "animals/Swan.png", "animals/Tiger.png", "animals/Tiger.png", "animals/Ant.png", "animals/Ant.png", "animals/Butterfly.png", "animals/Butterfly.png", "animals/Diplodocus.png", "animals/Diplodocus.png", "animals/Dolphin.png", "animals/Dolphin.png", "animals/Fish1.png", "animals/Fish1.png", "animals/Stegosaurus.png", "animals/Stegosaurus.png", "animals/Fish2.png", "animals/Fish2.png", "animals/Pterodactyl.png", "animals/Pterodactyl.png"] 
#create global array for storing the Card objects  
global deck
deck = [Card() for i in range(48)]

#initialise variables for x,y coordinates and game variables like score/temp
x=0
y=0

lastx = 0
lasty = 0

score = 0

temp = None

cards_clicked =0


#shuffle string array of image locations
def shuffleCards():
 random.shuffle(animals)



#write function to assign images to Card objects
def assignImages():
  for i in range(0,48):
     deck[i].name2=animals[i]
  
  

#create a grid of cards using for loop
def placeCards(): 

  global x
  global y
  
  x = 150
  y = 150
  for i in range(0,48):
    image(x, y,deck[i].name1)
    if x < 600:
      x = x + 100
    else:
      x = 150
      y = y + 100
      
#refresh screen after each card is flipped over
def refreshCards(v):
  
  background("paper.jpg")
  image(245, 50, "http://i.imgur.com/uwIg3Du.png")
  
  global x
  global y
  global temp
  
    
  x = 150
  y = 150
  for i in range(0,48):
     
    if i==v:
       
       image(x,y,deck[v].name2)
       if x < 600:
        x = x + 100
       else:
        x = 150
        y = y + 100
        
    elif i == temp:
       
       image(x,y,deck[temp].name2)
       if x < 600:
        x = x + 100
       else:
        x = 150
        y = y + 100
        
    elif deck[i].turnedOver == True: 
      
      image(x,y,deck[i].name2)
      if x < 600:
        x = x + 100
      else:
        x = 150
        y = y + 100
        
    else:
        image(x, y,deck[i].name1)
        if x < 600:
         x = x + 100
        else:
         x = 150
         y = y + 100
      
        
  
shuffleCards()  
assignImages()
placeCards()
   

#Click detection and card identification and also game logic
def handle_mousedown(x,y,button):
  
  global lastx, lasty
  global cards_clicked
  global temp
  global score

  
  if button == "left":
    lastx = x
    lasty = y
    a = (lastx - 150)/100
    b = (lasty - 150)/100
    v = b * 6 + a
    print "Cell: (%d, %d), n: %d" % (a,b,v)
    
    

    #when a card has been clicked
    
    cards_clicked = cards_clicked + 1

    if cards_clicked == 1:
  
    
     temp = v
      
     refreshCards(v)
     
    if cards_clicked==2:
      
        #refreshCards(v)
      
        if deck[temp].name2==deck[v].name2:
          
          deck[temp].turnedOver=True
          deck[v].turnedOver=True
          
          refreshCards(v)
          
          score=score+1
          print score
          cards_clicked=0
          temp=None
          v=None
          
        else:
          
          refreshCards(v)
          
          cards_clicked=0
          temp=None
          v=None
          
          
          
    if score == 24:
      image(275, 400, "http://i.imgur.com/eSSXfA8.png")
      
    else:
      text(780,50,"Score: %d" %score)
     
    
 


  
  
  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

  
  
  
  
  
  

  
  

