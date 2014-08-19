from tealight.logo import move, turn

def square():
  angle = 360.0 / 4
  for i in range(0, 4):
    move(30)
    turn(angle)
    
    

for n2 in range(0,8):  
 for n in range(0,8):
  square()
  move(30)

  
  
