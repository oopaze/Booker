from flask import Flask
import click
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager
from flask.cli import with_appcontext

app =  Flask(__name__)
app.config.from_object('config.ProductionConfig')

db = SQLAlchemy(app)

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

lm = LoginManager()
lm.init_app(app)

from app.models import table	
from app.controllers import default

@click.command(name='create')
@with_appcontext
def create():
	db.drop_all()
	db.create_all()

app.cli.add_command(create)



