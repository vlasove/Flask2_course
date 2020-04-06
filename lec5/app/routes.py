from app import app
from flask import render_template

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

@app.route('/')
@app.route('/home')
def homepage():
    return render_template('home.html', title= 'Home', user=mock_user, posts=mock_posts)


@app.route('/about')
def about():
    return render_template('about.html', user=mock_user)
