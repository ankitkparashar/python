import turtle
import pandas as pd

states = pd.read_csv("50_states.csv")
screen = turtle.Screen()
screen.title("U.S.States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

turtle_writer = turtle.Turtle()
turtle_writer.hideturtle()
turtle_writer.penup()
game_on = True
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
score = 0
correct_guesses = []
all_states = states["state"].to_list()
while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f"{score}/50 States correct.", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        # set_all_states = set(all_states)
        # set_correct_guesses = set(correct_guesses)
        # states_not_guessed = set_all_states.difference(set_correct_guesses)
        pd.DataFrame([state_name for state_name in all_states if state_name not in correct_guesses]).\
            to_csv("states_not_guessed.csv")
        break
    if answer_state in all_states:
        x = states[states["state"] == answer_state]["x"]
        y = states[states["state"] == answer_state]["y"]
        turtle_writer.goto(int(x), int(y))
        turtle_writer.write(answer_state, align="center")
        score += 1
        correct_guesses.append(answer_state)

turtle.mainloop()
