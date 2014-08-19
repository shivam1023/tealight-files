from tealight.logo import move, turn

def square(edges, size):
  angle = 360.0 / edges
  
  
  for i in range(0, edges):
    move(size)
    turn(angle)
    
    

for n2 in range(0,8):  
  turn(180)
 for n in range(0,8):
  square(4,30)
  move(30)

  
  
