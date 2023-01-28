
import os
import openai
##OPEN API STUFF



openai.api_key = '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'




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
