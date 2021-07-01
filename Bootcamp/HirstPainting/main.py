# import colorgram
import random
import turtle as t
from turtle import Turtle, Screen

# 23 * 17
# hirst_colours = colorgram.extract('image.jpg', 30)
hirst_rgb = [(245, 244, 243), (239, 247, 243), (237, 241, 247), (249, 241, 245), (219, 156, 91), (127, 166, 192),
             (55, 102, 146), (182, 65, 29), (238, 209, 96), (128, 178, 146), (229, 66, 99), (62, 118, 83),
             (240, 65, 36), (213, 126, 151), (10, 43, 66), (182, 19, 9), (143, 71, 98), (173, 147, 53), (80, 158, 111),
             (65, 40, 20), (165, 22, 35), (239, 157, 173), (158, 212, 199), (28, 87, 55), (17, 60, 129),
             (244, 166, 152), (20, 53, 37), (107, 120, 168), (173, 188, 217), (70, 42, 50)]
# print(hirst_rgb)

trtl = t.Turtle()
trtl.speed("fastest")
t.colormode(255)
trtl.pu()
trtl.goto(-255, 255)
for i in range(17):
    for _ in range(23):
        trtl.pd()
        trtl.dot(25, random.choice(hirst_rgb))
        trtl.pu()
        trtl.goto(trtl.pos()[0] + 45, trtl.pos()[1])
    trtl.goto(-255, 255 - (i + 1) * 45)

s = Screen()
s.exitonclick()

