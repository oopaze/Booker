import os.path

basedir = os.path.abspath(os.path.dirname(__file__))
DEBUG = True

SECRET_KEY = 'MinhaNamoradaEUmaGostosinhaLinda'


SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'storage.db')


