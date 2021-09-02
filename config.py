import os


class Config(object):
    """Parent configuration class."""
    DEBUG = False
    SECRET = os.getenv("SECRET")


class DevelopmentConfiguration(Config):
    """Configurations for Development."""
    DEBUG = True
    DATABASE_URL = ''
    ENV= 'development'

class TestingConfiguration(Config):
    """Configurations for Testing."""
    TESTING = True
    DEBUG = True
    DATABASE_URL = ''
    ENV = 'testing'

class ProductionConfiguration(Config):
    """Configurations for Production."""
    DEBUG = False
    DATABASE_URL = ''
    ENV = 'production'
    


app_config = {
    'DEFAULT': DevelopmentConfiguration,
    'TESTING': TestingConfiguration,
    'PRODUCTION': ProductionConfiguration
}
