import os

class Config(object):

    DEBUG = False

    CSRF_ENABLED = True

    SECRET_KEY = '\x01\xe7\xeb\xb7\xbe@\xc1\xa4Y\xc7\xe5R\xbe\xb0\xc0\xbbcLb.\xb6\xd6\x1bW'  

    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URI']
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True