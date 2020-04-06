from app import app
from flask import render_template

mock_user = {"username" : "Evgen"}

@app.route('/')
@app.route('/home')
def homepage():
    return render_template('home.html', title='Home', user=mock_user)