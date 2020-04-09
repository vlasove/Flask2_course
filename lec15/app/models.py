from datetime import datetime
from hashlib import md5

from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from app import db, login


@login.user_loader
def load_user(id :str):
    return User.query.get(int(id))


followers = db.Table(
    'followers', 
    db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('follows_id', db.Integer, db.ForeignKey('user.id'))
)

class User(UserMixin , db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), index=True, unique=True)
    password_hash = db.Column(db.String(300))
    email = db.Column(db.String(100), index=True, unique=True)

    about_me = db.Column(db.String(400))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)


    posts = db.relationship('Post', backref='author', lazy='dynamic')

    followed = db.relationship('User', secondary=followers ,
        primaryjoin=(followers.c.follower_id == id),
        secondaryjoin=(followers.c.follows_id == id),
        backref=db.backref('followers', lazy='dynamic'), lazy ='dynamic')


    def follow(self, user):
        if not self.is_following(user):
            self.followed.append(user) 

    def unfollow(self, user):
        if self.is_following(user):
            self.followed.remove(user) 

    def is_following(self, user):
        return self.followed.filter(followers.c.follows_id == user.id).count() > 0

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

