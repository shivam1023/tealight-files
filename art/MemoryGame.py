from tealight.art import (color, line, spot, circle, box, image, text, background)
from tealight.art import (screen_width, screen_height)
import random

background("paper.jpg")
image(200,200,"misc/Card.png")

class Card():
  def __init__(self):
    self.Suit = 0
    self.Rank = 0


listOfCards=[i for i in range(6)]+[i for i in range(8)]
random.shuffle(listOfCards)
 

  
  
  
  
  
  

  
  
  
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
  
