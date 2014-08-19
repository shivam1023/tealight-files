from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)



while True:
  if touch()!="fruit":
    if right_side=="fruit":
      turn(1)
    if left_side=="fruit":
      turn(-1)
  move()    
    
