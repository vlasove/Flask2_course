from flask import Flask 

app = Flask(__name__)



@app.route('/anothers')
@app.route('/home', methods=['GET'])
@app.route('/', methods=['GET'])
def homepage():
    return "Hello world!"


@app.route('/info')
def information():
    return "Information page"

app.run(port=8080, debug=True)

