import os


class Config(object):
    """Parent configuration class."""
    DEBUG = False
    SECRET = os.getenv("SECRET") or 'secret'


class DevelopmentConfiguration(Config):
    """Configurations for Development."""
    DEBUG = True
    DATABASE_URL = os.environ.get('DEV_DATABASE_URL')
    ENV= 'development'

class TestingConfiguration(Config):
    """Configurations for Testing."""
    TESTING = True
    DEBUG = True
    DATABASE_URL = os.environ.get('TEST_DATABASE_URL')
    ENV = 'testing'

class ProductionConfiguration(Config):
    """Configurations for Production."""
    DEBUG = False
    DATABASE_URL = os.environ.get('DATABASE_URL')
    ENV = 'production'
    


app_config = {
    'DEFAULT': DevelopmentConfiguration,
    'TESTING': TestingConfiguration,
    'PRODUCTION': ProductionConfiguration
}
