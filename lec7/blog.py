from app import app , db 
from app.models import Post, User 

@app.shell_context_processor
def make_shell_context():
    return {'User' : User ,'Post' : Post, 'db' : db}

if __name__ == '__main__':
    app.run(port=8080, debug=True)