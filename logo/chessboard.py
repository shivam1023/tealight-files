from tealight.logo import move, turn

def polygon(edges, size):
  angle = 360.0 / edges
  
  
  for i in range(0, edges):
    move(size)
    turn(angle)
    
    turn(angle)
  for i in range(0, edges):
    move(size)
    turn(angle)
    
    
    
    
    
polygon(4,30)