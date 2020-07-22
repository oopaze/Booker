import os.path


class Config(object):
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SECRET_KEY = 'MinhaNamoradaEUmaGostosinhaLinda'

	DEBUG = False
	TESTING = False

class ProductionConfig(Config):
	
	postgres = ''	
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
    postgresLocal = 'postgres://postgres:1112@localhost:5432/postgres'
    SQLALCHEMY_DATABASE_URI = postgresLocal

