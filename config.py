
import os
import openai
##OPEN API STUFF

OPENAI_API_KEY='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'

openai.api_key = os.getenv("OPENAI_API_KEY")




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
