from app import db
from datetime import datetime

class User(db.Model):
	__tablename__ = 'users'

	id = db.Column(db.Integer, primary_key='True')
	username = db.Column(db.String(20), unique=True)
	password = db.Column(db.String)
	image = db.Column(db.LargeBinary)
	name = db.Column(db.String)
	email = db.Column(db.String)
	
	def __init__(self, username, password, name, email, image):
		self.username = username
		self.password = password
		self.name = name
		self.email = email
		self.image = image

	@property
	def is_authenticated(self):
		return True

	@property
	def is_active(self):
		return True

	@property
	def is_anonymous(self):
		return False	

	def get_id(self):
		return str(self.id)	
		
	def __repr__(self):
		return f'<User {self.name}>'


class Book(db.Model):
	__tablename__ = 'books'

	book_id = db.Column(db.Integer, primary_key=True)
	titulo = db.Column(db.String(50), nullable=False)
	image = db.Column(db.LargeBinary)
	autor = db.Column(db.String(30), default='Desconhecido')
	atualizado_em = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now())
	nota = db.Column(db.Float)

	def __init__(self, titulo, autor, lido, atualizado_em):
		self.titulo = titulo
		self.autor = autor
		self.atualizado_em = atualizado_em

	def __repr__(self):
		return f'<Book {self.titulo}>'


class Categories(db.Model):
	__tablename__ = 'categories'

	categoria_id = db.Column(db.Integer, primary_key=True)
	categoria = db.Column(db.Integer, nullable=False, unique=True)

	def __init__(self, categoria):
		self.categoria = categoria

	def __repr__(self):
		return f'<Category {self.categoria}>'
		

class Book_category(db.Model):
	
	__tablename__ = 'book_category'

	id = db.Column(db.Integer, primary_key=True)
	book_id = db.Column(db.Integer, db.ForeignKey('books.book_id'))
	category_id = db.Column(db.Integer, db.ForeignKey('categories.categoria_id'))

	book = db.relationship('Book', foreign_keys=book_id)
	category = db.relationship('Categories', foreign_keys=category_id)

	def __init__(self, book_id, category_id):
		self.book_id = book_id
		self.category_id = category_id

	def __repr__(self):
		return f'< Book/Category {self.id}>'

class User_book(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	book_id = db.Column(db.Integer, db.ForeignKey('books.book_id'))

	user = db.relationship('User', foreign_keys=user_id)
	book = db.relationship('Book', foreign_keys=book_id)

	def __init__(self, user_id, book_id):
		self.user_id = user_id
		self.book_id = book_id

	def __repr__(self):
		return f'<User/Book {self.id}>'
		




