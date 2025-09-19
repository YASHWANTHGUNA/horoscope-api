from decouple import config

class Config(object):
    SECRET_key = config('SECRET_KEY', default='gess-me')
    DEBUG = False
    TESTING = False
    
    # Cache configuration
    CACHE_TYPE = 'SimpleCache'
    CACHE_DEFAULT_TIMEOUT = 3600 # 1 hour

class ProductionConfig(Config):
    DEBUG = False
    MAIL_DEBUG = False 

class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    
class TestingConfig(Config):
    TESTING = True