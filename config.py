import os.path


class Config(object):
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SECRET_KEY = 'MinhaNamoradaEUmaGostosinhaLinda'

	basedir = os.path.abspath(os.path.dirname(__file__))
	sqlite = 'sqlite:///' + os.path.join(basedir, 'storage.db')
	DATABASE_URI = sqlite
	
	DEBUG = False

class ProductionConfig(Config):
	
	postgres = 'postgres://tmtwbwwmhlmxdh:4260a7b8d6a55429da3021e1768727e1eec76b41d28cf18fda4405059e50a2e4@ec2-52-202-146-43.compute-1.amazonaws.com:5432/dbuqjpd86km3jc'
	
	DATABASE_URI = postgres
	SQLALCHEMY_DATABASE_URI = DATABASE_URI
	DEBUG = False

class DevelopmentConfig(Config):
	
	basedir = os.path.abspath(os.path.dirname(__file__))
	sqlite = 'sqlite:///' + os.path.join(basedir, 'storage.db')

	SQLALCHEMY_DATABASE_URI = sqlite 
	DEBUG = True

class TestingConfig(Config):
    DEBUG = True
    postgresLocal = 'postgres://postgres:1112@localhost:5432/booker-storage'
    SQLALCHEMY_DATABASE_URI = postgresLocal

