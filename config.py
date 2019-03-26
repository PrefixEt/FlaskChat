


class Config(object):
    DEBUG = True
    SECRET_KEY = '\x01\xe7\xeb\xb7\xbe@\xc1\xa4Y\xc7\xe5R\xbe\xb0\xc0\xbbcLb.\xb6\xd6\x1bW'
    SQL_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgres+psycopg2://postgres:postgres@localhost/ChatBase'