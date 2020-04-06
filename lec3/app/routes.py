from app import app

@app.route('/')
@app.route('/home')
def homepage():
    return "Привет мир!"