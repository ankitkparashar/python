import requests
from flask import Flask, render_template
from post import Post


blog_url = "https://api.npoint.io/f549cdec175bddae3ace"
response = requests.get(url=blog_url)
all_posts = response.json()
post_objects = []
for post in all_posts:
    post_obj = Post(post)
    post_objects.append(post_obj)

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)


@app.route("/post/<int:num>")
def get_blog(num):
    for blog in post_objects:
        if blog.id == num:
            return render_template("post.html", blog=blog)


if __name__ == "__main__":
    app.run(debug=True)
