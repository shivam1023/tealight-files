from tealight.art import (color, line, spot, circle, box, image, text, background)
from tealight.art import (screen_width, screen_height)
import random
from random import shuffle

background("paper.jpg")

#create the card class
class Card:
  def __init__(self):
    self.name1 = "misc/Card.png"
    self.name2= ""
    self.turnedOver=False
    
#create two global arrays for storing the Card objects and the animal locations    
global animals
animals = ["animals/Bear.png", "animals/Bear.png", "animals/Cat.png", "animals/Cat.png", "animals/Dog.png", "animals/Dog.png", "animals/Elephant.png", "animals/Elephant.png", "animals/Frog.png", "animals/Frog.png", "animals/Horse.png", "animals/Horse.png", "animals/Ladybird.png", "animals/Ladybird.png", "animals/Lion.png", "animals/Lion.png", "animals/Lobster.png", "animals/Lobster.png", "animals/Penguin.png", "animals/Penguin.png", "animals/Puffin.png", "animals/Puffin.png", "animals/Seagull.png", "animals/Seagull.png", "animals/Seal.png", "animals/Seal.png", "animals/Sheep.png", "animals/Sheep.png", "animals/Swan.png", "animals/Swan.png", "animals/Tiger.png", "animals/Tiger.png", "animals/Ant.png", "animals/Ant.png", "animals/Butterfly.png", "animals/Butterfly.png", "animals/Diplodocus.png", "animals/Diplodocus.png", "animals/Dolphin.png", "animals/Dolphin.png", "animals/Fish1.png", "animals/Fish1.png", "animals/Stegosaurus.png", "animals/Stegosaurus.png", "animals/Fish2.png", "animals/Fish2.png", "animals/Pterodactyl.png", "animals/Pterodactyl.png"] 
global deck
deck = [Card() for i in range(48)]
foundCards=[i for i in range(48)]

x=0
y=0


#shuffle string array of image locations
def shuffleCards():
 random.shuffle(animals)



#write function to assign images to Card objects
def assignImages():
  for i in range(0,48):
     deck[i].name2=animals[i]
  
  

#create a grid of cards using for loop etc
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
      
#assign individual card
def refreshCards(v):
  
  global x
  global y
    
  x = 150
  y = 150
  for i in range(0,48):
    
   if deck[i].turnedOver == False:
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
        
    else:
      
       
        image(x, y,deck[i].name1)
        if x < 600:
         x = x + 100
        else:
         x = 150
         y = y + 100
      
      
      
      
#handle mouse events etc  
lastx = 0
lasty = 0




score = 0

 
temp = None

cards_clicked =0

#Click detection and card identification
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
      
        refreshCards(v)
      
        if deck[temp].name2==deck[v].name2:
          
          deck[temp].turnedOver=True
          deck[v].turnedOver=True
          
          score=score+1
          print score
          cards_clicked=0
          temp=None
          v=None
          
        else:
          
          cards_clicked=0
          temp=None
          v=None
     
    
 


  
  
  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
         
  
shuffleCards()  
assignImages()
placeCards()
   
  
  
  
  
  
  

  
  

