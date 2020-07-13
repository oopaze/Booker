import os.path


class Config(object):
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SECRET_KEY = 'MinhaNamoradaEUmaGostosinhaLinda'
	DEBUG = False
	TESTING = False

class ProductionConfig(Config):
	PSQL = {
		'user' : 'zozdgdwbfdgnwu',
		'pw' : 'b146f7bfd1bf7069dc41901382b97ca8b7a49bbc038ed4414a444a837afb7ca3',
		'endereco' : 'ec2-34-236-215-156.compute-1.amazonaws.com',
		'db' : 'd8cqcaclcmulpo',
		'port': '5432'
		}
	
	postgres = f'postgres://{PSQL["user"]}:PSQL["pw"]@{PSQL["endereco"]}:{PSQL["port"]}/{PSQL["db"]}'
	DATABASE_URI = postgres
	SQLALCHEMY_DATABASE_URI = DATABASE_URI
	DEBUG = False

class DevelopmentConfig(Config):
	basedir = os.path.abspath(os.path.dirname(__file__))
	sqlite = 'sqlite:///' + os.path.join(basedir, 'storage.db')
	DATABASE_URI = sqlite
	SQLALCHEMY_DATABASE_URI = DATABASE_URI
	DEBUG = True

class TestingConfig(Config):
    TESTING = True