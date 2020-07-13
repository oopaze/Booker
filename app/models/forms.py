from app import db
from app.models.table import Category

from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField,
					 BooleanField, SubmitField,
					 IntegerField, FileField,
					 SelectField, TextAreaField)

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

"""
categories = Category.query.with_entities(Category)
category_list = [(categoria.id, categoria.categoria) for categoria in categories]
"""
category_list = [(0, 'None')]
class BookForm(FlaskForm):
	titulo = StringField('titulo', validators=[DataRequired()])
	autor = StringField('autor', validators=[DataRequired()])
	comentario = TextAreaField('comentario', validators=[DataRequired()])
	categoria1 = SelectField('categoria1', choices=category_list, validators=[DataRequired()]) 
	categoria2 = SelectField('categoria2', choices=category_list)
	lido = BooleanField('lido')
	nota = DecimalRangeField('nota', validators=[NumberRange(min=1, max=100)])
	file = FileField('arquivo')