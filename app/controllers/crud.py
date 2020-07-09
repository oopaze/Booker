from app.models.table import User
from app import app, db

def createUser(username=None, password=None, email=None, name=None):
	try:
		newUser = User(username, password, email, name)	
		db.session.add(newUser)
		db.session.commit()
		return True

	except Exception:
		return False

def readUser(username=None, password=None, id=None):
	if id:
		user = User.query.filter_by(id=id).all()
	elif username:
		user = User.query.filter_by(username=username).first()

	return user
	

def updateUser(username=None, id=None, column=None):
	user = None
	if id:
		user = readUser(id=id)
	elif username:
		user = readUser(username=username)
	if user:
		for x in column.keys():
			if x == 'password':
				user.password = column[x]
			elif x == 'name':
				user.name = column[x]
			elif x == 'username':
				user.username = column[x]
			elif x == 'email':
				user.emial = column[x]
			else:
				return False

		db.session.add(user)
		db.session.commit()
		return True

	return False


def deleteUser(id=None, username=None):
	if id:
		user = readUser(id=id)
	elif username:
		user = readUser(username=username)
	else:
		return False
	
	db.session.delete(user)
	db.session.commit()
	return False		



