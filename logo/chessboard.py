from tealight.logo import move, turn

def polygon(edges, size,times):
  angle = 360.0 / edges
  
 for i2 in range(0,times): 
  for i in range(0, edges):
    move(size)
    turn(angle)
    
    
    
    
polygon(4,30,8)