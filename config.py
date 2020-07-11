import os.path

basedir = os.path.abspath(os.path.dirname(__file__))
DEBUG = True

SECRET_KEY = 'MinhaNamoradaEUmaGostosinhaLinda'


SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'storage.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True


'''POSTGRES = {
    'user': 'postgres',
    'pw': '1112',
    'db': 'flask-app',
    'host': 'localhost',
    'port': '5432',
}
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{POSTGRES.user}:{POSTGRES.pw}@{POSTGRES.host}:{POSTGRES.port}/{POSTGRES.db}'''




