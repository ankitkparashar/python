from datetime import datetime
import requests
from flask import Flask, render_template
import random

app = Flask(__name__)

AGIFY_URL = "https://api.agify.io"
GENDER_URL = "https://api.genderize.io"


@app.route("/")
def home():
    random_number = random.randint(1, 10)
    year = datetime.now().year
    name = "Ankit"
    return render_template("index.html", num=random_number, year=year, name=name)


@app.route("/guess/<name>")
def guess_gender_age(name):
    params = {
        "name": name
    }
    age_data = requests.get(url=AGIFY_URL, params=params).json()
    gender_data = requests.get(url=GENDER_URL, params=params).json()
    return render_template("guess.html", name=name, age=age_data["age"], gender=gender_data["gender"].capitalize())


@app.route("/blog/<num>")
def get_blog(num):
    blog_url = "https://api.npoint.io/f549cdec175bddae3ace"
    response = requests.get(url=blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
