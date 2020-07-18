from os import listdir, remove
from datetime import timedelta
from app import app, db, lm
from flask import render_template, send_file, flash, redirect, url_for, request, session
from flask_login import login_user, logout_user, login_required, current_user
from app.models.table import Category, User, UserImage, Book, BookFile, Book_category, testRelation
from app.models.forms import LoginForm, RegisterForm, BookForm

#app.permanent_session_lifetime = timedelta(days=2)

@app.route("/home", methods=['GET', 'POST'])
@app.route("/", methods=['GET', 'POST'])
def index():
	Loginform_= LoginForm()
	RegisterForm_ = RegisterForm()

	RegisterForm_.data['password'] = ''
	Loginform_.data['password'] = ''

	if 'user' in session:
		return redirect(url_for('books'))

	return render_template('index.html', 
							title='home',
	 						lform=Loginform_,
	 						rform=RegisterForm_,)


@app.route('/perfil/<username>', methods=['GET', 'POST'])
@login_required
def perfil(username=None):
	return render_template('perfil.html', title=current_user.username)

@app.route('/books', methods=['GET', 'POST'])
def books():
	books = Book.query.filter_by(owner=int(current_user.id)).all()
	categories = []

	categories.append(Category("Todos"))
	files = []

	for book in books:
		for category in book.categories:
			if category not in categories:
				categories.append(category)

			if book.file:		
				loadbook(book.file[0].file, book.id)	
	
	BookForm_ = BookForm()
	updateBookForm_ = BookForm()

	return render_template('books.html',
	 						title='Livros', 
	 						user=current_user, 
	 						categorias=categories,
	 						books=books,
	 						newBook=BookForm_,
	 						updatebook=updateBookForm_)

@app.route('/login', methods=['GET', 'POST'])
def login():

	form = request.form
	user = User.query.filter_by(username=form['username'].lower()).first()
	
	if user: 
		if user.password == form['password']:
			login_user(user)
			session['user'] = user.serialize()
			return redirect(url_for('books'))

		else:
			return redirect(url_for('index'))
	return redirect(url_for('index'))


@app.route('/newUser', methods=['GET', 'POST'])
def newUser():

	form = request.form
	user = User(username=form['username'].lower(), password=form['password'], name=form['password'], email=form['password'])

	db.session.add(user)
	db.session.commit()

	return redirect(url_for('index'))


@app.route('/newBook', methods=['GET', 'POST'])
@login_required
def newBook():
	user = current_user
	form = request.form
	
	lido = True if 'lido' in dict(form).keys() else False


	book = Book(titulo=form['titulo'],
				autor=form['autor'],
				comment=form['comentario'],
				lido=lido)

	if (request.files['file'].filename != ''):
		book.file = []
		file = request.files['file']
		fileB = file.read()
		bookfile = BookFile(fileB)
		book.file.append(bookfile)
		
	
	
	if int(form['categoria2']) != int(form['categoria1']):
		categoria = Category.query.get(int(form['categoria1']))
		categoria2 = Category.query.get(int(form['categoria2']))
		book.categories.append(categoria)
		book.categories.append(categoria2)

	else:	
		categoria = Category.query.get(int(form['categoria1']))
		book.categories.append(categoria)

	db.session.add(book)

	current_user.books.append(book)
	
	db.session.commit()


	return redirect(url_for('books'))

@app.route('/delete/<id>', methods=['GET', 'POST'])
@login_required
def deleteBook(id=None):

	book = Book.query.filter_by(id=id).first()
	book.categories = []
	book.bookfile = []

	db.session.delete(book)
	db.session.commit() 

	return redirect(url_for('books'))

@app.route('/update/<id>', methods=['GET', 'POST'])
def updatebook(id=None):
	form = request.form

	lido = True if 'lido' in form else False 

	book = Book.query.get(id)

	categoria1 = Category.query.get(form['categoria1'])
	categoria2 = Category.query.get(form['categoria2'])
	
	book.titulo = form['titulo']
	book.autor = form['autor']
	book.comment = form['comentario']
	book.lido = lido

	if (request.files['file'].filename != ''):
		book.file = []
		file = request.files['file']
		fileB = file.read()
		bookfile = BookFile(fileB)
		book.file.append(bookfile)
		

	if categoria1 == categoria2:
		book.categories = [categoria1]	
	else:
		book.categories = [categoria1, categoria2]
	db.session.commit()

	return redirect(url_for('books'))

@app.route('/logout')
@login_required
def logout():
	session.pop('user', None)
	logout_user()
	return redirect(url_for('index'))

@lm.unauthorized_handler
def unauthorized_callback():            
       return redirect(url_for('index'))

@lm.user_loader
def load_user(user_id):
    
    return User.query.filter_by(id=user_id).first()

def loadbook(file, id):
	book = open(f'app/static/files/book{id}.pdf', 'w')
	book.close()

	book = open(f'app/static/files/book{id}.pdf', 'wb')
	book.write(file)
	book.close()




