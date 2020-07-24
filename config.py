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
	
	postgres = 'postgres://icxiyyqzlopiqh:7f97f877c6623eaaf1780ef339e9424cedc8db3eaf88036ddd5f2b02af8af992@ec2-34-193-117-204.compute-1.amazonaws.com:5432/da4m2ia61i2qde'
	
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

