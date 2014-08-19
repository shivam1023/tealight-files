from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

def movement():
 while touch()!="wall":
  move()
 if touch()=="wall":
    turn(1)
   
  
movement()  
  
  
