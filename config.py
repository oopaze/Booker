import os.path


class Config(object):
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SECRET_KEY = 'MinhaNamoradaEUmaGostosinhaLinda'

	basedir = os.path.abspath(os.path.dirname(__file__))
	sqlite = 'sqlite:///' + os.path.join(basedir, 'storage.db')
	DATABASE_URI = sqlite
	
	DEBUG = False
	TESTING = False

class ProductionConfig(Config):
	
	postgres = 'postgres://gyiwsztabkirow:9caef036b7e4a88e8f8d8f2ab29f0a13302fcd17c27ad4fc6983c521ca90fd01@ec2-34-233-226-84.compute-1.amazonaws.com:5432/df1anrfho1a3ce'
	
	DATABASE_URI = postgres
	SQLALCHEMY_DATABASE_URI = DATABASE_URI
	DEBUG = False

class DevelopmentConfig(Config):
	
	basedir = os.path.abspath(os.path.dirname(__file__))
	sqlite = 'sqlite:///' + os.path.join(basedir, 'storage.db')

	SQLALCHEMY_DATABASE_URI = sqlite 
	DEBUG = True

class TestingConfig(Config):
    TESTING = True

