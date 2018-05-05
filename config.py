import os
basedir = os.path.abspath(os.path.dirname(__name__))

class Config(object):
    """ Конфигурация сервера """

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'very-secret-key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST = 'static/img'
