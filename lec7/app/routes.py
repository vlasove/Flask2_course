from app import app
from flask import render_template, redirect, url_for
from app.forms import LoginForm

mock_user = {"username" : "Evgen", 'phone' : '+9 999 222 333 444'}
mock_posts = [
    {
        'author' : {"username" : "Bob"},
        'body' : "It's my first post on this site!",
    },
    {
        'author' : {"username" : "Alice"},
        'body' : "Cool!",
    },
    {
        'author' : {"username" : "Alex"},
        'body' : "My fav book is LOTR!",
    },
]

@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html', title= 'Home', user=mock_user, posts=mock_posts)


@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html', user=mock_user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('home'))


    return render_template('login.html', form=form )
