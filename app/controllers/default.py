from app import app, db, lm
from flask import render_template, flash, redirect
from flask_login import login_user
from app.models.table import Categories, User
from app.models.forms import LoginForm, RegisterForm
from app.controllers.crud import readUser, createUser, updateUser, deleteUser


@lm.user_loader
def load_user(user_id):
    return None

@app.route("/home", methods=['GET', 'POST'])
@app.route("/", methods=['GET', 'POST'])
def index():
	
	Loginform_ = LoginForm()
	RegisterForm_ = RegisterForm()

	if Loginform_.validate_on_submit():
		userNow = readUser(username=Loginform_.username.data, password=Loginform_.password.data)
		if	userNow and userNow.password == Loginform_.password.data:
			login_user(userNow)
			return redirect('/books')

		else:
			flash('Invalid login.')

	if RegisterForm_.validate_on_submit():
			form = dict(RegisterForm_.data)
			print(form)
			if form['terms']:
				createUser(username=form['username'], password=form['password'], email=form['email'], name=form['name'])
				return redirect('/home')
	
		
	registeredAlert = False
	RegisterForm_.data['password'] = ''
	Loginform_.data['password'] = ''
	return render_template('index.html', title='home', lform=Loginform_, rform=RegisterForm_, rAlert=registeredAlert)


@app.route('/perfil')
def perfil():
	return render_template('perfil.html')

@app.route('/books')
def books():
	return render_template('books.html')

