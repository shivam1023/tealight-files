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
 turn(1)
 if touch()!="wall":
    continue
 turn(2)
    
    
    
