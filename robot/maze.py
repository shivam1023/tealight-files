from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

for i in range(0,7):
 move()
turn(1)  
for i in range(0,2):
 move()
turn(-1)
for i in range(0,5):
 move()
turn(1) 

