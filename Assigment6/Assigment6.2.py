import turtle
import time
import math

Dimensions = 20

p = turtle.Pen()
p.shape("turtle")

p.penup()
p.goto(Dimensions, 0)
p.pendown()
for i in range(1,12):
    p.left((i*90)/(i+2)) # teta
    for j in range(i+2):
        p.left(360/(i+2))
        ange = 90-((i*90)/(i+2))
        ange = ange / 180 * math.pi
        side_length = 2 * Dimensions * i * math.sin(ange)
        p.forward(side_length)
    p.right((i*90)/(i+2))
    p.penup() #is used to stop the drawing.
    p.goto(Dimensions*i + Dimensions, 0)
    p.pendown()# is used to start the drawing.

turtle.done()