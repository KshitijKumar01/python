from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Enter the color of the turtle : ")
# print(user_bet)
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    t = Turtle(shape="turtle")
    t.color(colors[turtle_index])
    t.penup()
    t.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(t)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if(winning_color == user_bet):
                print(f"You've won! The winning color is {winning_color}")
            else:
                print(f"You've lose! The winning color is {winning_color}")

        random_distance =  random.randint(0,10)
        turtle.forward(random_distance)


screen.exitonclick()