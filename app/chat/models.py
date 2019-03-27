import uuid.uuid4
import datetime
from app.database import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(UUID(as_uuid = True) primary_key = True)
    username = db.Column(db.String(300))
    email = db.Column(db.String(300) unique = True)
    password_hash = db.Column(db.String)
    description = db.Column(db.String(1500))
    

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
    
    

class Messages(db.Model):
    __tablename__ = 'messages'

    id = db.Column(UUID(as_uuid = True) primary_key = True)
    user_id = db.Column(db.UUID, db.ForeignKey(User, verbose_name=_(""), on_delete=models.CASCADE))
    user = db.relationship('User', foreign_keys = user_id)
    message = db.Column(db.String(1500))
    date_create = db.Column(db.DateTime(), auto_field = datetime.datetime.now()))

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
