from tealight.art import (color, line, spot, circle, box, image, text, background)
from tealight.art import (screen_width, screen_height)
import random

background("paper.jpg")

animals=["animals/Ant.png","animals/Ant.png","animals/Bear.png","animals/Bear.png"]

class Card:
  def __init__(self,image):
    self.name = ""
    self.turnedOver=False
   
#create an array of objects of Card class 
def createDeck():
 deck=[Card() for i in range(2)]+[Card() for i in range(2)]
  
  
#shuffle string array of image locations  

#write function to assign images to Card objects
def assignImages():
  
  deck[1].name="animals/Ant.png"
  

#create a grid of cards using for loop etc

image(200,200,deck[1].name)
 

  
  
  
  
  
  

  
  
#handle mouse events etc  

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
  
