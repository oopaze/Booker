from app import db
from datetime import datetime

class User(db.Model):
	__tablename__ = 'users'

	id = db.Column(db.Integer, primary_key='True')
	username = db.Column(db.String(20), unique=True)
	password = db.Column(db.String)
	name = db.Column(db.String)
	email = db.Column(db.String)

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
		
	def __init__(self, username, password, name, email):
		self.username = username
		self.password = password
		self.name = name
		self.email = email
		
	def __repr__(self):
		return f'<User {name}'


class Book(db.Model):
	__tablename__ = 'books'

	book_id = db.Column(db.Integer, primary_key=True)
	titulo = db.Column(db.String(50), nullable=False)
	autor = db.Column(db.String(30), default='Desconhecido')
	atualizado_em = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now())

	def __init__(self, titulo, autor, lido, atualizado_em):
		self.titulo = titulo
		self.autor = autor
		self.atualizado_em = atualizado_em

	def __repr__(self):
		return f'<Book {self.titulo}'


class Categories(db.Model):
	__tablename__ = 'categories'

	categoria_id = db.Column(db.Integer, primary_key=True)
	categoria = db.Column(db.Integer, nullable=False, unique=True)

	def __init__(self, categoria):
		self.categoria = categoria

	def __repr__(self):
		return f'<Category {self.categoria}'
		

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
		return f'<Book {id}'

