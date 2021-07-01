from flask import Flask
import random

app = Flask(__name__)
rand_num = random.randint(0, 9)


@app.route("/")
def hello_world(text="Guess a number between 0 & 9",
                image="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"):
    return f'<h1 style="text-align: left">{text}</h1>' \
           f'<img src={image}>'


@app.route("/<int:number>")
def guess(number):
    if number > rand_num:
        return hello_world(text="Too high, try again!", image="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif")
    elif number < rand_num:
        return hello_world(text="Too low, try again!", image="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif")
    else:
        return hello_world(text="You found me!", image="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif")


if __name__ == "__main__":
    app.run(debug=True)
