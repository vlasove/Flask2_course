from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from app import login 

@login.user_loader
def load_user(id :str):
    return User.query.get(int(id))

@login.user_loader
def load_user(id :str):
    return Store.query.get(int(id))

    
class Store(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    inn = db.Column(db.String(100), index=True, unique=True)
    password_hash = db.Column(db.String(300))

    email = db.Column(db.String(100), index=True, unique=True)
    books = db.relationship('Book', backref='store', lazy='dynamic')

    def set_password(self, password):
            self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<Store {}>'.format(self.inn)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    author = db.Column(db.String(300), index=True)
    bookname = db.Column(db.String(300), index=True)
    storenum = db.Column(db.Integer)
    store_id = db.Column(db.Integer, db.ForeignKey('store.id'))

    def __repr__(self):
        return '<Book {}>'.format(self.bookname)