from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)




    
   
    
 int moves   
  
   
while True: 
  move()
  moves=moves+1
  if left_side()!="wall":
    turn(-1)
    move() 
    moves=moves+1
    continue
  if touch()=="wall":
    turn(1)
    move()
    moves=moves+1
    continue
    
  print moves  
    
    
 
  
    
 
   
   
      
    
    
    
