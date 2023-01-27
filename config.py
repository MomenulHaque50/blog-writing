##OPEN API STUFF
OPENAI_API_KEY = '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'



## FLASK STUFF
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "this-is-a-super-secret-key"


config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}
