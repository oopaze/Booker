import os.path


class Config(object):
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SECRET_KEY = 'MinhaNamoradaEUmaGostosinhaLinda'

	basedir = os.path.abspath(os.path.dirname(__file__))
	sqlite = 'sqlite:///' + os.path.join(basedir, 'storage.db')
	DATABASE_URI = sqlite
	
	DEBUG = False

class ProductionConfig(Config):
	
	postgres = 'postgres://mlkzfnnzzpgxgc:49e0b4428d15d050923141b429d35594c1797d176f888710ffa722e8daca195a@ec2-54-161-208-31.compute-1.amazonaws.com:5432/d8iruqe7anrn6l'
	
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

