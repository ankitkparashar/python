from turtle import Turtle, Screen
import turtle as t
import random

timmy_the_turtle = Turtle()

# # Changing the shape and colour
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")

# # Creating a square
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)

# # Creating a dashed line
# for _ in range(5):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()

# # Creating n sided shapes
# for sides in range(3, 11):
#     for _ in range(sides):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(360/sides)

# Creating a Random Walk
direction = [0, 90, 180, 270]
# colour = ["dark slate gray", "olive drab", "coral", "saddle brown", "dark slate blue", "Cornflower Blue",
#           "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen"]

# timmy_the_turtle.pensize(15)
timmy_the_turtle.speed("fastest")

t.colormode(255)


def random_colour():
    r: int = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


# for _ in range(200):
#     timmy_the_turtle.color(random_colour())
#     timmy_the_turtle.setheading(random.choice(direction))
#     timmy_the_turtle.forward(20)


def draw_spirograph(gap_size):
    for _ in range(int(360 / gap_size)):
        timmy_the_turtle.color(random_colour())
        timmy_the_turtle.circle(100)
        timmy_the_turtle.setheading(timmy_the_turtle.heading() + gap_size)


draw_spirograph(5)
screen = Screen()
screen.exitonclick()
