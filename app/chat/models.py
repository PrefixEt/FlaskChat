from datetime import datetime
from app.database import db, login
from flask_login import UserMixin
import hashlib

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True, unique=True)
    username = db.Column(db.String(300), nullable=False)
    email = db.Column(db.String(300), unique=True, nullable=False)
    password_hash = db.Column(db.String)
    description = db.Column(db.String(1500))
    
    def __init__(self, **kwargs):
        self.username = kwargs.get('username')
        self.email = kwargs.get('email')
        self.password_hash = self.password_to_hash(kwargs.get('password_hash'))
        self.description = kwargs.get('description', '')


    def __repr__(self):
        return '<User: {} >'.format(self.username)
    
    def valid_pass(self, password):
        if password:
            return self.password_hash == self.password_to_hash(password)   
        return False

       
    def password_to_hash(self, pas):
        print(pas)
        return hashlib.sha224(pas.encode()).hexdigest()
    


class Message(db.Model):
    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key = True, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', foreign_keys = user_id)
    message = db.Column(db.String(1500), nullable= False)
    date_create = db.Column(db.DateTime(),  default=datetime.utcnow)

    def __init__(self, **kwargs):        
        self.user = kwargs.get('user', '')
        self.message = kwargs.get('message','')

    def __repr__(self):
        return  '<Message from {} [{}]: \n <{}>'.format(self.name, self.date_create, self.message) 



@login.user_loader
def login_user(id):
    return User.query.get(int(id))
    