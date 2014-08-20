from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)





   
while True: 
  move()
  
  if left_side()!="wall":
    turn(-1)
    move() 
   
    continue
  if touch()=="wall":
    turn(1)
    move()
   
    continue
    
 
    
    
 
  
    
 
   
   
      
    
    
    
