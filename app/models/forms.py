from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField,
					 BooleanField, SubmitField,
					 IntegerField, FileField)

from wtforms.fields.html5 import DecimalRangeField

from wtforms.validators import DataRequired, Length, NumberRange


class LoginForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired(), Length(min=6, max=25)])
	password = PasswordField('Password', validators=[DataRequired(), Length(min=3, max=25)])
	remember_me = BooleanField('Remember_me')

class RegisterForm(FlaskForm):
	email = StringField('email', validators=[DataRequired()])
	name = StringField('name', validators=[DataRequired()])
	username = StringField('user', validators=[DataRequired(), Length(min=6, max=25)])
	password = PasswordField('passw', validators=[DataRequired(), Length(min=2, max=25)])
	terms = BooleanField('terms', validators=[DataRequired()])


class BookForm(FlaskForm):
	titulo = StringField('titulo', validators=[DataRequired()])
	autor = StringField('autor', validators=[DataRequired()])
	comentario = StringField('comentario', validators=[DataRequired()])
	categoria1 = StringField('categoria1', validators=[DataRequired()]) 
	categoria2 = StringField('categoria2')
	lido = BooleanField('lido', validators=[DataRequired()])
	nota = DecimalRangeField('nota', validators=[NumberRange(min=1, max=100)])
	file = FileField('arquivo')