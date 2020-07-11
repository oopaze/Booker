from app import app, db, lm
from flask import render_template, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from app.models.table import Categories, User
from app.models.forms import LoginForm, RegisterForm
from app.controllers.crud import readUser, createUser, updateUser, deleteUser

@app.route("/home", methods=['GET', 'POST'])
@app.route("/", methods=['GET', 'POST'])
def index():
	Loginform_= LoginForm()
	RegisterForm_ = RegisterForm()

	if Loginform_.validate_on_submit():
		userNow = readUser(username=Loginform_.username.data.lower())
		if	userNow and userNow.password == Loginform_.password.data.lower():
			login_user(userNow)
			global user
			user = userNow.id
			return redirect(url_for('books'))

		else:
			flash('l-Invalid login')

	if RegisterForm_.validate_on_submit():
			form = dict(RegisterForm_.data)
			if createUser(username=form['username'], password=form['password'],
						  email=form['email'], name=form['name']):
				
				return redirect(url_for('index'))
		
	registeredAlert = False
	RegisterForm_.data['password'] = ''
	Loginform_.data['password'] = ''
	return render_template('index.html', title='home',
	 						lform=Loginform_, rform=RegisterForm_,)


@app.route('/perfil', methods=['GET', 'POST'])
@login_required
def perfil():
	if current_user.is_authenticated:
		return render_template('perfil.html', title='perfil')
	else:
		return redirect(url_for('index'))

@app.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('index'))


@app.route('/books', methods=['GET', 'POST'])
@login_required
def books():
	return render_template('books.html', title='books', user=current_user)

@lm.unauthorized_handler
def unauthorized_callback():            
       return redirect(url_for('index'))

@lm.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()







