from app import db
from hashlib import md5 
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from app import login 

@login.user_loader
def load_user(id :str):
    return User.query.get(int(id))


class User(UserMixin , db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), index=True, unique=True)
    password_hash = db.Column(db.String(300))
    email = db.Column(db.String(100), index=True, unique=True)
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def avatar(self, size):
        nums = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(nums, size)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password) 

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format( self.username)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    body = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)




