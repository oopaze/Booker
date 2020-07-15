from app import db
from datetime import datetime
from flask import url_for 

class User(db.Model):
	__tablename__ = 'users'

	id = db.Column(db.Integer, primary_key='True')
	username = db.Column(db.String(20), unique=True)
	password = db.Column(db.String(30))
	name = db.Column(db.String(30))
	email = db.Column(db.String(30))

	image = db.relationship('UserImage', backref='users')
	books = db.relationship('Book', backref='users')
	
	def __init__(self, username, password, name, email):
		self.username = username
		self.password = password
		self.name = name
		self.email = email

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

	def serialize(self):
		json = {
			'id' : self.id,
			'username' : self.username,
			'password' : self.password,
			'name' : self.name,
			'email' : self.email
		}
		return json


Book_category = db.Table(
	'book_category',
	db.Column('book_id', db.Integer, db.ForeignKey('books.id')),
	db.Column('category_id', db.Integer, db.ForeignKey('categories.id'))
)

class Category(db.Model):
	__tablename__ = 'categories'

	id = db.Column(db.Integer, primary_key=True)
	categoria = db.Column(db.String(40), nullable=False, unique=True)
	
	def __init__(self, categoria):
		self.categoria = categoria

	def __repr__(self):
		return f'<Category {self.categoria}>'

class Book(db.Model):
	__tablename__ = 'books'

	id = db.Column(db.Integer, primary_key=True)
	titulo = db.Column(db.String(100), nullable=False)
	#image = db.Column(db.LargeBinary)
	autor = db.Column(db.String(30), default='Desconhecido')
	nota = db.Column(db.Float)
	lido = db.Column(db.Boolean, default=False)
	comment = db.Column(db.String(100), default="Aaaah, depois eu comento esse livro!")

	owner = db.Column(db.Integer, db.ForeignKey('users.id'))

	file = db.relationship('BookFile', backref='Book')
	categories = db.relationship(Category, 
							secondary=Book_category, 
							backref=db.backref('books', 
												lazy='dynamic'))


	def __init__(self, titulo, autor, comment=None, lido=None, nota=None):

		self.titulo = titulo
		self.autor = autor
		self.nota = nota
		if lido:
			self.lido = lido

		if comment:
			self.comment = comment

	def __repr__(self):
		return f'<Book {self.titulo}>'

class UserImage(db.Model):
	__tablename__ = 'userimage'
	id = db.Column(db.Integer, primary_key=True)
	image = db.Column(db.LargeBinary)

	user = db.Column(db.Integer, db.ForeignKey('users.id'))		
	
	def __init__(self, image):
		self.image = image

class BookFile(db.Model):
	__tablename__ = 'bookfile'
	id = db.Column(db.Integer, primary_key=True)
	file = db.Column(db.LargeBinary)

	book = db.Column(db.Integer, db.ForeignKey('books.id'))		
	
	def __init__(self, file):
		self.file = file

def testRelation():
	
	db.drop_all()
	db.create_all()

	categorias = 'Documentário,Romance,Drama,Conto,Crônica,Poesia,Carta,Ficção,Aventura,Memórias,Biografia,Clássico,História em Quadrinhos (HQ),Literatura fantástica,Ficção científica,Fantasia,Sobrenatural,Realismo Mágico'
	for x in categorias.split(','):
		db.session.add(Category(x))

	db.session.commit()

	b = Book(
		titulo='As crônicas do gelo e fogo', 
		autor='George R R Martin',
		lido=True
	)

	db.session.add(b)

	#Add categoria ao livro
	c = Category.query.get(4)
	b.categories.append(c)


	u = User(
			username='kaah17', 
			password='florzinha', 
			email='kaah-sousa@gmail.com',
			name='Caroline Ribeiro' 
		)

	u2 = User(
			username='oopaze',
			password='mae12345',
			email='pedroosd28@gmail.com',
			name='José Pedro da Silva Gomes'
		)
	db.session.add(u2)
	db.session.add(u)

	#adicionando relação entre livro e usuario
	u.books.append(b)
	
	db.session.commit()

testRelation()




