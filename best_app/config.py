import os

class DbConfig(object):
    #SQLALCHEMY_DATABASE_URI = "postgresql://admin_user1:12345@127.0.0.1:5432/single_db"
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
