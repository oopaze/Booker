import os.path

basedir = os.path.abspath(os.path.dirname(__file__))
DEBUG = True

SECRET_KEY = 'MinhaNamoradaEUmaGostosinhaLinda'

POSTGRES = {
    'user': 'postgres',
    'pw': '1112',
    'db': 'flask-app',
    'host': 'localhost',
    'port': '5432',
}
<<<<<<< HEAD
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{POSTGRES.user}:{POSTGRES.pw}@{POSTGRES.host}:{POSTGRES.port}/{POSTGRES.db}'''
=======

#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'storage.db')
SQLALCHEMY_DATABASE_URI = f"postgresql://{POSTGRES['user']}:{POSTGRES['pw']}@{POSTGRES['host']}:{POSTGRES['port']}/{POSTGRES['db']}"
SQLALCHEMY_TRACK_MODIFICATIONS = True


>>>>>>> 31550b4e8008fca927ab9d5ce294d820d4aaec71




