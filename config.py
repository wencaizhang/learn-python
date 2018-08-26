#encoding: utf-8
import os

DEBUG = True

SECRET_KEY = os.urandom(24)

USERNAME = 'root'
PASSWORD = 'iforget'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'db_demo1'

DB_URI = 'mysql+mysqldb://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOST, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
