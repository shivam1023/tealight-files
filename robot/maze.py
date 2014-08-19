from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

def movement():
  moves=0
  while moves<1250:
   while touch()!="wall":
    move()
   if touch()=="wall":
    turn(1)
   
  
movement()  
  
  
