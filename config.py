import os


class Config(object):
    """Parent configuration class."""
    DEBUG = False
    SECRET = os.getenv("SECRET")


class DevelopmentConfiguration(Config):
    """Configurations for Development."""
    DEBUG = True
    DATABASE_URL = 'postgresql://postgres:password@localhost:5432/datavizr_db'
    ENV= 'development'

class TestingConfiguration(Config):
    """Configurations for Testing."""
    TESTING = True
    DEBUG = True
    DATABASE_URL = 'postgresql://postgres:password@localhost:5432/datavizr_test_db'
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
