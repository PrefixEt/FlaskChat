import datetime
from app.database import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(300))
    email = db.Column(db.String(300), unique=True)
    password_hash = db.Column(db.String)
    description = db.Column(db.String(1500))
    

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
    
    

class Messages(db.Model):
    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', foreign_keys = user_id)
    message = db.Column(db.String(1500))
    date_create = db.Column(db.DateTime(),  default=db.func.current_timestamp())

    def __init__(self, *args, **kwargs):
        super(Messages, self).__init__(*args, **kwargs)
