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
  
   
while True: 
 movement()
 if touch()=="wall":
   turn(1)
