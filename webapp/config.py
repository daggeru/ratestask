import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'securethis_eg_by_vault_as_global_env'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestConfig(Config):
    DEBUG = True


class ProdConfig(Config):
    DEBUG = False
