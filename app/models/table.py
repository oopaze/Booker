from app import db
from datetime import datetime
from flask import url_for 

class User(db.Model):
	__tablename__ = 'users'

	id = db.Column(db.Integer, primary_key='True')
	username = db.Column(db.String(20), unique=True)
	password = db.Column(db.String)
	#image = db.Column(db.LargeBinary, nullable=True)
	name = db.Column(db.String)
	email = db.Column(db.String)

	books = db.relationship('Book', backref='users')
	
	def __init__(self, username, password, name, email, image=None):
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

Book_category = db.Table(
	'book_category',
	db.Column('book_id', db.Integer, db.ForeignKey('books.id')),
	db.Column('category_id', db.Integer, db.ForeignKey('categories.id'))
)


class Book(db.Model):
	__tablename__ = 'books'

	id = db.Column(db.Integer, primary_key=True)
	titulo = db.Column(db.String(50), nullable=False)
	#image = db.Column(db.LargeBinary)
	autor = db.Column(db.String(30), default='Desconhecido')
	comment = db.Column(db.String(30), default="Aaaah, depois eu comento esse livro!")
	atualizado_em = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now())
	nota = db.Column(db.Float)

	owner = db.Column(db.Integer, db.ForeignKey('users.id'))


	def __init__(self, titulo, autor, comment=None, nota=None):

		self.titulo = titulo
		self.autor = autor
		self.nota = nota
	
		if comment:
			self.comment = comment

	def __repr__(self):
		return f'<Book {self.titulo}>'

class Category(db.Model):
	__tablename__ = 'categories'

	id = db.Column(db.Integer, primary_key=True)
	categoria = db.Column(db.String(40), nullable=False, unique=True)

	books = db.relationship(Book, 
							secondary=Book_category, 
							backref=db.backref('categories', 
												lazy='dynamic'))

	def __init__(self, categoria):
		self.categoria = categoria

	def __repr__(self):
		return f'<Category {self.categoria}>'



def testRelation():
	
	db.drop_all()
	db.create_all()

	categorias = 'Romance,Drama,Conto,Crônica,Poesia,Carta,Ficção,Aventura,Memórias,Biografia,Clássico,História em Quadrinhos (HQ),Literatura fantástica,Ficção científica,Fantasia,Sobrenatural,Realismo Mágico'
	for x in categorias.split(','):
		db.session.add(Category(x))

	db.session.commit()

	b = Book(
		titulo='As crônicas do gelo e fogo', 
		autor='George R R Martin',
	)

	db.session.add(b)

	#Add categoria ao livro
	c = Category.query.get(4)
	c.books.append(b)


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






