from tealight.logo import (move, 
                           turn, 
                           color)

colors = ["red", "green", "blue"]

for i in range(0,1000):
  move(i)
  turn(91)
  color(colors[i%3])