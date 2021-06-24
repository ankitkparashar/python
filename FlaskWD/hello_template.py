from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField("Submit")


app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'a5tr0N@ut^!23'


# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     name = None
#     form = NameForm()
#     if form.validate_on_submit():
#         name = form.name.data
#         form.name.data = ''
#     return render_template('index_wtf_bstrp.html', form=form, name=name)

# Using session
# @app.route("/", methods=["GET", "POST"])
# def index():
#     form = NameForm()
#     if form.validate_on_submit():
#         session["name"] = form.name.data
#         return redirect(url_for("index"))
#     return render_template("index_wtf_bstrp.html", form=form, name=session.get("name"))

# Using Flash message
@app.route("/", methods=["GET", "POST"])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash("Looks like you have changed your name!")
        session["name"] = form.name.data
        return redirect(url_for('index'))
    return render_template("index_wtf_bstrp.html", form=form, name=session.get("name"))


@app.route("/user/<name>")
def user(name):
    return render_template("user_inherited.html", name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
