import math
from turtle import *

speed(0)
bgcolor('black')
setup(width=1080, height=768)
for t in range(0,361):  # values in degrees for turtle
    t_rad = math.radians(t)
    x = 12 * math.pow(math.sin(t_rad), 3)
    y = 11 * math.cos(t_rad) - 5 * math.cos(2*t_rad) - 2 * math.cos(3*t_rad) - math.cos(4*t_rad)
    goto(x*17, y*15) # you might need to scale your x and y
    for j in range(5):
        color('red')
    goto(0, 0)
done()