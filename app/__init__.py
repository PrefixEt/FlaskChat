import os
from flask import Flask

from .database import db, login, migrate
from .soket import socketio

def create_app():
    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])
    login.init_app(app)
    socketio.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    
    with app.test_request_context():
        db.create_all()


    import app.chat.controllers as chat

    app.register_blueprint(chat.module)

    return app
