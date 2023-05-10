from turtle import Turtle, Screen
import random

t = Turtle()
t.shape("turtle")

colors = ["DarkOrchid", "IndianRed", "DeepSkyBlue", "wheat", "SeaGreen"]

directions = [0, 90, 180, 270]
t.pensize(10)
for _ in range(100):
    t.color(random.choice(colors))
    t.forward(20)
    t.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()