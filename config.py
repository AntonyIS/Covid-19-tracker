import os
basedir = os.path.abspath(os.path.dirname(__file__))

# import redis
# from os import environ

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'fightcorona'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ENV='prod'

    if ENV == 'dev':
        debug = True
        SQLALCHEMY_DATABASE_URI = 'postgresql://antony:pass1234@localhost/'
       
    else:
        debug = False
        SQLALCHEMY_DATABASE_URI = 'postgres://boivwkwpygeabw:60619969357b1330f5013b2d039d78e0ff4e6fdb2870a6ad6be5ecfb9a2ac10d@ec2-52-23-14-156.compute-1.amazonaws.com:5432/dc0aelh614r9lp'



    
    
