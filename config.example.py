"""
@author: raymondchen
@date: 2018/5/10
Description:
    This is the example config file.
"""

class Config(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'mysql://username:password@ip_address:port/DB_NAME'