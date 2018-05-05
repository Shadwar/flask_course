import os


class Config(object):
    """ Конфигурация сервера """

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'very-secret-key'
