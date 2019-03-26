from app import db
import uuid.uuid4



class User(db.Model):
    __tablename__ = 'users'    
    id = db.Column(UUID(as_uuid = True) primary_key = True)
    username = db.Column(db.String(300))
    email = db.Column(db.String(300) unique = True)


    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
    
    

class Messages(db.model):
    __tablename__ = 'messages'


    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.UUID, db.ForeignKey(User, verbose_name=_(""), on_delete=models.CASCADE))
    user = db.relationship('User', foreign_keys = user_id)
    email = db.Column(db.String(300) unique = True)
