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
	
	postgres = 'postgres://zozdgdwbfdgnwu:b146f7bfd1bf7069dc41901382b97ca8b7a49bbc038ed4414a444a837afb7ca3@ec2-34-236-215-156.compute-1.amazonaws.com:5432/d8cqcaclcmulpo'
	
	DATABASE_URI = postgres
	SQLALCHEMY_DATABASE_URI = 'DATABASE_URI'
	DEBUG = False

class DevelopmentConfig(Config):
	
	basedir = os.path.abspath(os.path.dirname(__file__))
	sqlite = 'sqlite:///' + os.path.join(basedir, 'storage.db')

	DATABASE_URI = sqlite
	SQLALCHEMY_DATABASE_URI = DATABASE_URI  
	DEBUG = True

class TestingConfig(Config):
    TESTING = True