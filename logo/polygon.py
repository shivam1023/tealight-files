from tealight.logo import move, turn

def polygon(edges, size):
  angle = 1.0
  for i in range(0, edges):
    move(size)
    turn(angle)
    
polygon(0,150)