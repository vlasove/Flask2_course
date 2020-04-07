from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), index=True, unique=True)
    password = db.Column(db.String(60))
    email = db.Column(db.String(100), index=True, unique=True)
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format( self.username)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    body = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)

class Equation(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    a = db.Column(db.Integer) 
    b = db.Column(db.Integer) 
    c = db.Column(db.Integer)
    #x12 = (-b +- D**0.5) / (2*a)

    def solve(self):
        d = self.b**2 - 4*self.a*self.c
        if self.a == 0:
            if self.b == 0:
                return 0
            else:
                return 1
        elif d > 0:
            return 2
        elif d == 0:
            return 1
        else: 
            return 0


    def __repr__(self):
        return '<Equation {}*x^2 + {}*x + {} = 0 has {} solution(s)>'.format(self.a, self.b, self.c, self.solve())
        


