from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired(), Length(min=6, max=25)])
	password = PasswordField('Password', validators=[DataRequired(), Length(min=3, max=25)])
	remember_me = BooleanField('Remember_me')

class RegisterForm(FlaskForm):
	email = StringField('email', validators=[DataRequired()])
	name = StringField('name', validators=[DataRequired()])
	username = StringField('username', validators=[DataRequired(), Length(min=6, max=25)])
	password = PasswordField('password', validators=[DataRequired(), Length(min=2, max=25)])
	terms = BooleanField('terms', validators=[DataRequired()])
