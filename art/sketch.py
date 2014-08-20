from tealight.art import (color, line, spot, circle, box, image, text, background)

lastx = 0
lasty = 0



def handle_mousedown(x,y):
  global lastx, lasty
  
  lastx = x
  lasty = y

def handle_mousemove(x,y,button):
  global lastx, lasty
  
  if button == "left":
    color("blue")
    line(lastx, lasty, x, y)
    lastx = x
    lasty = y
  
  if button == "right":
    color("red")
    line(lastx, lasty, x, y)
    lastx = x
    lasty = y
    