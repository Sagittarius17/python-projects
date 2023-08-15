import math
from turtle import *
import colorsys

h = 0.5  # Hue
s = 1  # Saturation
v = 1  # Value
n=36

speed(0)
bgcolor('black')
setup(width=1080, height=768)

# for t in range(0,361):  # values in degrees for turtle
#     rgb_color = colorsys.hsv_to_rgb(h, s, v)
#     h+=1/n
#     color(rgb_color)
#     t_rad = math.radians(t)
#     x = 12 * math.pow(math.sin(t_rad), 3)
#     y = 11 * math.cos(t_rad) - 5 * math.cos(2*t_rad) - 2 * math.cos(3*t_rad) - math.cos(4*t_rad)
#     goto(x*17, y*15) # you might need to scale your x and y
#     for j in range(5):
#         color(rgb_color)
#     goto(0, 0)
# done()


def hearta(k):
    return 15*math.sin(k)**3
def heartb(k):
    return 12*math.cos(k)-5*\
        math.cos(2*k)-2*\
            math.cos(3*k)-\
                math.cos(4*k)

for i in range(200):
    rgb_color = colorsys.hsv_to_rgb(h, s, v)
    h+=1/n
    color(rgb_color)
    goto(hearta(i)*15, heartb(i)*15)
    for j in range(5):
        color(rgb_color)
    goto(0, 0)
done()