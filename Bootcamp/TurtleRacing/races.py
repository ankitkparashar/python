from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput("Make your bet!", "Which turtle will win the race? Enter a colour: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

for i in range(6):
    trtl = Turtle(shape="turtle")
    trtl.color(colors[i])
    trtl.pu()
    trtl.goto(-230, 100 - (i * 40))
    all_turtles.append(trtl)

is_race_on = False
if user_bet:
    is_race_on = True

while is_race_on:
    for trtl in all_turtles:
        if trtl.xcor() > 230:
            is_race_on = False
            winning_color = trtl.pencolor()
            if winning_color == user_bet:
                print(f"You've won! {winning_color} has won the race.")
            else:
                print(f"You've lost. {winning_color} has won the race.")
        random_dist = random.randint(0, 10)
        trtl.forward(random_dist)

screen.exitonclick()
