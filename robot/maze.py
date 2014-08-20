from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)




moves=0
   
while True: 
  move()
  moves+=1
  if left_side()!="wall":
    turn(-1)
    move()
    moves+=1
    continue
  if touch()=="wall":
    turn(1)
    move()
    moves+=1
    continue
    
 
    
    
 
  
    
 
   
   
      
    
    
    
