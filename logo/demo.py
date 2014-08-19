from tealight.logo import (move, 
                           turn, 
                           color)

colors = ["red", "green", "blue"]

for i in range(0,500):
  move(i)
  turn(170)
  color(colors[i%3])