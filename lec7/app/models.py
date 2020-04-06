from app import db 

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), index=True, unique=True)
    password = db.Column(db.String(60))
    email = db.Column(db.String(100), index=True, unique=True)

    def __repr__(self):
        return '<User {} {}>'.format( self.username)
