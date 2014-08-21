from tealight.art import (color, line, spot, circle, box, image, text, background)
from tealight.art import (screen_width, screen_height)
import random

background("paper.jpg")


class Card:
  def __init__(self):
    self.name1 = "misc/Card.png"
    self.name2= ""
    self.turnedOver=False
    
global animals
animals=["animals/Ant.png","animals/Ant.png","animals/Bear.png","animals/Bear.png"]

global deck
deck = [Card() for i in range(4)]
   

  
  
#shuffle string array of image locations
def shuffleCards():
 random.shuffle(animals)



#write function to assign images to Card objects
def assignImages():
  
  for i in range(0,3):
     deck[i].name2=animals[i]
  
  

#create a grid of cards using for loop etc
def createGrid():
  for i in range(0,3):
     image(200,200,deck[i].name2)
 

  
shuffleCards()  
assignImages()
createGrid()
  
  
  
  
  
  

  
  
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
  
