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
   
#shuffle string array of image locations
def shuffleCards():
 random.shuffle(animals)



#write function to assign images to Card objects
def assignImages():
  for i in range(0,48):
     deck[i].name2=animals[i]
  
  

#create a grid of cards using for loop etc
def placeCards():   
  x = 150
  y = 150
  for i in range(0,48):
    image(x, y,deck[i].name2)
    if x < 600:
      x = x + 100
    else:
      x = 150
      y = y + 100
      
#handle mouse events etc  
def mousestuff():
 lastx = 0
 lasty = 0

 def handle_mousedown(x,y):
  global lastx, lasty
  lastx = x
  lasty = y

 def handle_mousemove(x,y,button):
  global lastx, lasty
  if button == "left":
    lastx = x
    lasty = y
        
    
 

  
shuffleCards()  
assignImages()
placeCards()
  
  
  
  
  
  

  
  

