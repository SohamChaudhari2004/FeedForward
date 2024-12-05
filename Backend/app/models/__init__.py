from flask import Flask
from flask_pymongo import PyMongo

mongo = PyMongo()

def init_app(app: Flask):
    ''' 
    initialize the flask application
    '''
    mongo.init_app(app)

